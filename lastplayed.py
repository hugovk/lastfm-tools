#!/usr/bin/env python
"""
Show 20 last played tracks, or all the last played tracks of an artist (and optionally track)
"""

import argparse
import sys
from mylast import *


def get_recent_tracks(username, number):
    recent_tracks = lastfm_network.get_user(username).get_recent_tracks(limit = number)
    for track in recent_tracks:
        print_track(track)


def get_artist_tracks(username, artist, title):
    if TRACK_SEPARATOR in artist:
        (artist, title) = split_artist_track(artist)

    print "Searching Last.fm library...\r",
    try:
        tracks = lastfm_network.get_user(username).get_artist_tracks(artist = artist)
    except Exception as e:
        sys.exit("Exception: " + str(e))

    total = 0

    if title is None: # print all
        for track in tracks:
            print_track(track)
        total = len(tracks)
        
    else: # print matching titles
        find_track = pylast.Track(artist, title, lastfm_network)
        for track in tracks:
            if str(track.track).lower() == str(find_track).lower():
                print_track(track)
                total += 1

    print "Total:", total


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description = "Show 20 last played tracks, or all the last played tracks of an artist (and song)", 
        formatter_class = argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('artist',  nargs='?', 
        help="Artist, or 'artist - track'")
    parser.add_argument('track',  nargs='?', 
        help="Track")
    parser.add_argument('-u', '--username', 
        help="Last.fm username")
    parser.add_argument('-n', '--number', default=20, type=int,
        help="Number of tracks to show (when no artist given)")
    args = parser.parse_args()

    if not args.username:
        args.username = lastfm_username
    
    if args.artist:
        get_artist_tracks(args.username, args.artist, args.track)
    else:
        get_recent_tracks(args.username, args.number)

# End of file
