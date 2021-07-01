"""A video player class."""
import random

from .video_library import VideoLibrary
from .video_playlist import Playlist


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._current_video = None
        self._paused_video = None
        self._playlists = Playlist()
        self._all_playlists=list()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")
        #get the list of all videos in the library
        all_videos=self._video_library.get_all_videos()
        #sorting the list in lexicographical order
        all_videos.sort(key=lambda x: x.title)
        #reading the list line by line
        for video in all_videos:
            #converting tags into strings and removing the brackets
            tagString = str(video.tags).strip("()")
            #printing out the list in the format needed
            print(video.title, "(" + video.video_id + ")", "["+ (tagString.translate({39: None})).replace(',', '') + "]")


    def play_video(self, video_id):
        """Plays the respective video. Args: video_id: The video_id to be played."""
        #get video id from the library
        video = self._video_library.get_video(video_id)
        #if library doesn't have the id
        if not video:
            print("Cannot play video: Video does not exist")
            return
        # if such id exists and another video is currently playing
        if self._current_video != None:
            print(f"Stopping video: {self._current_video.title}")
            print('Playing video:' + " " + video.title)
            # changing current video
            self._current_video = video
            self._paused_video = None
        # if no video is playing or paused
        else:
            print('Playing video:' + " " + video.title)
            # changing current video
            self._current_video = video
            self._paused_video = None
            return

    def stop_video(self):
        """Stops the current video."""
        # gets current video variable
        if self._current_video:
            print(f"Stopping video: {self._current_video.title}")
            self._current_video= None
            self._paused_video = None
        else:
            print("Cannot stop video: No video is currently playing")
            return

    def play_random_video(self):
        """Plays a random video from the video library."""
        #get list of all videos from the library
        videos_list=self._video_library.get_all_videos()
        #checking if the list is empty
        if len(videos_list)==0:
            print("No videos available")
            return
        #picking a random video from the list
        self._random_video=random.choice(videos_list)
        #stopping current video if needed
        if self._current_video:
            print(f"Stopping video: {self._current_video.title}")
            print('Playing video:' + " " + self._random_video.title)
            self._current_video= self._random_video
        else:
            print('Playing video:' + " " + self._random_video.title)
            self._current_video = self._random_video
            return


    def pause_video(self):
        """Pauses the current video."""
        # gets current video variable
        if self._paused_video:
            print(f"Video already paused: {self._paused_video.title}")
        else:
            if self._current_video:
                self._paused_video=None
                print(f"Pausing video: {self._current_video.title}")
                self._paused_video=self._current_video
            else:
                print("Cannot pause video: No video is currently playing")
                return
            return


    def continue_video(self):
        """Resumes playing the current video."""
        if not self._current_video:
            print("Cannot continue video: No video is currently playing")
        else:
            if not self._paused_video:
                print("Cannot continue video: Video is not paused")
            else:
                print(f"Continuing video: {self._paused_video.title}")
                self._current_video=self._paused_video
                self._paused_video = None
                return
            return


    def show_playing(self):
        """Displays video currently playing."""
        #if there is a playing video and no paused one
        if self._current_video and not self._paused_video:
            video_info = self._video_library.get_video(self._current_video.video_id)
            tagString = str(video_info.tags).strip("()")
            print('Currently playing: '+ video_info.title + " (" + video_info.video_id + ")", "[" + (tagString.translate({39: None})).replace(',', '') + "]")
        else:
            #no video is playing or paused
            if not self._paused_video:
                print("No video is currently playing")
            #no video is playing but there is a paused one
            else:
                video_info = self._video_library.get_video(self._paused_video.video_id)
                tagString = str(video_info.tags).strip("()")
                print('Currently playing: ' + video_info.title + " (" + video_info.video_id + ")", "[" + (tagString.translate({39: None})).replace(',', '') + "]"+ " - PAUSED")
                return
            return

#===============================================================

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """
        self._all_playlists = self._playlists.get_all_playlists()
        for item in self._all_playlists:
            if playlist_name == item:
                print('Cannot create playlist: A playlist with the same name already exists')
        else:
                print('Successfully created new playlist:' + " " + playlist_name)
                self._all_playlists.append(playlist_name)
                playlist_name=list()
                print(self._all_playlists)


    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.
        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        # get video id from the library
        video = self._video_library.get_video(video_id)
        # if library doesn't have the id
        if not video:
            print("Cannot add video to "+playlist_name+": Video does not exist")
            return
        else:
            self._playlist_name=self._playlist_name.append(video_id)
            print("Added video to "+playlist_name+":" + video_id)

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """

        print("allow_video needs implementation")
