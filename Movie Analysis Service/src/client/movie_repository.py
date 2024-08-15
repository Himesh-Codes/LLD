"""
NOTE: We could implement a cache client for search items, movie name, year, genre. To avoid 
multiple hit on the IMDB API.
Data Access Object (DAO) for IMDB API, abstracts data access logic from the service layer.
(Repository Pattern)

High-level modules like MovieService and MovieAnalyticsAPI should not depend on low-level modules, so
we introduced the abstract repository class in between.
"""
from typing import List, Optional
from model.movie import Movie
from mock.imbd_client import IMDBClient


class MovieRepository:
    def __init__(self, client: IMDBClient):
        self.client = client

    def find_movies(self, query: Optional[str] = None, genre: Optional[str] = None, year: Optional[int] = None) -> List[Movie]:
        return self.client.search_movies(query, genre, year)

    def get_movie_details(self, title: str) -> Optional[Movie]:
        return self.client.get_movie_details(title)