shower = float(input ("How many showers per day? "))
meals = float(input ("How many meals are cooked per day? "))
stove = input ("What kind of stove? Gas, Electric, or Induction? ")
if stove == "gas" or "Gas":
    stove = float (0.45)
elif stove == "electric" or "Electric":
    stove = float (0.3)
elif stove == "induction" or "Induction":
    stove = float (0.18)
trans = input ("How do you mostly commute? ")
if trans == "gas car":
    trans = float (0.4)
elif trans == "electric car":
    trans = float(.140)
elif trans == "plane":
    trans = float(2267.96)
elif trans == "bike":
    trans = float(0.5)
elif trans == "train":
    trans = float(1.361)
elif trans == "bus":
    trans = float(0.725748)
elif trans == "hybrid car":
    trans = float(0.25)
trans_times = float(input ("How many trips do you take per day?"))
lights = float(input ("How many lights are in your house? "))
lights_on = float(input ("How many hours are lights on per day? "))
comp = float(input ("How many hours do you use use computer for personal use per day? "))
ac = float(input ("How many hours daily is your AC on? "))
total = float((shower*1.200) + (meals*stove*1.500) + (lights*lights_on*0.0204) + (comp*0.060) + (ac*2.500) + (trans*trans_times))
print(f"{total} kilograms of CO2 are produced per day by you.  This is {total * 365} kilograms of CO2 per year.")