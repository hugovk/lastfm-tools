# lastfm-tools

[![Lint](https://github.com/hugovk/lastfm-tools/actions/workflows/lint.yml/badge.svg)](https://github.com/hugovk/lastfm-tools/actions)
[![Python: 3.7+](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Code style: Black](https://img.shields.io/badge/code%20style-Black-000000.svg)](https://github.com/psf/black)

Some Python CLI tools for talking to the Last.fm API.

Uses [pylast](https://github.com/pylast/pylast):

```
pip install pylast
```

## np.py

Show my now playing song, or that of a given username.

## lastplayed.py

Shows the last 20 tracks you scrobbled (or of a given username).

## loveit.py

Loves whatever track is now playing on Last.fm, then prints confirmation of last loved
track.

## loved.py

Shows your last 20 (or a given number of) loved tracks.

## nowplaying.py

Command-line loopy thing to show what a Last.fm user is now playing. Based on
[bbcscrobbler](https://github.com/hugovk/bbcscrobbler).

## scrobble.py

Takes a track and scrobbles it

- Mandatory parameter 1: "artist - track"
- Optional parameter 2: UNIX timestamp. Default: now

## mylast.py

Config and common things. You need your own Last.fm API key and secret, get them from
https://www.last.fm/api/account/create and put them here. Also put your username and
either password or password hash.
