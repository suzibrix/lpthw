name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches 
cm = height * 2.54 # VLL makes it metric for CM
round(cm)
weight = 180 # lbs
kg = weight * 0.45359237 # VLL makes it metric for KG
round(kg)
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}")
print(f"He's {height} inches tall.")
print(f"That's {cm} cm  in metric.") # VLL metric 
print(f"He's {weight} pounds heavy.")
print(f"That makes {kg} in kilograms.") # VLL goes full metric
print("Actually that's not too heavy.")
print("The kilograms won't kill you either.")  # VLL snark
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
mtotal = age + cm + kg 
round(mtotal)
print(f"If I add {age}, {height}, and {weight} I get {total}.")
print(f"With metric numbers plus age, you have {age}, plus {cm}, and {kg} equal {mtotal}.")



