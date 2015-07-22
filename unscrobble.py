#!/usr/bin/env python
# coding: utf-8
"""
Unscrobble the last played track or tracks
Prerequisites:
mylast.py, lastplayed.py, pyLast >= 1.0.0
"""
from __future__ import print_function
import argparse
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
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
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
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")


def unscrobble(library, scrobble):
    artist = str(scrobble.track.artist)
    title = scrobble.track.title
    timestamp = scrobble.timestamp

    try:
        my_library.remove_scrobble(
            artist=artist, title=title, timestamp=timestamp)
    except AttributeError as e:
        print("Exception: " + str(e))
        sys.exit(
            "Error: pylast 0.5.11 does not support removing scrobbles. "
            "Please install latest pylast: pip install -U pylast")
    except Exception as e:
        sys.exit("Exception: " + str(e))
    print_it("Scrobble removed: " + unicode_track_and_timestamp(scrobble))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Unscrobble the last played track or tracks",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '-u', '--username', default=lastfm_username,
        help="Last.fm username")
    parser.add_argument(
        '-n', '--number', default=1, type=int,
        help="Number of tracks to unscrobble")
    args = parser.parse_args()

    print("Last scrobbles:")
    # +1 because now-playing tracks may also be included
    last_scrobbles = get_recent_tracks(lastfm_username, args.number+1)
    # Now make sure we only unscrobble the required number
    last_scrobbles = last_scrobbles[:args.number]

    answer = query_yes_no("Unscrobble last " + str(args.number) + "?")
    if not answer:
        sys.exit("Scrobble kept")
    else:
        my_library = pylast.Library(user=lastfm_username, network=lastfm_network)

        for last_scrobble in last_scrobbles:
            unscrobble(my_library, last_scrobble)

    print("Last few are now:")
    get_recent_tracks(lastfm_username, 5)

# End of file
