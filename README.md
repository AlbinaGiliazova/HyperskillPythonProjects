# Hyperskill Python Projects
Projects from https://hyperskill.org, implementation by Albina Giliazova in Python.

**Banking System**

A banking system with text interface that can:
create a card with a number according to Luhn algorithm and a random pin-code,
log into account of the card to add money, 
see balance, 
transfer money to another card, 
close account.
Cards are stored in SQLite3 database.

**Chat bot**

A simple chat bot that asks name, guesses age, counts to a specified number and
asks a question about programming.

**Coffee Machine**

Simulator of a coffee machine. It can run out of ingredients, such as milk or 
coffee beans, it can offer you various types of coffee, and, finally, it will 
take money for the prepared drink.

**Hangman**

Hangman is a popular yet grim intellectual game. A cruel computer hides a word 
from you. Letter by letter you try to guess it. If you fail, you'll be hanged, 
if you win, you'll survive.

**HyperCar**

A website made with Django 2.2, HTML for processing a car service queue. Users 
can get tickets for three types of service. Workers can process these tickets.
The next ticket is shown according to priority rules. The Django files that were
not modified are not included here.

**HyperJob**

A website made with Django 2.2, SQLite database, Django ORM, HTML, CSS for providing
a service to add and show resumes and vacancies. Only authenticated users can add texts
with privileges if staff or not. The Django files that were not modified are not included here.

**HyperNews**

A website made with Django 2.2, HTML, CSS, JSON which can show to a user the news
grouped by the date with clickable links to each news; the user can add news and search.
The Django files that were not modified are not included here.

**Loan Calculator**

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

**Multilingual Online Translator**

This program translates the given word from one given language to 
another given language or to all supported. The program supports 13 languages and 
uses parsing of the website Reverso. It uses requests, BeautifulSoup and supports
command line arguments, for example: translator.py english all hello

**Numeric Matrix Processor**

A numeric processor which can add matrices, multiply a matrix by a constant or
by another matrix, transpose a matrix in four different ways, calculate
a determinant and inverse a matrix.

**Password Hacker**

A login and password hacking program with algorithms for simple brute-force, 
dictionary-based brute-force, brute-force using vulnerability with exception and
brute-force using vulnerability with time.

**Regex Engine**

A regex engine that supports these metacharacters:
. matches any single char,
^ matches only the beginning of the string,
$ matches only the end of the string,
\\ is the escape sequence,
? means that preceding char is repeated zero or one times,
\* means that preceding char is repeated zero or more times,
\+ means that preceding char is repeated one or more times. 
Note: In Spider IDE the input string "\\" doesn't need to be escaped like "\\\\".

**Rock, Paper, Scissors**

Rock, paper, scissors is a well-known hand game. Each one of two players 
simultaneously forms one of three shapes with their hands, and then, 
depending on the chosen shapes, the winner is determined: rock beats scissors, 
paper wins over rock, scissors beat paper.
The game is widely used to make a fair decision between equal options.
This game supports custom number of playable options to choose from.
The player can enter them like this: 
rock,gun,lightning,devil,dragon,water,air,paper,sponge,wolf,tree,human,snake,scissors,fire. 
Print !rating to see the rating (100 for win, 50 for draw, 0 for lose).
Print !exit to exit the game.
The rating is written to a file rating.txt

**Smart Calculator**

A calculator for the expressions. Commands: /help, /exit. Supports: +-*^()=/. 

**Text Based Browser**

A text-based browser that can show the text from the requested URLs, parsed 
for the particular HTML tags; colour the links in blue; return back to the 
previous tabs; save the tabs in a directory and show the cached tabs. The 
commands are: "back", "exit", an Internet address with or without "https://".

**Tic-Tac-Toe**

Tic-tac-toe is a game played by two players on a 3x3 field where the duel takes place.
 One of the players plays as 'X', and the other player is 'O'. 'X' plays first, 
 then the 'O' side plays, and so on. The first player that writes 3 'X' or 3 'O' 
 in a straight line (including diagonals) wins.

**To-Do List**

A To-Do list that supports: 
adding and deleting tasks with deadlines, 
listing today's tasks, week's tasks, missed tasks and all tasks.
Tasks are stored in SQLite database and SQLAlchemy is used.


