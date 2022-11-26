import pyautogui as p, time

for i in range(26):
    p.hotkey('ctrl', 'shift', 'n')
    time.sleep(1)   
    p.write('cd C:\Sahith\.vscode\Faculty-login-hack')
    p.press('enter')
    p.write('python faculty-login-bruteforce2.py')
    p.press('enter')
    p.write(str(i))
    p.press('enter')