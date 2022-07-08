import json
import keyboard
import sys
from API.API import API


# CHANGE DICTIONARY FOR CUSTOM KEYMAPS
KEYMAPS = {
    "exit": ["alt", "esc"],
    "play_pause": ["ctrl", "alt", "space"],
    "next_song": ["ctrl", "alt", "right"],
    "previous_song": ["ctrl", "alt", "left"],
    "like_song": ["ctrl", "alt", "up"],
    "dislike_song": ["ctrl", "alt", "down"],
    "empty_playlist": ["ctrl", "alt", "p"],
}

# DO NOT CHANGE BELOW THIS LINE


def check_for_keypress(api: API) -> None:
    def check_playback_state():
        is_playing = api.is_playing()
        if is_playing:
            api.pause_song()
        else:
            api.resume_song()

    keyboard.add_hotkey("+".join(KEYMAPS["next_song"]), lambda: api.next_song())
    keyboard.add_hotkey("+".join(KEYMAPS["previous_song"]), lambda: api.previous_song())
    keyboard.add_hotkey("+".join(KEYMAPS["like_song"]), lambda: api.like_song())
    keyboard.add_hotkey("+".join(KEYMAPS["dislike_song"]), lambda: api.dislike_song())
    keyboard.add_hotkey(
        "+".join(KEYMAPS["empty_playlist"]), lambda: api.clear_liked_playlist()
    )
    keyboard.add_hotkey("+".join(KEYMAPS["play_pause"]), lambda: check_playback_state())

    keyboard.wait("+".join(KEYMAPS["exit"]))


if __name__ == "__main__":
    try:
        with open("secrets.json", "r") as in_file:
            file = json.load(in_file)
    except FileNotFoundError:
        with open("secrets.json", "w+") as new_file:
            json.dump(
                {
                    "spotify_client_id": "",
                    "spotify_client_secret": "",
                    "spotify_liked_id": "",
                },
                new_file,
            )
            file = json.load(new_file)

    if file["spotify_liked_id"] == "":
        liked_id = input(
            "please input link to playlist that you would like to act as a buffer\n>>>"
        )
        liked_id = liked_id.split("/")[-1].split("?")[0]
        file["spotify_liked_id"] = liked_id
        with open("secrets.json", "w") as out_file:
            json.dump(file, out_file)

    api = API()
    print("RUNNING PROGRAM")
    check_for_keypress(api)
    print("STOPPING PROGRAM")
