# Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not present, a message without exiting the program must be printed prompting the same.

import time
from typing import Union


class CheckExistFiles:
    """Class to check if files exist and display their contents."""

    def __init__(self, username: str):
        """
        Constructor to initialize the class with the user's name.
        :param username: The name of the user
        """
        self._username = username  # store the username for greetings

    def run(self):
        """Main workflow of the program."""
        self.welcome_msg()  # greet the user
        num_of_files = self.ask_no_of_files()  # ask how many files to check
        file_list = self.ask_file_names(num_of_files)  # ask for filenames
        self.find_file_content(file_list)  # check each file

    def welcome_msg(self):
        """Display a welcome message to the user."""
        print(f"Hey {self._username}, now you can search for files.")

    def ask_no_of_files(self) -> int:
        """
        Ask the user how many files they want to check.
        Keeps asking until a valid positive integer is entered.
        :return: number of files (int)
        """
        while True:
            try:
                file_no = int(input("How many files do you want to find? "))
                if file_no > 0:
                    return file_no  # valid input
                else:
                    print("⚠️ Please enter a positive number.")
            except ValueError:
                print("⚠️ Invalid input. Please enter a number.")

    def ask_file_names(self, count: int) -> list[str]:
        """
        Ask the user to enter filenames one by one.
        :param count: number of files
        :return: list of filenames
        """
        print(f"{self._username}, now enter all the file names one by one.")
        file_list = []
        for i in range(1, count + 1):
            filename = input(f"Enter the {i}. file name: ").strip()
            file_list.append(filename)
        return file_list

    def find_file_content(self, files: list[str]):
        """
        Try to open each file and display its content.
        If a file does not exist, show an error message without stopping the program.
        :param files: list of filenames
        """
        print(f"{self._username}, we are finding the files...")
        time.sleep(1)  # simulate processing time

        for filename in files:
            try:
                # Open the file safely using 'with'
                with open(filename, "r") as f:
                    content = f.read()

                # If successful
                print(f"\n✅ Successfully found '{filename}'.")
                print("File content:\n", content)

            except FileNotFoundError:
                # Specific error if file is missing
                print(f"\n❌ Error: The file '{filename}' does not exist.")

            except Exception as e:
                # Catch any other unexpected error
                print(f"\n⚠️ Unexpected error with '{filename}': {e}")


def main():
    """Main function: Entry point of the program."""
    time.sleep(1)  # just for a smooth effect
    username: Union[str, int] = input("Hey! First enter your name: ").strip()
    app = CheckExistFiles(username)  # create object
    app.run()  # start the workflow


# ✅ Run only if file is executed directly
if __name__ == "__main__":
    main()
