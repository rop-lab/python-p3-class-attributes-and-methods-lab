class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment the count and call instance methods to update other attributes
        Song.count += 1
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()

    def add_to_genres(self):
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

    def add_to_artists(self):
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

    def add_to_genre_count(self):
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1

    def add_to_artist_count(self):
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1

# Example usage
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
print(ninety_nine_problems.name)  # "99 Problems"
print(ninety_nine_problems.artist)  # "Jay-Z"
print(ninety_nine_problems.genre)  # "Rap"

print(Song.count)  # 1
print(Song.genres)  # ["Rap"]
print(Song.artists)  # ["Jay-Z"]
print(Song.genre_count)  # {"Rap": 1}
print(Song.artist_count)  # {"Jay-Z": 1}
