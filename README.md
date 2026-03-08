# 🎬 Movie Recommender System

A content-based movie recommendation system built with Python, utilizing machine learning techniques to suggest similar movies based on various features like genres, keywords, cast, crew, and plot overview.



## 🎯 Overview

This Movie Recommender System uses **Content-Based Filtering** to recommend movies similar to a user's selection. The system analyzes movie metadata including genres, keywords, cast, crew, and plot descriptions to find the most similar movies using **Cosine Similarity**.

The project includes:
- A **Jupyter Notebook** for data preprocessing and model building
- A **Streamlit Web Application** for interactive movie recommendations
- **TMDB API integration** for fetching movie posters

## Features

- 🎭 **Interactive Web Interface** - Beautiful Streamlit UI for easy movie exploration
- **Movie Posters** - Real-time poster fetching from TMDB API
- **Smart Search** - Searchable dropdown with 4800+ movies
- **Personalized Recommendations** - Get 10 similar movies instantly
- **Infinite Discovery** - Click any recommended movie to explore more
- **Responsive Design** - Works on desktop and mobile devices
- **Fast Performance** - Pre-computed similarity matrix for instant results
- 🌐 **Offline Support** - Graceful fallback when API is unavailable

## 📊 Dataset

### TMDB 5000 Movie Dataset
The project uses two CSV files from [The Movie Database (TMDB)](https://www.themoviedb.org/):

1. **tmdb_5000_movies.csv** (4803 movies)
   - Budget, Revenue, Runtime
   - Genres, Keywords, Production Companies
   - Overview, Tagline, Title
   - Vote Average, Vote Count, Popularity
   - Release Date, Status

2. **tmdb_5000_credits.csv** (4803 movies)
   - Cast (actors and characters)
   - Crew (directors, producers, etc.)
   - Movie ID for merging

**Dataset Statistics:**
- Total Movies: 4,803
- Features Used: 7 (title, overview, genres, keywords, cast, crew, movie_id)
- Languages: Primarily English
- Time Period: Various decades of cinema

## 🔧 How It Works

### 1. Data Preprocessing
```python
# Features extracted from the dataset
- Overview: Movie plot description
- Genres: Action, Comedy, Drama, etc.
- Keywords: Relevant tags and themes
- Cast: Top 3 actors
- Crew: Director
```

### 2. Feature Engineering
- Merged movies and credits datasets
- Extracted top 3 actors from cast
- Extracted director from crew
- Combined all features into a single 'tags' column
- Removed spaces from multi-word terms
- Created a bag-of-words representation

### 3. Vectorization & Similarity
- Used **CountVectorizer** with:
  - max_features = 5000
  - stop_words = 'english'
- Calculated **Cosine Similarity** between all movie vectors
- Created a 4803 x 4803 similarity matrix

### 4. Recommendation Algorithm
```python
def recommend(movie_title):
    1. Find movie index in dataset
    2. Get similarity scores for that movie
    3. Sort movies by similarity (descending)
    4. Return top 10 most similar movies
    5. Fetch posters from TMDB API
```

### Mathematical Foundation
**Cosine Similarity Formula:**
```
similarity = (A · B) / (||A|| × ||B||)
```
where A and B are feature vectors of two movies.

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git (for cloning)

### Step 1: Clone the Repository
```bash
git clone https://github.com/SalmanRajpuat/movie_recommender_system.git
cd movie_recommender_system
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Download Dataset & Generate Model Files

**Option A: Download Datasets (Required for first-time setup)**

The large dataset and model files are not included in the repository. Download them from:

1. **TMDB Dataset**: 
   - Download [tmdb_5000_movies.csv](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
   - Download [tmdb_5000_credits.csv](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
   - Place both CSV files in the project root directory

2. **Or use Google Drive/Dropbox** (if you have the files):
   - [Download movie.pkl](YOUR_LINK_HERE)
   - [Download similarity.pkl](YOUR_LINK_HERE)

**Option B: Generate Model Files from Notebook**

After downloading the CSV datasets:
```bash
jupyter notebook movie-recommender-system.ipynb
```
Run all cells to generate `movie.pkl` and `similarity.pkl`

> **Note**: The similarity.pkl file is ~176MB and is automatically generated from the notebook. This is similar to `node_modules` in MERN - we don't commit it to Git.

### Step 4: Run the Streamlit App
```bash
streamlit run movie_recommender_sytsem.py
```
or
```bash
python -m streamlit run movie_recommender_sytsem.py
```

The app will open automatically in your browser at `http://localhost:8501`

## 💻 Usage

### Web Application
1. **Search for a Movie**: Click on the search box and type or select a movie
2. **Get Recommendations**: Click the "Show Recommendations" button
3. **Explore More**: Click on any movie poster to get recommendations based on that film
4. **Infinite Discovery**: Keep clicking to explore the movie universe!

### API Usage (if extended)
```python
from movie_recommender import recommend

# Get recommendations
recommendations = recommend("The Dark Knight")
print(recommendations)
```

## 📁 Project Structure

```
movie_recommender_system/
│
├── movie-recommender-system.ipynb  # Jupyter notebook with model building
├── Movie_recommender_sytsem.py     # Streamlit web application
│
├── tmdb_5000_movies.csv           # Movies dataset (download separately)
├── tmdb_5000_credits.csv          # Credits dataset (download separately)
│
├── movie.pkl                       # Processed movie data (generated from notebook)
├── similarity.pkl                  # Similarity matrix (generated from notebook)
│
├── requirements.txt                # Python dependencies
├── .gitignore                      # Git ignore file
├── LICENSE                         # MIT License
└── README.md                       # Project documentation
```

> **Note**: Files marked with *(download separately)* or *(generated from notebook)* are NOT in the GitHub repository due to their large size (176MB total). See installation instructions above.

### Why Some Files Are Not Included?

Similar to **Node.js projects** that exclude `node_modules`:
- **✅ Included**: Source code (.py, .ipynb), requirements.txt
- **❌ Excluded**: Large generated files (.pkl), datasets (.csv)
- **📥 After Cloning**: Run the notebook or download files separately

This keeps the repository lightweight and fast to clone!

## 🛠️ Technologies Used

### Python Libraries
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Scikit-learn** - Machine learning (CountVectorizer, Cosine Similarity)
- **NLTK** - Natural language processing (stemming)
- **Streamlit** - Web application framework
- **Requests** - HTTP library for API calls
- **Pickle** - Object serialization

### APIs & Services
- **TMDB API** - The Movie Database API for movie posters
- **Streamlit Sharing** (optional) - For deployment

### Development Tools
- Jupyter Notebook
- VS Code / PyCharm
- Git & GitHub

## 📸 Screenshots

### Home Page
Search for your favorite movie and start exploring!

### Recommendations View
Get 10 personalized movie recommendations with beautiful posters.

### Interactive Experience
Click any movie to instantly discover similar films - Netflix-style browsing!

## 🔮 Future Enhancements

- [ ] **Hybrid Recommendation System** - Combine content-based and collaborative filtering
- [ ] **User Ratings Integration** - Incorporate user preferences
- [ ] **Movie Details Page** - Show full movie information, trailers, reviews
- [ ] **Advanced Filters** - Filter by genre, year, rating, runtime
- [ ] **Watchlist Feature** - Save movies to watch later
- [ ] **Similar Movies Network** - Visualize movie relationships
- [ ] **Multi-language Support** - Support for international movies
- [ ] **Deep Learning Model** - Use neural networks for better recommendations
- [ ] **Real-time Updates** - Sync with TMDB for latest releases
- [ ] **User Authentication** - Personal recommendation history

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Areas for Contribution
- Improve recommendation algorithm
- Add new features to the web app
- Enhance UI/UX design
- Add unit tests
- Improve documentation
- Fix bugs

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Salman Rajpuat**
- GitHub: [@SalmanRajpuat](https://github.com/SalmanRajpuat)

## 🙏 Acknowledgments

- [TMDB](https://www.themoviedb.org/) for providing the movie database and API
- [Streamlit](https://streamlit.io/) for the amazing web framework
- [Scikit-learn](https://scikit-learn.org/) for machine learning tools
- The open-source community for inspiration and resources

## 📧 Contact

For questions, suggestions, or collaboration:
- Create an issue in this repository
- Email: [Your Email]

---

⭐ If you found this project helpful, please give it a star!

🎬 Happy Movie Watching! 🍿
