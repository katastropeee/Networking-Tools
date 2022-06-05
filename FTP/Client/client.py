import socket
import pyautogui

s = socket.socket()
host = pyautogui.prompt(str("Enter the host address here:"), title="FTP Client")
port = 8080
s.connect((host, port))
pyautogui.alert(title="Connected!", text="Connection has been established!!")

# receive file
filename = pyautogui.prompt(str("Please input a name to the file you want to recieved:"), title="Received File")
file = open(filename, 'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close()
pyautogui.alert(title="Success", text="File has been received")
