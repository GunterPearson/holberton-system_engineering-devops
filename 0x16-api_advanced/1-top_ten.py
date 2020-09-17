#!/usr/bin/python3
""" return top ten from given page"""
import requests


def top_ten(subreddit):
    """ return top ten"""
    if not subreddit:
        print("None")
    headers = {'User-Agent': 'gunter'}
    data = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'.format(
                        subreddit), headers=headers).json()
    info = data.get('data', {}).get('children', [])
    if info == []:
        print("None")
    new = []
    for dic in info:
        t = dic.get('data', {}).get('title', None)
        if t:
            new.append(t)
    for obj in new:
        print(obj)
