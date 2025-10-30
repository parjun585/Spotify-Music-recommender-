# Spotify Music Recommender System  
**A Python-based music recommendation engine using content-based filtering and collaborative filtering techniques.**

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://python.org)  
[![Scikit-learn](https://img.shields.io/badge/scikit--learn-1.3-orange)](https://scikit-learn.org)  
[![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red)](https://your-streamlit-link.com)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Project Overview
This project builds a **hybrid music recommender system** using the **Spotify Million Song Dataset** (subset). It combines:
- **Content-based filtering** (using audio features: danceability, energy, tempo, etc.)
- **Collaborative filtering** (KNN on user-item interactions)

Users input a song → system returns **top 5 similar tracks** with **confidence scores**.



---

## Key Features
| Feature | Description |
|-------|-----------|
| **Audio Feature Analysis** | Uses 12 Spotify audio features (danceability, valence, etc.) |
| **Cosine Similarity + KNN** | Finds nearest neighbors in feature space |
| **Hybrid Scoring** | Combines content + user ratings |
| **Interactive UI** | Search by song name → instant recommendations |
| **Evaluation Metrics** | Precision@5, NDCG@5 on holdout set |

---

## Tech Stack
```text
Python
├── pandas, numpy
├── scikit-learn (KNeighbors, cosine_similarity)
├── spotipy (Spotify API)
├── matplotlib, seaborn
├── streamlit (UI)
└── Jupyter Notebook (exploration)
```



# 1. Clone repo
git clone https://github.com/parjun585/Spotify-Music-Recommender-.git
cd Spotify-Music-Recommender-

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run Streamlit app
streamlit run app.py
