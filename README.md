# Anime Recommendation System 🎌

[Live Demo](https://anime-recommender-system-xr8mhifbmbappybdyelbkb4.streamlit.app/)

A content-based Anime Recommendation System built using Machine Learning and Streamlit. The application recommends similar anime based on their features and metadata using vectorization and cosine similarity.

## Features

* Anime recommendation based on content similarity
* Interactive Streamlit web application
* Fast recommendation generation
* Large anime dataset support
* Simple and user-friendly interface

## Live Demo

https://anime-recommender-system-xr8mhifbmbappybdyelbkb4.streamlit.app/

## Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Pickle

## Dataset

The project uses a large anime dataset containing information such as genres, themes, studios, ratings, and other metadata to generate recommendations.

## How It Works

1. Data preprocessing and cleaning
2. Feature extraction using Count Vectorization
3. Similarity calculation using Cosine Similarity
4. Recommendation generation
5. Interactive web deployment using Streamlit

## Installation

```bash
git clone https://github.com/rajanjaiswalml/Anime-Recommender-System.git

cd Anime-Recommender-System

pip install -r requirements.txt

streamlit run app.py
```

## Project Structure

```text
Anime-Recommender-System/
│
├── app.py
├── anime.pkl
├── anime_dict.pkl
├── similarity.pkl
├── popular_anime.csv
├── Anime_Data.ipynb
├── requirements.txt
└── README.md
```

## Future Improvements

* Poster and trailer integration
* Genre-based filtering
* Personalized recommendations
* User rating system
* Hybrid recommendation engine

## Author

Rajan Jaiswal

Machine Learning Engineer | AI/ML Enthusiast
