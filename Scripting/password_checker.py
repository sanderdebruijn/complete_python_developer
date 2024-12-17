import requests
import hashlib


def request_api_data(query_char):
    url = f"https://api.pwnedpasswords.com/range/{query_char}"
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(
            f"Error fetching: {response.status_code}. Check the API and try again."
        )
    else:
        return response


def hash_pw(password):
    # Hash pw to sha1 hash
    password_sha1 = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    return password_sha1


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def print_final_statement(leak_count):
    if int(leak_count) > 0:
        print(f"This password was leaked {leak_count} times. DO NOT USE!")
    else:
        print("This password is safe to use!")


if __name__ == '__main__':
    password = input("The password you want to check: ")
    password_hashed = hash_pw(password)
    password_hashed_short, password_hashed_remaining = (
        password_hashed[:5], password_hashed[5:]
    )
    response = request_api_data(query_char=password_hashed_short)
    leak_count = get_password_leaks_count(
        hashes=response,
        hash_to_check=password_hashed_remaining
    )
    print_final_statement(leak_count=leak_count)
