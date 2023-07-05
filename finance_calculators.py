import math

print("Investment - to calculate the amount of interest you'll earn on an investment")
print("Bond       - to calculate the amount you'll have to pay on a home loan")
print()

user_input = input("Enter either 'Investment' or 'Bond' from the menu above to proceed: ").lower()              #User chooses whether they want investment or bond

if user_input == "investment":                                                                        #If user chooses investment then the if statement will run below
  P = int(input("How much are you depositing? "))                                                     #P = The value they are depositing
  r = int(input("What interest rate? "))/100                                                          #r = The interest rate
  t = int(input("How many years do you plan to invest for? "))                                        #t = The length of time they are investing
  interest_type = input("What interest would you like? 'Simple' or 'Compound'? ").lower()             #Choose simple or compound interest
  
  if interest_type == "simple":                                                             
    A = (P*(1 + r*t))                                               #if simple is chosen this calculation will run
    print(A)
  elif interest_type == "compound":
    A = P * math.pow((1+r),t)                                       #if compound is chosen this calculation will run
    print(A)
  else:
    print("Invalid input. Please enter either 'Simple' or 'Compound' interest ")

elif user_input == "bond":                                                      #If user chooses bond then the elif statement will run
  P = int(input("What is your current house value? "))                          #P = the current house value
  i = int(input("What is your monthly interest rate? "))/100/12                 #i = the monthly interest rate
  n = int(input("How many months will the bond be repaid? "))                   #n = the amount of months to repay the bond
  repayment = (i * P)/(1 - (1 + i)**(-n))                                       #This calculation will run to return the amount to be repaid per month
  print(repayment)

else:
  print("Invalid input. Please select either 'Investment' or 'Bond' ")  
