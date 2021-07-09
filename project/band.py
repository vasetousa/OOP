from album import Album
from typing import List

class Band:
    def __init__(self, band_name: str):
        self.band_name = band_name
        self.album_list: List[Album] = []

    def add_album(self, album: Album):
        if album not in self.album_list:
            self.album_list.append(album)
            return f"Band {self.band_name} has added their newest album {album.album_name}."
        return f"Band {self.band_name} already has {album.album_name} in their library."

    def remove_album(self, album_name):
        for album in self.album_list:
            if album.album_name == album_name:
                if album.published:
                    return "Album has been published. It cannot be removed."
            self.album_list.remove(album_name)
            return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."


    def details(self):
        band_info = [f'Band {self.band_name}']
        nr = '\n'

        for alb in self.album_list:
            band_info.append(alb.details())
        return nr.join(band_info) + nr