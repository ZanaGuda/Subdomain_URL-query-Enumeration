import dns.resolver
import sys
import pyfiglet
import itertools

banner = pyfiglet.figlet_format("Subdomain Enumeration TOOL")
print(banner)

FILE = open('myfile.txt', 'w')

chrs = 'bew'
n = 6
for i in range(1, n):
    for j in itertools.product(chrs, repeat=i):
        wgen = (''.join(j))
        wordlist = wgen.splitlines()
        FILE.writelines(wordlist)
        FILE.write("\n")


FILE.close()

domain = sys.argv[1]

subdomain_array = ["subdomain_array.txt", "subdomains.txt"]

for file in subdomain_array:
    with open(file) as inputfile:
        content = inputfile.read()
        subs = content.splitlines()


def main():
    subdomain_store = []
    parameter = "q"
    for subdoms in subs:
        try:
            ip_value = dns.resolver.resolve(f'{subdoms}.{domain}', 'A')
            if ip_value:
                subdomain_store.append(
                    f'{subdoms}.{domain}')
                if f"{subdoms}.{domain}" in subdomain_store:
                    print(f'{subdoms}.{domain} valid')
                else:
                    pass
        except dns.resolver.NXDOMAIN:
            pass
        except dns.resolver.NoAnswer:
            pass
        except KeyboardInterrupt:
            print('Subdomain not found!')
            quit()


main()
