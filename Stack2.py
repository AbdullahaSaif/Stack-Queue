class stack:
    def __init__(self):  # Creating Stack
        self.limit = int(input("Enter the limit of Stack: "))
        print(f"Limit of Stack: {self.limit}")
        self.stack = []
        print(f"Values of Stack: {self.stack}")
    def push(self): # Adding Values in Stack
        if len(self.stack) == self.limit:
            print(f"Stack is filled.")
        else:
            print(f"Stack have {len(self.stack)} values.")
            for i in range(self.limit - len(self.stack)):
                user_input = int(input("Enter Value for stack: "))
                self.stack.append(user_input)
                print(f"Updated Stack: {self.stack}")
    def remove(self): # Remove Values from Stack 
        if not self.stack:
            print(f"\nStack is empety")
        else:
            print(f"Value Removed: {self.stack.pop()}")
            print(f"Updated Stack: {self.stack}")
    def display(self): # Display Stack
        if not self.stack:
            print(f"\nStack is empety")
        else:
            print(f"\nStack Values\n{self.stack}")
    def sorting(self): # Sorting Stack
        if len(self.stack) == 0:
            print (f"Stack is Empety.")
        else:
            choice = int(input("1: Assacding\n2: Desacding"))
            if choice ==1:
                self.stack.sort()
                print(f"Sorted Stack in assacding order: {self.stack}")
            elif choice == 2:
                self.stack.sort(reverse=True)
                print(f"Sorted Stack in desacding order: {self.stack}")
            else:
                print(f"Enter valid option.")
    def peak(self): # Peak Value
        if len(self.stack) == 0:
            print(f"Stack is Empety.")
        print(f"Peak Value is {self.stack[-1]}")
    def remove_val(self):
        user_input = input(f"Enter the value for remove: ")
        if user_input in self.stack:
            self.stack.remove(user_input)
            print(f"Value is removed.")
        else:
         print(f"Value is not in stack.")
    def replace_val(self):
        user_input = input(f"Enter the value for replace: ")
        user_input2 = input(f"Enter the value for replace with: ")
        if user_input in self.stack:
            self.stack[self.stack.index(user_input)] = user_input2
            print(f"Value is replaced.")
        else:
            print(f"Value is not in stack.")
def main():
    while True:
        print(f"Enter the:\n")
        print(f"1: Creat Stack")
        print(f"2: Add Values")
        print(f"3: Remove Values")
        print(f"4: Display Values")
        print(f"5: Sort Values")
        print(f"6: Peak Values")
        print(f"7: Remove Value")
        print(f"8: Replace Value")
        print(f"0: Exit")
        choice = int(input("Enter the Function choice: "))
        if choice == 1:
            obj1 = stack()
        elif choice == 2:
            obj1.push()
        elif choice == 3:
            obj1.remove()
        elif choice  == 4:
            obj1.display()
        elif choice == 5:
            obj1.sorting()
        elif choice == 6:
            obj1.peak()
        elif choice == 7:
            obj1.remove_val()
        elif choice == 8:
            obj1.replace_val()
        elif choice == 0:
            print(f"Exiting!")
            break
        else:
            print(f"Enter Valid option.")
main()