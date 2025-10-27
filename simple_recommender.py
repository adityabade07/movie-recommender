

movies = {
    "The Matrix": ["sci-fi", "action", "hacker"],
    "Inception": ["sci-fi", "dream", "thriller"],
    "Titanic": ["romance", "drama", "historical"],
    "John Wick": ["action", "revenge", "hitman"],
    "Interstellar": ["sci-fi", "space", "drama"],
    "The Notebook": ["romance", "drama", "love"]
}

def recommend(fav_movie):
    if fav_movie not in movies:
        return "Sorry, movie not found."

    fav_tags = movies[fav_movie]
    print("\nYour favorite movie tags:", fav_tags)

   
    similar_movies = {}

    for movie in movies:
        if movie == fav_movie:
            continue

        match_count = 0
        for tag in movies[movie]:
            if tag in fav_tags:
                match_count += 1

        similar_movies[movie] = match_count

    
    best_match = None
    max_match = 0
    for movie, count in similar_movies.items():
        if count > max_match:
            max_match = count
            best_match = movie

    if max_match > 0:
        return f"You might also like '{best_match}'. (Matched tags: {max_match})"
    else:
        return "No similar movies found."


fav_movie = input("Enter a movie you like: ")
print(recommend(fav_movie))
