# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 12:36:53 2020

@author: VIRUS
"""

# a program implementing queue using list
queue = []

def Enqueue():
        element = int(input("Enter an element: "))
        queue.append(element)
        print(element," added to the queue")
        
def Dequeue():
    if not queue:
        print("queue is empty!")
    else:
        element = queue.pop(0)
        print(element," Removed from the queue")
        
def Display():
    print("*****************************")
    for x in queue:
        print("Elements in the queue are: ",x)
    
while True:
    print("Enter an operation 1.Enqueue, 2.Dequeue, 3.Display")
    operation = int(input())
    
    if operation == 1:
        Enqueue()
    elif operation == 2:
        Dequeue()
    elif operation == 3:
        Display()
    elif operation == 4:
        break
    else:
        print("Enter a proper value!")