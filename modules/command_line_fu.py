import os
import sys
import urllib.request
import json
import re
import base64


def print_title(message):
    os.system("clear")
    print("-"*len(message))
    print(message)
    print("-"*len(message))


def banner(text):
    print("="*len(text))
    print(text)
    print("="*len(text))
    sys.stdout.flush()


def sort_by_votes():
    banner("Sort by votes!")
    url = "http://www.commandlinefu.com/commands/browse/sort-by-votes/json"
    request = urllib.request.Request(url)
    response = json.load(urllib.request.urlopen(request))
    for item in response:
        print(item["command"])
        print("-" * len(item["command"]))


def sort_by_votes_today():
    banner("Printing All commands the last day (Sort By Votes)")
    url = "http://www.commandlinefu.com/commands/browse/last-day/sort-by-votes/json"
    request = urllib.request.Request(url)
    response = json.load(urllib.request.urlopen(request))
    for item in response:
        print(item["command"])
        print("-" * len(item["command"]))


def sort_by_votes_week():
    banner("Printing All commands the last week (Sort By Votes)")
    url = "http://www.commandlinefu.com/commands/browse/last-week/sort-by-votes/json"
    request = urllib.request.Request(url)
    response = json.load(urllib.request.urlopen(request))
    for item in response:
        print(item["command"])
        print("-" * len(item["command"]))


def sort_by_votes_month():
    banner("Printing All commands the last months (Sort By Votes)")
    url = "http://www.commandlinefu.com/commands/browse/last-month/sort-by-votes/json"
    request = urllib.request.Request(url)
    response = json.load(urllib.request.urlopen(request))
    for item in response:
        print(item["command"])
        print("-" * len(item["command"]))


def sort_by_match():
    banner("Sort by Match")
    match = input("Please enter a search command:")
    best_match = re.compile(r"")
    search = best_match.sub("+", match)
    b64_encoded = base64.b64encode(search)
    url = "http://www.commandlinefu.com/commands/matching/" + search + "/" + b64_encoded + "/json"
    request = urllib.request.Request(url)
    response = json.load(urllib.request.urlopen(request))
    for item in response:
        print(item["command"])
        print("-" * len(item["command"]))


def command_line_fu():
    message = """
1. Sort By Votes (All time)
2. Sort By Votes (Today)
3. Sort by Votes (Week)
4. Sort by Votes (Month)
5. Search for a command
 
Press enter to quit
"""
    print(message)

    while True:
        answer = input("Choose a command:")
        if answer == "":
            break
        elif answer == "1":
           print(sort_by_votes())
        elif answer == "2":
            print(sort_by_votes_today())
        elif answer == "3":
            print(sort_by_votes_week())
        elif answer == "4":
            print(sort_by_votes_month())
        elif answer == "5":
            print(sort_by_match())
        else:
            print("Not a valid command!!")

