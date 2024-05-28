#!/usr/bin/env python3

"""
Used to notify Last.fm that a user has started listening to a track.

    Parameters:
        artist (Required) : The artist name
        title (Required) : The track title
        duration (Optional) : The length of the track in seconds.
"""

import os
import sys

from mylast import lastfm_network

if len(sys.argv) < 2:
    print("Usage: " + os.path.basename(__file__) + " artist title [song_duration]")
    sys.exit(1)

artist = sys.argv[1]
title = sys.argv[2]

if len(sys.argv) >= 3:
    duration = int(sys.argv[3])
else:
    duration = None


def send_now_playing():
    lastfm_network.update_now_playing(artist=artist, title=title, duration=duration)


try:
    send_now_playing()

except Exception as e:
    print("Error:", e)
    sys.exit(1)
