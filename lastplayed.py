#!/usr/bin/env python3
"""
Show 20 last played tracks
"""
import argparse

import pylast

from mylast import lastfm_network, lastfm_username, track_and_timestamp


def get_recent_tracks(username, number):
    recent_tracks = lastfm_network.get_user(username).get_recent_tracks(limit=number)
    for i, track in enumerate(recent_tracks):
        printable = track_and_timestamp(track)
        print(str(i + 1) + " " + printable)
    return recent_tracks


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Show 20 last played tracks",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("-u", "--username", help="Last.fm username")
    parser.add_argument(
        "-n",
        "--number",
        default=20,
        type=int,
        help="Number of tracks to show (when no artist given)",
    )
    args = parser.parse_args()

    if not args.username:
        args.username = lastfm_username

    print(args.username + " last played:")
    try:
        get_recent_tracks(args.username, args.number)
    except pylast.WSError as e:
        print("Error: " + str(e))

# End of file
