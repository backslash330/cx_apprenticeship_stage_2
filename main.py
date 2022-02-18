# Notes
# Program Requires installation of Selenium Chrome Webdriver to run
# Program Requires Windows 10 Notifications to run


# Imports
import PySimpleGUI as sg
import multiprocessing as mp

import sys

class Bill:
        # create an order that uses a dictionary to store the items
    # the key is the item name and the value is the price
    # the order is a list of items belonging to a given customer

    def __init__(self, customer):
        self.customer = customer
        self.order = {}
    def add_item(self, item, price):
        self.order[item] = price
    def get_total(self):
        total = 0
        for item in self.order:
            total += self.order[item]
        return total
    def get_items(self):
        return self.order
    def get_customer(self):
        return self.customer
    def __str__(self):
        return f"{self.customer}'s order: {self.order}"
    def remove_item(self, item):
        del self.order[item]
    

def main():
    # Create the Welcome Screen and get the user's name
    welcomeScreenVar = welcomeScreen()
    while True:
        event, values = welcomeScreenVar.read()
        if event in (None, 'Exit'):
            break
        if event == 'Request a Table':
            # if not values[0]:
            #     sg.Popup('Please enter your name')
            # else:
            #     name = values[0]
            #     welcomeScreenVar.close()
            #     break
            name = "Nick"
            welcomeScreenVar.close()
            break
        if event == sg.WIN_CLOSED:
            name = "Nick"
            welcomeScreenVar.close()
            quit()


    # Create bill object
    bill = Bill(name)

    # Create the main window
    mainScreenVar = mainScreen(name,bill)
    while True:
        # main loop for the main screen
        event, values = mainScreenVar.read()
        if event == 'leave':
            mainScreenVar.close()
            break
        if event == 'Yes':
            sg.Popup('You have been given a free refill!')
        if event == 'No':
            sg.Popup('Not a problem! I\'ll come back later.')


        if event == sg.WIN_CLOSED:
            mainScreenVar.close()
            quit()  



def welcomeScreen():
    layout = [
        [sg.Text('Welcome to Goan')],
        [sg.Text('Please enter your name:')],
        [sg.InputText()],
        [sg.Button('Request a Table')]
    ]

    return sg.Window('Goan Places - Welcome to the Restaurant', layout)


def mainScreen(name,bill):
    layout = [
        [sg.Text('Hello ' + name + '!')],
        [sg.Text('Would you like a free refill?')],
        [sg.Button('Yes')], [sg.Button('No')],
        [[sg.Button('Drinks Menu')], [sg.Button('Appetizer Menu')], [sg.Button('Entree Menu')], [sg.Button('Dessert Menu')],],
        [sg.Text('Here is your current order:')],
        # give a list of all ordered items 
        [sg.Listbox(bill.get_items(), size=(30, 10))],

        [sg.Button('Leave')]
    ]

    return sg.Window('Goan Places - Main Menu', layout)

# def drinksScreen():
#     layout = [
#         [sg.Text('What drinks would you like?')],
#         [sg.Text('Water: Free!')], [sg.Button('Order Water')],
#         [sg.Text('Coke: $1.00')], [sg.Button('Order Coke')],
#         [sg.Text('Sprite: $1.00')], [sg.Button('Order Sprite')],
#         [sg.Text('Fanta: $1.00')], [sg.Button('Order Fanta')],
#         [sg.Text('Coffee: $2.00')], [sg.Button('Order Coffee')],
#         [sg.Text('Tea: $2.00')], [sg.Button('Order Tea')],
#         [sg.Text('Mango Lassi: $3.00')], [sg.Button('Order Mango Lassi')],
#         [sg.InputText()],
#         [sg.Button('Return to Main Menu')]
#     ]

#     return sg.Window('Goan Places - Drinks', layout)

if __name__ == '__main__':
    main()