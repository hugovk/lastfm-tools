#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function
import os
import pylast
import sys

# You have to have your own unique two values for API_KEY and API_SECRET
# Obtain yours from http://www.last.fm/api/account for Last.fm

try:
    API_KEY = os.environ['LASTFM_API_KEY']
    API_SECRET = os.environ['LASTFM_API_SECRET']
except KeyError:
    API_KEY = "my_api_key"
    API_SECRET = "my_apy_secret"

try:
    lastfm_username = os.environ['LASTFM_USERNAME']
    lastfm_password_hash = os.environ['LASTFM_PASSWORD_HASH']
except KeyError:
    # In order to perform a write operation you need to authenticate yourself
    lastfm_username = "my_username"
    # You can use either use the password, or find the hash once and use that
    lastfm_password_hash = pylast.md5("my_password")
    print(lastfm_password_hash)
    # lastfm_password_hash = "my_password_hash"


lastfm_network = pylast.LastFMNetwork(
    api_key=API_KEY, api_secret=API_SECRET,
    username=lastfm_username, password_hash=lastfm_password_hash)


# Windows cmd.exe cannot do Unicode so encode first
def print_it(text):
    print(text.encode('utf-8'))


def unicode_track_and_timestamp(track):
    unicode_track = unicode(str(track.track), 'utf8')
    return track.playback_date + "\t" + unicode_track


def print_track(track):
    print_it(unicode_track_and_timestamp(track))


TRACK_SEPARATOR = u" - "


def split_artist_track(artist_track):
    artist_track = artist_track.replace(u" – ", " - ")
    artist_track = artist_track.replace(u"“", "\"")
    artist_track = artist_track.replace(u"”", "\"")

    (artist, track) = artist_track.split(TRACK_SEPARATOR)
    artist = artist.strip()
    track = track.strip()
    print_it("Artist:\t\t'" + artist + "'")
    print_it("Track:\t\t'" + track + "'")

    # Validate
    if len(artist) is 0 and len(track) is 0:
        sys.exit("Error: Artist and track are blank")
    if len(artist) is 0:
        sys.exit("Error: Artist is blank")
    if len(track) is 0:
        sys.exit("Error: Track is blank")

    return (artist, track)

# End of file
