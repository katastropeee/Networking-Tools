import subprocess
import pyautogui

Computer_List = []
Computer_List.append(pyautogui.prompt(title="Remote Shutdown", text="Enter IP Address to shutdown!"))
for Computer in Computer_List:
    pyautogui.alert(title="Results", text=subprocess.getoutput("shutdown -m \\\\" + Computer + " -f -r -t 30"))
