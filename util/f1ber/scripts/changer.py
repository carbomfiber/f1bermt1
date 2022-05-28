import requests 
import os 
from colorama import Fore 
from plugins .standard import SlowPrint ,getheaders ,proxy 
def HouseChanger (OOO000OO0OO00OOOO ,_OOOO000O0OO00OOOO ):
    OOOO0OOO0000O0O00 ={1 :"Hype Squad Bravery",2 :"Hype Squad Brilliance",3 :"Hype Squad Balance",}
    OOO0O0O0OO0000O00 ={'house_id':_OOOO000O0OO00OOOO }
    requests .post ('https://discord.com/api/v9/hypesquad/online',headers =getheaders (OOO000OO0OO00OOOO ),json =OOO0O0O0OO0000O00 )
    SlowPrint (f"\n{Fore.GREEN}Hypesquad changed to {Fore.WHITE}{OOOO0OOO0000O0O00[_OOOO000O0OO00OOOO]}{Fore.GREEN} ")
    print ("Enter anything to continue. . . ",end ="")
    input ()
    os .system ('cmd /k "python util/f1ber/discordtools.py"')
def StatusChanger (O0OO000OO0O0OOOOO ,OO0000O0OOOO0O000 ):
    O0000OOO0OO00O000 ={"custom_status":{"text":OO0000O0OOOO0O000 }}
    try :
        requests .patch ("https://discord.com/api/v9/users/@me/settings",proxies =proxy (),headers =getheaders (O0OO000OO0O0OOOOO ),json =O0000OOO0OO00O000 )
        SlowPrint (f"\n{Fore.GREEN}Status changed to {Fore.WHITE}{OO0000O0OOOO0O000}{Fore.GREEN} ")
    except Exception as OOO0000OOO0O0000O :
        print (f"{Fore.RED}Error:\n{OOO0000OOO0O0000O}\nOccurred while trying to change the status :/")
    print ("Enter anything to continue. . . ",end ="")
    input ()
    os .system ('cmd /k "python util/f1ber/discordtools.py"')
def BioChanger (O0OOO00OOOOO0OOO0 ,OOO0000000OOOO00O ):
    OO0OOO0OO00OOO0O0 ={"bio":str (OOO0000000OOOO00O )}
    try :
        requests .patch ("https://discord.com/api/v9/users/@me",proxies =proxy (),headers =getheaders (O0OOO00OOOOO0OOO0 ),json =OO0OOO0OO00OOO0O0 )
        SlowPrint (f"\n{Fore.GREEN}Bio changed to {Fore.WHITE}{OOO0000000OOOO00O}{Fore.GREEN} ")
    except Exception as O0O0O000000OO0OOO :
        print (f"{Fore.RED}Error:\n{O0O0O000000OO0OOO}\nOccurred while trying to change the status :/")
    print ("Enter anything to continue. . . ",end ="")
    input ()
    os .system ('cmd /k "python util/f1ber/discordtools.py"')