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
        self.tip = 1

    def add_item(self, item, price):
        # use the item name as the key
        # use the price as the first value in an array
        # use the quantity as the second value in an array
        quantity = 1
        if item in self.order:
            self.order[item][1] += quantity
        else:
            self.order[item] = [price, quantity]
    def get_items(self):
        # returns a list of items in the order and their
        #  respective prices as a list of tuples
        formattedString = ""
        for item in self.order:
            # format should be 
            itemCost = format(self.order[item][0], '.2f')
            totalCost = format(self.order[item][0] * self.order[item][1], '.2f')
            # X items ordered at $Y each for $Z total
            if self.order[item][1] > 1:
                # if the key ends in an s, add an 'es' to the end
                # convert item to two digits 

                if item[-1] == 's':
                    formattedString += str(self.order[item][1]) + " " + item + " ordered at $" + str(itemCost) + " for a total of $" + str(totalCost) + "\n"
                else:
                    formattedString += str(self.order[item][1]) + " " + item + "s ordered at $" + str(itemCost) + " for a total of $" + str(totalCost) + "\n"
            else:
                formattedString += str(self.order[item][1]) + " " + item + " ordered at $" + str(itemCost) + " for a total of $" + str(totalCost) + "\n"
        return formattedString

    def get_customer(self):
        return self.customer

    def __str__(self):
        return f"{self.customer}'s order: {self.order}"

    def remove_item(self, item):
        del self.order[item]

    def add_tip(self, tip):
        self.tip = tip 

    def get_total(self):
        # returns the total cost of the order
        total = 0
        for item in self.order:
            total += self.order[item][0] * self.order[item][1]
        total = total * self.tip
        total = total * 1.05
        # round to the nearest cent
        return format(round(total, 2), '.2f')
    
    def get_tip(self):
        return self.tip

