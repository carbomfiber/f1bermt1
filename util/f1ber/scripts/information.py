import requests 
import os 
from datetime import datetime 
from colorama import Fore 
from plugins .standard import getheaders 
def Info (O0O00O0O000O00OOO ):
    OO0O0O0OOOO0OO0O0 =requests .get ('https://discord.com/api/v9/users/@me',headers =getheaders (O0O00O0O000O00OOO ))
    O0OO0000OO0OO0O00 ={'american express':'3','visa':'4','mastercard':'5'}
    OOOOOOOO0OOO0OOOO =""
    OO00O00O0OOO0O00O =1 
    O0O0OO0OO000O000O =2 
    O0O00000O0OOO0OO0 =4 
    OO000O00O00000O0O =8 
    O00O0000O0O00OOO0 =64 
    OO0OOOO0O00O0O0O0 =128 
    O00OO0000O0OOOOOO =256 
    O0O0OOO00O0O00O0O =512 
    O0OOO0O0O00O00000 =16384 
    OO0OOO0O0OOOOOO0O =131072 
    OO0OO0O0OO00O0O00 =OO0O0O0OOOO0OO0O0 .json ()['flags']
    if (OO0OO0O0OO00O0O00 ==OO00O00O0OOO0O00O ):
        OOOOOOOO0OOO0OOOO +="Staff, "
    if (OO0OO0O0OO00O0O00 ==O0O0OO0OO000O000O ):
        OOOOOOOO0OOO0OOOO +="Partner, "
    if (OO0OO0O0OO00O0O00 ==O0O00000O0OOO0OO0 ):
        OOOOOOOO0OOO0OOOO +="Hypesquad Event, "
    if (OO0OO0O0OO00O0O00 ==OO000O00O00000O0O ):
        OOOOOOOO0OOO0OOOO +="Green Bughunter, "
    if (OO0OO0O0OO00O0O00 ==O00O0000O0O00OOO0 ):
        OOOOOOOO0OOO0OOOO +="Hypesquad Bravery, "
    if (OO0OO0O0OO00O0O00 ==OO0OOOO0O00O0O0O0 ):
        OOOOOOOO0OOO0OOOO +="HypeSquad Brillance, "
    if (OO0OO0O0OO00O0O00 ==O00OO0000O0OOOOOO ):
        OOOOOOOO0OOO0OOOO +="HypeSquad Balance, "
    if (OO0OO0O0OO00O0O00 ==O0O0OOO00O0O00O0O ):
        OOOOOOOO0OOO0OOOO +="Early Supporter, "
    if (OO0OO0O0OO00O0O00 ==O0OOO0O0O00O00000 ):
        OOOOOOOO0OOO0OOOO +="Gold BugHunter, "
    if (OO0OO0O0OO00O0O00 ==OO0OOO0O0OOOOOO0O ):
        OOOOOOOO0OOO0OOOO +="Verified Bot Developer, "
    if (OOOOOOOO0OOO0OOOO ==""):
        OOOOOOOO0OOO0OOOO ="None"
    OOOO00O0000OO0000 =OO0O0O0OOOO0OO0O0 .json ()['username']+'#'+OO0O0O0OOOO0OO0O0 .json ()['discriminator']
    OO0OO0OOOO0O00O00 =OO0O0O0OOOO0OO0O0 .json ()['id']
    OOO0OOOO00OO00O00 =OO0O0O0OOOO0OO0O0 .json ()['phone']
    OOOOO0OO0000OO000 =OO0O0O0OOOO0OO0O0 .json ()['email']
    OO0OO00O0OOO0OOO0 =OO0O0O0OOOO0OO0O0 .json ()['locale']
    OOO0OOOO000OO0OOO =OO0O0O0OOOO0OO0O0 .json ()['mfa_enabled']
    O0OOOOO00O0O0000O =OO0O0O0OOOO0OO0O0 .json ()['avatar']
    OO0000O00O00O000O =False 
    O00OOO00OOOOOO0OO =requests .get ('https://discordapp.com/api/v9/users/@me/billing/subscriptions',headers =getheaders (O0O00O0O000O00OOO ))
    OOO00OOO0OOO00OO0 =O00OOO00OOOOOO0OO .json ()
    OO0000O00O00O000O =bool (len (OOO00OOO0OOO00OO0 )>0 )
    O0OO000OOO0O0O000 =f'https://cdn.discordapp.com/avatars/{OO0OO0OOOO0O00O00}/{O0OOOOO00O0O0000O}.webp'
    O0000OOO000OO0000 =datetime .utcfromtimestamp (((int (OO0OO0OOOO0O00O00 )>>22 )+1420070400000 )/1000 ).strftime ('%d-%m-%Y %H:%M:%S UTC')
    if OO0000O00O00O000O :
        O0OOOOOO0O0OO0000 =datetime .strptime (OOO00OOO0OOO00OO0 [0 ]["current_period_end"].split ('.')[0 ],"%Y-%m-%dT%H:%M:%S")
        OOOOO000O00OOOO00 =datetime .strptime (OOO00OOO0OOO00OO0 [0 ]["current_period_start"].split ('.')[0 ],"%Y-%m-%dT%H:%M:%S")
        OO0OO0OO00O00O0OO =abs ((OOOOO000O00OOOO00 -O0OOOOOO0O0OO0000 ).days )
    OOOO00000O0000O0O =[]
    for O00OOOOO0OOO0OO0O in requests .get ('https://discordapp.com/api/v9/users/@me/billing/payment-sources',headers =getheaders (O0O00O0O000O00OOO )).json ():
        OOOO0OOO00OO0OO0O =O00OOOOO0OOO0OO0O ['billing_address']
        O000O0O00O0OOOO0O =OOOO0OOO00OO0OO0O ['name']
        OO0OOO00OO0O000OO =OOOO0OOO00OO0OO0O ['line_1']
        OO000OOO00O0OO0O0 =OOOO0OOO00OO0OO0O ['line_2']
        O00O000OO000O00O0 =OOOO0OOO00OO0OO0O ['city']
        OOOO0O0OO000000O0 =OOOO0OOO00OO0OO0O ['postal_code']
        OO00OOOOOOOOOO0OO =OOOO0OOO00OO0OO0O ['state']
        O0O00O000O0000000 =OOOO0OOO00OO0OO0O ['country']
        if O00OOOOO0OOO0OO0O ['type']==1 :
            OO0000OO0000000OO =O00OOOOO0OOO0OO0O ['brand']
            OOOOO0O0OO0OOO0OO =O0OO0000OO0OO0O00 .get (OO0000OO0000000OO )
            O00O00O0OO00000O0 =O00OOOOO0OOO0OO0O ['last_4']
            O0000O00OO00O0O00 =str (O00OOOOO0OOO0OO0O ['expires_month'])
            O0000OO0O0O000O0O =str (O00OOOOO0OOO0OO0O ['expires_year'])
            OOO00OO00O0O000O0 ={'Payment Type':'Credit Card','Valid':not O00OOOOO0OOO0OO0O ['invalid'],'CC Holder Name':O000O0O00O0OOOO0O ,'CC Brand':OO0000OO0000000OO .title (),'CC Number':''.join (OO0O00000O0000000 if (O000O000O00O000OO +1 )%2 else OO0O00000O0000000 +' 'for O000O000O00O000OO ,OO0O00000O0000000 in enumerate ((OOOOO0O0OO0OOO0OO if OOOOO0O0OO0OOO0OO else '*')+('*'*11 )+O00O00O0OO00000O0 )),'CC Exp. Date':('0'+O0000O00OO00O0O00 if len (O0000O00OO00O0O00 )<2 else O0000O00OO00O0O00 )+'/'+O0000OO0O0O000O0O [2 :4 ],'Address 1':OO0OOO00OO0O000OO ,'Address 2':OO000OOO00O0OO0O0 if OO000OOO00O0OO0O0 else '','City':O00O000OO000O00O0 ,'Postal Code':OOOO0O0OO000000O0 ,'State':OO00OOOOOOOOOO0OO if OO00OOOOOOOOOO0OO else '','Country':O0O00O000O0000000 ,'Default Payment':O00OOOOO0OOO0OO0O ['default']}
        elif O00OOOOO0OOO0OO0O ['type']==2 :
            OOO00OO00O0O000O0 ={'Payment Type':'PayPal','Valid':not O00OOOOO0OOO0OO0O ['invalid'],'PayPal Name':O000O0O00O0OOOO0O ,'PayPal Email':O00OOOOO0OOO0OO0O ['email'],'Address 1':OO0OOO00OO0O000OO ,'Address 2':OO000OOO00O0OO0O0 if OO000OOO00O0OO0O0 else '','City':O00O000OO000O00O0 ,'Postal Code':OOOO0O0OO000000O0 ,'State':OO00OOOOOOOOOO0OO if OO00OOOOOOOOOO0OO else '','Country':O0O00O000O0000000 ,'Default Payment':O00OOOOO0OOO0OO0O ['default']}
        OOOO00000O0000O0O .append (OOO00OO00O0O000O0 )
    print (f'''
    {Fore.RESET}{Fore.LIGHTRED_EX}<<────────────{OOOO00O0000OO0000}────────────>>{Fore.RESET}
    [{Fore.RED}User ID{Fore.RESET}]         {OO0OO0OOOO0O00O00}
    [{Fore.RED}Created at{Fore.RESET}]      {O0000OOO000OO0000}
    [{Fore.RED}Language{Fore.RESET}]        {OO0OO00O0OOO0OOO0}
    [{Fore.RED}Badges{Fore.RESET}]          {OOOOOOOO0OOO0OOOO}
    [{Fore.RED}Avatar URL{Fore.RESET}]      {O0OO000OOO0O0O000 if O0OOOOO00O0O0000O else ""}
    [{Fore.RED}Token{Fore.RESET}]           {O0O00O0O000O00OOO}
    {Fore.RESET}{Fore.LIGHTRED_EX}<───────────Security Info───────────>{Fore.RESET}
    [{Fore.RED}2 Factor{Fore.RESET}]        {OOO0OOOO000OO0OOO}
    [{Fore.RED}Email{Fore.RESET}]           {OOOOO0OO0000OO000}
    [{Fore.RED}Phone number{Fore.RESET}]    {OOO0OOOO00OO00O00 if OOO0OOOO00OO00O00 else ""}
    {Fore.RESET}{Fore.LIGHTRED_EX}<────────────Nitro Info─────────────>{Fore.RESET}
    [{Fore.RED}Nitro Status{Fore.RESET}]    {OO0000O00O00O000O}
    [{Fore.RED}Expires in{Fore.RESET}]      {OO0OO0OO00O00O0OO if OO0000O00O00O000O else "0"} day(s)
                ''')
    if len (OOOO00000O0000O0O )>0 :
        print (f"\t\t{Fore.RESET}{Fore.LIGHTRED_EX}<────────────Billing Info────────────>{Fore.RESET}")
        if len (OOOO00000O0000O0O )==1 :
            for O00OOOOO0OOO0OO0O in OOOO00000O0000O0O :
                for OO0O0O00000OO0OO0 ,OO0O0000OOOO000O0 in O00OOOOO0OOO0OO0O .items ():
                    if not OO0O0000OOOO000O0 :
                        continue 
                    print (f"[{Fore.RED}"+'{:<23}{:<10}{}'.format (OO0O0O00000OO0OO0 +Fore .RED +Fore .RESET +"]",Fore .RESET ,OO0O0000OOOO000O0 ))
        else :
            for OOOO00O0OOO0000OO ,O00OOOOO0OOO0OO0O in enumerate (OOOO00000O0000O0O ):
                O0OOOOO0O000000OO =f'Payment Method #{OOOO00O0OOO0000OO + 1} ({O00OOOOO0OOO0OO0O["Payment Type"]})'
                print (''+O0OOOOO0O000000OO )
                print (''+('='*len (O0OOOOO0O000000OO )))
                for OO0OO0OOO0O0O0O0O ,(OO0O0O00000OO0OO0 ,OO0O0000OOOO000O0 )in enumerate (O00OOOOO0OOO0OO0O .items ()):
                    if not OO0O0000OOOO000O0 or OO0OO0OOO0O0O0O0O ==0 :
                        continue 
                    print (f"[{Fore.RED}"+'{:<23}{:<10}{}'.format (OO0O0O00000OO0OO0 +Fore .RED +Fore .RESET +"]",Fore .RESET ,OO0O0000OOOO000O0 ))
                if OOOO00O0OOO0000OO <len (OOOO00000O0000O0O )-1 :
                    print (f'{Fore.RESET}\n')
        print (f'{Fore.RESET}')
    print (f'{Fore.GREEN}CREDIT TO RDIMO {Fore.RED}')
    input (f'{Fore.LIGHTRED_EX}[{Fore.WHITE}X{Fore.LIGHTRED_EX}] {Fore.RESET}Enter anything to continue . . .  {Fore.RED}')
    os .system ('cmd /k "python util/f1ber/discordtools.py"')