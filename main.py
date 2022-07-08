import json
import secrets
import keyboard
import math
from datetime import datetime
from API.API import API


# CHANGE DICTIONARY FOR CUSTOM KEYMAPS
KEYMAPS = {
    "exit": ["alt", "esc"],
    "pause": ["space"],
    "play": ["space"],
    "next_song": ["ctrl", "alt", "l"],
    "previous_song": ["ctrl", "alt", "h"],
    "like_song": ["ctrl", "alt", "k"],
    "dislike_song": ["ctrl", "alt", "j"],
    "empty_playlist": ["ctrl", "alt", "p"],
}

# DO NOT CHANGE BELOW THIS LINE

TIMEOUT = 30


def is_playing(api: API) -> bool:
    playback_state = api.is_playing()
    if playback_state:
        return True

    else:
        start_time = datetime.now()
        while not playback_state:
            if keyboard.is_pressed("+".join(KEYMAPS["play"])):
                api.resume_song()
                playback_state = api.is_playing()
                return True

            check = datetime.now() - start_time
            if math.floor(check.total_seconds()) > TIMEOUT:
                playback_state = api.is_playing()
                start_time = datetime.now()
        else:
            return True


if __name__ == "__main__":
    with open("secrets.json", "r") as in_file:
        file = json.load(in_file)
    
    if file["spotify_liked_id"] == "":
        liked_id = input("please input link to playlist to store saved songs\n>>>")
        liked_id = liked_id.split("/")[-1].split("?")[0]
        file["spotify_liked_id"] = liked_id
        with open("secrets.json", "w") as out_file:
            json.dump(file, out_file)

    api = API()
    is_playing_ = is_playing(api)
    start_time = datetime.now()

    while is_playing_:
        if keyboard.is_pressed("+".join(KEYMAPS["exit"])):
            api.pause_song()
            break

        if keyboard.is_pressed("+".join(KEYMAPS["play"])):
            api.pause_song()
            is_playing_ = is_playing(api)

        if keyboard.is_pressed("+".join(KEYMAPS["next_song"])):
            api.previous_song()
        if keyboard.is_pressed("+".join(KEYMAPS["previous_song"])):
            api.next_song()

        if keyboard.is_pressed("+".join(KEYMAPS["like_song"])):
            api.like_song()
        if keyboard.is_pressed("+".join(KEYMAPS["dislike_song"])):
            api.dislike_song()

        if keyboard.is_pressed("+".join(KEYMAPS["empty_playlist"])):
            api.clear_liked_playlist()

        check = datetime.now() - start_time
        if math.floor(check.total_seconds()) > TIMEOUT:
            is_playing_ = is_playing(api)
            start_time = datetime.now()
