import requests
import pyautogui

ip = pyautogui.prompt(text=str("Enter valid IP address here:"), title="IP Locator")
response = requests.get(f"http://ip-api.com/json/{ip}").json()
pyautogui.alert(title="IP Address Information", text=f"IP Address: {ip} \n"
                                                     f"Country: {response['country']}\n"
                                                     f"Region: {response['regionName']}\n"
                                                     f"City: {response['city']}\n"
                                                     f"Latitude: {response['lat']}\n"
                                                     f"Longitude: {response['lon']}\n"
                                                     f"Internet Service Provider: {response['isp']}")
