import requests 
from time import sleep #
from colorama import Fore 
from plugins .standard import SlowPrint ,proxy 
def WebhookSpammer (OO0OO000O000O00O0 ,O0O00O0OOO0O0O00O ):
    SlowPrint ("\"ctrl + c\" at anytime to stop\n")
    sleep (1.5 )
    while True :
        OOOOOOOO0000OOOOO =requests .post (OO0OO000O000O00O0 ,proxies =proxy (),json ={"content":O0O00O0OOO0O0O00O },params ={'wait':True })
        try :#line:18:try:
            if OOOOOOOO0000OOOOO .status_code ==204 or OOOOOOOO0000OOOOO .status_code ==200 :
                print (f"{Fore.GREEN}Message sent{Fore.RESET}")
            elif OOOOOOOO0000OOOOO .status_code ==429 :
                print (f"{Fore.YELLOW}Rate limited ({OOOOOOOO0000OOOOO.json()['retry_after']}ms){Fore.RESET}")
                sleep (OOOOOOOO0000OOOOO .json ()["retry_after"]/1000 )
            else :#line:24:else:
                print (f"{Fore.RED}Error : {OOOOOOOO0000OOOOO.status_code}{Fore.RESET}")
            sleep (.01 )
        except KeyboardInterrupt :
            break 
    SlowPrint (f'{Fore.RED}Spammed Webhook Successfully!{Fore.RESET} ')
    print ("Enter anything to continue. . . ",end ="")
    input ()