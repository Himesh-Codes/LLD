"""
Core model for director entity to represent data
"""
from movie import Movie

class Director:
    def __init__(self, name: str):
        self.name = name
        self.movies = []

    def add_movie(self, movie: Movie):
        self.movies.append(movie)