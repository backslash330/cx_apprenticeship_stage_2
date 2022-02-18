# Notes
# Program Requires installation of Selenium Chrome Webdriver to run
# Program Requires Windows 10 Notifications to run


# Imports
from tkinter import Listbox
from turtle import update
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
        # use the item name as the key
        # use the price as the first value in an array
        # use the quantity as the second value in an array
        quantity = 1
        if item in self.order:
            self.order[item][0] += price
            self.order[item][1] += quantity
        else:
            self.order[item] = [price, quantity]
    def get_total(self):
        total = 0
        for item in self.order:
            total += self.order[item]
        return total
    def get_items(self):
        # returns a list of items in the order and their
        #  respective prices as a list of tuples
        formattedString = ""
        for item in self.order:
            # format should be 
            # X items ordered at $Y each for $Z total
            if self.order[item][1] > 1:
                formattedString += str(self.order[item][1]) + " " + item + "s ordered at $" + str(self.order[item][0]) + " for a total of $" + str(self.order[item][0] * self.order[item][1]) + "\n"
            else:
                formattedString += str(self.order[item][1]) + " " + item + " ordered at $" + str(self.order[item][0]) + " for a total of $" + str(self.order[item][0] * self.order[item][1]) + "\n"
        return formattedString

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
        # when an item button is pressed
        # add the item to the order
        # update the order listbox




    # Create bill object
    bill = Bill(name)

    sg.popup(bill.get_items())
    # Create the main window
    mainScreenVar = mainScreen(name,bill).Finalize()
    mainScreenVar.Maximize()
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
        if event == 'Order Water':
            bill.add_item('Water', 0.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order Coke':
            bill.add_item('Coke', 1.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order Coffee':
            bill.add_item('Coffee', 2.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order Tea':
            bill.add_item('Tea', 2.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order Mango Lassi':
            bill.add_item('Mango Lassi', 3.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order Pakoras':
            bill.add_item('Pakoras', 3.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order with Mint Chutney':
            bill.add_item('Pakoras with Mint Chutney', 3.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order with Tomato Chutney':
            bill.add_item('Pakoras with Tomato Chutney', 3.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order Samosas':
            bill.add_item('Samosas', 3.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order with Masala Sauce':
            bill.add_item('Samosas with Masala Sauce', 3.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order with Coriander Chutney':
            bill.add_item('Samosas with Coriander Chutney', 3.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order Masala Papad':
            bill.add_item('Masala Papad', 5.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order with Raita':
            bill.add_item('Masala Papad with Raita', 5.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order with Mango Chutney':
            bill.add_item('Masala Papad with Mango Chutney', 5.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order Chicken Curry':
            bill.add_item('Chicken Curry', 5.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order with Rice':
            bill.add_item('Chicken Curry with Rice', 5.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order with Yogurt':
            bill.add_item('Chicken Curry with Yogurt', 5.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order Beef Curry':
            bill.add_item('Beef Curry', 5.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order with Pakoras':
            bill.add_item('Beef Curry with Pakoras', 5.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order with Aloo Gobi':
            bill.add_item('Beef Curry with Aloo Gobi', 5.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order Paneer':
            bill.add_item('Paneer', 5.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order with Vegetables':
            bill.add_item('Paneer with Vegetables', 5.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order with Meat':
            bill.add_item('Paneer with Meat', 5.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue


            



def welcomeScreen():
    layout = [
        [sg.Text('Welcome to Goan')],
        [sg.Text('Please enter your name:')],
        [sg.InputText()],
        [sg.Button('Request a Table')]
    ]

    return sg.Window('Goan Places - Welcome to the Restaurant', layout)


def mainScreen(name,bill):

    drinksColumn = [
    [sg.Text('Drinks', background_color='red')],
    [sg.Text('Water: Free!')], [sg.Button('Order Water')],
    [sg.Text('Coke: $1.00')], [sg.Button('Order Coke')],
    [sg.Text('Coffee: $2.00')], [sg.Button('Order Coffee')],
    [sg.Text('Tea: $2.00')], [sg.Button('Order Tea')],
    [sg.Text('Mango Lassi: $3.00')], [sg.Button('Order Mango Lassi')]
    ]

    appetizersColumn = [
    [sg.Text('Appetizers', background_color='blue')],
    [sg.Text('Pakoras: $5.00 (Add Mint Chutney for $2.50 or Add Tomato Chutney $2.50)')], [sg.Button('Order Pakoras')], [sg.Button('Order with Mint Chutney')], [sg.Button('Order with Tomato Chutney')],
    [sg.Text('Samosas: $5.00 (Add Masala Sauce for $1.50 or Add Coriander Chutney for $2.00)')], [sg.Button('Order Samosas')], [sg.Button('Order with Masala Sauce')], [sg.Button('Order with Coriander Chutney')],
    [sg.Text('Masala Papad: $5.00 (Add Raita for $3.00 or Mango Chutney for $1.50)')], [sg.Button('Order Masala Papad')], [sg.Button('Order with Raita')], [sg.Button('Order with Mango Chutney')],
    ]

    entreeColumn = [
        [sg.Text('Entrees', background_color='green')],
        [sg.Text('Chicken Curry: $10.00 (Add Rice for $3.00 or Yogurt for $2.00)')], [sg.Button('Order Chicken Curry')], [sg.Button('Order with Rice')], [sg.Button('Order with Yogurt')],
        [sg.Text('Beef Curry: $10.00 (Add Pakoras for $2.00 or Aloo Gobi for $4.00)')], [sg.Button('Order Beef Curry')], [sg.Button('Order with Pakoras')], [sg.Button('Order with Aloo Gobi')],
        [sg.Text('Paneer: $10.00 (Add Vegetables for $3.00 or Meat for $5.00)')], [sg.Button('Order Paneer')], [sg.Button('Order with Vegetables')], [sg.Button('Order with Meat')],
    ]

    dessertsColumn = [
        [sg.Text('Desserts', background_color='yellow')],
        [sg.Text('Ice Cream: $3.00')], [sg.Button('Order Ice Cream')],
        [sg.Text('Cake: $3.00')], [sg.Button('Order Cake')],
        [sg.Text('Pie: $3.00')], [sg.Button('Order Pie')],
        [sg.Text('Cookie: $3.00')], [sg.Button('Order Cookie')],
        [sg.Text('Brownie: $3.00')], [sg.Button('Order Brownie')],
    ]

    layout = [
        [sg.Text('Hello ' + name + '!')],
        [sg.Text('Would you like a free refill?')],
        [sg.Button('Yes'), sg.Button('No')],
        [sg.Column(drinksColumn), sg.Column(appetizersColumn), sg.Column(entreeColumn), sg.Column(dessertsColumn)],
        [sg.Text('Here is your current order:')],
        # give a list of all ordered items and their prices
        [sg.Text(bill.get_items(), key= 'order')],
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