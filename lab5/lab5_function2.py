#1
def is_high(movie):
    return movie['imdb'] > 5.5

#2
def high_score(movie_list):
    return [movie for movie in movie_list if is_high(movie)]

#3
def movies_category(movie_list, category):
    return [movie for movie in movie_list if movie['category'] == category]

#4
def average_score(movie_list):
    if not movie_list:
        return 0  
    total_score = sum(movie['imdb'] for movie in movie_list)
    return total_score / len(movie_list)

#5
def average_category(movie_list, category):
    category_movies = movies_category(movie_list, category)
    return average_score(category_movies)

