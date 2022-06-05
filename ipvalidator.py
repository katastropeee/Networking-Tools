import os
import ipaddress
import pyautogui

os.system('cls')
ip = pyautogui.prompt(title="IP Validator", text='Enter IP Address: ')
while True:

    try:
        print(ipaddress.ip_address(ip))
        pyautogui.alert(title="IP Validator", text=f'"{ip}"\n'
                                                   f"is a valid IP Address  ")
        break
    except:
        print: ('-' * 50)
        pyautogui.alert(title="IP Validator", text=f'"{ip}"\n'
                                                  f"is not valid a IP Address ")
        break
    finally:
        if ip == 'q':
            print('Script Finished')
            break
