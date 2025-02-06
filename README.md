# Movie Recommender System

## Overview

This project is a personalized movie recommender system that leverages machine learning techniques to suggest movies based on user input. The application provides detailed information about each movie such as tags and a brief synopsis via an interactive web interface built with Python and Streamlit. The system is designed to help users discover new movies that match their interests by analyzing movie similarities based on features extracted from a movie dataset.

## Features

- **Personalized Recommendations:**  
  Suggest movies based on similarity metrics derived from user-selected movies.

- **Detailed Movie Information:**  
  Display key details for each movie, including formatted tags and a synopsis that describes the movie's essence.

- **Interactive and Responsive UI:**  
  A modern, dark-themed interface with custom fonts and well-structured layouts, ensuring a user-friendly experience.

- **Easy Setup and Deployment:**  
  Quick installation using a virtual environment and dependencies managed through `requirements.txt`. The application can be easily run with a single command using Streamlit.

- **Extensible Design:**  
  The code structure allows for further enhancements (e.g., integrating additional movie details, refining the recommendation algorithm, or adding more interactive features).

## Technology Stack

- **Python 3.9+**  
  The primary programming language used for backend development.

- **Streamlit**  
  For building the interactive web application interface.

- **Pandas & Pickle**  
  For data manipulation and loading precomputed similarity matrices and movie datasets.

- **Scikit-learn** (or similar libraries)  
  For calculating movie similarity and processing features (if applicable).

## Installation and Setup

### Prerequisites

- **Python 3.9 or later:** Ensure Python is installed on your machine.
- **Git:** For cloning the repository.

### Steps

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. **Set up a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**

    ```bash
    streamlit run app.py
    ```

## Usage

1. **Select a Movie:**  
   When the application starts, use the dropdown menu to select a movie from the dataset.

2. **Generate Recommendations:**  
   Click the **Recommend** button to see the top 5 recommendations based on the selected movie. The system displays each recommendation with its title and a brief summary of associated tags.

3. **View Detailed Information:**  
   Use the interactive radio buttons to select any recommended movie. Detailed information about the selected movie is then displayed in a well-formatted paragraph.

4. **Explore and Enjoy:**  
   The recommender system is designed for exploration—feel free to experiment with different movies and discover new ones that match your taste.

## Project Structure
- **app.py** # Main application file
- **movie_dict.pkl** # Pickle file containing the movie dataset
- **similarity.pkl** # Pickle file with the precomputed similarity matrix
- **requirements.txt** # Python dependencies for the project
- **README.md** # A description of what the project is, its purpose, and its key features.
- **.gitignore** # Git ignore file for excluding unnecessary files

## Movie Recommender Screenshort

![Screenshot 2025-02-06 212643](https://github.com/user-attachments/assets/ac2b93f0-a732-4fee-99d7-3e7de2549aaf)
![Screenshot 2025-02-06 212816](https://github.com/user-attachments/assets/36d510cb-1f47-4fb3-afe2-dd0017f86a20)
  
## How It Works

- **Data Loading:**  
  The system loads a preprocessed movie dataset and a similarity matrix (computed using techniques such as cosine similarity on movie tags).

- **Recommendation Algorithm:**  
  When a user selects a movie, the system retrieves its index in the dataset, computes similarity scores with all other movies, and returns the top 5 recommendations.

- **Text Formatting:**  
  Movie titles and tags are formatted for readability using custom functions to ensure proper capitalization and spacing.

## Contributing

Contributions are welcome! If you have suggestions for improvements or encounter any issues, please follow these steps:

## Acknowledgments
- **Inspiration & Tutorials:**
This project was inspired by various machine learning and web development tutorials.
- **Community Resources:**
Special thanks to the open-source community for their valuable resources and support.
- **Frameworks & Libraries:**
Gratitude to the developers of Streamlit, Pandas, and scikit-learn, which made this project possible.

Happy Coding! Enjoy exploring movies with this recommender system.
