"""
Core model for movie entity to represent data
"""
class Movie:
    def __init__(self, title: str, release_year: int, genre: str, director: str, rating: float):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.director = director
        self.rating = rating

    def __str__(self):
        return f"{self.title} ({self.release_year}) - Genre: {self.genre}, Director: {self.director}, Rating: {self.rating}"
