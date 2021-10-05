#!/usr/bin/env python3
import argparse
import os
import shlex
import time

from mylast import lastfm_network, lastfm_username

# Show my now playing song, or that of a given username
# Prerequisites: mylast.py, pyLast


def say(thing):
    cmd = f"say {shlex.quote(str(thing))}"
    os.system(cmd)


if __name__ == "__main__":
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
        print(now_playing)
        if args.say:
            say(now_playing)
    else:
        last_played = None
        while True:
            now_playing = lastfm_network.get_user(args.username).get_now_playing()
            # print("last:", last_played)
            # print("now: ", now_playing)
            if now_playing != last_played:
                last_played = now_playing
                if now_playing:
                    print(now_playing)
                    if args.say:
                        say(now_playing)

            time.sleep(15)
