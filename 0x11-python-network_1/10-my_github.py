#!/usr/bin/python3
"""Get GitHub id using github API along with Basic Authentication"""

if __name__ == "__main__":
    from requests import get
    from sys import argv

    try:
        req = get('https://api.github.com/user', auth=(argv[1], argv[2]))
        j = req.json()
        print(j.get('id'))
    except ValueError as err:
        print(err)
