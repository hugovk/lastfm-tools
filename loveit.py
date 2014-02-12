#!/usr/bin/python
import sys
from mylast import *

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

last_loved_track = str(lastfm_network.get_user(lastfm_username).get_loved_tracks(limit=1)[0][0])
print "Last:\t" + str(last_loved_track)

print "Loving:\t" + str(track)
if track is not None:
    track.love()

# Confirm the track has been loved by retrieving the last loved track from Last.fm
last_loved_track = str(lastfm_network.get_user(lastfm_username).get_loved_tracks(limit=1)[0][0])
print "Loved:\t" + str(last_loved_track)
