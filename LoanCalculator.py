# -*- coding: utf-8 -*-
"""
A loan calculator that supports these command line arguments:
    
--interest is an obligatory argument, no "%" needed    
    
--type = annuity or diff  

Differentiate payment is where the loan principal is reduced by a constant 
amount each month. The rest of the monthly payment goes toward interest 
repayment and it is gradually reduced over the term of the loan. 
Only monthly payments are calculated for --type=diff.

Annuity payment is fixed during the whole loan term.

--principal

--payment

--periods

It takes two arguments and calculates the third for --type=annuity.

A project for hyperskill.org

@author: Giliazova
"""
import math
from argparse import ArgumentParser

#functions in an alphabetical order
def calc_annuity_monthly_payment(args):
    i = args.interest
    n = args.periods
    payment = args.principal * i * (1 + i) ** n / ((1 + i) ** n - 1) 
    payment = math.ceil(payment)  
    overpayment = math.ceil(payment * n - args.principal)
    if payment > overpayment:  # a small hack 
        s = overpayment
        overpayment = payment
        payment = s    
    print(f"Your monthly payment = {payment}!")    
    print(f"Overpayment = {overpayment}")    
    
def calc_diff_payments(args):
    sum_payments = 0
    for i in range(args.periods):
        m = i + 1
        p = args.principal
        payment = p / args.periods + args.interest * \
            (p - (p * (m - 1)) / args.periods)
        payment = math.ceil(payment)    
        sum_payments += payment    
        print(f"Month {m}: payment is {payment}")       
    overpayment = math.ceil(sum_payments - p)    
    print(f"\nOverpayment = {overpayment}")  

def calc_number_of_monthly_payments(args):
    i = args.payment / (args.payment - args.interest * args.principal)
    number_of_months = math.ceil(math.log(i,1 + args.interest))
    if number_of_months == 1:
        print("It will take 1 month to repay this loan!")
    elif number_of_months < 12:
        print(f"It will take {number_of_months} months to repay this loan!")
    elif number_of_months == 12:
        print("It will take 1 year to repay this loan!")
    elif number_of_months < 24:
        print(f"It will take 1 year and {number_of_months - 12} months to repay this loan!")
    elif number_of_months % 12 == 0:
        print(f"It will take {round(number_of_months / 12)} years to repay this loan!")
    else:
        years = round(number_of_months // 12)
        months = round(number_of_months - years * 12)
        print(f"It will take {years} years and {months} months to repay this loan!")
    overpayment = math.ceil(args.payment * number_of_months - args.principal)
    print(f"Overpayment = {overpayment}")        

def calc_principal(args):
    i = args.interest
    n = args.periods
    loan = args.payment / ((i * (1 + i) ** n) / ((1 + i) ** n - 1))
    print(f"Your loan principal = {round(loan)}!")
    overpayment = math.ceil(args.payment * n - loan)
    print(f"Overpayment = {overpayment}")    
    
def check_arguments(args):
    if not args.interest or args.interest[0] == "-":
        return False
    if args.type != "annuity" and args.type != "diff":
        return False  
    if args.type == "annuity":
        check = 0
        check += 1 if args.principal else 0
        check += 1 if args.periods else 0
        check += 1 if args.payment else 0
        if check != 2:
            return False 
    if args.type == "diff" and args.payment:
        return False  
    if args.type == "diff" and (not args.principal or not args.periods):  
        return False
    if args.principal and args.principal[0] == "-":
        return False
    if args.periods and args.periods[0] == "-":
        return False
    if args.payment and args.payment[0] == "-":
        return False
    return True    

def convert_arguments(args):
    args.payment = int(args.payment) if args.payment else None
    args.principal = int(args.principal) if args.principal else None
    args.periods = int(args.periods) if args.periods else None
    args.interest = float(args.interest) / (12 * 100)  # nominal interest
    return args    

def parse_command_line_args():
    parser = ArgumentParser()
    parser.add_argument("--type", dest = "type", 
                    help='"annuity" or "diff" (differentiated)')
    parser.add_argument("--payment", dest = "payment",
                    help="monthly payment amount")
    parser.add_argument("--principal", dest = "principal",
                    help="loan principal")
    parser.add_argument("--periods", dest = "periods",
                    help="the number of months needed to repay the loan")
    parser.add_argument("--interest", dest = "interest",
                    help="interest is specified without a percent sign")
    args = parser.parse_args()
    return args        

def what_to_calc(args):
    if args.type == "diff":
        return "d"
    if args.payment is None:
        return "a"
    if args.periods is None:
        return "n"
    if args.principal is None:
        return "p"

# main 
# e.g.: python loan_calculator.py --type=annuity --payment=1000 --principal=10000 --interest=10
while True:
    args = parse_command_line_args()
    if not check_arguments(args):
        print("Incorrect parameters")
        break 
    args = convert_arguments(args)       

    option = what_to_calc(args)
    if option == "a":
        calc_annuity_monthly_payment(args)
    elif option == "n":
        calc_number_of_monthly_payments(args)        
    elif option == "p":
        calc_principal(args)
    elif option == "d":
        calc_diff_payments(args)
    break   
        
