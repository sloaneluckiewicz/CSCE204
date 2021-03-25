def getMovies():
    movies = []
    # empty lists []
    # list with stuff inside ()

    # get movies from file
    try:
        with open("exercises/mar23/movies.txt") as file:
            for line in file:
                movie = line.replace("\n", "")
                movies.append(movie)
            return movies
    except FileNotFoundError:
        print("The movie file could not be located. Check permissions. ")
        return movies # returns the empty array or list on line 2, a list of nothing

# using my movie program 
print("Awesome movies:")
movies = getMovies()

for movie in movies:
    print(movie)