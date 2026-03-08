import streamlit as st
import pickle
import pandas as pd
import requests

# Initialize session state for selected movie
if 'selected_movie' not in st.session_state:
    st.session_state.selected_movie = None
if 'show_recommendations' not in st.session_state:
    st.session_state.show_recommendations = False

def fetch_poster(movie_id):
    try:
        response = requests.get(
            f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=c1f1e53576db2df0f3a5f58fac40890e&language=en-US',
            timeout=5
        )
        data = response.json()
        if 'poster_path' in data and data['poster_path']:
            return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
        else:
            # Return placeholder if no poster path
            return "https://via.placeholder.com/500x750/cccccc/666666?text=No+Poster"
    except:
        # Return placeholder image if API call fails
        return "https://via.placeholder.com/500x750/cccccc/666666?text=No+Poster"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]
    
    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        #fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies, recommended_movies_posters

movies_list = pickle.load(open('movie.pkl', 'rb'))
movies = pd.DataFrame(movies_list)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("🎬 Movie Recommender System")
st.subheader("Click on any movie poster to discover similar movies!")

# Check API connectivity
try:
    test_response = requests.get("https://api.themoviedb.org", timeout=2)
    if test_response.status_code != 200:
        st.warning("⚠️ Unable to connect to movie poster service. Showing placeholder images.")
except:
    st.warning("⚠️ No internet connection detected. Showing placeholder images instead of movie posters.")

# Search/Filter box for initial selection (optional)
with st.expander("🔍 Search for a movie to start", expanded=not st.session_state.get('show_recommendations', False)):
    search_movie = st.selectbox(
        'Type or select a movie:',
        movies['title'].values,
        key='search_box')
    
    if st.button('Show Recommendations', type="primary"):
        st.session_state.selected_movie = search_movie
        st.session_state.show_recommendations = True
        st.rerun()

# Show recommendations if triggered
if st.session_state.show_recommendations and st.session_state.selected_movie:
    st.markdown(f"### 🎯 Currently Exploring: **{st.session_state.selected_movie}**")
    st.markdown("---")
    
    name, posters = recommend(st.session_state.selected_movie)
    
    # First row - 5 movies
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(posters[0], use_column_width=True)
        if st.button(name[0], key=f"btn_0", use_container_width=True):
            st.session_state.selected_movie = name[0]
            st.rerun()
    with col2:
        st.image(posters[1], use_column_width=True)
        if st.button(name[1], key=f"btn_1", use_container_width=True):
            st.session_state.selected_movie = name[1]
            st.rerun()
    with col3:
        st.image(posters[2], use_column_width=True)
        if st.button(name[2], key=f"btn_2", use_container_width=True):
            st.session_state.selected_movie = name[2]
            st.rerun()
    with col4:
        st.image(posters[3], use_column_width=True)
        if st.button(name[3], key=f"btn_3", use_container_width=True):
            st.session_state.selected_movie = name[3]
            st.rerun()
    with col5:
        st.image(posters[4], use_column_width=True)
        if st.button(name[4], key=f"btn_4", use_container_width=True):
            st.session_state.selected_movie = name[4]
            st.rerun()
    
    # Second row - 5 movies
    col6, col7, col8, col9, col10 = st.columns(5)
    with col6:
        st.image(posters[5], use_column_width=True)
        if st.button(name[5], key=f"btn_5", use_container_width=True):
            st.session_state.selected_movie = name[5]
            st.rerun()
    with col7:
        st.image(posters[6], use_column_width=True)
        if st.button(name[6], key=f"btn_6", use_container_width=True):
            st.session_state.selected_movie = name[6]
            st.rerun()
    with col8:
        st.image(posters[7], use_column_width=True)
        if st.button(name[7], key=f"btn_7", use_container_width=True):
            st.session_state.selected_movie = name[7]
            st.rerun()
    with col9:
        st.image(posters[8], use_column_width=True)
        if st.button(name[8], key=f"btn_8", use_container_width=True):
            st.session_state.selected_movie = name[8]
            st.rerun()
    with col10:
        st.image(posters[9], use_column_width=True)
        if st.button(name[9], key=f"btn_9", use_container_width=True):
            st.session_state.selected_movie = name[9]
            st.rerun()
    
    st.markdown("---")
    st.info("💡 Click on any movie title button below the poster to explore similar movies!")
    
