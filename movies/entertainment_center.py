import media
import fresh_tomatoes

# TODO(Chris) Change intended to dynamically gather each required arguement of
# the class Movie() located in the media.py file.
# My favorite movies. These are instances of the class Movie() that include the
# title, a brief synopsis, box art, and trailer.

# TODO(Chris) Add a list variable that will add each new instance when it is
# created.
john_wick = media.Movie("John Wick",
                        "An ex-hitman comes out of retirement to track down "
                        "the gangsters that took everything from him.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTU2NjA1ODgzMF5BMl5BanBnXkFtZTgwMTM2MTI4MjE@._V1_SY1000_CR0,0,666,1000_AL_.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=C0BMx-qxsP4")


john_wick_2 = media.Movie("John Wick: Chapter 2",
                          "After returning to the criminal underworld to "
                          "repay a debt, John Wick discovers that a large "
                          "bounty has been put on his life.",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BMjE2NDkxNTY2M15BMl5BanBnXkFtZTgwMDc2NzE0MTI@._V1_SY1000_CR0,0,648,1000_AL_.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=ChpLV9AMqm4")

inception = media.Movie("Inception",
                        "A thief, who steals corporate secrets through use "
                        "of dream-sharing technology, is given the inverse "
                        "task of planting an idea into the mind of a CEO.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")

pitch_perfect = media.Movie("Pitch Perfect",
                            "Beca, a freshman at Barden University, is "
                            "cajoled into joining The Bellas, her school's "
                            "all-girls singing group. Injecting some much"
                            "needed energy into their repertoire, The Bellas "
                            "take on their male rival in a campus competition",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BMTcyMTMzNzE5N15BMl5BanBnXkFtZTcwNzg5NjM5Nw@@._V1_SY1000_CR0,0,631,1000_AL_.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=8dItOM6eYXY")

end_of_watch = media.Movie("End of Watch",
                           "Shot documentary-style, this film follows the "
                           "daily grind of two young police officers in LA "
                           "who are partners and friends, and what happens "
                           "when they meet criminal forces greater "
                           "than themselves.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMjMxNjU0ODU5Ml5BMl5BanBnXkFtZTcwNjI4MzAyOA@@._V1_SY1000_CR0,0,647,1000_AL_.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=9mQYxib26FM")

logan = media.Movie("Logan",
                    "In the near future, a weary Logan cares for an ailing "
                    "Professor X, somewhere on the Mexican border. However, "
                    "Logan's attempts to hide from the world, and his legacy, "
                    "are upended when a young mutant arrives, pursued by "
                    "dark forces.",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjQwODQwNTg4OV5BMl5BanBnXkFtZTgwMTk4MTAzMjI@._V1_.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=Div0iP65aZo")


# Defines which instances of class Movie() will be used in the
# open_movies_page method.

movies = [john_wick, john_wick_2, inception,
          pitch_perfect, end_of_watch, logan]

# Generates an HTML file to include the instances of class Movie() defined
# above.

fresh_tomatoes.open_movies_page(movies)
