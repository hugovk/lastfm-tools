#!/usr/bin/env python3
"""
Check what BBC radio station iTunes/Winamp is now playing.
Stop playing until the next track starts.
"""
import time
from sys import platform as _platform

import bbcrealtime
from bbcscrobbler import normalise_station, osascript, output


def winamp_now_playing():
    """
    If not Windows, return None.
    If Windows, return BBC station Winamp is now playing or None.
    """
    global w
    station = None
    if _platform != "win32":
        return None

    else:
        # Is Winamp playing?

        if w.getPlayingStatus() == "playing":

            # Is Winamp playing BBC Radio?
            now_playing = w.getCurrentTrackName()
            if "bbc" not in now_playing.lower():
                print("Winamp:      Not BBC")
            else:
                station = normalise_station(now_playing)
    return station


def itunes_now_playing():
    """
    If not Mac, return None.
    If Mac, return BBC station iTunes is now playing or None.
    """
    station = None
    if _platform != "darwin":
        return None

    else:

        # Is iTunes running?
        count = int(
            osascript(
                "osascript "
                "-e 'tell application \"System Events\"' "
                "-e 'count (every process whose name is \"iTunes\")'"
                " -e 'end tell'"
            )
        )
        if count == 0:
            output("iTunes:      not running")
        else:

            # Is iTunes playing?
            state = osascript(
                "osascript "
                "-e 'tell application \"iTunes\" to player state as string'"
            )

            if state != "playing":
                output("iTunes:      " + state)
            else:
                # Is iTunes playing BBC Radio?
                now_playing = osascript(
                    "osascript "
                    "-e 'tell application \"iTunes\"' "
                    "-e 'set thisTitle to name of current track' "
                    "-e 'set output to thisTitle' "
                    "-e 'end tell'"
                )
                if "bbc" not in now_playing.lower():
                    output("iTunes:      Not BBC")
                else:
                    station = normalise_station(now_playing)
    return station


def init():
    if _platform == "win32":
        global w
        import winamp  # http://www.shalabh.com/software/about_winamp_py.html

        w = winamp.winamp()


def media_player_now_playing():
    if _platform == "darwin":
        return itunes_now_playing()
    elif _platform == "win32":
        return winamp_now_playing()
    else:
        return None


def itunes_stop():
    if _platform == "darwin":
        return osascript("osascript -e 'tell application \"iTunes\" to pause'")


def itunes_play():
    if _platform == "darwin":
        return osascript("osascript -e 'tell application \"iTunes\" to play'")


def media_player_stop():
    global w
    if _platform == "darwin":
        return itunes_stop()
    elif _platform == "win32":
        w.stop()
    else:
        return None


def media_player_play():
    global w
    if _platform == "darwin":
        return itunes_play()
    elif _platform == "win32":
        w.play()
    else:
        return None


def format_track(track):
    out = "{} - {}".format(track["artist"], track["title"])
    return out


def thing():
    init()

    station = media_player_now_playing()
    print("Station:", station)
    if station is None:
        return

    skip = bbcrealtime.nowplaying(station)
    if skip is None:
        return

    skip = format_track(skip)
    print(skip)

    media_player_stop()

    while True:
        try:
            time.sleep(5)
            now = bbcrealtime.nowplaying(station)
            now = format_track(now)
            # print(now)
            print(".", end="")
            if now != skip:
                print()
                print(now)
                break

        except BaseException:
            break

    media_player_play()


if __name__ == "__main__":

    thing()

# End of file
