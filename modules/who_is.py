import whois


def who_is():
    json = whois.whois(input("Please enter the domain name:"))
    print("Server Name/s:", json.get("domain_name"))
    print("Creation Date:", json.get("creation_date")[0].date())
    print("Expiration Date:", json.get("expiration_date")[0].date())
