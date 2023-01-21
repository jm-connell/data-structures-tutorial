# Queue
## Introduction
Picture yourself in line at the grocery store. You're patiently waiting your turn to pay for your items, then somebody appears out of nowhere and cuts you in line! You've now experienced firsthand the importance of **queues**.<br>
**Queues** are a list of items waiting to perform an action or have something performed to them, whether it be making a calculation, a network request, or something else. **Queues** use the First In First Out method, often referred to as FIFO for short.<br>
![Diagram of a Queue](https://media.geeksforgeeks.org/wp-content/uploads/20220816162225/Queue.png)
*Credit to GeeksforGeeks.org*

## Performance
In Python, **queues** are oftentimes no more than a simple list variable. This means that appending to the end of the list is an O(1) operation, and removing the first (oldest) element is an O(n) operation. This is because the element at the index of [0] being removed causes a shift by one for every other element in the **queue**.<br>
The performance of the **queue** can be improved by the use of the double ended **queue**, or **deque** class in Python.

## Uses
A queue is useful when a program needs to fulfill requests in the order that the requests are received. For example, if a calculation needs to be performed on each item in a list, a queue will take the first (oldest) item and work through the list, even if more items are appended to the end. This way, every calculation will be performed as it reaches the front of the queue fairly and in order.<br>
The grocery store line is a perfect example of a real-life use for a queue. We use queues constantly, even if we don't realize it. Everytime we wait on hold on the phone, sit at a red light, or wait for our turn at the drinking fountain we are part of a queue.<br>
Queues are just as useful in the programming world. Imagine if you're trying to download an app to your phone, but every time you start downloading it, someone else downloading something takes priority over you and you have to wait longer. That's obviously unfair, and your download would never finish.

## Python
In Python, queues are written using the **list** variable type. The programmer uses built-in functions to remove elements from the front and append to the back, thus treating the list as a queue. A Python list is a dynamic array, which means the performance of removing items from the front isn't ideal. To address this, you can use the Python built-in **deque** class, which allows for improved performance.

## Example: Restaurant Queue
In this example, we'll write a simple program for an employee at a restaurant to track newly arrived guests and seat them in order of arrival. The employee can choose to either 1) Add new party, or 2) Seat next party.<br>
When a new party is added, the employee inputs the name for the party, and they are appended to the end of the queue. When the employee selects the option to seat the next party, the program will display the name of the party to be seated, then adjust the queue accordingly.
```
def main():
    # Initialize queue
    partyQueue = []
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
        nextParty = queue.pop(0)
        print(f"\nPlease seat the {nextParty} party\n")

main()
```
It's important to notice that the key operations being used to modify the queue in this example are `queue.append()` and `queue.pop(0)`. Using these, we are able to append new parties to the end of the queue, and remove from the front of the queue, respectively.

## Practice Problem: Car Wash
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

Check your program with the solution [here](1-queue-solution.md)