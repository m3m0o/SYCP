import sys
import re

import requests
from bs4 import BeautifulSoup

TO_CRAWL = []
CRAWLED = set()
EMAILS = []


def check_url(url: str) -> None:
    if ('http://' or 'https://') not in url:
        raise ValueError('Invalid schema.')


def request(url: str) -> str | None:
    header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}

    try:
        response = requests.get(url, headers=header)

        return response.text
    except KeyboardInterrupt:
        sys.exit(0)
    except:
        pass


def get_links(html: str) -> list[str] | None:
    links = []

    try:
        soup = BeautifulSoup(html, "html.parser")

        tags_a = soup.find_all("a", href=True)
        
        for tag in tags_a:
            link = tag["href"]

            if link.startswith("http"):
                links.append(link)

        return links
    except:
        pass


def get_emails(html: str) -> list[str]:
    emails = re.findall(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', html)

    return emails


def crawl() -> None:
    while True:
        if TO_CRAWL:
            url = TO_CRAWL.pop()

            html = request(url)
            if html:
                links = get_links(html)

                if links:
                    for link in links:
                        if link not in CRAWLED and link not in TO_CRAWL:
                            TO_CRAWL.append(link)

                emails = get_emails(html)

                for email in emails:
                    if email not in EMAILS:
                        print(email)

                        EMAILS.append(email)

                CRAWLED.add(url)
            else:
                CRAWLED.add(url)
        else:
            print("Done")

            break


if __name__ == "__main__":
    try:
        _, url = sys.argv

        check_url(url)
    except ValueError:
        print('Usage: python3 email_finder.py <url> (use http:// or https:// schemas on url)')

    TO_CRAWL.append(url)
    crawl()
