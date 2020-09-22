# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 18:46:24 2020

@author: Giliazova
"""
import sqlite3
import random


class Account:
    def __init__(self, id_num, card_num, pin_code, balance):
        self.id = id_num
        self.card_number = card_num
        self.pin = pin_code
        self.balance = balance

    def add_income(self):
        income = int(input("Enter income: \n"))
        self.balance += income
        change_db('UPDATE card SET balance = {} WHERE id = {};'
                  .format(self.balance, self.id))
        print("Income was added!\n")

    def close_account(self):
        change_db('DELETE FROM card WHERE id = {};'
                  .format(self.id))
        print("The account has been closed!\n")
        return

    def do_transfer(self):
        print("Transfer")
        card_num = input("Enter card number:\n")
        if card_num == self.card_number:
            print("You can't transfer money to the same account!\n")
            return
        if not check_luhn(card_num):
            print("Probably you made a mistake in the card number. Please try again!\n")
            return
        cur.execute('SELECT balance FROM card WHERE number = {};'
                    .format(card_num))
        balance = cur.fetchone()  # debugged
        if balance is None:
            print("Such a card does not exist.\n")
            return
        else:
            balance = int(balance[0])  # debugged
        money = int(input("Enter how much money you want to transfer:\n"))
        if money > self.balance:
            print("Not enough money!\n")
            return
        self.balance -= money
        change_db('UPDATE card SET balance = {} WHERE number = {};'
                  .format(self.balance, self.card_number))
        balance += money
        change_db('UPDATE card SET balance = {} WHERE number = {};'
                  .format(balance, card_num))
        print("Success!\n")
        return

    def print_balance(self):
        print("Balance: " + str(self.balance) + "\n")


def change_db(query):
    cur.execute(query)
    conn.commit()


def check_luhn(card_num):
    number = [int(i) for i in card_num[:-1]]
    # multiply odd digits by 2 using 1-indexation
    for i in range(0, len(number), 2):
        number[i] = number[i] * 2
        # subtract 9 to numbers over 9
        if number[i] > 9:
            number[i] = number[i] - 9
    # add all numbers
    number_sum = sum(number)
    # the received number should be divisible by 10
    checksum = (10 - number_sum % 10) % 10
    if checksum == int(card_num[-1]):
        return True
    else:
        return False


def create_account():
    # Issuer Identification Number
    iin = "400000"
    # id
    cur.execute('SELECT MAX(id) FROM card;')
    id_num = cur.fetchone()[0]  # (None,) for empty database
    if id_num is None:  # new empty table card
        id_num = 1
    else:
        id_num += 1
    # account number
    account_number = str(id_num).zfill(9)  # 1 -> 000000001
    # checksum
    checksum = generate_luhn(iin, account_number)
    card_number = iin + account_number + checksum
    # PIN code
    pin = str(random.randrange(1000, 9999))
    # balance
    balance = 0

    # put this new card into the database card.s3db
    change_db('INSERT INTO card VALUES ({}, {}, {}, {});'
              .format(id_num, card_number, pin, balance))

    print("Your card has been created")
    print("Your card number:")
    print(card_number)
    print("Your card PIN:")
    print(pin)


# generate checksum for account number according to Luhn algorithm
def generate_luhn(iin, account_number):
    number = iin + account_number  # string
    number = [int(i) for i in number]
    # multiply odd digits by 2 using 1-indexation
    for i in range(0, len(number), 2):
        number[i] = number[i] * 2
        # subtract 9 to numbers over 9
        if number[i] > 9:
            number[i] = number[i] - 9
    # add all numbers
    number_sum = sum(number)
    # the received number should be divisible by 10
    checksum = (10 - number_sum % 10) % 10
    return str(checksum)


def input_account_data():
    print("Enter your card number:")
    card_num = input()
    print("Enter your PIN:")
    pin_code = input()
    return card_num, pin_code


def log_into_account(card_num, pin_code):

    cur.execute('SELECT id, balance FROM card WHERE \
                number = {} AND pin = {};'
                .format(card_num, pin_code))
    # unique id defines number so there is only 1 such card
    res = cur.fetchone()
    if res is None:  # debugged with empty database
        print("Wrong card number or PIN!\n")
        return False
    else:
        print("You have successfully logged in!\n")
        id_num, balance = (i for i in res)
        account = Account(id_num, card_num, pin_code, balance)
        return account


def on_log_out():
    print("You have successfully logged out!\n")


def on_exit():
    print("Bye!")


# connecting to the SQLite3 database card.s3db
conn = sqlite3.connect('card.s3db')  # used in function create_account
cur = conn.cursor()  # used in functions

change_db('CREATE TABLE IF NOT EXISTS card(\
            id INTEGER,\
            number TEXT,\
            pin TEXT,\
            balance INTEGER DEFAULT 0);')

menu = "main menu"
while True:
    if menu == "main menu":

        print("1. Create an account")
        print("2. Log into account")
        print("0. Exit")

        user_input = input()
        if user_input == "1":
            create_account()
        elif user_input == "2":
            card_num, pin_code = (i for i in input_account_data())
            account = log_into_account(card_num, pin_code)
            if account:
                menu = "account menu"
        elif user_input == "0":
            on_exit()
            break

    if menu == "account menu":
        print("1. Balance")
        print("2. Add income")
        print("3. Do transfer")
        print("4. Close account")
        print("5. Log out")
        print("0. Exit")

        user_input = input()
        if user_input == "1":
            account.print_balance()
        elif user_input == "2":
            account.add_income()
        elif user_input == "3":
            account.do_transfer()
        elif user_input == "4":
            account.close_account()
            menu = "main menu"
        elif user_input == "5":
            on_log_out()
            menu = "main menu"
        elif user_input == "0":
            on_exit()
            break
