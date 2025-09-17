from dataclasses import dataclass


@dataclass
class Movie:
    """
    Represents a movie 
    Attributes:
        id (int): A unique identifier
        rating(float): A number from 1 to 10 to represent the relative score of the movie
        movie_title: The movie title is the name of the movie
        certified_fresh: is whether or not the movie is considered a movie by most criticts
    """
    id: int
    rating: float
    movie_title: str
    certified_fresh: bool

    def __repr__(self):
        return f"{self.movie_title} ({self.rating}) "

    def __str__(self):
        return self.__repr__()

    @classmethod
    def _from_list(cls, movie):
        # TODO Validate Movie creation, easiest way could be with pydantic
        return Movie(movie[0], movie[1], movie[2], movie[3])        

    @classmethod
    def top(cls, movies, n=10, fresh=True):
        """
        The function returns the top n movies
        ordered by their score from top to bottom

        Parameters:
            movies: the list of movies sent as a list of lists
                where the inner list has the fields in the correct order
                example: movie_list = [[1, 9.0, 'Insterstellar', True], [2, 8.5, 'Fast and the Furious', True]]
            n: this is the number of movies I want returned,
                if not set 10 is the default value
            fresh: this filters if I want fresh movies,
                not fresh movies or all (for this pass on the None value)

        """
        # TODO When the database is implemented
        # this method should use the db to retrieve the data in the correct order
        movies = [Movie._from_list(m) for m in movies]
        if fresh is not None:
              movies = [m for m in movies if m.certified_fresh == fresh]
        result = sorted(movies, key=lambda m: m.rating, reverse=True)
        return result[:n]
