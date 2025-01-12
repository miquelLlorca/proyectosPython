import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter


def save_genre_histogram(df, filename='genre_histogram_horizontal.png', dpi=600):
    # Flatten the list of genres
    all_genres = [genre for genres_list in df['genres'] for genre in genres_list]

    # Count occurrences of each genre
    genre_counts = Counter(all_genres)

    # Create the DataFrame for plotting
    genre_df = pd.DataFrame(genre_counts.items(), columns=['Genre', 'Count'])

    # Sort genres by frequency
    genre_df = genre_df.sort_values(by='Count', ascending=False)

    # Plot the horizontal bar chart
    plt.figure(figsize=(12, 50))  # Tall figure for better readability
    plt.barh(genre_df['Genre'], genre_df['Count'], color='skyblue')
    plt.xlabel('Frequency')
    plt.ylabel('Genres')
    plt.title('Genre Distribution in Playlist')
    plt.tight_layout(pad=2.0)  # Add extra padding
    plt.gca().invert_yaxis()  # Flip genres to start from the most frequent

    # Save the plot to a file
    plt.savefig(filename, dpi=dpi)
    print(f"Histogram saved to {filename}")


# TODO: change to plotly, create popularity histogram, top artists, release date histogram, length histogram