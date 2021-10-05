#!/usr/bin/env python3

# Takes a track and scrobbles it
# Mandatory parameter 1: "artist - track"
# Optional parameter 2: UNIX timestamp. Default: now
# Prerequisites: mylast.py, pyLast

import datetime
import sys
import time

from mylast import lastfm_network, split_artist_track

if len(sys.argv) < 2:
    print('Usage: scrobble.py "artist - title" [unix_timestamp]')
    sys.exit(1)

testMode = False
if testMode:
    print("Test mode, won't actually scrobble.")
else:
    print("Live mode, can scrobble.")

unix_timestamp = 0
if len(sys.argv) > 2:
    unix_timestamp = sys.argv[2]
print(unix_timestamp)

artist_track = sys.argv[1]
print("input:\t\t'" + artist_track + "'")
# print(type(artist_track))


def scrobble_track(artist_track, unix_timestamp):

    (artist, track) = split_artist_track(artist_track)

    # Validate
    if unix_timestamp == 0:
        # Get UNIX timestamp
        unix_timestamp = int(time.mktime(datetime.datetime.now().timetuple()))
    print("Timestamp:\t" + str(unix_timestamp))

    # Scrobble it
    if not testMode:
        lastfm_network.scrobble(artist=artist, title=track, timestamp=unix_timestamp)

    # Confirm
    # print("Confirmation from Last.fm:")
    # recent_tracks = lastfm_network.get_user(
    # lastfm_username).get_recent_tracks(limit=1)
    # for track in recent_tracks:
    # unicode_track = unicode(str(track.track), 'utf8')
    # # print_it(track.playback_date + "\t" + unicode_track)
    # print(track.playback_date + "\t" + unicode_track)


scrobble_track(artist_track, unix_timestamp)

# End of file
