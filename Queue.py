# quee pverview
# use an opbject
# Make example use of Quee

class Quee:
    def __init__(self):
        self.quee = []
    def push(self):
        user_input = input("Enter Value: ")
        self.quee.append(user_input)
        print(f"Updated Quee: {self.quee}")
    def pop(self):
        if not self.quee:
            print("Quee is Empety.")
        else:
            print(f"Value Removed: {self.quee.pop(0)}")
            print(f"Updated Quee: {self.quee}")
    def display(self):
        if not self.quee:
            print("Quee is Empety.")
        else:
            print(f"Quee Values: {self.quee}")
    def size(self):
        print(f"Size of Quee: {len(self.quee)}")
    
def main():
    obj1 = Quee()
    while True:
        try:
            print(f"Enter the:\n")
            print(f"1: Add Value\n2: Remove Value\n3: Display Quee\n4: Size of Quee\n5: Exit")
            user_input = int(input("Enter Option: "))
            if user_input == 1:
                obj1.push()
            elif user_input == 2:
                obj1.pop()
            elif user_input == 3:
                obj1.display()
            elif user_input == 4:
                obj1.size()
            elif user_input == 5:
                break
            else:
                print(f"Enter valid option.")
        except ValueError:
            print(f"Enter valid option.")
main()