#!/usr/bin/python
# coding: utf-8

# Takes a track and scrobbles it
# Mandatory parameter 1: "artist - track"
# Optional parameter 2: UNIX timestamp. Default: now
# Prerequisites: mylast.py, pyLast

import datetime
import pylast
import sys
import time
from mylast import *

if len(sys.argv) < 2:
    print "Usage: scrobbletrack.py \"artist - title\" [unixTimestamp]"
    sys.exit(1)

testMode = False
if testMode:
    print "Test mode, won't actually scrobble."
else:
    print "Live mode, can scrobble."

unixTimestamp = 0
if len(sys.argv) > 2:
    unixTimestamp = sys.argv[2]
print unixTimestamp

artistTrack = sys.argv[1].decode(sys.getfilesystemencoding())
print "input:\t\t'" + artistTrack + "'"
# print type(artistTrack)

def scrobbleTrack(artistTrack, unixTimestamp):

    (artist, track) = split_artist_track(artistTrack)
        
    # Validate
    if unixTimestamp == 0:
    # Get UNIX timestamp
        unixTimestamp = int(time.mktime(datetime.datetime.now().timetuple()))
    print "Timestamp:\t" + str(unixTimestamp)

    # Scrobble it
    if not testMode:
        lastfm_network.scrobble(artist = artist, title = track, timestamp = unixTimestamp)

    # Confirm
    # print "Confirmation from Last.fm:"
    # recent_tracks = lastfm_network.get_user(lastfm_username).get_recent_tracks(limit=1)
    # for track in recent_tracks:
        # unicode_track = unicode(str(track.track), 'utf8')
        # # print_it(track.playback_date + "\t" + unicode_track)
        # print track.playback_date + "\t" + unicode_track

scrobbleTrack(artistTrack, unixTimestamp)
