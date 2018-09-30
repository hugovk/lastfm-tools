#!/usr/bin/env python3
"""
Suggest a pronoun to use for a musical artist,
by looking at their biography on Last.fm.

Usage: python artist_pronoun.py artist_name
"""
import argparse

from mylast import lastfm_network, print_it


def count_em(words, text):
    """Count how many times these words apear in the text"""
    total = 0
    for thing in words:
        num = 0
        for thing2 in [thing, thing.capitalize()]:
            num += text.count(" " + thing2 + " ")
        total += num
        print(num, thing)
    return total


def pick_word(artist_name):
    """Suggest a pronoun for this artist"""
    artist = lastfm_network.get_artist(artist_name)

    members = artist.get_band_members()
    print(members)

    bio = artist.get_bio_summary()
    print_it(bio)

    if members is None:
        members = 0
        print(0, None)
    else:
        print(len(members), ", ".join(members))

    plural, female, male = 0, 0, 0
    band_words = ["the band", "the group", "their", "they"]
    female_words = ["she", "her"]
    male_words = ["he", "his"]

    plural = count_em(band_words, bio)
    female = count_em(female_words, bio)
    male = count_em(male_words, bio)
    print(plural, female, male)

    if members >= 2 and plural > 0 and female == 0 and male == 0:
        choice = "they"
        certainty = "very good"
    elif members == 1 and plural == 0 and female > 0 and male == 0:
        choice = "her"
        certainty = "very good"
    elif members == 1 and plural == 0 and female == 0 and male > 0:
        choice = "he"
        certainty = "very good"
    elif plural > 1 and female == 0 and male == 0:
        choice = "they"
        certainty = "good"
    elif plural == 0 and female > 0 and male == 0:
        choice = "she"
        certainty = "good"
    elif plural == 0 and female == 0 and male > 0:
        choice = "he"
        certainty = "good"
    elif members >= 2:
        choice = "they"
        certainty = "quite good"
    else:
        choice = "they"
        certainty = "default"

    print("Use " + choice.upper() + " (" + certainty + ")")
    return choice, certainty


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Suggest a pronoun to use for a musical artist",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("artist", help="Artist")
    args = parser.parse_args()

    pick_word(args.artist)

# End of file
