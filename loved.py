#!/usr/bin/env python3
import sys

from mylast import lastfm_network, lastfm_username

# Prints a list of you last loved tracks on Last.fm.
# Optional parameter: number of tracks
# Prerequisites: mylast.py, pyLast


if len(sys.argv) > 1:
    number = int(sys.argv[1])
else:
    number = 20

last_loved_tracks = lastfm_network.get_user(lastfm_username).get_loved_tracks(
    limit=number
)

for i, track in enumerate(last_loved_tracks):
    print(str(i + 1) + ")\t" + str(track[0]))

# End of file
