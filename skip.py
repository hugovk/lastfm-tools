#!/usr/bin/env python
"""
Check what BBC radio station iTunes/Winamp is now playing.
Stop playing until the next track starts.
"""
from __future__ import print_function
import subprocess
import time
from mylast import print_track
from sys import platform as _platform


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

        if w.getPlayingStatus() == 'playing':

            # Is Winamp playing BBC Radio?
            now_playing = w.getCurrentTrackName()
            if "bbc" not in now_playing.lower():
                print("Winamp:      Not BBC")
            else:
                if "BBC Radio 1" in now_playing:
                    station = "bbcradio1"
                elif "BBC 1Xtra" in now_playing:
                    station = "bbc1xtra"
                elif "BBC Radio 2" in now_playing:
                    station = "bbcradio2"
                elif ("BBC 6Music" in now_playing or
                      "BBC 6 Music" in now_playing or
                      "bbc 6music" in now_playing):
                    station = "bbc6music"
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
        count = int(osascript([
            "osascript",
            "-e", "tell application \"System Events\"",
            "-e", "count (every process whose name is \"iTunes\")",
            "-e", "end tell"]))
        if count == 0:
            output("iTunes:      not running")
        else:

            # Is iTunes playing?
            state = osascript([
                "osascript",
                "-e", "tell application \"iTunes\" to player state as string"
                ])

            if state != "playing":
                output("iTunes:      " + state)
            else:

                # Is iTunes playing BBC Radio?
                now_playing = osascript([
                    "osascript",
                    "-e", "tell application \"iTunes\"",
                    "-e", "set thisTitle to name of current track",
                    "-e", "set output to thisTitle",
                    "-e", "end tell"])
                if "BBC Radio" not in now_playing:
                    print("iTunes:      Not BBC")
                else:
                    if "BBC Radio 1" in now_playing:
                        station = "bbcradio1"
                    elif "BBC Radio 1Xtra" in now_playing:
                        station = "bbc1xtra"
                    elif "BBC Radio 2" in now_playing:
                        station = "bbcradio2"
                    elif "BBC Radio 6 Music" in now_playing:
                        station = "bbc6music"
    return station


def get_recent_tracks(username, number):
    recent_tracks = lastfm_network.get_user(
        username).get_recent_tracks(limit=number)
    for track in recent_tracks:
        print_track(track)
    return recent_tracks


def lastfm_now_playing(station):
    recent_tracks = lastfm_network.get_user(station).get_recent_tracks(limit=2)
    last = recent_tracks[0]
    return last


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


def osascript(args):
    return subprocess.check_output(args).strip()


def itunes_stop():
    if _platform == "darwin":
        return osascript([
            'osascript',
            '-e', 'tell application "iTunes" to pause'])


def itunes_play():
    if _platform == "darwin":
        return osascript([
            'osascript',
            '-e', 'tell application "iTunes" to play'])


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


def thing():
    init()

    station = media_player_now_playing()
    print(station)
    if station is None:
        return

    skip = lastfm_now_playing(station)
    print_track(skip)

    media_player_stop()

    while(True):
        try:
            time.sleep(5)
            now = lastfm_now_playing(station)
            print(".", end="")
            if now != skip:
                print()
                print_track(now)
                break

        except:
            break

    media_player_play()


if __name__ == "__main__":

    thing()

# End of file
