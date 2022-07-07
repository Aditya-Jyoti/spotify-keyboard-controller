import time
import keyboard
from API.API import API


def is_playing(api: API) -> bool:
    playback_state = api.is_playing()
    if playback_state:
        return True

    else:
        print("There is no song being played currently, trying again in 30 seconds")
        time.sleep(1)
        return is_playing(api)

if __name__ == "__main__":
    api = API("https://open.spotify.com/playlist/0W7c7SB8ERPBoArb8PqCbJ")
    is_playing_ = is_playing(api) 
    while is_playing_:
        if keyboard.is_pressed("esc"):
            api.pause_song()
            break
        
        if keyboard.is_pressed("space"):
            playback = is_playing_
            if playback is False:
                api.resume_song()
            else:
                api.pause_song()

        if keyboard.is_pressed("ctrl+left"):
            api.previous_song()
        if keyboard.is_pressed("ctrl+right"):
            api.next_song()
        if keyboard.is_pressed("ctrl+up"):
            api.like_song()
        if keyboard.is_pressed("ctrl+down"):
            api.dislike_song()

        is_playing_ = is_playing(api)
        print("playing")
        time.sleep(0.5)