from sys import exit
class Bank:
    def __init__(self,name,deposit):
        self.name = name
        self.balance = deposit
    def deposit(self, deposit):
        self.deposit = deposit
        self.balance += deposit
        return self.balance
    def withdrawl(self,withdrawl):
        if withdrawl < self.balance:
            self.balance -= withdrawl
            return self.balance
        else:
            print('Not enough balance')

class HDFC(Bank):
    def __init__(self):
        
        super().__init__(l)



name = input('Enter your name: ')
balance = int(input('Enter starting balance: '))
person1 =Bank(name, balance)

end = 'no'
action = 'E'
while(end != 'e'):
    action == 'E'
    if action == 'E':
        print("press 'E' for Repeat Instructions\n"
              "press 'd' for Deposit\n"
              "press 'w' for Withdraw\n"
              "press 'e' for exit")
        action = input('Enter action: ')
    if action == 'd':
        deposit = int(input('Enter amount to deposit: '))

        print('Your balance now is: ',person1.deposit(deposit))
        action = input('Enter action: ')
        # continue
    elif action == 'w':
        withdrawl = int(input('Enter amount to withdraw: '))
        print('Your balance now is: ',person1.withdrawl(withdrawl))
        action = input('Enter action: ')
    elif action == 'e':
        exit()
    else:
        print('Please enter correct action')
        action = input('Enter action: ')


