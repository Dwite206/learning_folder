import requests
import hashlib
import sys

# Ez megkapja az APItól a kódokat


def request_api_data(request_code):
    url = 'https://api.pwnedpasswords.com/range/' + request_code
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError('Try again')
    return res


def get_psw_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

# A jelszavam átalakítja hash , hexre


def hashed_pws(password):
    # Szét szedi az első 5 karaktert, és a maradékot
    sh1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sh1password[:5], sh1password[5:]
    response = request_api_data(first5_char)
    return get_psw_leaks_count(response, tail)


# lecsekkolja, hogy a jelszó megtalálható-e az adatbázisban
def main(args):
    for password in args:
        count = hashed_pws(password)
        if count:
            print(f'{password} was found {count} times...')
        else:
            print(f'{password} is secured!')
    return 'done!'


if __name__ == '__main__':
    # több jelszó is bevihető
    sys.exit(main(sys.argv[1:]))
