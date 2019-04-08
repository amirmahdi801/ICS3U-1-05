print ("Hi, this program will calculate the cost of a pizza")
inch = input("how many inches is the diameter of the pizza? ")
labour = 0.75 # per pizza
rent = 1.0 # per pizza
lare = labour + rent # lare is the first 2 letters of labour and rent
inch = int(inch)
cost = lare + 5 * inch / 10 # i couldn't multiply a float so i turned 0.5 into 5 so that it could multiplied and then i divided it
cost = str(cost) 
print ("the total cost of the pizza is " + cost + "$")
