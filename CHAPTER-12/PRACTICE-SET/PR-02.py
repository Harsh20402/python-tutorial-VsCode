# Program to print the 3rd, 5th, and 7th element from a list using enumerate()

from typing import List

class ListPrinter:
    def __init__(self):
        self.items: List[str] = []

    def take_input(self):
        """Take items from user and store in list"""
        n = int(input("Enter number of items: "))
        for i in range(1, n + 1):
            item = input(f"Enter item {i}: ")
            self.items.append(item)

    def display_selected(self):
        """Display 3rd, 5th, and 7th elements using enumerate"""
        print("\nAll items in the list:")
        for index, value in enumerate(self.items, start=1):
            print(f"Item {index}: {value}")

        print("\nNow printing only 3rd, 5th and 7th elements:")
        for index, value in enumerate(self.items, start=1):
            if index in (3, 5, 7):
                print(f"✅ Item {index}: {value}")


def main():
    app = ListPrinter()
    app.take_input()
    app.display_selected()


if __name__ == "__main__":
    main()
