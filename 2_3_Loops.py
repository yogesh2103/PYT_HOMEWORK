#Problem 1: IOU!
#Create list of disney_characters
print('Problem 1: IOU!')

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


#Problem 2: If You're Cold, Sit in a Corner. It's 90 Degrees!
print('')
print('')
print('#Problem 2: If You''re Cold, Sit in a Corner. It''s 90 Degrees!')
#Declare & assign 90 to variable temperature
temperature = 90

#Loop start
while temperature >= 75:
    #Condition start
    if temperature > 75:
        print("The temperature is",temperature, "— crank the AC!temperature")
    else:
        print(temperature,". Ahh, that's better")
    #Condition end

    #Decrease the counter
    temperature -= 3
#Loop end
