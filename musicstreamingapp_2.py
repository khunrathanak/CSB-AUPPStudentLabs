import csv
import pandas as pd
 
class Song:
    def __init__(self, title, artist, album, genre, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.length = length

    def __str__(self):
        return f"{self.title} - {self.artist}"

class MusicLibrary:
    def __init__(self, csv_file="data_music/music_library.csv"):
        self.songs = []
        self.csv_file = csv_file
        self.load_music_library_from_csv()

    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)
            self.update_csv_file()

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            self.update_csv_file()

    def load_music_library_from_csv(self):
        try:
            df = pd.read_csv(self.csv_file)
            self.songs = [Song(*row) for _, row in df.iterrows()]
        except FileNotFoundError:
            # If the file doesn't exist, it will be created when saving
            pass

    def update_csv_file(self):
        df = pd.DataFrame([(song.title, song.artist, song.album, song.genre, song.length) for song in self.songs],
                          columns=["Title", "Artist", "Album", "Genre", "Length"])
        df.to_csv(self.csv_file, index=False)

    def display_all_songs(self):
        try:
            df = pd.DataFrame([(song.title, song.artist, song.album, song.genre, song.length) for song in self.songs],
                              columns=["Title", "Artist", "Album", "Genre", "Length"])
            print("\nAll Songs in the Music Library:")
            print(df)
        except FileNotFoundError:
            print("No songs found in the music library.")

    def get_songs_by_artist(self, artist):
        return [song for song in self.songs if song.artist == artist]

    def get_songs_by_album(self, album):
        return [song for song in self.songs if song.album == album]

    def get_songs_by_genre(self, genre):
        return [song for song in self.songs if song.genre == genre]

    def get_songs_by_title(self, title):
        return [song for song in self.songs if song.title == title]
# I decided not to use csv to store data from playlist because I cannot do it
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)
            print("Song added to playlist")

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print("Song removed from playlist")

    def display_playlist(self):
        try:
            df = pd.DataFrame([(song.title, song.artist, song.album, song.genre, song.length) for song in self.songs],
                              columns=["Title", "Artist", "Album", "Genre", "Length"])
            print(f"\nDisplaying Playlist: {self.name}")
            print(df)
        except FileNotFoundError:
            print(f"Playlist '{self.name}' is empty.")

def main():
    music_library = MusicLibrary()
    playlists = []

    while True:
        print("\nChoose an action:")
        print("1. Add new song to the music library")
        print("2. Get songs by artist")
        print("3. Get songs by album")
        print("4. Get songs by genre")
        print("5. Get songs by title")
        print("6. Display all songs in the music library")
        print("7. Create a new playlist")
        print("8. Add songs to a playlist")
        print("9. Remove song from the music library")
        print("10. Remove song from a playlist")
        print("11. Display all playlists")
        print("12. Display songs in a playlist")
        print("13. Search for songs by artist in playlists")
        print("0. Exit")

        try:
            choice = int(input("Enter your choice (0-13): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        try:
            if choice == 0:
                print("Exiting the program.")
                break
            elif choice == 1:
                new_song = Song(*input("Enter song details (title artist album genre length): ").split())
                music_library.add_song(new_song)
            elif choice == 2:
                artist_to_search = input("Enter the artist to search for: ")
                songs_by_artist = music_library.get_songs_by_artist(artist_to_search)
                print(f"Songs by {artist_to_search}:")
                for song in songs_by_artist:
                    print(song)
            elif choice == 3:
                album_to_search = input("Enter the album to search for: ")
                songs_by_album = music_library.get_songs_by_album(album_to_search)
                print(f"Songs in album '{album_to_search}':")
                for song in songs_by_album:
                    print(song)
            elif choice == 4:
                genre_to_search = input("Enter the genre to search for: ")
                songs_by_genre = music_library.get_songs_by_genre(genre_to_search)
                print(f"Songs in genre '{genre_to_search}':")
                for song in songs_by_genre:
                    print(song)
            elif choice == 5:
                title_to_search = input("Enter the title to search for: ")
                songs_by_title = music_library.get_songs_by_title(title_to_search)
                print(f"Songs with title '{title_to_search}':")
                for song in songs_by_title:
                    print(song)
            elif choice == 6:
                music_library.display_all_songs()
            elif choice == 7:
                playlist_name = input("Enter playlist name: ")
                new_playlist = Playlist(playlist_name)
                playlists.append(new_playlist)
                print(f"Playlist '{new_playlist.name}' created.")
            elif choice == 8:
                playlist_name = input("Enter playlist name: ")
                found_playlist = next((playlist for playlist in playlists if playlist.name == playlist_name), None)
                if found_playlist:
                    title_to_add = input("Enter the title of the song to add: ")
                    song_to_add = next((song for song in music_library.songs if song.title == title_to_add), None)
                    if song_to_add:
                        found_playlist.add_song(song_to_add)
                        print(f"{song_to_add.title} added to {playlist_name}.")
                    else:
                        print(f"Song with title '{title_to_add}' not found in the music library.")
                else:
                    print(f"Playlist with name '{playlist_name}' not found.")
            elif choice == 9:
                title_to_remove = input("Enter the title of the song to remove from the music library: ")
                song_to_remove = next((song for song in music_library.songs if song.title == title_to_remove), None)
                if song_to_remove:
                    music_library.remove_song(song_to_remove)
                    print(f"{song_to_remove.title} removed from the music library.")
                else:
                    print(f"Song with title '{title_to_remove}' not found in the music library.")
            elif choice == 10:
                playlist_name = input("Enter playlist name: ")
                found_playlist = next((playlist for playlist in playlists if playlist.name == playlist_name), None)
                if found_playlist:
                    title_to_remove = input("Enter the title of the song to remove from the playlist: ")
                    song_to_remove = next((song for song in found_playlist.songs if song.title == title_to_remove), None)
                    if song_to_remove:
                        found_playlist.remove_song(song_to_remove)
                        print(f"{song_to_remove.title} removed from {playlist_name}.")
                    else:
                        print(f"Song with title '{title_to_remove}' not found in the playlist.")
                else:
                    print(f"Playlist with name '{playlist_name}' not found.")
            elif choice == 11:
                print("\nAll Playlists:")
                for playlist in playlists:
                    print(playlist.name)
            elif choice == 12:
                playlist_name = input("Enter playlist name: ")
                found_playlist = next((playlist for playlist in playlists if playlist.name == playlist_name), None)
                if found_playlist:
                    found_playlist.display_playlist()
                else:
                    print(f"Playlist with name '{playlist_name}' not found.")
            elif choice == 13:
                artist_to_search = input("Enter the artist to search for: ")
                songs_in_playlists = [song for playlist in playlists for song in playlist.songs if song.artist == artist_to_search]
                if songs_in_playlists:
                    print(f"Songs by {artist_to_search} in playlists:")
                    for song in songs_in_playlists:
                        print(song)
                else:
                    print(f"No songs by {artist_to_search} found in playlists.")
            else:
                print("Invalid choice. Please enter a number between 0 and 13.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
