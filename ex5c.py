name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches 
cm = height * 2.54 # VLL makes it metric for CM
cm_r = round(cm ,2) # cm_r = rounded cm
weight = 180 # lbs
kg = weight * 0.45359237 # VLL makes it metric for KG
kg_r = round( kg , 2 ) # kg_r = rounded kg
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"That's {cm_r} cm  in metric.") # VLL goes  metric 
print(f"He's {weight} pounds heavy.")
print(f"That makes {kg_r} in kilograms.") # VLL goes full metric
print("Actually that's not too heavy.")
print("The kilograms won't kill you either.")  # VLL snark
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
mtotal = age + cm_r + kg_r 
# round(mtotal) <-- Ack, mistake! Round doesn't work that way.
print(f"If I add {age}, {height}, and {weight} I get {total}.")
print(f"With metric numbers plus age, you have {age}, plus {cm_r}, and {kg_r} equal {mtotal}.")



