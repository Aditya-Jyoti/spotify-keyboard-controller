import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from typing import List


class API:
    def __init__(self) -> None:
        with open("secrets.json", "r") as file:
            file = json.load(file)
            client_id = file["spotify_client_id"]
            client_secret = file["spotify_client_secret"]
            playlist_id = file["spotify_liked_id"]

        if client_id == "" or client_secret == "":
            client_id = input("please enter your client ID\n>>>")
            client_secret = input("please enter your client secret\n>>>")
            with open("secrets.json", "w") as file:
                json.dump(
                    {
                        "spotify_client_id": client_id,
                        "spotify_client_secret": client_secret,
                    },
                    file,
                )

        scopes = [
            "playlist-modify-public",
            "playlist-modify-private",
            "user-library-read",
            "user-read-private",
            "user-modify-playback-state",
            "user-read-currently-playing",
            "user-read-playback-state",
        ]

        self.spotify = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=client_id,
                client_secret=client_secret,
                redirect_uri="http://example.com/callback/",
                scope=" ".join(scopes),
            )
        )
        self.liked_playlist = playlist_id

    def read_playlist_content(self, id_: str) -> List[str]:
        song_ids = []

        result = self.spotify.playlist(id_)
        if not result:
            raise RuntimeError(f"could not find the playlist at id: {id_}")

        for song in result["tracks"]["items"]:
            song_id = song["track"]["id"]
            song_ids.append(song_id)

        return song_ids

    def is_playing(self) -> bool:
        return self.spotify.current_playback()["is_playing"]

    def next_song(self) -> bool:
        return self.spotify.next_track()

    def previous_song(self) -> bool:
        return self.spotify.previous_track()

    def pause_song(self) -> bool:
        return self.spotify.pause_playback()

    def resume_song(self) -> bool:
        return self.spotify.start_playback()

    def like_song(self) -> bool:
        current_song = self.spotify.current_user_playing_track()["item"]["id"]
        return self.spotify.playlist_add_items(self.liked_playlist, [current_song])

    def dislike_song(self) -> bool:
        current_song = self.spotify.current_user_playing_track()["item"]["id"]
        if current_song in self.read_playlist_content(self.liked_playlist):
            return self.spotify.playlist_remove_all_occurrences_of_items(
                self.liked_playlist, [current_song]
            )
        else:
            return False

    def clear_liked_playlist(self) -> bool:
        songs = self.read_playlist_content(self.liked_playlist)
        return self.spotify.playlist_remove_all_occurrences_of_items(
            self.liked_playlist, songs
        )
