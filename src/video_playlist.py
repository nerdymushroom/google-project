"""A video playlist class."""

class Playlist:
    """A class used to represent a Playlist."""
    def __init__(self):
        """The Playlist class is initialized."""
        self._playlists = {}

    def get_all_playlists(self):
        """Returns all available video information from the video library."""
        return list(self._playlists.values())

    def get_playlist(self, playlist_name):
        """Returns playlists as objects."""
        return self._playlists.get(playlist_name, None)