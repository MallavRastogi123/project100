class atm:
    
    def CashWithdraw(cardNumber):
        print("To Go Ahead with Cash Withdrawl for your Card Number "+ cardNumber+" press 1");
    def BalaceEnquiry(pinNumber,cardNumber):
        print("You still have an active balance of Rs. 29900 for your card " + cardNumber + "with pin " + pinNumber);
    
def main():
    cardNumber=input("Enter your card number: ");
    pinNumber=input("Enter the pin: ");
    
    atm.CashWithdraw(cardNumber);
    atm.BalaceEnquiry(pinNumber,cardNumber);

main()