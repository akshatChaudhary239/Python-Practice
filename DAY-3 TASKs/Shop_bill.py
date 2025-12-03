# Shop billing system
Product = input("Enter the product you purchased ")
Quantity = float(input("how much is the quantity ")) 
price = float(input("what's the price of the product "))

total_price = price*Quantity
if total_price>=1000:
    discount = total_price*0.10
else:
    discount = 0    
final_amount= total_price-discount

print(f"""
---------BILL--------
Product        : {Product}
Quantity       : {Quantity}
Price per unit : {price}
Total          : {total_price}
Discount       : {discount}
Final Price    : {final_amount}  
---------------------
""")