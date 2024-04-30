def restart(): #this is defining the restart part of the code, and also ending the calculation part
    KeepGoing = input("Would you like to do another calculation? Y/N?: ").upper() #Giving the user the chance to restart
    while (KeepGoing == "Y"): #This is saying that if the user types Y then the following things should happen
        calc() #It should loop again to the user entering the 2 variables
        restart()#once it has done the calculation again this is making sure that it asks the user again if they would like to do another calculation. This line is important as it stops am infinite loop
    else: # covers the possibility that the user dosen't type Y
        print("Goodbye")
        exit()#stops the program


def calc(): #this is defining the calcualtion part of the code
    try:
        num1 = float(input("Enter 1st number: ")) 
        num2 = float(input("Enter 2nd number: "))
    except ValueError: #this is adding the possibillity that the user dosen't enter a number
        print("Please enter a number, I will now start again")
        restart()#this is the prompting the restart function that is defined later to ask the user if they would like to restart the code
    
    operator = input("Please enter the operator you would like to use, It must be one of +, -, * or /: ") #asking the user what operator they would like to use

    if operator == "+": 
        addanswer = float(num1+num2)#line is added so the user can do decimal calculations if wanted
        print ("Your answer is",addanswer)

    elif operator == "-":
        subanswer = float(num1-num2)
        print ("Your answer is",subanswer)

    elif operator == "*":
        multanswer = float(num1*num2)
        print ("Your answer is",multanswer)

    elif operator == "/":
        try:
            divanswer = float(num1/num2)#float line is more needed here than others and dividing will more often then the other operators return a decimal
            print ("Your answer is",divanswer)
            pass
        except ZeroDivisionError: #This is convering the fact that the code originally wouldnt be able to divde by 0 and then printing them message i put after
            print ("Cannot divide by 0")

    else: # this is covering the possiblity of the user not entering one of the for operators
        print ("Please enter one of the 4 operators")



calc()# these 2 lines are the actual calculation with this one running the calc function
restart()#and this one running the restart. Without these the code wouldnt work as everything else is within functions
