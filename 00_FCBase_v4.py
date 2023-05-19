# import libs
import pandas


# functions

# gets profit goal
def profit_goal(total_costs):

    # Initialize variables and error message
    error = "Please enter a valid profit goal\n"

    valid = False
    while not valid:

        # ask for profit goal
        response = input("What is your profit goal (eg $500 or 50%: ")

        # Check if first character is $
        if response[0] == "$":
            profit_type = "$"
            # Get amount (everything after the $)
            amount = response[1:]

        # check if last character is %
        elif response[-1] == "%":
            profit_type = "%"
            # Get amount (everything after the %)
            amount = response[:-1]

        else:
            # set response to amount for now
            profit_type = "unknown"
            amount = response

        try:
            # Check amount is number more than zero
            amount = float(amount)
            if amount <= 0:
                print(error)
                continue

        except ValueError:
            print(error)
            continue

        if profit_type == "unknown" and amount >= 100:
            dollar_type = yes_no(f"Do you mean ${:.2f}. "
                                 f"ie {:.2f} dollars? ,"
                                 "y / n ")

            # Set profit type based under answer above
            if dollar_type == "yes":
                profit_type = "$"
            else:
                profit_type = "%"

        elif profit_type == "unknown" and amount < 100:
            percent_type = yes_no(f"Do you mean {amount}%? , "
                                  f"y / n")
            if percent_type == "yes":
                profit_type = "%"
            else:
                profit_type = "4"

            # return profit goal to main routine
            if profit_type == "$":
                return amount
            else:
                goal = (amount / 100) * total_costs
                return goal

            type == yes_no(f"Do you mean {}%?, y / n")
            if percent_type == "yes":
                profit_type = "%"
            else:
                profit_type = "$"

        # return profit goal to main routine
        if profit_type == "$":
            return amount
        else:
            goal = (amount / 100) * total_costs
            return goal

# number checker that checks whether input is a float or
# an integer that is more than zero, takes in custom error messages

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

print()
print("Please enter your variable costs below...")
# get variable expenses
variable_costs = get_expenses("variable")
variable_frame = variable_costs[0]
variable_sub_total = variable_costs[1]

print()
have_fixed = yes_no("Do you have fixed costs? ")

print()
print(f"**** Fund Raising - {product_name} ****")
print()
expense_print("Variable", variable_frame, variable_sub)

if have_fixed == "yes":
    expense_print("Fixed", fixed_frame[['Cost']], fixed_sub)

# **** PRINTING AREA ****

print()
print(f"**** Total Costs: ${all_costs:.2f} ****")
print()

print()
print(f"**** Profit & Sales Targets ****")
print(f"Profit Target: ${profit_target:.2f}")
print(f"Total Sales : ${all_costs + profit_target:.2f}")
print()

print()
print("**** Recommended Selling Price:"
      f" ${selling_price:.2f}")

if have_fixed == "yes":
    # Get fixed costs
    fixed_costs = get_expenses("fixed")
    fixed_frame = fixed_costs[0]
    fixed_sub_total = fixed_costs[1]
else:
    fixed_frame = ""
    fixed_sub_total = 0

# work out total costs and profit target
all_costs = variable_sub + fixed_sub_total
profit_target = profit_goal(all_costs)

# calculate recommended price
selling_price = 0

print(variable_frame)
print(variable_sub_total)

print(fixed_frame)
print(fixed_sub_total)