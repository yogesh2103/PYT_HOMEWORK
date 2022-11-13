#Problem 2: If You're Cold, Sit in a Corner. It's 90 Degrees!

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
