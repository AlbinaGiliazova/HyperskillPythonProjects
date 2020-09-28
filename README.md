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

**To-Do List**

A To-Do list that supports: 
adding and deleting tasks with deadlines, 
listing today's tasks, week's tasks, missed tasks and all tasks.
Tasks are stored in SQLite database and SQLAlchemy is used.


