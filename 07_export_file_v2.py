import pandas

# Frames and content for export

variable_dict = {
    "Item": ["Mugs", "Printing", "Packaging"],
    "Quantity": [300, 300, 50],
    "Price": [1, .5, .75]
}

fixed_dict = {
    "Item": ["Rent", "Artwork", "Advertising"],
    "Price": [25, 35, 10]
}

variable_frame = pandas.DataFrame(variable_dict)
fixed_frame = pandas.DataFrame(fixed_dict)

product_name = "Custom Mugs"
profit_target = "$100.00"
required_sales = "$200.00"
recommended_price = "$5.00"

print(variable_frame)

# Change dataframe to string (so it can be written to a txt file)
to_write = [product_name, variable_txt, fixed_txt,
            profit_target, required_sales,
            recommended_price]

# Write to file
# create file to hold data (add .txt extension)
file_name = f"{product_name}.txt"
text_file = open(file_name, "w+")

# heading
text_file.write(f"**** Fund Raising - {product_name} "
                "****\n\n")

text_file.write(variable_txt)

text_file.close()