#Hotel Fee
rate_per_day = 1500 #rate per day
aircon_fee = 50 #aircon fee
internet_fee = 300 #internet fee
tv_fee = 100 #tv fee
evat = .12 #vat

#user input
num_days = int(input("Enter the number of days:")) #enter hotel days

#Compute for the Bill
amount = rate_per_day * num_days #get the amount depending on the days
total = amount + aircon_fee #total amount of aircon fee depending on days
internet_fee = tv_fee #total amount for internet fee depending on days
tax = total * evat #total vat depending on days
bill = total + tax #total tax depending on days

print("Number of Days",num_days) #number of days
print("Final Bill:", bill) #final bill
print("-----Nothing Follows-----") #print nothing follows