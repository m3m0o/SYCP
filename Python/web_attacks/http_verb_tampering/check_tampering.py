import requests
from sys import argv

if len(argv) != 3:
    print(f'Usage: python3 {__file__} [default_response_code] [url]')
    exit(0)

verbs = {
    'GET': requests.get,
    'POST': requests.post,
    'PUT': requests.put,
    'HEAD': requests.head,
    'PATCH': requests.patch
}

_filename, default_code, url = argv

for verb in verbs.items():
    verb_name, function = verb
    status_code = function(url).status_code

    if status_code != int(default_code):
        print(f'{verb_name} -> {status_code}')