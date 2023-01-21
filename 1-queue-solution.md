```
def main():
    # Initialize queue
    carQueue = []
    done = False

    # Get input from user, choose action
    while not done:
        choice = int(input("What would you like to do?\n1) Add car to queue\n2) Remove car\n3) Quit\n"))
        if choice == 1:
            addCar(carQueue)
        if choice == 2:
            removeCar(carQueue)
        if choice == 3:
            print("\nQuitting...\n")
            done = True

def addCar(queue):
    # Get name of new car, append to queue
    newCar = input("\nWhat is the name of the new car?\n")
    queue.append(newCar)
    print(f"{newCar} car added to queue!\n")

def removeCar(queue):
    # Check if queue is empty
    if len(queue) == 0:
        print("\nNo cars in queue!\n")
    # Remove next car from queue
    else:
        nextCar = queue.pop(0)
        print(f"\n{nextCar}'s car removed!\n")

main()
```