def main():
    # Create the Welcome Screen and get the user's name
    welcomeScreenVar = welcomeScreen()
    while True:
        event, values = welcomeScreenVar.read()
        if event in (None, 'Exit'):
            break
        if event == 'Request a Table':
            if not values[0]:
                sg.Popup('Please enter your name')
            else:
                name = values[0]
                welcomeScreenVar.close()
                break

        if event == sg.WIN_CLOSED:
            name = "Nick"
            welcomeScreenVar.close()
            quit()

    # Create bill object
    bill = Bill(name)

    # Create the main window
    mainScreenVar = mainScreen(name,bill).Finalize()
    mainScreenVar.Maximize()
    while True:
        # main loop for the main screen
        event, values = mainScreenVar.read()
        if event == 'Ask for the Bill':
            # ask if they would like to tip the waiter
            # if yes, ask how much
            # if no, just show the bill
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
            bill.add_item('Pakoras', 5.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order with Mint Chutney':
            bill.add_item('Pakoras with Mint Chutney', 7.50)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order with Tomato Chutney':
            bill.add_item('Pakoras with Tomato Chutney', 7.50)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order Samosas':
            bill.add_item('Samosas', 5.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order with Masala Sauce':
            bill.add_item('Samosas with Masala Sauce', 6.50)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order with Coriander Chutney':
            bill.add_item('Samosas with Coriander Chutney', 7.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order Masala Papad':
            bill.add_item('Masala Papad', 5.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order with Raita':
            bill.add_item('Masala Papad with Raita', 8.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order with Mango Chutney':
            bill.add_item('Masala Papad with Mango Chutney', 6.50)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order Chicken Curry':
            bill.add_item('Chicken Curry', 10.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order with Rice':
            bill.add_item('Chicken Curry with Rice', 13.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order with Yogurt':
            bill.add_item('Chicken Curry with Yogurt', 12.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order Beef Curry':
            bill.add_item('Beef Curry', 10.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order with Pakoras':
            bill.add_item('Beef Curry with Pakoras', 12.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order with Aloo Gobi':
            bill.add_item('Beef Curry with Aloo Gobi', 14.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order Paneer':
            bill.add_item('Paneer', 10.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order with Vegetables':
            bill.add_item('Paneer with Vegetables', 13.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order with Meat':
            bill.add_item('Paneer with Meat', 15.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order Gulab Jamun':
            bill.add_item('Gulab Jamun', 8.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order Rice Pudding':
            bill.add_item('Rice Pudding', 4.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order Jalabi':
            bill.add_item('Jalabi', 6.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order Kheer':
            bill.add_item('Kheer', 4.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue
        if event == 'Order Laddoo':
            bill.add_item('Laddoo', 3.00)
            mainScreenVar.FindElement('order').Update(bill.get_items())
            continue


    # Ask customer if they would like to tip the waiter
    tipScreenVar = tipScreen(name).Finalize()
    tipScreenVar.Maximize()
    while True:
        event, values = tipScreenVar.read()
        if event == 'Yes':
            # if 10% was selected, add 10% to the bill
            if values['10'] == True:
                bill.add_tip(1.10)
                tipScreenVar.close()
                break
            # if 20% was selected, add 20% to the bill
            if values['15'] == True:
                bill.add_tip(1.15)
                tipScreenVar.close()
                break
            # if 30% was selected, add 30% to the bill
            if values['20'] == True:
                bill.add_tip(1.20)
                tipScreenVar.close()
                break
            else:
                tipScreenVar.close()
                break
        if event == 'No':
            tipScreenVar.close()
            break
        if event == sg.WIN_CLOSED:
            tipScreenVar.close()
            quit()

    # show the bill
    billScreenVar = billScreen(name, bill).Finalize()
    billScreenVar.Maximize()
    while True:
        event, values = billScreenVar.read()
        if event == 'Close':
            sg.popup("Thank you for your business!", title="Thank You!")
            billScreenVar.close()
            break
        if event == sg.WIN_CLOSED:
            billScreenVar.close()
            quit()
    



def welcomeScreen():
    layout = [
        [sg.Text('Welcome to Goan Places')],
        [sg.Text('Please enter your name:')],
        [sg.InputText()],
        [sg.Button('Request a Table')]
    ]

    return sg.Window('Goan Places - Welcome to the Restaurant', layout)


def mainScreen(name,bill):
    # create columns for the main screen
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
        [sg.Text('Gulab Jamun: $8.00')], [sg.Button('Order Gulab Jamun')],
        [sg.Text('Rice Pudding: $4.00')], [sg.Button('Order Rice Pudding')],
        [sg.Text('Jalabi: $6.00')], [sg.Button('Order Jalabi')],
        [sg.Text('Kheer: $4.00')], [sg.Button('Order Kheer')],
        [sg.Text('Laddoo: $3.00')], [sg.Button('Order Laddoo')],
    ]
    # create the main screen layout with columns
    layout = [
        [sg.Text('Hello ' + name + '!')],
        [sg.Text('Would you like a free refill?')],
        [sg.Button('Yes'), sg.Button('No')],
        [sg.Column(drinksColumn), sg.Column(appetizersColumn), sg.Column(entreeColumn), sg.Column(dessertsColumn)],
        [sg.Text('Here is your current order:')],
        # give a list of all ordered items and their prices
        [sg.Text(bill.get_items(), key= 'order')],
        [sg.Button('Ask for the Bill')]
        
    ]

    return sg.Window('Goan Places - Main Menu', layout)

def tipScreen(name):
    layout = [
        [sg.Text('Hello ' + name + ' I hope you enjoyed your meal!')], 
        [sg.Text('I was wondering if you would like to add a tip to the bill?')],
        [sg.Text('What percentage would you like to tip?')],
        [sg.Radio('10%', 'tip', key='10', default=True), sg.Radio('15%', 'tip', key='15'), sg.Radio('20%', 'tip', key='20')],
        [sg.Button('Yes'), sg.Button('No')],
    ]

    return sg.Window('Goan Places - Tip Screen', layout)

def billScreen(name, bill):
    layout = [
        [sg.Text('Hello ' + name + '!')],
        [sg.Text('Here is your bill:')],
        [sg.Text(bill.get_items(), key= 'order')],
        [sg.Text('Tax: 5%')],
        [sg.Text('Tip: ' + str(bill.get_tip()))],
        [sg.Text("Grand Total: $" + bill.get_total(), key='order')],
        [sg.Button('Close')]
    ]

    return sg.Window('Goan Places - Bill Screen', layout)


if __name__ == '__main__':
    main()