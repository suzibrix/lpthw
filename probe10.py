# Python play VLL #2, or 10 depending on how you count

# Let's see how things play out

formatter = "{}\n{}\f{}\t{}"

print(formatter.format( 1, 2, 3, 4))
print(formatter.format( "one", "two", "three", "four"))

pretty_maker = "\f{}\v{}\v{}:{}\t{}"

print(pretty_maker.format("this", "is", "a", "test", "of"))
print(pretty_maker.format("the", "emergency", "broadcast", "system", "this"))
print(formatter.format("is", "only", "a", "test"))

print("~" * 22) 
print(" :-) " * 7) 

print('''
        \fStrange things done under the Midnight Sun\n by the men who moil for gold:
        \n\t\tThe Artic trails\n\t have their secret tales that will make your blood
        run cold;\n\t\tThe Northern Lights have seen queer sights\n but the strangest         they ever did see\n\t Was that night on the marge of Lake LeBarge\n\t where         I cremated Sam McGee.
        ''')
    
