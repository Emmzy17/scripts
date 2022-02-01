import requests
from hashlib import sha1
def request_data(query):
    url = 'https://api.pwnedpasswords.com/range/' + str(query)
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error Fetching: {res.status_code}, check your api and try again")
    return res

def get_password_check(hashes,hash_tail ):
    hashes = (line.split(':') for line in hashes.text.splitline)
    for h, count in hashes:
        print(h, count)


def pwned_api_check(password):
    sha1pswd = sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1pswd[:5], sha1pswd[5:]
    response = request_data(first5_char)
    return get_password_check(response, tail)

print(pwned_api_check('emmyj'))