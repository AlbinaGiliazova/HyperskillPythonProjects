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


