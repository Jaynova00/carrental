#rent car



#input
first3days = 100
after3days = 50
thredays = 3
days = int(input('enter number of days'))


#process
if(days <= 3):
    cost = days * first3days
else:
    cost = (first3days * thredays) + (days - thredays) * after3days 


#output
print('for', days, 'days', 'the cost is',format(cost,'.2f'))
