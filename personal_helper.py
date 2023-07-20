from address_book.address_book import main as address_book
from notes.notes import main as notes
from sort.sort import main as sort
from prettytable import PrettyTable
from abc import ABC, abstractmethod

class UserInterface(ABC):
    @abstractmethod
    def show_message(self):
        pass
    @abstractmethod
    def show_table(self):
        pass
    @abstractmethod
    def get_user_input(self):
        pass
    
class PersonalHelper(UserInterface):
    @staticmethod
    def show_message():
        print("\nHello, this is Personal Helper")

    @staticmethod
    def show_table():
        table = PrettyTable(["Command", "instruction"])
        table.add_rows(
            [
                ["1", "Go to Address Book"],
                ["2", "Go to Notes"],
                ["3", "Go to Sorter"],
                ["4", "Exit the program"],
            ]
        )
        print("\nPersonal Helper Menu:")
        print(table)

    @staticmethod
    def get_user_input():
        PersonalHelper.show_message()  
        while True:
            PersonalHelper.show_table()
            string = input("Enter command to Personal Helper: ").lower()

            if string == "1":
                print("\n\nYou went to Address Book")
                address_book() 
                print("\n\nYou went to Personal Helper")
            elif string == "2":
                print("\n\nYou went to Notes")
                notes()
                print("\n\nYou went to Personal Helper")
            elif string == "3":
                print("\n\nYou went to Sorter")
                sort()
                print("\n\nYou went to Personal Helper")
            elif string == "4":
                print("Good bye!")
                break
            else:
                print("invalid command")

if __name__ == "__main__":
    PersonalHelper.get_user_input()