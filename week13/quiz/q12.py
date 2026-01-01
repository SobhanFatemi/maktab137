class Song:
    def __init__(self, title, duration, genre, track_number):
        self.title = title
        self.duration = duration
        self.genre = genre
        self.track_number = track_number

    def info(self):
        return f"Title: {self.title}, Duration: {self.duration}, Genre: {self.genre}, Track: {self.track_number}"


class Album:
    def __init__(self, title, year, artist, songs = None):
        self.title = title
        self.year = year
        self.artist = artist
        self.songs = [] if not songs else songs

    def add_song(self, song):
        if not isinstance(song, Song):
            print("Not a valid Song!")
            return
        self.songs.append(song)
        print(f"{song.title} was added!")

    def remove_song(self, song):
        if not isinstance(song, Song):
            print("Not a valid Song!")
            return
        if song not in self.songs:
            print("Song was not found!")
            return
        self.songs.remove(song)
        print(f"{song.title} was removed!")

    def total_duration(self):
        duration = 0
        for song in self.songs:
            duration += song.duration
        return duration
    
    def show_songs(self):
        print(f"Songs in album '{self.title}': ")
        for i, song in enumerate(self.songs):
            print(f"{i+1}. {song.title}")

class Artist:
    def __init__(self, name, genre, albums = None):
        self.name = name
        self.genre = genre
        self.albums = [] if albums is None else albums

    def add_album(self, album):
        if not isinstance(album, Album):
            print("Not a valid Album!")
            return
        self.albums.append(album)
        print(f"{album.title} was added!")
    
    def remove_album(self, album):
        if not isinstance(album, Album):
            print("Not a valid album!")
            return
        if album not in self.albums:
            print("album was not found!")
            return
        self.albums.remove(album)
        print(f"{album.title} was removed!")

    def search_song(self, given_song):
        results = []
        for album in self.albums:
            for song in album.songs:
                if given_song.lower() in song.title.lower():
                    results.append((album.title, song))
        return results
                
    def show_all(self):
        for album in self.albums:
            album.show_songs()


if __name__ == "__main__":
    artist = Artist("Hans Zimmer", "Soundtrack")

    album1 = Album("Interstellar", 2014, artist.name)
    album2 = Album("Inception", 2010, artist.name)

    artist.add_album(album1)
    artist.add_album(album2)

    album1.add_song(Song("Cornfield Chase", 120, "Soundtrack", 1))
    album1.add_song(Song("Stay", 240, "Soundtrack", 2))

    album2.add_song(Song("Time", 260, "Soundtrack", 1))
    album2.add_song(Song("Dream is Collapsing", 150, "Soundtrack", 2))

    artist.show_all()

    print("\nSearch Results for 'time':")
    search_results = artist.search_song("time")
    for album_title, song in search_results:
        print(f"- Found in {album_title}: {song.info()}")

    print("\nTotal duration Interstellar:", album1.total_duration(), "seconds")