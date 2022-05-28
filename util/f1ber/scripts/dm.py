import requests 
from colorama import Fore 
from plugins .standard import setTitle ,proxy 
def MassDM (OOOOOOOO0O00O0000 ,O000OO0O0O000OOO0 ,OOO0OOOO0O00OO000 ):
    for OO0O000OOOO00OO00 in O000OO0O0O000OOO0 :
        for O0O0OO0O000OO000O in [OO00O0OOO0OOOO00O ["username"]+"#"+OO00O0OOO0OOOO00O ["discriminator"]for OO00O0OOO0OOOO00O in OO0O000OOOO00OO00 ["recipients"]]:
            try :
                setTitle (f"Messaging "+O0O0OO0O000OO000O )
                requests .post (f'https://discord.com/api/v9/channels/'+OO0O000OOOO00OO00 ['id']+'/messages',proxies =proxy (),headers ={'Authorization':OOOOOOOO0O00O0000 },data ={"content":f"{OOO0OOOO0O00OO000}"})
                print (f"{Fore.RED}Messaged: {Fore.WHITE}"+O0O0OO0O000OO000O +Fore .RESET )
            except Exception as OO00O0O000000OOOO :
                print (f"The following error has been encountered and is being ignored: {OO00O0O000000OOOO}")