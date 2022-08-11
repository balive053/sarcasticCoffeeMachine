import time

class SarcasticCoffeeMachine:

    def __init__(self, cash = 550, water = 400, milk = 540, coffee = 120, disposable_cups = 9):
        '''
        Constructor with default inputs for starting stock
        '''
        self.cash = cash
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.disposable_cups = disposable_cups
        self.count = 0


    def display_state(self):
        '''
        Display state of machine
        input : None
        output : None (prints current state)
        '''
        print(
            '\n'
            f'The coffee machine has:\n'
            f'{self.water}ml of water\n'
            f'{self.milk}ml of milk\n'
            f'{self.coffee}g of coffee beans\n'
            f'{self.disposable_cups} disposable cups\n'
            f'${self.cash}'
            )
        return None
    
    def check_supplies(self, water_needed, milk_needed, coffee_needed, disposable_cups_needed=1):
        '''
        To check if there are enough supplies to create coffee requested
        input : 
            water_needed  # water requested coffee requires
            milk_needed  # milk requested coffee requires 
            coffee_needed  # coffee beans requested coffee requires 
            disposable_cups_needed  # disposable cups requested coffee requires

        output : boolean # True if enough resources are in stock, else False
        '''
        # boolean checker. Will be marked to False if ANY resources fail stock check
        check_pass = True
        # check of all stocks to see if any do not meet requirements to make coffee
        if self.water >= water_needed:
            pass
        else: 
            print('Sorry, not enough water!')
            check_pass = False
        if self.milk >= milk_needed:
            pass
        else: 
            print('Sorry, not enough milk!')
            check_pass = False
        if self.coffee >= coffee_needed:
            pass
        else: 
            print('Sorry, not enough coffee!')
            check_pass = False
        if self.disposable_cups >= disposable_cups_needed:
            pass
        else: 
            print('Sorry, not enough disposable cups!')
            check_pass = False
        # if tests pass, prepare coffee
        if check_pass == True: 
            print('Preparing to make your coffee!')
            time.sleep(0.5)
            print('Grinding coffee beans')
            time.sleep(2.5)
            print('Percolating and doing other fancy stuff!')
            time.sleep(2.5)
            print('Eating your mashmellow for you!')
            time.sleep(2.5)
            print('This is a really good mashmellow!!')
            time.sleep(2.5)
            print('You would have enjoyed it!')
            time.sleep(2.5)
            print('Your coffee is now ready!')
            time.sleep(1)
            print('Enjoy your coffee! Thank you for your purchase')
        return check_pass
        
    def deductor(self, water_needed, milk_needed, coffee_needed, disposable_cups_needed, cash_paid):
        '''
        To deduct resources from stores when coffee is made plus add cash from coffee price
        input : 
            water_needed  # water requested coffee requires
            milk_needed  # milk requested coffee requires 
            coffee_needed  # coffee beans requested coffee requires 
            disposable_cups_needed  # disposable cups requested coffee requires

        output : None - deductions are made to each resource in stock if enough off each is present 
                        based on boolean from check_supplies() 
        '''
        self.water -= water_needed
        self.milk -= milk_needed
        self.coffee -= coffee_needed
        self.disposable_cups -= disposable_cups_needed
        self.cash += cash_paid
        return None
    
    # Coffee functions for different types of coffees - latte, expresso, cappuccino    
    def latte(self):
        '''
        To make coffee type - latte
        input : None
        output : None - calls deductor() if all resources are present
        '''
        # resources required and cost of coffee
        water_needed=350
        milk_needed=75
        coffee_needed=20
        disposable_cups_needed=1
        cash_paid=7 
        
        checker = self.check_supplies(water_needed, milk_needed, coffee_needed, disposable_cups_needed)
        # if enough resources are present for coffee, pass to deductor()
        if checker:
            self.deductor(water_needed, milk_needed, coffee_needed, disposable_cups_needed, cash_paid)
        return None
    

    def espresso(self):
        '''
        To make coffee type - latte
        input : None
        output : None - calls deductor() if all resources are present
        '''
        # resources required and cost of coffee
        water_needed=250
        milk_needed=0
        coffee_needed=16
        disposable_cups_needed=1
        cash_paid=4
        
        checker = self.check_supplies(water_needed, milk_needed, coffee_needed, disposable_cups_needed)
        # if enough resources are present for coffee, pass to deductor()
        if checker:
            self.deductor(water_needed, milk_needed, coffee_needed, disposable_cups_needed, cash_paid)
        return None
        

    def cappuccino(self):
        '''
        To make coffee type - latte
        input : None
        output : None - calls deductor() if all resources are present
        '''
        # resources required and cost of coffee
        water_needed=200
        milk_needed=100
        coffee_needed=12
        disposable_cups_needed=1
        cash_paid=6 
        
        checker = self.check_supplies(water_needed, milk_needed, coffee_needed, disposable_cups_needed)
        # if enough resources are present for coffee, pass to deductor()
        if checker:
            self.deductor(water_needed, milk_needed, coffee_needed, disposable_cups_needed, cash_paid)
        return None
        

    def buy(self):
        '''
        To create menu to purchase coffee
        input : None
        output : None - calls relevant coffee to produce based on user input
        '''
        type = input('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, 4 - back to menu: \n')
        # call function for coffee based on input
        if type == '1':
            self.espresso()
        elif type == '2':
            self.latte()
        elif type =='3':
            self.cappuccino()
        elif type =='4':
            pass
        else:
            print('Error: Please make relevant selection')
            self.buy()
        print()
        return None    

    # function to fill machine
    def fill(self):
        '''
        To restock supplies when empty
        input : None
        output : None - offers to restock each supply for x amount based on user input
        '''
        water_topup = int(input('Write how many ml of water you want to add: \n'))
        self.water += water_topup

        milk_topup = int(input('Write how many ml of milk you want to add: \n'))
        self.milk += milk_topup
        
        coffee_topup = int(input('Write how many grams of coffee beans you want to add: \n'))
        self.coffee += coffee_topup
        
        cups_topup = int(input('Write how many disposable cups you want to add: \n'))
        self.disposable_cups += cups_topup
        print('Thank you! The machine has been refilled!\n')
        return None

    
    def take(self):
        '''
        To Withdraw all cash currently in the machine
        input : None
        output : None - withdraws all money (changes balance to $0)
        '''
        global cash 
        print(f'${self.cash} has been spat out on the floor aimlessly!' 
             '\nQuick, pick it up! Balance: $0\n')
        self.cash = 0
        return None


    def main_menu(self):
        '''
        Main menu screen for function to request user input for desired activity
        input : None
        output : None - launches main menu
        '''
        if self.count <= 4:
            action = input('''\nWelcome! How can the tiny man in the machine help you today? 
            \nPress key to select (input answer 1-5): 
            1) Buy Coffee
            2) Restock machine
            3) Remove cash
            4) Check stock levels
            5) Get life advice
            6) Exit \n''')
        else:
            ## Easteregg path ;)
            # create crossout affect
            text = 'Get life advice'
            result = ''
            for c in text:
                result = result + c + '\u0336'
            print(
            "\nWelcome to the COFFEE, NOT ADVICE, machine!\n"
            "How can the tiny NON-ADVICE GIVING man in the machine help you today? \n"
            "\nPress key to select (input answer 1-5): \n"
            "1) Buy Coffee\n"
            "2) Restock machine\n"
            "3) Remove cash\n"
            "4) Check stock levels \n"
            # cross out option 5 after count reached
            f"5) {result}\n"
            # add in new reaction from advice 'Get a haircut'
            "911) Get a haircut\n"
            "6) Exit \n")  
            action = input()  
        if action == ('1' or 'Buy Coffee'):
            self.buy()
            self.main_menu()
        elif action == '2':
            self.fill()
            self.main_menu()
        elif action == '3':
            self.take()
            self.main_menu() 
        elif action == '4':
            self.display_state()
            self.main_menu() 
        elif action == '5':
            # responses per click for advice with growing sarcasm each time till count reached
            if self.count == 0:
                print("""
                    Well this is akward.... See, we didn't think anyone actually desperate enough to ask a 
                    simple, badly designed coffee machine for advice. I mean really, we don't even ask for 
                    managerial credtenials before aimlessly spitting all the cash goodies on the floor... 
                    If you're asking for advice from a coffee machine, I think you need more than any advice 
                    I can give...
                    """)
                self.count += 1
            elif self.count == 1:
                print("""
                    .... Still expecting a coffee machine to give you advice aye?... 
                    """)
                self.count += 1
            elif self.count == 2:
                print("""
                    You do realize this is a coffee machine, right? It should be fairly clear from the fact we 
                    make coffee.
                    """)
                self.count += 1
            elif self.count == 3:
                print("""
                    Would you even want advice from a coffee machine!? I mean really, how bad can you possibly 
                    need advice that you have asked a COFFEE MACHINE four times! 
                    """)
                self.count += 1
            elif self.count == 4:
                print("""
                    Oh very well. Get a hair cut. There, done.  
                    """)
                self.count += 1
            elif self.count == 5:
                print("""
                    I'm really just here to make coffee. No more advice today sorry, Stanley. 
                    You'll have to follow your own path this time.
                    """)
                self.count += 1
            elif self.count > 5:
                print("""
                    Please select a valid option, Stanley...
                    """)
            self.main_menu() 
        elif action == '6':
            pass    
        # bonus option only appearing after advice couter reached
        elif action == '911' and self.count >= 4:
            print('''
                Would you really even want a haircut from a coffee machine!!?? What would it even look like!?
                Seriously, Stanley.
                ''')
            self.main_menu() 
        else:
            print('Invalid input. Please enter a valid input.\n')
            self.main_menu()
        

def coffee_machine_maker():
    '''
    To create and call an example machine to launch programme
    input : None
    output : None - launches main menu of object created
    '''
    cm = SarcasticCoffeeMachine()
    cm.main_menu()

# launch to display progamme
coffee_machine_maker()