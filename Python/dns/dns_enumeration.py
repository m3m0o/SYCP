import sys
import dns.resolver

try:
    _, domain, wordlist = sys.argv

    try:
        with open(wordlist, 'r') as wordlist:
            subdomains = wordlist.read().splitlines()
    except FileNotFoundError:
        print('Invalid wordlist path.')

    resolver = dns.resolver.Resolver()

    for subdomain in subdomains:
        try:
            results = resolver.resolve(f'{subdomain}.{domain}', 'A')

            for result in results:
                print(f'{subdomain} -> {result}')
        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer):
            pass
except ValueError:
    print('Usage: python dns_enumeration.py <domain> <wordlist>')