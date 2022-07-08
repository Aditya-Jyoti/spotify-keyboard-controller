# spotify-keyboard-controller

This program is a keyboard controller for spotify. The program takes control of the keyboard and on press of certain hotkeys can do various things with spotify like play, pause, next etc

**Note: the program is still in beta phase so bugs may occur**

### How to run:

1. Please check the [installation guide](https://github.com/Reverend-Toady/spotify-keyboard-controller/blob/main/installation.md)

2. Download necessary requirements

   - for linux
   - `$ sudo pip3 install -r requirements.txt`
   - for windows/mac
   - `$ pip3 install -r requirements.txt`

3. Run the program
   - for linux
   - `$ sudo python3 main.py`
   - for windows/mac
   - `$ py main.py`

### Keymaps:

| Sno |         Keymap         |              Action               |
| :-: | :--------------------: | :-------------------------------: |
| 01  |       `alt+esc`        |         quit the program          |
| 02  |    `ctrl+alt+space`    |        play or pause song         |
| 03  | `ctrl+alt+right_arrow` |         skip to next song         |
| 04  | `ctrl+alt+left_arrow`  |       skip to previous song       |
| 05  |  `ctrl+alt+up_arrow`   |  add current song to a playlist   |
| 06  | `ctrl+alt+down_arrow`  | remove current song from playlist |
| 07  |      `ctrl+alt+p`      |      empty out the playlist       |

**Note: all keymaps can be changed by changing the [KEYMAPS](https://github.com/Reverend-Toady/spotify-keyboard-controller/blob/43b3ff25a0b226543fc47ee1d852efc39da50763/main.py#L8-L16) dictionary in `main.py`**

### After thoughts:

please do open issues relating to bugs and new feature ideas
