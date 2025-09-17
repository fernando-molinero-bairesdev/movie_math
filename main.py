from movies.movie import Movie


movie_list = [
    [1, 9.2, "The Godfather", True],
    [2, 9.0, "The Godfather Part II", True],
    [3, 7.6, "The Godfather Part III", False],
    [4, 8.4, "Avengers: Endgame", True],
    [5, 3.6, "The Room", False],
    [6, 1.9, "Manos: The Hands of Fate", False],
    [7, 2.9, "Troll 2", False],
    [8, 8.0, "A Special Day", True],
    [9, 9.0, "The Dark Knight", True],
    [10, 8.6, "Pulp Fiction", True],
    [11, 8.8, "Schindler's List", True],
    [12, 8.6, "Inception", True],
    [13, 9.3, "The Shawshank Redemption", True],
    [14, 8.1, "Gladiator", True],
    [15, 8.5, "Parasite", True],
    [16, 8.2, "Whiplash", True],
    [17, 8.5, "Interstellar", True],
    [18, 8.4, "The Prestige", True],
    [19, 8.6, "Mad Max: Fury Road", True],
    [20, 8.3, "The Silence of the Lambs", True]
]

def check_order(data_list):
    for i in range(1, len(data_list)):
        try:
             assert data_list[i-1].rating >= data_list[i].rating
        except Exception:
            raise ValueError(data_list[i-1],'should have a better score than' ,data_list[i])

movies = Movie.top(movie_list)
ordered_fresh_full = Movie.top(movie_list,20, True)
ordered_rotten = Movie.top(movie_list, fresh=False)
all = Movie.top(movie_list, 20, None)
print("\n---------------------------------")
print("TOP TEN FRESH")
print(movies)

print("\n---------------------------------")
print("TOP TWENTY FRESH")
print(ordered_fresh_full)

print("\n---------------------------------")
print("TOP TWENTY ROTTEN")
print(ordered_rotten)

print("\n---------------------------------")
print("ALL")
print(all)

check_order(movies)
check_order(ordered_fresh_full)
check_order(ordered_rotten)
check_order(all)

assert len(movies) == 10
assert len(ordered_fresh_full) == 16
assert len(ordered_rotten) == 4
assert len(all) == 20