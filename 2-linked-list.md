# Linked List
## Introduction
A train is a series of connected cars, each car containing different things. A train can be just a couple cars long, or dozens of cars. A **linked list** is like a train. There are a varying number of **nodes**, each with their own contents. Each node connects to the next, just like a train car.<br>
If you're traveling on a train and you're in the second car and you want to get to the fifth, you can't go directly from the second car to the fifth. You have to go from the second to the third, to the fourth, then to the fifth. This is how a linked list works. Each node tells you where the next node is.
![Diagram of a Singly Linked List](https://media.geeksforgeeks.org/wp-content/uploads/20220816144425/LLdrawio.png)
*Singly Linked List - Credit to GeeksforGeeks.org*<br><br>
The above image is an example of what's called a **singly linked list**. A singly linked list can only be traversed in one direction, like a one-way street. Each node tells you where the next one is, but each node can't tell you where the previous node is. If you need links or **pointers** to both the previous and next node, you'll need to use a **doubly linked list**. Each node in a doubly linked list contains pointers to the previous and next nodes.
![Diagram of a Doubly Linked List](https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2014/03/DLL1.png)
*Doubly Linked List - Credit to GeeksforGeeks.org*<br><br>

## Performance
While linked lists often seem complicated at first glance, there's a reason they exist. Linked lists can perform operations very quickly. Inserting and removing nodes from the front or the end is an O(1) operation, as is checking the size of the linked list. Inserting and removing a node from the middle is an O(n) operation, as the program has to loop through the list to find the node to be removed.

## Uses
One of the most common uses for a linked list is a queue. When used as a queue, a linked list works in O(1) time almost exclusively as the program only interacts with the first and last nodes at any given time. Beginner programmers in Python often use the built in **list** function, which is a dynamic array. This is an easy solution, however there are performance costs. When you need to remove the first item in a queue, it's an O(n) operation.<br>
When using a queue, you are constantly removing from the front of the queue. A better way to implement a queue would be using a linked list, which can be easily achieved in Python by using the **deque** class. 

## Python 
The Python **deque** class has several built in functions that make is easy to create and manipulate a linked list. Deque uses `my_deque.append(value)` and `my_deque.appendleft(value)` to append to the end and beginning of the linked list, respectively. To remove from the end or beginning you use `my_deque.pop()` and `my_deque.popleft()`. All of these functions run in O(1) time.<br>
If you need to manipulate the middle of the linked list, you use `my_deque.insert(i, value)` and `del my_deque[i]`. With these functions, it's important to keep in mind that these are O(n) operations.

## Example: Restaurant Queue
In this example, we are going to rewrite the program from the [queue page](1-queue.md), but using a linked list to improve performance. To review the problem specifications, we are writing a program to track new guests arriving at a restaurant. The program must be able to 1) Add new guest parties to end of queue, and 2) Remove party from front of queue when it's their turn to be seated.

```
from collections import deque

def main():
    # Initialize queue
    partyQueue = deque([])
    done = False

    # Get input from user, choose action
    while not done:
        choice = int(input("What would you like to do?\n1) Add party to queue\n2) Seat party (remove from queue)\n3) Quit\n"))
        if choice == 1:
            addParty(partyQueue)
        if choice == 2:
            seatParty(partyQueue)
        if choice == 3:
            print("Quitting...\n")
            done = True

def addParty(queue):
    # Get name of new party, append to queue
    newParty = input("\nWhat is the name of the new party?\n")
    queue.append(newParty)
    print(f"{newParty} party added to queue!\n")

def seatParty(queue):
    # Check if queue is empty
    if len(queue) == 0:
        print("\nNo parties in queue!\n")
    # Get next party from queue
    else:
        nextParty = queue.popleft()
        print(f"\nPlease seat the {nextParty} party\n")

main()
```
As you can see if you compare this program to the original, the differences are subtle. Firstly, we have to put `from collections import deque` in order to use the deque function. Next, we have to change how we initialize our queue. Instead of creating a normal Python list, we use `partyQueue = deque([])`. To append to the queue, we don't need to change anything, as **deque** uses the `append()` method just like a standard list. To remove from the front of the queue however, we use `queue.popleft()`. This is where the real improvement is, as we went from O(n) efficiency to O(1). 

## Practice Problem: Car Wash
Just as we rewrote the restaurant queue program to use **deque**, we'll do the same with the Car Wash practice problem. To review, here are the program specifications:<br>
Write a program for an employee working at a car wash. They write down a name from each car in line in order. This allows the rest of the employees to track the order of the cars. The program must include two basic functionalities: 
- Add new car to queue
- Remove car from queue as they finish their carwash

Test your program using the following scenario:
1. Add car - "Steven"
2. Add car - "Lauren"
3. Remove car (Should be "Steven")
4. Add car - "Taylor"
5. Add car - "Brian"
6. Remove car (Should be "Lauren")
7. Remove car (Should be "Taylor")
8. Remove car (Should be "Brian")

Check your program with the solution [here](2-linked-list-solution.md)
