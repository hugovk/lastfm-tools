#!/usr/bin/env python3
"""Tests for mylast helpers.

pylast is stubbed in sys.modules before importing mylast, so these tests
need no Last.fm API credentials and make no network requests.
"""

import sys
import types

import pytest

_pylast_stub = types.ModuleType("pylast")
_pylast_stub.md5 = lambda value: "stub-hash"  # noqa: E731


class _StubLastFMNetwork:
    def __init__(self, *args, **kwargs):
        pass


_pylast_stub.LastFMNetwork = _StubLastFMNetwork
sys.modules.setdefault("pylast", _pylast_stub)

from mylast import split_artist_track  # noqa: E402


def test_split_artist_track_valid():
    assert split_artist_track("Artist - Track") == ("Artist", "Track")


def test_split_artist_track_en_dash():
    assert split_artist_track("Artist – Track") == ("Artist", "Track")


def test_split_artist_track_missing_separator():
    with pytest.raises(SystemExit) as excinfo:
        split_artist_track("NoSeparatorHere")
    assert "artist - track" in str(excinfo.value.code)


def test_split_artist_track_extra_separator():
    with pytest.raises(SystemExit):
        split_artist_track("Artist - Track - Remix")
