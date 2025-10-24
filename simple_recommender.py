
movies = {
    "The Matrix": ["sci-fi", "action", "hacker"],
    "Inception": ["sci-fi", "dream", "thriller"],
    "Titanic": ["romance", "drama", "historical"],
    "John Wick": ["action", "revenge", "hitman"],
    "Interstellar": ["sci-fi", "space", "drama"],
    "The Notebook": ["romance", "drama", "love"],
}


def recommend(favorite_movie):
    if favorite_movie not in movies:
        return " Sorry, movie not found."

    fav_tags = set(movies[favorite_movie])
    recommendations = []

    for title, tags in movies.items():
        if title == favorite_movie:
            continue
        score = len(fav_tags.intersection(tags))
        recommendations.append((title, score))

    recommendations.sort(key=lambda x: x[1], reverse=True)
    top_matches = [title for title, score in recommendations if score > 0]

    if top_matches:
        return "You might also like:\n" + "\n".join(top_matches)
    else:
        return " No similar movies found."


fav_movie = input(" Enter a movie you like: ")
print(recommend(fav_movie))

