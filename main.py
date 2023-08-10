import math
import json
import os
import random
from datetime import datetime
from os.path import exists


def home():
    print("====================================================")
    print("Hello there, Welcome to BlackTek")
    print("we offer :")
    print("1. Get Educated with our AI")
    print("2. Tax Optimzation")
    print("3. Retirement Planning")
    print("4.Expenditure Tracker")
    print("5.Debt Management")
    print("====================================================")

    sel = int(input("PLease enter your selection > "))
    return sel;


while True:
    x = home()
    if x == -1:
        print("Thanks for using the product")
        break
