def show_welcome():
    print("*" * 38)
    print("**   Welcome to the Snakes Cafe!    **")
    print("**   Please see our menu below.     **")
    print(f"**{' '*34}**")
    print('** To quit at any time, type "quit" **')
    print("*" * 40)
    print("\n")

def show_menu(menu):
    for key, value in menu.items():
        print(f"{key}")
        print("----------")
        for item in value:
            print(item)
        print("")

def prompt_user() -> str:
    print("*" * 40)
    print("**     What would you like to order?  **")
    print("*" * 40)
    return input("> ")


def order_summary(orders: dict):
    for order, amount in orders.items():
        if amount > 0:
            print(f"{order} => {amount}")
            print("")

def main():
    orders = {}
    menu = {
        'Appetizers': ['Wings', 'Cookies', 'Spring Rolls'],
        'Entrees': ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden'],
        'Desserts': ['Ice Cream', 'Cake', 'Pie'],
        'Drinks': ['Coffee', 'Tea', 'Unicorn Tears'],
    }
    response = ""
    for section in menu:
        for item in menu[section]:
            orders[item] = 0
    show_welcome()
    show_menu(menu)
    while response != "quit":
        response = prompt_user()
        if response in orders.keys():
            orders[response] += 1
            print(f"** {orders[response]} { 'order' if orders[response] == 1 else 'orders'} of {response} have been added to your meal **")
        elif response != "quit":
            orders[response] = 1
            print(f"** {response} is not in stock but we will fetch it for your meal **")
        else:
            order_summary(orders)

if __name__ == "__main__":
    main()