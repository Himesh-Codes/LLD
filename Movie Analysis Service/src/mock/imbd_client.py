"""
Class is to mock the IMDBClient simulates fetching data from an IMDB-like API.
"""
import random
from typing import List, Optional
from model.movie import Movie

class IMDBClient:
    def __init__(self):
        self.movies = self._mock_data()

    def search_movies(self, query: Optional[str] = None, genre: Optional[str] = None, year: Optional[int] = None) -> List[Movie]:
        results = []
        if not query and not genre and not year:
            return self.movies
        for movie in self.movies:
            if (query and query.lower() in movie.title.lower()) or \
               (genre and genre.lower() == movie.genre.lower()) or \
               (year and year == movie.release_year):
                results.append(movie)
        return results

    def get_movie_details(self, title: str) -> Optional[Movie]:
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                return movie
        return None

    def _mock_data(self) -> List[Movie]:
        genres = ["Action", "Drama", "Comedy", "Horror", "Sci-Fi"]
        directors = ["Director A", "Director B", "Director C"]
        movies = []
        for i in range(100):
            movies.append(
                Movie(
                    title=f"Movie {i}",
                    release_year=2010 + (i % 10),
                    genre=random.choice(genres),
                    director=random.choice(directors),
                    rating=round(random.uniform(1, 10), 1)
                )
            )
        return movies
