# Library Challenge
This is a simple REST application that mimicks some activities of an actual library.

## Overview
- The goal is to complete as many user stories as possible.
- Some user stories are more challenging than others

## Pre-Requisites
- Basic python understanding
- Understanding of RESTful Services
- Basic understanding of SQL and SQL Lite

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

