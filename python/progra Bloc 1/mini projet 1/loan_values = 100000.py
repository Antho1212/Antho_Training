loan_values = 100000
monthly_repay = 800
year_interest = 0.04
monthly_interst = (1+year_interest) **(1/12) - 1

while loan_values > 0:
    #compute interst
    interst = loan_values*monthly_interst
    #check if last month
    if monthly_repay <= loan_values + interst:
        amortisation = monthly_repay - interst
    else:
        amortisation = loan_values
    #uptade loan value
    loan_values - amortisation
    #update total cost
    total_cost += interst
print("month %d -> amortisation=%d interest")