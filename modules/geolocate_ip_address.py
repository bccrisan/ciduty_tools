import urllib.request

def geolocate_adress():
    ip_adress = input("Please enter an IP:")
    geody = "http://www.geody.com/geoip.php?ip=" + ip_adress
    html_page = urllib.request.urlopen(geody).read()
    print(html_page)


if __name__ == "__main__":
    geolocate_adress()