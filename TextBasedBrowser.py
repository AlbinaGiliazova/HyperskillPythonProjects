# -*- coding: utf-8 -*-
"""
A text-based browser that can show the text from the requested URLs, parsed 
for the particular HTML tags; colour the links in blue; return back to the 
previous tabs; save the tabs in a directory and show the cached tabs. The 
commands are: "back", "exit", an Internet address with or without "https://".

A project for hyperskill.org

@author: Giliazova
"""
from argparse import ArgumentParser
from bs4 import BeautifulSoup
from collections import deque
import colorama
import os
import requests
import sys


# functions in an alphabetical order
def add_https(address):
    if not address.startswith("http"):
        return "https://" + address
    return address


def check_address(address):
    if "." not in address and address != "back":
        return False
    return True


def check_arguments(args):
    if not args.dir:
        return False
    return True


def check_cache(cache, address):
    if address in cache:
        return True
    return False


def create_dir():
    args = parse_command_line_args()  # args.dir to store webpages
    if not check_arguments(args):
        args.dir = "tb_tabs"
    if not os.path.exists(args.dir):
        os.makedirs(args.dir)
    return args.dir


def get_from_history(history, history_flag):
    if not history_flag:
        n = 2
    else:
        n = 1
    for _ in range(n):
        try:
            address = history.pop()
            history_flag = True
        except IndexError:
            address = ""
            history_flag = False
    return address, history_flag


def get_text(r):
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup, soup.get_text()


def main():
    directory = create_dir()
    cache = set()  # check only in this cache, not directory
    history = deque()
    history_flag = False

    while directory:
        address = input()
        if address == "exit":
            break
        if not check_address(address):
            print("Error: Incorrect URL")
            continue
        if address == "back":
            address, history_flag = get_from_history(history, history_flag)
        elif history_flag:
            history_flag = False
        address = add_https(address)
        if not history_flag:
            history.append(address)
        if check_cache(cache, address):
            print_from_file(directory, address)
            continue
        print_from_internet_and_save(cache, directory, address)


def parse_command_line_args():
    parser = ArgumentParser()
    parser.add_argument(dest="dir",
                        help="a directory for saving webpages")
    args = parser.parse_args()
    return args


def print_from_file(directory, address):
    file_name = address[address.find("//") + 2:address.rfind(".")]
    file_path = directory + "\\" + file_name  # Windows
    with open(file_path) as f:
        sys.stdout.write(f.read() + "\n")


def print_from_internet_and_save(cache, directory, address):
    r = requests.get(address)
    if r.status_code == 200:
        soup, text = get_text(r)
        print_text(soup, text)
        save(cache, directory, address, text)
    else:
        sys.stdout.write(f"Error {r.status_code}\n")


def print_text(soup, text):
    colorama.init()
    links = soup.find_all("a")
    if not links:
        return text
    text_ind = 0
    for link in links:
        ind = text.find(link.text)
        print(colorama.Style.RESET_ALL + text[text_ind:ind])
        print(colorama.Fore.BLUE + link.text)
        text_ind = ind + len(link.text)

def save(cache, directory, address, text):
    cache.add(address)
    file_name = address[address.find("//") + 2:address.rfind(".")]
    file_path = directory + "\\" + file_name  # Windows
    with open(file_path, "w") as f:  # no rewrite check
        f.write(text)


if __name__ == "__main__":
    main()
