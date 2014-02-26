#!/usr/bin/python
# coding: utf-8
"""
Unscrobble the last played track
Prerequisites: 
mylast.py, lastplayed.py, pyLast from https://github.com/hugovk/pylast
"""
import pylast
import sys
from mylast import *
from lastplayed import get_recent_tracks

# http://stackoverflow.com/a/3041990/724176
def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is one of "yes" or "no".
    """
    valid = {"yes":True,   "y":True,  "ye":True,
             "no":False,     "n":False}
    if default == None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "\
                             "(or 'y' or 'n').\n")


print "Last scrobble:"
last_scrobble = get_recent_tracks(lastfm_username, 1)[0]

answer = query_yes_no("Unscrobble?")
if not answer:
    print "Left scrobbled"
else:
    my_library = pylast.Library(user = lastfm_username, network = lastfm_network)
    artist = last_scrobble.track.artist
    title = last_scrobble.track.title
    timestamp = last_scrobble.timestamp

    try:
        my_library.remove_scrobble(artist = artist, title = title, timestamp = timestamp)
    except AttributeError as e:
        print "Exception: " + str(e)
        sys.exit("Error: pylast 0.5.11 does not support removing scrobbles. Please install latest pylast from https://github.com/hugovk/pylast")
    except Exception as e:
        sys.exit("Exception: " + str(e))
    print "Scrobble removed"

print "Last five are now:"
get_recent_tracks(lastfm_username, 5)

# End of file
