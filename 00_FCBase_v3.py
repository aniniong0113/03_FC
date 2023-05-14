# import libs
import pandas


# functions

# number checker
def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# yes no checker
def yes_no(question):
    to_check = ["yes", "no"]

    valid = False
    while not valid:

        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item

        print("Please enter either yes or no...\n")


# not blank checker
def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print(f"\n {error}. Please try again.\n")
            continue

        return response


# apply currency
def currency(x):
    return f"${x:.2f}"


# gets expenses, returns list which has the data frame and sub total
def get_expenses(var_fixed):
    # Set up dictionaries and lists
    item_list = []
    quantity_list = []
    price_list = []

    variable_dict = {
        "Item": item_list,
        "Quantity": quantity_list,
        "Price": price_list
    }

    # loop to get component, quantity and price
    item_name = ""
    while item_name.lower() != "xxx":
        print()
        # get name, quantity and item
        item_name = not_blank("Item name: ", "The component name must not be blank")
        if item_name.lower() == "xxx":
            break

        if var_fixed == "fixed":
            quantity = 1
        else:
            quantity = num_check("Quantity:",
                                 "Tha amount must be a whole number,",
                                 int)

        price = num_check("How much for a single item? $",
                          "The price must be a number <more than zero>",
                          float)
        # add item, quantity and price to lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('Item')

    # Calculate cost of each component
    expense_frame['Cost'] = expense_frame['Quantity'] * expense_frame['Price']
    sub_total = expense_frame['Cost'].sum()

    # Currency Formatting (uses currency function)
    add_dollars = ['Price', 'Cost']
    for item in add_dollars:
        expense_frame[item] = expense_frame[item].apply(currency)

    return [expense_frame, sub_total]


# main routine

product_name = not_blank("What is the product name? ",
                         "Please enter a name, this can't be blank")

# get variable expenses
variable_costs = get_expenses("variable")
variable_frame = variable_costs[0]
variable_sub_total = variable_costs[1]

have_fixed = yes_no("Do you have fixed costs? ")

if have_fixed == "yes":
    fixed_costs = get_expenses("fixed")
    fixed_frame = fixed_costs[0]
    fixed_sub_total = fixed_costs[1]
else:
    fixed_frame = ""
    fixed_sub_total = 0

print(variable_frame)
print(variable_sub_total)

print(fixed_frame)
print(fixed_sub_total)