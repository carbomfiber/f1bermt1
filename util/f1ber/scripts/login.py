import requests
import os 
from time import sleep 
from selenium import webdriver ,common
from colorama import Fore ,Back 
from plugins .standard import getDriver ,getheaders ,SlowPrint
def TokenLogin (O0O000OO000O0000O ):
    O0OOO00O0000000O0 =requests .get ("https://discord.com/api/v9/users/@me",headers =getheaders (O0O000OO000O0000O )).json ()
    OOO0O0OOO00O00OO0 =O0OOO00O0000000O0 ["username"]+"#"+str (O0OOO00O0000000O0 ["discriminator"])
    O00OO0OOO00OO0000 ="""
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"%s"`
            location.reload();
        """%(O0O000OO000O0000O )
    O0OOO0OO00OOOO00O =getDriver ()
    if O0OOO0OO00OOOO00O =="chromedriver.exe":
        OOO0OOO0O0OOO000O =webdriver .ChromeOptions ()
        OOO0OOO0O0OOO000O .add_experimental_option ('excludeSwitches',['enable-logging'])
        OOO0OOO0O0OOO000O .add_experimental_option ("detach",True )
        try :
            OOO00000O00O00OO0 =webdriver .Chrome (options =OOO0OOO0O0OOO000O )
        except common .exceptions .SessionNotCreatedException as OO0O0OOO0OO00000O :
            print (OO0O0OOO0OO00000O .msg )
            sleep (2 )
            SlowPrint ("Enter anything to continue. . . ")
            input ()
    elif O0OOO0OO00OOOO00O =="operadriver.exe":
        OOO0OOO0O0OOO000O =webdriver .opera .options .ChromeOptions ()
        OOO0OOO0O0OOO000O .add_experimental_option ('excludeSwitches',['enable-logging'])
        OOO0OOO0O0OOO000O .add_experimental_option ("detach",True )
        try :
            OOO00000O00O00OO0 =webdriver .Opera (options =OOO0OOO0O0OOO000O )
        except common .exceptions .SessionNotCreatedException as OO0O0OOO0OO00000O :
            print (OO0O0OOO0OO00000O .msg )
            sleep (2 )
            SlowPrint ("Enter anything to continue. . . ")
            input ()
    elif O0OOO0OO00OOOO00O =="msedgedriver.exe":
        OOO0OOO0O0OOO000O =webdriver .EdgeOptions ()
        OOO0OOO0O0OOO000O .add_experimental_option ('excludeSwitches',['enable-logging'])
        OOO0OOO0O0OOO000O .add_experimental_option ("detach",True )
        try :
            OOO00000O00O00OO0 =webdriver .Edge (options =OOO0OOO0O0OOO000O )
        except common .exceptions .SessionNotCreatedException as OO0O0OOO0OO00000O :
            print (OO0O0OOO0OO00000O .msg )
            sleep (2 )
            SlowPrint (f"Enter anything to continue. . .")
            input ()
    else :
        print (f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Coudln\'t find a suitable driver to automatically login to {OOO0O0OOO00O00OO0}')
        sleep (3 )
        print (f"{Fore.YELLOW}Paste this script into the console of a browser:{Fore.RESET}\n\n{Back.RED}{O00OO0OOO00OO0000}\n{Back.RESET}")
        print ("Enter anything to continue. . . ",end ="")
        input ()
    print (f"{Fore.LIGHTRED_EX}Logging into {Fore.WHITE}{OOO0O0OOO00O00OO0}")
    OOO00000O00O00OO0 .get ("https://discordapp.com/login")
    OOO00000O00O00OO0 .execute_script (O00OO0OOO00OO0000 )
    os .system ('cmd /k "python util/f1ber/discordtools.py"')