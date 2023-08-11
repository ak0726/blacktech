import math
import json
import os
import random
import slabs
import expenseList
import questionAir
from datetime import datetime
from os.path import exists



def home():
    print("====================================================")
    
    print("Hello there, Welcome to BlackTek")
    print("we offer :")
    print("1. Get Educated with our AI")
    print("2. Tax Calculator")
    print("3. Retirement Planning")
    print("4. Expenditure Tracker")
    print("5. Debt Management")
    print("-1.Exit")
    print("====================================================")

    sel = int(input("PLease enter your selection > "))
    if sel == 2:
        slabs.calTax()
    elif sel == 1:
        questionAir.askQuestion()
    elif sel == 4:
        expenseList.temp()
    else:
        print("feature not yet implmented")
    return sel;


while True:
    x = home()
    if x == -1:
        print("Thanks for using the product")
        break
