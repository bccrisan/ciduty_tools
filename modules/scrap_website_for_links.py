import urllib.request
import re


def scrap_website_for_links():
    website = urllib.request.urlopen(input("Please enter the URL:"))
    html = website.read()
    html = str(html)
    links = re.findall('"((http|ftp)s?://.*?)"', html)
    print(links)


if __name__ == "__main__":
    scrap_website_for_links()

