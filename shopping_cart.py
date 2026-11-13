# 1. Ask for Customar's name
name = input("Enter customer name:")

# 2. Ask for 3 Product's names and prices
product1 = input("Enter first product name:")
price1 = float(input("Enter first product price:"))

product2 = input("Enter second product name:")
price2 = float(input("Enter second product price:"))

product3 = input("Enter third product name:")
price3 = float(input("Enter third product price:"))

# 3. Calculate subtotal
subtotal = price1 + price2 + price3

# 4. Determine discount
if subtotal >= 5000:
  discount_rate = 0.20
elif subtotal >= 3000:
  discount_rate = 0.10
elif subtotal >= 1000:
  discount_rate = 0.05

else:
  discount_rate = 0

# Calculate discount and final total

discount = subtotal * discount_rate 
final_total = subtotal - discount 

# 5. Display shopping summary 
print(f"Customer Name: {name}")
print()
print(f"Product 1: {product1}")
print(f"Price: {price1:.2f}")

print(f"Product 2: {product2}")
print(f"Price: {price2:.2f}")

print(f"Product 3: {product3}")
print(f"Price: {price3:.2f}")

print()

print(f"Subtotal: {subtotal:.0f}")
print(f"Discount: {discount:.2f}")
print(f"Final Total: {final_total:.2f}")