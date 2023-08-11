import math
import json
import os
import random
import slabs
import expenseList
import questionAir
import retirement
from datetime import datetime
from os.path import exists
from colorama import Fore , Style



def home():
    # print("====================================================")
    os.system("clear")
    print(Fore.BLUE + Style.BRIGHT+
        '''
 ██████╗ ██╗███╗   ██╗███╗   ██╗██╗███████╗
██╔════╝ ██║████╗  ██║████╗  ██║██║██╔════╝
██║  ███╗██║██╔██╗ ██║██╔██╗ ██║██║█████╗  
██║   ██║██║██║╚██╗██║██║╚██╗██║██║██╔══╝  
╚██████╔╝██║██║ ╚████║██║ ╚████║██║███████╗
 ╚═════╝ ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚═╝╚══════╝


'''
    )
    print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"Hello there, Welcome to BlackTek"+Fore.RESET)
    print(Fore.GREEN+Style.BRIGHT+"we offer :")
    print(Fore.BLUE+Style.BRIGHT+"1. Get Educated with our AI")
    print(Fore.BLUE+Style.BRIGHT+"2. Tax Calculator")
    print(Fore.BLUE+Style.BRIGHT+"3. Retirement Planning")
    print(Fore.BLUE+Style.BRIGHT+"4. Expenditure Tracker")
    #print(Fore.BLUE+Style.BRIGHT+"5. Debt Management")
    print(Fore.RED+Style.BRIGHT+"5. Exit"+Fore.RESET)
    print("====================================================")

    sel = int(input("PLease enter your selection > "))
    if sel == 2:
        slabs.calTax()
    elif sel == 1:
        questionAir.askQuestion()
    elif sel == 4:
        expenseList.temp()
    elif sel == 3:
        retirement.temp2()
    elif sel == 5:
        return -1
    else:
        print("feature not yet implmented")
    return sel;

while True:
    x = home()
    if x == -1:
        print(Fore.RED+Style.BRIGHT+"Thanks for using the product ")
        break
