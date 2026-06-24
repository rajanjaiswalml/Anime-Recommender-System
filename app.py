import streamlit as st
import pickle
import pandas as pd
import requests

# ======================================
# PAGE CONFIG
# ======================================

st.set_page_config(
    page_title="Anime Recommender",
    page_icon="🎌",
    layout="wide"
)

# ======================================
# CUSTOM CSS
# ======================================

st.markdown("""
<style>import streamlit as st
import pickle
import pandas as pd
import requests

# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="Anime Recommender",
    page_icon="🎌",
    layout="wide"
)

# ==========================
# LOAD FILES
# ==========================

anime_dict = pickle.load(
    open("anime_dict.pkl", "rb")
)

anime_df = pd.DataFrame(anime_dict)

recommendations = pickle.load(
    open("recommendations.pkl", "rb")
)

# ==========================
# JIKAN API
# ==========================

@st.cache_data(show_spinner=False)
def get_anime_details(name):

    try:

        url = f"https://api.jikan.moe/v4/anime?q={name}&limit=1"

        response = requests.get(url, timeout=10)

        data = response.json()["data"][0]

        return {
            "title": data["title"],
            "image": data["images"]["jpg"]["image_url"],
            "score": data.get("score", "N/A"),
            "episodes": data.get("episodes", "N/A"),
            "genres": ", ".join(
                [g["name"] for g in data.get("genres", [])]
            )
        }

    except:

        return {
            "title": name,
            "image": "https://via.placeholder.com/300x450?text=Anime",
            "score": "N/A",
            "episodes": "N/A",
            "genres": "N/A"
        }

# ==========================
# HEADER
# ==========================

st.title("🎌 Anime Recommendation System")

st.write(
    "Content Based Anime Recommender using Machine Learning + Streamlit"
)

# ==========================
# SELECT BOX
# ==========================

selected_anime = st.selectbox(
    "Select Anime",
    anime_df["name"].values
)

# ==========================
# SELECTED ANIME DETAILS
# ==========================

details = get_anime_details(selected_anime)

col1, col2 = st.columns([1, 2])

with col1:
    st.image(details["image"], width=250)

with col2:

    st.subheader(details["title"])

    st.write(f"⭐ Rating : {details['score']}")

    st.write(f"📺 Episodes : {details['episodes']}")

    st.write(f"🎭 Genres : {details['genres']}")

# ==========================
# RECOMMEND BUTTON
# ==========================

if st.button(
    "🚀 Get Recommendations",
    use_container_width=True
):

    st.subheader("Recommended Anime")

    recs = recommendations[selected_anime]

    cols = st.columns(5)

    for i, anime_name in enumerate(recs):

        anime = get_anime_details(anime_name)

        with cols[i]:

            st.image(anime["image"])

            st.markdown(
                f"**{anime['title']}**"
            )

            st.write(
                f"⭐ {anime['score']}"
            )

# ==========================
# FOOTER
# ==========================

st.markdown("---")

st.caption(
    "Built by Rajan Jaiswal | Machine Learning Project"
)

.main {
    background-color: #0E1117;
}

.anime-card {
    background-color: #262730;
    padding: 10px;
    border-radius: 10px;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# ======================================
# LOAD DATA
# ======================================

anime_dict = pickle.load(open("anime_dict.pkl", "rb"))
anime_df = pd.DataFrame(anime_dict)

similarity = pickle.load(open("similarity.pkl", "rb"))

# ======================================
# API FUNCTIONS
# ======================================

@st.cache_data
def get_anime_details(anime_name):

    try:

        url = f"https://api.jikan.moe/v4/anime?q={anime_name}&limit=1"

        response = requests.get(url)

        data = response.json()['data'][0]

        details = {
            "title": data.get("title", "N/A"),
            "image": data['images']['jpg']['image_url'],
            "score": data.get("score", "N/A"),
            "episodes": data.get("episodes", "N/A"),
            "synopsis": data.get("synopsis", "N/A"),
            "genres": [g['name'] for g in data.get("genres", [])],
            "trailer": data.get("trailer", {}).get("url")
        }

        return details

    except:

        return {
            "title": anime_name,
            "image": "https://via.placeholder.com/300x450?text=No+Image",
            "score": "N/A",
            "episodes": "N/A",
            "synopsis": "Not Available",
            "genres": [],
            "trailer": None
        }

# ======================================
# RECOMMENDATION FUNCTION
# ======================================

def recommend(anime_name):

    anime_index = anime_df[
        anime_df['name'] == anime_name
    ].index[0]

    distances = similarity[anime_index]

    anime_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = []

    for anime in anime_list:

        anime_name = anime_df.iloc[
            anime[0]
        ]['name']

        recommendations.append(
            get_anime_details(anime_name)
        )

    return recommendations

# ======================================
# HEADER
# ======================================

st.title("🎌 Anime Recommendation System")

st.write(
    "Discover similar anime using Content-Based Filtering and Jikan API"
)

# ======================================
# SIDEBAR
# ======================================

st.sidebar.title("Project Information")

st.sidebar.info("""
Anime Recommender System

Tech Stack:
- Python
- Streamlit
- Pandas
- Pickle
- Jikan API
- Content Based Filtering
""")

st.sidebar.metric(
    "Anime Count",
    len(anime_df)
)

# ======================================
# ANIME SELECTION
# ======================================

selected_anime = st.selectbox(
    "Select Anime",
    anime_df['name'].values
)

# ======================================
# SHOW SELECTED ANIME
# ======================================

details = get_anime_details(selected_anime)

col1, col2 = st.columns([1,2])

with col1:

    st.image(
        details['image'],
        width=280
    )

with col2:

    st.subheader(details['title'])

    st.write(
        f"⭐ Rating: {details['score']}"
    )

    st.write(
        f"📺 Episodes: {details['episodes']}"
    )

    st.write(
        f"🎭 Genres: {', '.join(details['genres'])}"
    )

    st.write(
        details['synopsis']
    )

    if details['trailer']:

        st.link_button(
            "▶ Watch Trailer",
            details['trailer']
        )

# ======================================
# RECOMMENDATION BUTTON
# ======================================

if st.button(
    "🚀 Get Recommendations",
    use_container_width=True
):

    st.subheader(
        "Recommended Anime"
    )

    recommendations = recommend(
        selected_anime
    )

    cols = st.columns(5)

    for i in range(5):

        anime = recommendations[i]

        with cols[i]:

            st.image(
                anime['image']
            )

            st.markdown(
                f"**{anime['title']}**"
            )

            st.write(
                f"⭐ {anime['score']}"
            )

            st.write(
                f"📺 {anime['episodes']} Episodes"
            )

# ======================================
# FOOTER
# ======================================

st.markdown("---")

st.caption(
    "Built by Rajan Jaiswal | Streamlit + ML + Jikan API"
)