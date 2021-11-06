weight = 41.5
# ground shipping
flat_charge = 20.00
if weight <= 2:
  groundprice = weight * 1.50
elif weight > 2 and weight <= 6:
  groundprice = weight * 3.00
elif weight > 6 and weight <= 10:
  groundprice = weight * 4.00
else:
  groundprice = weight * 4.75

groundcost = groundprice + flat_charge
print("your ground shipping cost: $",str(groundcost))
premium_cost = 125.00
print("your premium ground shipping cost: $",str(premium_cost))
# Drone shipping
if weight <= 2:
  drone_price = weight * 4.50
elif weight > 2 and weight <= 6:
  drone_price = weight * 9.00
elif weight > 6 and weight <= 10:
  drone_price = weight * 12.00
else:
  drone_price = weight * 14.75
print("your drone shipping cost: $" , str(drone_price))


