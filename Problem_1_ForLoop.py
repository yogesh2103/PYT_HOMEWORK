#Problem 1: IOU!
#Create list of disney_characters
disney_characters = ["simba", "ariel", "pumba", "flounder", "nala", "ursula","scar", "flotsam", "timon"]
print (disney_characters,"\n")



#Find out if each of them contain i, o, or u in their names
for char in disney_characters:
    if 'u' in char:
        print(char,"U are so Uniquely U!")
    elif 'i' in char:
        print(char,"I bet you're Impressively Intelligent!")
    elif 'o' in char:
        print(char,"O My! How Original!")
    else:
        print(char,"Ehh, a's and e's are so ordinary.")
