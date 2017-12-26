#!python3.6.1
# -*- coding: utf-8 -*-
# author: https://github.com/vinlinch
# 第 0025 题： 使用 Python 实现：对着电脑吼一声,自动打开浏览器中的默认网站。
# 例如，对着笔记本电脑吼一声“百度”，浏览器自动打开百度首页。
# 关键字：Speech to Text
# 1 ：获取电脑录音-->WAV文件 python record wav
# 2：录音文件-->文本
# STT: Speech to Text
# STT API Google API
# 3:文本-->电脑命令
# 作者：海上牧云l
# 链接：http://www.jianshu.com/p/7bfea1079e78
# 來源：简书
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
from tkinter import *
import pyaudio
import wave
import requests
import json
import pycurl
from io import BytesIO
import os


CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 8000
RECORD_SECONDS = 5


# 录音保存
def record_wave():
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("正在录音...")
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("录音结束")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open('output.wav', 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


# 界面
def button():
    root = Tk()

    label = Label(root)
    label['text'] = '点击开始，开始录音'
    label.pack()

    button1 = Button(root)
    button1['text'] = '开始'
    button1['command'] = record_wave
    button1["fg"] = "red"
    button1.pack({"side": "left"})

    button2 = Button(root)
    button2['text'] = '退出'
    button2['command'] = root.quit
    button2["fg"] = "blue"
    button2.pack({"side": "left"})

    root.mainloop()
    root.destroy()


def get_token():
    apiId = '9550153'
    apiKey = 't2ePzNA79W4dOEVkhmDCB7al'
    secretKey = '248a85ff8c633684760a0b53bfebe2ef'

    url = 'https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id='\
          + apiKey + '&client_secret=' + secretKey + '&'
    data = requests.post(url)
    token = json.loads(data.content).get('access_token')
    return token


def post_voice(token):
    fp = wave.open('output.wav', 'rb')
    nf = fp.getnframes()
    f_len = nf * 2
    audio_data = fp.readframes(nf)

    cuid = "778617402"
    srv_url = 'http://vop.baidu.com/server_api' + '?cuid=' + cuid + '&token=' + token
    http_header = [
        'Content-Type: audio/pcm; rate=8000',
        'Content-Length: %d' % f_len
    ]

    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(pycurl.URL, str(srv_url))
    c.setopt(c.HTTPHEADER, http_header)
    c.setopt(c.POST, 1)
    c.setopt(c.CONNECTTIMEOUT, 30)
    c.setopt(c.TIMEOUT, 30)
    c.setopt(c.POSTFIELDS, audio_data)
    c.setopt(c.POSTFIELDSIZE, f_len)

    c.setopt(c.WRITEDATA, buffer)

    c.perform()
    c.close()
    resp = buffer.getvalue().decode('utf-8')
    data = json.loads(resp)
    result = data.get('result')[0]
    return result


def run():
    # 运行用户界面，录音并保存文件
    button()
    # 获得token
    token = get_token()
    # 提交声音文件
    result = post_voice(token=token)
    return result



if __name__ == "__main__":
    result = run()
    print(result)
    exploreapp = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    if 'run' in result:
        os.startfile(exploreapp)


