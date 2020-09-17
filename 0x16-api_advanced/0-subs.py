#!/usr/bin/python3
""" subs """
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """ return number of subscrbers """
    if not subreddit:
        return 0
    headers = {'User-Agent': 'gunter'}
    data = requests.get('https://www.reddit.com/r/{}/about.json'.format(
                        subreddit), headers=headers).json()
    subs = data.get('data', {}).get('subscribers', 0)
    return subs
