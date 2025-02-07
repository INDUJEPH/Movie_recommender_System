This Movie Recommender System is built using Streamlit, Pandas, and Pickle to suggest similar movies based on user input. It leverages a precomputed similarity matrix to provide recommendations efficiently.

Features:


    User-Friendly Interface:

      Clean white-themed UI for a simple and elegant experience.

      Uses a dropdown select box for easy movie selection.

      Styled buttons for better interaction.


    Efficient Movie Recommendation:

      Accepts a movie title, converts it to lowercase for case-insensitive search.

      Retrieves the top 5 most similar movies using a precomputed similarity matrix.

      Displays recommendations with ✅ markers for better readability.


    Technical Overview:

     Loads movie data from movie_dict.pkl and similarity scores from similarity.pkl.

     Uses Pandas DataFrame for efficient filtering and processing.

     Sorts similarity scores and extracts the top 5 recommendations.
