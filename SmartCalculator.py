from collections import deque


def assignment(s, variables):
    error = False
    if s.count('=') > 1 or s[1] != '=':
        print('Invalid expression 1')
        error = True
        return '', error
    first = s[0]
    if first not in variables:
        if first.isalpha():
            variables[first] = 0
        else:
            print('Invalid identificator 2')
            error = True
            return '', error
    if len(s) > 3:
        last, error = postfix(s[2:])
        if error:
            return '', error       
        last, error = calc(last, variables)
        if error:
            return '', error
    else:
        last = s[2]
        if last in variables:
            last = variables[last]
        elif last.isalpha():
            print('Unknown variable 3')
            error = True
            return '', error
        elif is_number(last):
            last = int(last)
        else:
            print('Invalid identificator 4')
            error = True
            return '', error

    variables[first] = last
    return '', error

def calc(s, variables):
    error = False
    res = 0
    stack = deque()
    for i in s:
        if is_number(i):
            stack.append(int(i))
        elif i.isalpha():
            if i in variables:
                stack.append(variables[i])
            else:
                print('Unknown variable 5')
                error = True
                break
        elif i in '+-*/^':
            if i == '-':
                if len(stack) == 1 or (stack[-2] and str(stack[-2]) in '+-*/^'):
                    stack.append(-stack.pop())
                    continue
            if len(stack) < 2:
                print('Invalid expression 6')
                error = True
                break
            b = stack.pop()
            a = stack.pop()
            if i == '+':
                stack.append(a + b)
            elif i == '-':
                stack.append(a - b)
            elif i == '*':
                stack.append(a * b)
            elif i == '/':
                stack.append(a / b)
            elif i == '^':
                stack.append(a ^ b)
        else:
            print('Invalid identifier 7')
            error = True
            break
    if len(stack) < 1:
        print('Invalid expression 8')
        error = True
    if error:
        return '', error
    else:
        return stack.pop(), error


def parse_no_space(s):
    res = ''
    error = False
    prev = ''
    for i, j in enumerate(s):
        res2, error, prev = parse_no_space_2(j, prev)
        res += res2
        if error:
            break
    return res.split(), error


def parse_no_space_2(j, prev):
    res = ''
    error = False
    if j and j in '*/^=' and j == prev:
            error = True
    elif j == '+':
            if not prev or prev in '()':
                prev = '+'
            elif prev and prev in '*/^=':
                error = True
    elif j == '-':
            if prev == '-':
                prev = '+'
            elif prev and prev in '*/^=':
                error = True
            else:
                prev = '-'
    elif prev and prev in '+-':
            res += ' ' + prev + ' '
            prev = ''
    elif j and j in '/*^()=':
            res += ' ' + j + ' '
            prev = j
    else:
            res += j
            prev = ''
    if error:
        print('Invalid expression 10', s, prev)
    return res, error, prev


def postfix(s):
    error = False
    res = ''
    postfix = deque()
    for i in s:
        if not i:
            continue
        if i.isalnum() or is_number(i):
            res += i + ' '
            continue
        elif i not in '+-=*/^()':
            print('Invalid expression 15')
            error = True
            return res, error
        if i == '(':
            postfix.append(i)
            continue
        if len(postfix) > 0:
            top = postfix[-1]
        else:
            top = ''
        if i == ')':
            while True:
                if len(postfix) == 0:
                    print('Invalid expression 16')
                    error = True
                    return res, error
                if top == '(':
                    postfix.pop()
                    break
                else:
                    res += postfix.pop() + ' '
                    if len(postfix) > 0:
                        top = postfix[-1]
            continue
        while len(postfix) > 0 and top != '(' and not precedence(i, top):
            res += postfix.pop() + ' '
            if len(postfix) > 0:
                top = postfix[-1]
        postfix.append(i)
    while len(postfix) > 0:
        res += postfix.pop() + ' '
    return res.split(), error


def precedence (i, j):
    if i == '^' and j in '+-*/=':
        return True
    elif i in '*/' and j in '+-=':
        return True
    elif i in '+-' and j in '=':
        return True
    return False

def is_number(n):  # check if string is number (float, minus, etc), better than .isdigit()!
    try:
        num = float(n)
        return True
    except ValueError:
        return False


variables = dict()
while True:
    s = input()

    if s == '/exit':
        print('Bye!')
        break
    if s == '/help':
        print('The program performs operations with integers and variables: +-=*/^()')
        continue
    if s.startswith('/'):
        print('Unknown command 17')
        continue
    if s == '':
        continue

    s, error = parse_no_space(s)  # list
    if error:
        continue

    if len(s) == 1:
        try:
            s = int(s[0])
            print(s)
        except:
            if s[0] in variables:
                print(variables[s[0]])
            elif s[0].isalpha():
                print('Unknown variable 18')
            else:
                print('Invalid identifier 19')
        finally:
            continue

    if '=' in s:
        res, error = assignment(s, variables)
    else:
        s, error = postfix(s)
        if error:
            continue
        res, error = calc(s, variables)
    if error:
        continue

    if res != '':
        print(int(res))
