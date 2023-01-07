import requests
import sys
import pyfiglet


banner = pyfiglet.figlet_format("SUDOMAIN AND URL QUERY ENUMERATION TOOL")
print(banner)


subdomain_list = open("subdomain.txt").read()
subs = subdomain_list.readlines()

for sub in subs:
    url = f"https://{sub}.{sys.argv[1]}"

    try:
        requests.get(url)
    except Exception as ex:
        pass
else:
    print("Valid: ", url)
