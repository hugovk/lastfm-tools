#!/usr/bin/python
# coding: utf-8
import sys
from mylast import *

# Shows the last 20 tracks you scrobbled (or of a given username)
# Prerequisites: mylast.py, pyLast

number = 20
username = lastfm_username

def assign_arg(arg):
    global number, username
    if arg.isdigit():
        number = int(arg)
    else:
        username = arg

if len(sys.argv) > 1:
    assign_arg(sys.argv[1])
if len(sys.argv) > 2:
    assign_arg(sys.argv[2])

recent_tracks = lastfm_network.get_user(username).get_recent_tracks(limit=number)
for track in recent_tracks:
    unicode_track = unicode(str(track.track), 'utf8')
    print_it(track.playback_date + "\t" + unicode_track)
