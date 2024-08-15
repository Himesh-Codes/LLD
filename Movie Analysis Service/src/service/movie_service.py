"""
Service layer contains the business logic and switches on the aggregation types (strategy pattern).
Multiple aggregration strategy methods can be implemented by extending the service class.
"""

from typing import List, Dict, Optional
from collections import defaultdict
from client.movie_repository import MovieRepository
from model.movie import Movie
from config.aggregated_data_type import AggregratedDataType
from config.chart_type import ChartType
from config.filter_by import FilterBy
from client.filter_data import FilterData

class MovieService:
    def __init__(self, repository: MovieRepository):
        self.repository = repository
        self.filterclient = FilterData()

    def search_movies(self, query: Optional[str] = None, genre: Optional[str] = None, year: Optional[int] = None) -> List[Movie]:
        return self.repository.find_movies(query, genre, year)

    def get_movie_details(self, title: str) -> Optional[Movie]:
        return self.repository.get_movie_details(title)

    def aggregate_movies_per_year(self, filter_by: Optional[Dict[FilterBy, str]] = None) -> Dict[int, int]:
        movies = self.repository.find_movies()
        try:
            if filter_by:
                movies = self.filterclient.filterBy(movies, filter_by)
        except KeyError:
                print("Invalid filter by key")
                return
        count_per_year = defaultdict(int)
        for movie in movies:
            count_per_year[movie.release_year] += 1
        return dict(count_per_year)

    def aggregate_average_ratings_per_genre(self, filter_by: Optional[Dict[FilterBy, str]] = None) -> Dict[str, float]:
        movies = self.repository.find_movies()
        try:
            if filter_by:
                movies = self.filterclient.filterBy(movies, filter_by)
        except KeyError:
                print("Invalid filter by key")
                return
        genre_ratings = defaultdict(list)
        for movie in movies:
            genre_ratings[movie.genre].append(movie.rating)
        return {genre: sum(ratings)/len(ratings) for genre, ratings in genre_ratings.items()}

    def aggregate_most_prolific_directors(self, filter_by: Optional[Dict[FilterBy, str]] = None) -> Dict[str, int]:
        movies = self.repository.find_movies()
        try:
            if filter_by:
                movies = self.filterclient.filterBy(movies, filter_by)
        except KeyError:
                print("Invalid filter by key")
                return
        director_count = defaultdict(int)
        for movie in movies:
            director_count[movie.director] += 1
        return dict(director_count)
    
    def get_chart_data(self, aggregation_type: AggregratedDataType, filter_by: Optional[Dict[FilterBy, str]] = None) -> Dict[str, List]:
        if aggregation_type == AggregratedDataType.MOVIES_PER_YEAR:
            data = self.aggregate_movies_per_year(filter_by)
            chart_type = ChartType.BAR
            xlabel = "Year"
            ylabel = "Number of Movies"
        elif aggregation_type == AggregratedDataType.AVERAGE_RATING_PER_GENRE:
            data = self.aggregate_average_ratings_per_genre(filter_by)
            chart_type = ChartType.BAR
            xlabel = "Genre"
            ylabel = "Average Rating"
        elif aggregation_type == AggregratedDataType.MOST_PROLIFIC_DIRECTORS:
            data = self.aggregate_most_prolific_directors(filter_by)
            chart_type = ChartType.BAR
            xlabel = "Director"
            ylabel = "Number of Movies"
        
        # Return the data structure for the frontend
        return {
            "chart_type": chart_type.value,
            "data": [{"label": key, "value": value} for key, value in data.items()],
            "xlabel": xlabel,
            "ylabel": ylabel,
            "title": f"{aggregation_type.value} Chart"
        }