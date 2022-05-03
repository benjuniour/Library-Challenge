# Library Challenge
This is a simple REST application that mimicks some activities of an actual library.

## Overview
- The goal is to complete as many user stories as possible.
- Some user stories are more challenging than others

## Pre-Requisites
- Python installed on your computer
- Basic python understanding
- Understanding of RESTful Services
- Basic understanding of SQL and SQL Lite

## Set Up
- Fork this repo
- Create a virtual environment in the cloned directory by entering `python -m venv env`in your terminal/cmd: 
- Activate your virtual environment by entering `env\scripts\activate`.
- Next, install all dependencies via this command `pip install -r requirements.txt`
- All done
- _NOTE: Activate your virtual environment using the command above whenever you need to start development. This is required once until you close your terminal. If you're using VSCode or any IDE, it may detect the virtual environment and might automatically change your workspace. In this case, you do not need to activate it manually _

## Requirements
- Expose a REST endpoint for each of the controller methods
- Create a database table to hold the room, books, student_info and their related relationships
- Create implementation for all the service methods

## Background
- Room Types
    - Single Room - Can only be used by one person at a time
    - Double Room - A max of 2 people can occupy the space
    - 4 to a Room - A max of 4 people can occupy the space
    - 5 or more - Special permission needed

### User Stories
1. Reserving a Room
    - As a student, I should be able to book a single room. Once I have booked this room, no one should be able to book this.
    - As a student, I cannot book more than room. An attempt to do this should show an error.
    - As a student, I should not be able to book a room that is fully occupied. If it is fully booked, I should get an error message.

2. Getting Room Details
    - As a student, I should be able to see all available rooms. I shouldn't be shown rooms that are already booked
    - As a student, once I have booked a room that can hold more than 1 person, I should be able to see who else has booked the room. I shouldn't be able to see the people who have booked a room outside the one I have booked.

3. Checking out a book
    - As a student, I should be able to see all books that are available for checkout.
    - As a student, I can only check out a max of 3 books. Any more than that should be prohibited.
    - As a student, I cannot checkout a book that has already been checked out.
    - As a student, I shouldn't be able to checkout the same book more than once.
    - As a student, I cannot checkout a book for more than 3 weeks
    - As a student, I once I have checked out a book, I should be able to look up how long I have before I'm to return the book. (<1 week = show me in days, >1 week = show me in weeks and days [e.g. 2 weeks, 1 day])

