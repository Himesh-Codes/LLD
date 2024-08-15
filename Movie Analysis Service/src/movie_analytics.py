"""
Class will be the central point for client interactions.
Serves as a facade, simplifying client interactions with the system. 
It delegate client requests to appropriate subsystem objects.

It handles the dependency injection to avoid multiple instances for repository, service, client.
"""
from typing import Optional, List, Dict
from client.movie_repository import MovieRepository
from mock.imbd_client import IMDBClient
from service.movie_service  import MovieService
from config.aggregated_data_type import AggregratedDataType

class MovieAnalyticsAPI:
    def __init__(self):
        self.client = IMDBClient()
        self.repository = MovieRepository(self.client)
        self.movie_service = MovieService(self.repository)

    def search_movies(self, query: Optional[str] = None, genre: Optional[str] = None, year: Optional[int] = None) -> List[str]:
        movies = self.movie_service.search_movies(query, genre, year)
        return [str(movie) for movie in movies]

    def get_movie_details(self, title: str) -> Optional[str]:
        movie = self.movie_service.get_movie_details(title)
        return str(movie) if movie else None

    def get_aggregated_data(self, aggregation_type: AggregratedDataType) -> Dict[str, float]:
        if aggregation_type == AggregratedDataType.MOVIES_PER_YEAR:
            return self.movie_service.aggregate_movies_per_year()
        elif aggregation_type == AggregratedDataType.AVERAGE_RATING_PER_GENRE:
            return self.movie_service.aggregate_average_ratings_per_genre()
        elif aggregation_type == AggregratedDataType.MOST_PROLIFIC_DIRECTORS:
            return self.movie_service.aggregate_most_prolific_directors()
        else:
            raise ValueError("Invalid aggregation type")

    def get_chart_details(self, aggregation_type: str, filter_by: Optional[Dict[str, str]] = None) -> Dict[str, List]:
        return self.movie_service.get_chart_data(aggregation_type, filter_by)