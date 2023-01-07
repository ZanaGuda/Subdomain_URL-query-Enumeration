import sys
import dns.resolver
import itertools
domain = sys.argv[1]
# subdomain_array = ['www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp',
#                    'pop', 'ns1', 'webdisk', 'cpanel', 'admin', 'news', 'img', 'ads', 'm', 'mx']

subdomain_array = ["subdomain_array.txt", "subdomains.txt"]

for file in subdomain_array:
    with open(file) as inputfile:
         content = inputfile.read()
         subs = content.splitlines()

def main():
    subdomain_store = []
    for subdoms in subdomain_array:
        try:
            ip_value = dns.resolver.resolve(f'{subdoms}.{domain}', 'A')
            if ip_value:
                subdomain_store.append(f'{subdoms}.{domain}')
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
