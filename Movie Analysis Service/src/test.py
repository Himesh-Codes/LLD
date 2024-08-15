"""
Test cases
"""
from movie_analytics import MovieAnalyticsAPI
from config.aggregated_data_type import AggregratedDataType


def main():
    api = MovieAnalyticsAPI()

    # Search for movies
    print("Searching for movies released in 2015...")
    print(api.search_movies(year=2015))

    # View movie details
    print("\nViewing details of 'Movie 5'...")
    print(api.get_movie_details("Movie 5"))

    # Aggregate data
    print("\nAggregating data: Movies per year...")
    print(api.get_aggregated_data(AggregratedDataType.MOVIES_PER_YEAR))

    print("\nAggregating data: Average ratings per genre...")
    print(api.get_aggregated_data(AggregratedDataType.AVERAGE_RATING_PER_GENRE))

    print("\nAggregating data: Most prolific directors...")
    print(api.get_aggregated_data(AggregratedDataType.MOST_PROLIFIC_DIRECTORS))

    # Get chart details
    print("\nGetting chart details: Movies per year...")
    chart_data = api.get_chart_details(AggregratedDataType.MOVIES_PER_YEAR)
    print(chart_data)

    print("\nGetting chart details: Average ratings per genre with filtering only genre...")
    chart_data = api.get_chart_details(AggregratedDataType.AVERAGE_RATING_PER_GENRE, filter_by={"genre": "Action"})
    print(chart_data)

    print("\nGetting chart details: Average ratings per genre with filtering genre and year...")
    chart_data = api.get_chart_details(AggregratedDataType.AVERAGE_RATING_PER_GENRE, filter_by={"genre": "Action", "year": "2015"})
    print(chart_data)

if __name__ == "__main__":
    main()
