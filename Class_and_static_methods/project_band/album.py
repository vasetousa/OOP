from song import Song
from typing import List

class Album:
    def __init__(self, album_name: str, *song_names):
        self.song_names:  List[Song] =  list(song_names)
        self.album_name = album_name
        self.published = False

    def add_song(self, song: Song):
        if self.published:
            return "Cannot add songs. Album is published."
        if song.single:
            return f"Cannot add {song.s_name}. It's a single"
        elif song not in self.song_names:
            self.song_names.append(song)
            return f"Song {song.s_name} has been added to the album {self.album_name}."
        return "Song is already in the album."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."
        elif song_name not in self.song_names:
            return "Song is not in the album."
        self.song_names.remove(song_name)
        return f"Removed song {song_name} from album {self.album_name}."

    def publish(self):
        if self.published:
            return f"Album {self.album_name} is already published."
        self.published = True
        return f"Album {self.album_name} has been published."

    def details(self):
        songs_info = [f'Album {self.album_name}']
        nr = '\n'

        for s in self.song_names:
            songs_info.append(f"== {s.get_info()}")
        return nr.join(songs_info) + nr

