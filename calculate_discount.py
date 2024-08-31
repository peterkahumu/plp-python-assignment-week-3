def calculate_discount(price, discount_percent):
    discount_calculator = lambda price, discount_percent: 0 if discount_percent < 20 else price * discount_percent / 100
    
    discount = discount_calculator(price, discount_percent)
    
    print(f"Discount granted: {discount}. Final Price: {price - discount}")
    
price = float(input("Please Enter the original Price: "))
discount_percent = float(input("Please Enter the discount percentage: "))

calculate_discount(price, discount_percent)