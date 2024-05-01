#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import shlex
import sys
import time

import pylast
from termcolor import colored  # pip install termcolor

from mylast import lastfm_network, lastfm_username

# Show my now playing song, or that of a given username
# Prerequisites: mylast.py, pyLast


last_output = None


def output(text: str, type: str | None = None) -> None:
    global last_output
    if last_output == text:
        return
    else:
        last_output = text
    if type == "error":
        print(colored(text, "red"))
    else:
        print(text)


def say(thing: str) -> None:
    cmd = f"say {shlex.quote(str(thing))}"
    os.system(cmd)


def is_track_loved(track: pylast.Track) -> str:
    """
    Input: Track
    If loved, return track string with a heart
    else return track string
    """
    text = f"{track.artist} - {colored(track.title, attrs=['bold'])}"
    try:
        if track:
            loved = track.get_userloved()
            if loved:
                heart = colored("❤", "red")
                return f"{text} {heart}"
    except (
        # KeyError,
        # pylast.MalformedResponseError,
        # pylast.NetworkError,
        pylast.WSError,
    ) as e:
        output("is_track_loved", "error")
        output(f"Error: {repr(e)}", "error")
        print(dir(e))
        output(e.message, "error")

    return text


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Show my now playing song, or that of a given username",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "username",
        nargs="?",
        default=lastfm_username,
        help="Show now playing of this username",
    )
    parser.add_argument("--loop", action="store_true", help="Loop until Ctrl-C")
    parser.add_argument("--say", action="store_true", help="Announcertron 4000")
    args = parser.parse_args()

    if not args.loop:
        now_playing = lastfm_network.get_user(args.username).get_now_playing()
        if type(now_playing) is pylast.Track:
            output(is_track_loved(now_playing))
            if args.say:
                say(now_playing)
        else:
            output("No track currently playing")

    else:
        last_played = None
        while True:
            try:
                now_playing = lastfm_network.get_user(args.username).get_now_playing()
                # output("last:", last_played)
                # output("now: ", now_playing)
                if now_playing != last_played:
                    last_played = now_playing
                    if now_playing:
                        output(is_track_loved(now_playing))
                        if args.say:
                            say(now_playing)

                time.sleep(15)
            except (
                # KeyError,
                pylast.MalformedResponseError,
                pylast.NetworkError,
                pylast.WSError,
            ) as e:
                output(f"Error: {e}", "error")
            except KeyboardInterrupt:
                sys.exit()


if __name__ == "__main__":
    main()
