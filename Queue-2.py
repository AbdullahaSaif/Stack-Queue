class Quee():
    def __init__(self):
        self.quee = []
        self.limit = int(input(f"Enter the limit of Quee: "))
    def push(self):  # Enter the value in quee
        if len(self.quee) == self.limit:
            print(f"Quee is fuiled.")
        for i in range(self.limit    - len(self.quee)):
            user_input = input(f"Enter the value for quee: ")
            self.quee.append(user_input)
            i += 1
        print(f"Updatet quee: {self.quee}")
    def pop(self):  # Remove the first value from quee
        if len(self.quee) != 0:  # if not self.quee:
            print(f"First value is {self.quee[0]}")
            self.quee.pop(0)
        else:
            print(f"Quee is Empety.")
    def display(self):  # Display the size of quee
        return f"Quee: {self.quee}"
    def remove_val(self):  # Remove the value from quee
        user_input = input(f"Enter the value for remove: ")
        if user_input in self.quee:
            self.quee.remove(user_input)
            print(f"Value is removed.")
        else:
            print(f"Value is not in quee.")
    def replace_val(self):   # Replace the value from quee
        user_input = input(f"Enter the value for replace: ")
        user_input2 = input(f"Enter the value for replace with: ")
        if user_input in self.quee:
            self.quee[self.quee.index(user_input)] = user_input2
            print(f"Value is replaced.")
        else:
            print(f"Value is not in quee.")
def main():
    obj1 = Quee()
    while True:
        try:
            print(f"Cruent size of quee: {obj1.display()}")
            print(f"Enter the:\n")
            print(f"1: Add Value\n2: Remove Value\n3: Display Quee\n4: Size of Quee\n5: Replace Value\n6: Remove Value\n0: Exit")
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
                obj1.replace_val()
            elif user_input == 6:
                obj1.remove_val()
            elif user_input == 0:
                break
            else:
                print(f"Enter valid option.")
        except ValueError:
            print(f"Enter valid option.")
main()