from modules.who_is import who_is
from modules.command_line_fu import command_line_fu
from modules.check_my_ip import check_my_ip
from modules.scrap_website_for_links import scrap_website_for_links
from modules.generate_random_string import generate_string
from modules.geolocate_ip_address import geolocate_adress
from modules.port_scanner import port_scanner


def main():
    menu_list = """
    1.Check domain with "WhoIs".
    2.Get commands with "CommandLineFU".
    3.Check my IP.
    4.Extract Links from URL.
    5.Generate random string.
    6.Geolocate IP Adress
    7.Port Scanner
    """
    while True:
        print(menu_list)
        answer = input("Choose a command:")
        if answer == "":
            print("I'm out! Have a nice day!")
            break
        elif answer == "1":
            who_is()
        elif answer == "2":
            command_line_fu()
        elif answer == "3":
            check_my_ip()
        elif answer == "4":
            scrap_website_for_links()
        elif answer == "5":
            generate_string()
        elif answer == "6":
            geolocate_adress()
        elif answer == "7":
            port_scanner()
        else:
            print("Not a valid command!!")


if __name__ == "__main__":
    main()
