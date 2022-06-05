import socket
import pyautogui

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host, port))
s.listen(1)
pyautogui.alert(title="FTP SERVER", text=f"Hostname: {host}\n"
                                         f"Waiting for any incoming connection...")
print(host)
conn, addr, = s.accept()
pyautogui.alert(title="Connected!", text=f"{str(addr)} Has connected to the server")

# file send 
filename = pyautogui.prompt(str("Please enter the name of the file with extension:"), title="Sending File")
file = open(filename, 'rb')
file_data = file.read(1024)
conn.send(file_data)
pyautogui.alert(title="Success", text="File has been send")