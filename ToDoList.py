# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 20:41:55 2020

A To-Do list that supports: 
adding and deleting tasks with deadlines, 
listing today's tasks, week's tasks, missed tasks and all tasks. 
Tasks are stored in SQLite database and SQLAlchemy is used.

@author: Giliazova
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker

# create a database and a table in it 
engine = create_engine('sqlite:///todo.db?check_same_thread=False')

Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.string_field

Base.metadata.create_all(engine)

# access database
Session = sessionmaker(bind=engine)
session = Session()

# functions in an alhabetical order
def add_task():
    new_task = input("Enter task\n")
    new_deadline = input("Enter deadline\n")
    if new_deadline == "today":
        new_deadline = datetime.today().strftime('%Y-%m-%d')
    elif new_deadline == "tomorrow":
        new_deadline = datetime.today() + timedelta(days=1)
        new_deadline = new_deadline.strftime('%Y-%m-%d') 
    new_deadline = datetime.strptime(new_deadline, '%Y-%m-%d')  # parse date
    new_row = Table(task=new_task, deadline=new_deadline)
    session.add(new_row)
    session.commit()
    print("The task has been added!\n")
    
def delete_task():    
    rows = print_all_tasks_sort_by_deadline(delete=True)
    number = int(input()) - 1
    session.delete(rows[number])
    session.commit()
    print("The task has been deleted!\n")
    
def print_all_tasks_sort_by_deadline(delete=False):
    if delete:
        print("Choose the number of the task you want to delete:")
    else:    
        print("All tasks:")
    rows = session.query(Table).order_by(Table.deadline).all()
    print_tasks(rows) 
    return rows

def print_day_tasks(day):
    rows = session.query(Table).filter(Table.deadline == day.date()).all()
    if not rows:
        print("Nothing to do!\n")
    else:    
        for id, row in enumerate(rows):
            print(str(id + 1) + ". " + row.task)
        print() 
        
def print_missed_tasks():
    print("Missed tasks:")
    rows = session.query(Table).filter(Table.deadline < datetime.today().date()).\
        order_by(Table.deadline).all()
    print_tasks(rows, missed=True)         

def print_tasks(rows, missed=False):
    if not rows:
        if missed:
            print("Nothing is missed!\n")
        else:
            print("Nothing to do!\n")
    else:  
        for id, row in enumerate(rows):
            deadline = row.deadline
            # e. g.: 1. Prepare presentation. 25 Sep
            print(str(id + 1) + ". " + row.task + ". " + str(deadline.day) + " " + 
               deadline.strftime('%b')) 
        print()     

def print_today_tasks():
    today = datetime.today()
    # e. g.: Today 25 Sep:
    print("Today " + str(today.day) + " " + today.strftime('%b') + ":")
    print_day_tasks(today) 
        
def print_week_tasks():
    today = datetime.today()
    week = [today + timedelta(days=i) for i in range(0, 7)]
    for day in week:
        # e. g.: Friday 25 Sep:
        print(day.strftime('%A') + " " + str(day.day) + " " + 
              day.strftime('%b') + ":")
        print_day_tasks(day)
        
# main menu
while True:
    
    print("1) Today's tasks")
    print("2) Week's tasks")
    print("3) All tasks")
    print("4) Missed tasks")
    print("5) Add task")
    print("6) Delete task")
    print("0) Exit")
    
    user_input = input()
    
    if user_input == "1":
        print_today_tasks()
    elif user_input == "2":
        print_week_tasks()
    elif user_input == "3":
        print_all_tasks_sort_by_deadline()
    elif user_input == "4": 
        print_missed_tasks()
    elif user_input == "5": 
        add_task()
    elif user_input == "6":
        delete_task()
    elif user_input == "0":
        break
