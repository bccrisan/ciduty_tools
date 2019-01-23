import urllib.request


def check_my_ip():
    url = "http://checkip.dyndns.org"
    print(url)
    request = urllib.request.urlopen(url).read()
    request = str(request)
    the_ip = request[request.find("<body>") + len("<body>"):request.rfind("</body>")]
    print(the_ip)


if __name__ == "__main__":
    check_my_ip()