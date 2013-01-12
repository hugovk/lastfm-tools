#!/usr/bin/python
import sys
from mylast import *

# Show my now playing song, or that of a given username
# Prerequisites: mylast.py, pyLast

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    username = lastfm_username

print lastfm_network.get_user(username).get_now_playing()
