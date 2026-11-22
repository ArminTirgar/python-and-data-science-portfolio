import csv

my_file = open("shop_list.csv")

csv_data = csv.reader(my_file)


data_file = []

next(csv_data)

for row in csv_data:
    product_name = row[0]
    product_number = row[1]
    product_price = row[2]
    
    total_value = int(product_number) * int(product_price)
    data_file.append([product_name, product_number, product_price, total_value])
    

    
    
    
new_file = open("calculate_shop_list.csv", "w")
writer = csv.writer(new_file)
writer.writerow(["Product Name", "Number", "Price", "Total Value"])
writer.writerows(data_file)

