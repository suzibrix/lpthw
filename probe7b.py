from sys import argv

script, apples, oranges, light_waves, crinoline = argv

print(f"\n\tCan you give {script} a better name?")
print("\tWe were thinking something more like", apples)
print("\tWe know you can come up with good args because of", oranges)
print(f"\tBut we also want {light_waves} and {crinoline}.")
print(f"""
\t\fListing:\n\n\t * {script} = bad name\n\t * {apples} = good name \n\t * {oranges} = good name\n\t * {light_waves} = so-so/try harder \n\t * {crinoline} is a sentimental favorite.
\n\t Just remember, make better script names!
""" )
print("  If you see this line you know the script executed successfully.")

