#!/usr/bin/env python3
import sys

import pylast

from mylast import lastfm_network, lastfm_username

# Loves whatever track is now playing on Last.fm,
# then prints confirmation of last loved track.
# Optional parameter: love "artist - title" instead.
# Prerequisites: mylast.py, pyLast


if len(sys.argv) > 1:
    (artist, title) = sys.argv[1].split("-")
    artist = artist.strip()
    title = title.strip()
    track = pylast.Track(artist, title, lastfm_network)
else:
    track = lastfm_network.get_user(lastfm_username).get_now_playing()

last_loved_track = str(
    lastfm_network.get_user(lastfm_username).get_loved_tracks(limit=1)[0][0]
)
print("Last:\t" + str(last_loved_track))

print("Loving:\t" + str(track))
if track is None:
    sys.exit("Didn't get the track now playing from Last.fm")

track.love()


# Confirm the track has been loved
if track.get_userloved():
    print("Loved it!")
else:
    print("Error?")

# End of file
