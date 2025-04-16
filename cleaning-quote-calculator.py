hours = float(input("How many hours? "))
hourly_rate = 70
base_price = hourly_rate * hours
first_clean = input("Is this your first clean? (yes/no) ")

if first_clean.lower() == "yes":
    discount = base_price * 0.20
else:
    discount = 0
final_price = base_price - discount
print(f"Original Price: ${base_price:.2f}")
print(f"Discount: ${discount:.2f}")
print(f"Final Price: ${final_price:.2f}")
