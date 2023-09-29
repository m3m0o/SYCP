import sys
import requests


def parse_url(url: str) -> str:
    if ('http://' or 'https://') not in url:
        return f'http://{url}'
    
    return url


def bruteforce(url: str, wordlist: str) -> None:
    with open(wordlist, 'r') as file:
        directories = file.readlines()

        for directory in directories:
            try:
                final_url = f'{url}/{directory}'

                response_status_code = requests.get(final_url).status_code

                if response_status_code != 404:
                    print(f'{final_url} -- {response_status_code}'.strip())
            except KeyboardInterrupt:
                exit(0)

if __name__ == '__main__':
    try:
        _, url, wordlist = sys.argv
    except ValueError:
        print('Usage: python3 directory-recon.py <url> <wordlist>')



    bruteforce(parse_url(url), wordlist)