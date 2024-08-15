"""
Logic class for filter with mutiple data
"""
from typing import Dict, List
from config.filter_by import FilterBy
from model.movie import Movie

class FilterData:
    def filterBy(self, movies: List[Movie], filter_by: Dict[FilterBy, str]):
        enum_keys = {e.name for e in FilterBy}
        keys_not_in_enum = set(filter_by.keys()) - enum_keys
        if keys_not_in_enum:
                raise KeyError("Key not found")
        for key, value in filter_by.items():
            if key == FilterBy.year.value:
                movies = [movie for movie in movies if movie.release_year == int(value)]
            if key == FilterBy.director.value:
                movies = [movie for movie in movies if movie.director == value]
            if key == FilterBy.genre.value:
                movies = [movie for movie in movies if movie.genre == value]
                
        return movies