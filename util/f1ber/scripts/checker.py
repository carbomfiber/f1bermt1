import requests
import sys, os
from os import system
from colorama import init, Fore, Back, Style
from plugins.standard import * 

system ("cls")
init(convert=True)

print(Fore.RED +      '                                    :::::::::: :::   :::::::::  :::::::::: :::::::::')
print(Fore.RED +     '                                    :+:      :+:+:   :+:    :+: :+:        :+:    :+:')
print(Fore.RED +    '                                    +:+        +:+   +:+    +:+ +:+        +:+    +:+')
print(Fore.RED +   '                                    :#::+::#   +#+   +#++:++#+  +#++:++#   +#++:++#:')
print(Fore.RED +  '                                    +#+        +#+   +#+    +#+ +#+        +#+    +#+')
print(Fore.RED + '                                    #+#        #+#   #+#    #+# #+#        #+#    #+#  ')  
print(Fore.RED + '                                    ###      ####### #########  ########## ###    ### ')  
print("")                                                             
print(f"{Fore.MAGENTA}                                             Developer: F1ber" + Fore.LIGHTMAGENTA_EX+ "   Version 0.1")
print(f"{Fore.MAGENTA}                    No i have not coded everything. Check credits.txt to see who i have got most code from")
print("") 

print(f"{Fore.LIGHTRED_EX}Enter the file path (It must be in .txt and it must contain 1 token per line): ")
global filePath, tokens
filePath = input(f"{Fore.WHITE}File path: ")
tokens = []

def load_token():
    try:
        with open(f'{filePath}', 'r') as f:   
            for x in f.readlines():
                tokens.append(x.replace('\n',''))
    except:
        print(f"          {y}[{Fore.LIGHTRED_EX}!{y}]{w} File not found")
        input(f"""\n{y}[{b}#{y}]{w} Press ENTER to exit""")
        

def checkvalidity():
    valid = 0
    needverif = 0
    invalid = 0
    clear()
    for x in tokens:
        setTitle(f"F1BER TOKEN CHECKER -- {valid} Valid | {needverif} Verification required | {invalid} Invalid")
        src = requests.get('https://discordapp.com/api/v6/users/@me', headers={'Authorization': x})
        if src.status_code == 200:
            res_json = src.json()
            verified = res_json['verified']
            if verified == True:
                print(f'{Fore.LIGHTGREEN_EX}[!] Valid: {w}'+x)
                with open("checker-output/valids.txt", "a") as save:
                    save.write(x+"\n")
                    valid += 1
            else:
                print(f'{Fore.LIGHTRED_EX}[!] Verification required: {w}'+x)
                needverif += 1
        else:
            print(f'{Fore.RED}[!] Invalid: {w}'+x)
            invalid += 1
    
    print(f"""\n
{y}[{b}+{y}]{w} Results:\n
          {y}[{Fore.LIGHTGREEN_EX}!{y}]{w} Valid: {valid}""")
    if valid >=1:
        print("               You can find the list of valid tokens in checker-output/valids.txt")
    print(f"""          {y}[{Fore.LIGHTRED_EX}!{y}]{w} Verification required: {needverif}
          {y}[{Fore.RED}!{y}]{w} Invalid: {invalid}""")

    input(f"""\n\n{y}[{b}#{y}]{w} Press ENTER to exit""")
    os.system('cmd /k "python util/f1ber/discordtools.py"')

load_token()     
checkvalidity()