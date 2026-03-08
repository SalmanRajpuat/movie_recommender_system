# 🎬 Movie Recommender System

A content-based movie recommendation system built with Python, utilizing machine learning techniques to suggest similar movies based on various features like genres, keywords, cast, crew, and plot overview.



## Overview

This Movie Recommender System uses **Content-Based Filtering** to recommend movies similar to a user's selection. The system analyzes movie metadata including genres, keywords, cast, crew, and plot descriptions to find the most similar movies using **Cosine Similarity**.

The project includes:
- A **Jupyter Notebook** for data preprocessing and model building
- A **Streamlit Web Application** for interactive movie recommendations
- **TMDB API integration** for fetching movie posters


- 🌐 **Offline Support** - Graceful fallback when API is unavailable

## Dataset

### TMDB 5000 Movie Dataset
The project uses two CSV files from [The Movie Database (TMDB)](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata):

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


## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git (for cloning)



### Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Download Dataset & Generate Model Files

**Option A: Download Datasets (Required for first-time setup)**

The large dataset and model files are not included in the repository. Download them from:

1. **TMDB Dataset**: 
   - Download [tmdb_5000_movies.csv](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
   - Download [tmdb_5000_credits.csv](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
   - Place both CSV files in the project root directory


After downloading the CSV datasets:
```bash
jupyter notebook movie-recommender-system.ipynb
```
Run all cells to generate `movie.pkl` and `similarity.pkl`

> **Note**: The similarity.pkl file is ~176MB and is automatically generated from the notebook. This is similar to `node_modules` in MERN - we don't commit it to Git.

### Step 3: Run the Streamlit App
```bash
streamlit run movie_recommender_sytsem.py
```
or
```bash
python -m streamlit run movie_recommender_sytsem.py
```

The app will open automatically in your browser at `http://localhost:8501`

## Usage

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


