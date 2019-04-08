print ("Hi, this program will calculate the cost of a pizza")
inch = input("how many inches is the diameter of the pizza? ")
labour = 0.75 # per pizza
rent = 1.0 # per pizza
lare = labour + rent # lare is the first 2 letters of labour and rent
inch = int(inch)
near = inch * 5 / 10 # we should divide by 10 because we turned 0.5 to 5
cost = (near + lare)
money = cost * 1.13 # calculating the HST 
money = str(money)
print ("the total cost of the pizza is " + money + "$")
