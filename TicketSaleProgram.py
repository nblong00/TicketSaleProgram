TICKET_PRICE = 10
SERVICE_CHARGE = 2


def calculate_price(number_of_tickets):
    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE


def main():
    tickets_remaining = 100 
    while tickets_remaining != 0:
        print("Number of tickets remaining: {}".format(tickets_remaining))
        user_name = input("Enter your name: ")
        try:
            tickets_needed = int(input("Hello {}, how many tickets are you looking to purchase? ".format(user_name)))
            if tickets_needed > tickets_remaining:
                raise ValueError("Requested ticket amount is above what is available. Try again.")
        except ValueError as err: 
            print("Invalid entry. {}".format(err))
        total_price = calculate_price(tickets_needed) 
        print("Your total is ${}".format(total_price))
        proceed = input("Would you like to proceed with purchase, {}?\n(Enter yes/no) ".format(user_name))
        if proceed.lower() == 'yes':
            print("Your tickets have been purchased.")
            tickets_remaining -= tickets_needed
        else:
            print("Thank you, {}, for using the Master Ticket service. Your purchase has been cancelled.".format(user_name))
            break
    if tickets_remaining <= 0:
        print("Sorry, {}, there are not enough tickets left".format(user_name))


main()
