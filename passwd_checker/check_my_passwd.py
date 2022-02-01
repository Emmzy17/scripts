import requests
from hashlib import sha1
import sys
def request_data(query):
    url = 'https://api.pwnedpasswords.com/range/' + str(query)
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error Fetching: {res.status_code}, check your api and try again")
    return res

def get_password_check(hashes,hash_tail ):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_tail:
            return count
    return 0


def pwned_api_check(password):
    sha1pswd = sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1pswd[:5], sha1pswd[5:]
    response = request_data(first5_char)
    return get_password_check(response, tail)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times ... you shoupld probably change your password ')
        else:
            print(f'{password} was not found ...carry on')

main(sys.argv[1:])