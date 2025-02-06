import pickle
import pandas as pd
import streamlit as st

# Load movie data and similarity matrix
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit App Configuration
st.set_page_config(page_title="Movie Recommender", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    /* Import Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

    /* Apply Font to Whole App */
    html, body, .stApp {
        font-family: 'Poppins', sans-serif;
        background-color: #121212; /* Dark Theme */
        color: white; /* Default Text Color */
    }

    /* Main Title */
    .stTitle {
        font-size: 40px;
        font-weight: 600;
        color: #FFFFFF; /* White */
        text-align: center;
        font-family: 'Poppins', sans-serif;
        letter-spacing: 1px;
    }

    /* Dropdown (Movie Selection) */
    .stSelectbox label {
        font-size: 18px;
        font-weight: 600;
        color: white !important;
        font-family: 'Poppins', sans-serif;
    }

    .stSelectbox div[data-baseweb="select"] {
        background-color: #1E1E1E !important; /* Dark Grey */
        color: white !important;
        border-radius: 8px;
        padding: 10px;
    }

    /* Recommend Button */
    .stButton > button {
        background-color: #FF4B4B !important; /* Red */
        color: white !important;
        font-size: 18px !important;
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        border-radius: 10px !important;
        padding: 12px 24px;
        border: none;
    }

    /* Movie Boxes */
    .movie-box {
        background-color: rgba(34, 34, 34, 0.9); /* Dark Grey */
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 10px;
        box-shadow: 0px 0px 10px rgba(255, 255, 255, 0.1); /* Subtle Glow */
        font-family: 'Poppins', sans-serif;
        text-align: center; /* Centered Movie Titles */
    }

    /* Movie Title */
    .movie-title {
        font-size: 22px;
        font-weight: 600;
        color: #FFFFFF; /* White */
        font-family: 'Poppins', sans-serif;
    }

    /* Section Titles (e.g. Selected Movie & Recommendations) */
    .section-title {
        font-size: 20px;
        font-weight: 600;
        color: white;
        margin-top: 20px;
        text-align: center; /* Centered Section Titles */
    }

    /* Custom Alignment for Recommendation Section */
    .recommendation-list {
        display: flex;
        flex-direction: column;
        align-items: center; /* Centering Recommendations */
    }
    </style>""",unsafe_allow_html=True
)


# Function to format text to title case
def format_text(text):
    return text.title() if isinstance(text, str) else "N/A"

# Function to capitalize each movie tag properly
def format_tags(tags):
    if isinstance(tags, str):
        return ", ".join([tag.strip().capitalize() for tag in tags.split(",")])
    return "N/A"

# Function to recommend movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]  # Top 5 recommendations

    recommended_movies = []
    for i in movies_list:
        movie_details = movies.iloc[i[0]]

        recommended_movies.append({
            "Title": format_text(movie_details["title"]),
            "About": format_tags(movie_details.get("tags", "N/A"))
        })

    return recommended_movies


# Streamlit UI
st.markdown("<h1 class='stTitle'>🎬 Movie Recommender System</h1>", unsafe_allow_html=True)

selected_movie_name = st.selectbox("🔍 Select a movie:", movies['title'].values)

if st.button('🎥 Recommend'):
    recommendations = recommend(selected_movie_name)
    st.markdown(f"<h1 class='section-title'> 🔥Top 5 Recommendations:</h1>", unsafe_allow_html=True)


    # Display movie recommendations with styling
    for movie in recommendations:
        st.markdown("<div class='movie-box'>", unsafe_allow_html=True)
        st.markdown(f"<p class='movie-title'>🎬 {movie['Title']}</p>", unsafe_allow_html=True)
        st.write(f"🎭 **About:** {movie['About']}")
        st.markdown("---")  # Separator between movies
