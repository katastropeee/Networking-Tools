import os
import pyautogui

ip_list = ["192.168.1.25", "192.168.1.10"]

pyautogui.alert(title="Continuous Ping", text="Run Continuous Ping?")

while True:
    for ip in ip_list:
        response = os.popen(f"ping {ip}").read()
        if "Received = 4" in response:
            print(f"UP {ip} Ping Successful")
        else:
            pyautogui.alert(title="Ping Unsuccessful", text=f"DOWN {ip} Ping Unsuccessful")
            quit()
