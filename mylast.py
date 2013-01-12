#!/usr/bin/python
# coding: utf-8

import pylast

# You have to have your own unique two values for API_KEY and API_SECRET
# Obtain yours from http://www.last.fm/api/account for Last.fm

API_KEY = "my_api_key"
API_SECRET = "my_apy_secret"

# In order to perform a write operation you need to authenticate yourself
lastfm_username = "my_username"
# You can use either use the password, or find the hash once and use that
lastfm_password_hash = pylast.md5("my_password")
print lastfm_password_hash
# lastfm_password_hash = "my_password_hash"

lastfm_network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET, username = lastfm_username, password_hash = lastfm_password_hash)

# Windows cmd.exe cannot do Unicode so encode first
def print_it(text):
    print text.encode('utf-8')

