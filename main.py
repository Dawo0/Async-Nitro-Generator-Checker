from colorama import Fore
import httpx
from discord_webhook import DiscordWebhook
from time import sleep
import numpy
import string
import asyncio
from cursor import hide
hide()
# Designs
logo = '''

        ___                             _   ___ __                
       /   |  _______  ______  _____   / | / (_) /__________      
      / /| | / ___/ / / / __ \/ ___/  /  |/ / / __/ ___/ __ \     
     / ___ |(__  ) /_/ / / / / /__   / /|  / / /_/ /  / /_/ /     
    /_/  |_/____/\__, /_/ /_/\___/  /_/ |_/_/\__/_/   \____/      
                /____/                                                                                                                                                                                 
'''


def loading(ex):

    load = [".", "..", "..."]

    for i in range(ex):

        pause = .60

        for i in load:

            print(i, end="\r")
            sleep(pause)
            pause += .2

        print("                   ", end="\r")


licence = '''





    Copyright (c) 2022 Dawoo#2993 dawoo.sa@protonmail.com
    Permission is hereby granted, free of charge, 
    to any person obtaining a copy of this software and associated documentation files (the “Software”), 
    to deal in the Software without restriction, including without limitation the rights to 
    use, copy, modify, merge, publish, distribute, sublicense, 
    and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, 
    subject to the following conditions:
    The above copyright notice and this permission notice shall be included in all copies 
    or substantial portions of the Software.
    THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
    INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
    IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
    DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

'''

# User-Interface


def cls():

    import os

    os.system('cls' if os.name == 'nt' else 'clear')


def slowprint(str):

    import sys

    for letter in str:

        sys.stdout.write(letter)
        sys.stdout.flush()
        sleep(0.01)


def ui():
    print(Fore.RED + licence)
    sleep(3)

    cls()
    sleep(.5)

    print(Fore.BLUE + logo)
    sleep(.5)

    slowprint(Fore.CYAN + "Discord: Dawoo#2993 | Email: dawoo.sa@protonmail.com")
    print("")
    sleep(.5)
    print("")

    check_internet()
    loading(ex=1)

    print("[+]Internet Checked.")
    im_checker()

    loading(ex=1)
    print("[+]Packages Imported.")

    sleep(.45)
    print("")

# Nitro Generator + Checker


async def gen_code():

    chars = []
    chars[:0] = string.ascii_uppercase + string.digits + string.ascii_lowercase
    c = numpy.random.choice(chars, size=[1999999, 16])

    for s in c:

        code = ''.join(x for x in s)
        return code


async def verify():

    async with httpx.AsyncClient() as client:

        while 1:

            # DO NOT add "await" command it will cause the scirpt to go slower.
            code = gen_code()
            r = await client.get(f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true")

            if r.status_code == 200:

                print(Fore.GREEN + "[+]Valid")
                whook_send(url=WEBHOOK, text=f"discord.gift/{code}")
            elif r.status_code != 200:

                print(Fore.RED + "[-]Invalid")

# Discord Webhook Related


def whook_send(webhook_url, text):

    DiscordWebhook(url=webhook_url, content=f"```{text}```").execute()


def webhook_check(whook):

    try:

        r = httpx.get(url=whook)

        if r.status_code == 200:

            pass

        elif r.status_code != 200:

            print("")
            print(
                Fore.RED + "[-]You Entered Wrong Webhook URL, \n[-]Re-Open The Script And Try Again.")
            sleep(1.5)

            exit()

    except httpx.UnsupportedProtocol:

        print("")
        print(Fore.RED + "[-]Please Enter A Webhook URL.")
        print(Fore.RED + "[-]Re-Open The Script And Try Again.")
        sleep(2)

        exit()


# Import Checker


def im_checker():

    try:

        import httpx

    except ImportError:

        print(
            Fore.RED + "[+]Please download HTTPX package using the following command on console: py pip install httpx")
        sleep(2)

        exit()

    try:

        from discord_webhook import DiscordWebhook

    except ImportError:

        print(
            Fore.RED + "[+]Please download discord_webhook package using the following command on console: py pip install discord_webhook")
        sleep(2)

        exit()

    try:

        import numpy

    except ImportError:

        print(
            Fore.RED + "[+]Please download numpy package using the following command on console: py pip install numpy")
        sleep(2)

        exit()

    try:

        from colorama import Fore

    except ImportError:

        print(
            Fore.RED + "[+]Please download colorama package using the following command on console: py pip install colorama")
        sleep(2)

        exit()

    try:

        from cursor import hide

    except ImportError:

        print(
            Fore.RED + "[+]Please download cursor package using the following command on console: py pip install cursor")
        sleep(2)

        exit()
# Internet Checker


def check_internet():

    url = "https://github.com"

    try:

        r = httpx.get(url=url)

    except httpx.ConnectError:

        print(Fore.RED + "[-]No Internet Connection.")
        sleep(1.8)
        exit()

# Main Loop


def main():
    global WEBHOOK

    ui()

    WEBHOOK = input(Fore.CYAN + "[+]Enter Webhook URL to send valid codes: ") # Or Replace input with "webhook-url"

    webhook_check(whook=WEBHOOK)

    try:

        whook_send(webhook_url=WEBHOOK,
                   text="Start Checking\nAny Valid Codes will be sent here.")

    except:

        pass

    asyncio.run(verify())


main()
