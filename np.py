#!/usr/bin/env python
from __future__ import print_function
import sys
from mylast import lastfm_network, lastfm_username

# Show my now playing song, or that of a given username
# Prerequisites: mylast.py, pyLast

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    username = lastfm_username

print(lastfm_network.get_user(username).get_now_playing())
