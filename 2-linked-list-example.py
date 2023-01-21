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