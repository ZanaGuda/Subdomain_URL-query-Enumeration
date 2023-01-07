import requests
import sys
import pyfiglet


banner = pyfiglet.figlet_format("SUDOMAIN AND URL QUERY ENUMERATION TOOL")
print(banner)


subdomain_list = open("subdomain.txt").read()
subs = subdomain_list.readlines()
