import json
import random


def get_movies():
    with open("movies.json") as m:
        movies = json.load(m)
    return movies


def get_random_movie(movies):
    random_number = str(random.randint(1, len(movies)))
    movie = movies[random_number]
    return movie


def get_dashed_string(movie):
    dashed_string = str()
    for char in movie:
        if char != " ":
            dashed_string += "-"
        else:
            dashed_string += char
    return dashed_string


def get_occurences(letter, movie):
    return [i for i, ltr in enumerate(movie) if ltr.lower() == letter.lower()]


def play(movie, dashed_string):
    print(dashed_string)
    count = 5
    dashed_string = list(dashed_string)
    while True:
        if count == 0:
            print("You Lost")
            break
        letter = input("Enter a letter : ")
        occurences = get_occurences(letter, movie)
        if occurences:
            for occurence in occurences:
                dashed_string[occurence] = movie[occurence]
            print("".join(dashed_string))
            if "".join(dashed_string) == movie:
                print("You Won")
                exit(0)
        else:
            count -= 1
            print( str(count) + " Lives")


if __name__ == "__main__":
    movies = get_movies()
    movie = get_random_movie(movies)
    dashed_string = get_dashed_string(movie)
    play(movie, dashed_string)