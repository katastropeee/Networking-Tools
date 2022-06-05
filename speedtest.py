import speedtest
import pyautogui


def run():
    pyautogui.alert(title='Loading', text="This might take several seconds")
    st = speedtest.Speedtest()
    run.download_speed = round(st.download() * 0.000001, 2)
    run.upload_speed = round(st.upload() * 0.000001, 2)
    run.ping = st.results.ping


pyautogui.confirm(text='Run Speedtest?', title='Speedtest', buttons=['Sure'])
run()
pyautogui.alert(title='Speedtest Result', text=f"Ping: {run.ping} ms\n"
                                               f"Download: {run.download_speed} Mbps\n"
                                               f"Upload: {run.upload_speed} Mpbs")
