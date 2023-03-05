"""PY Bank Code"""
#read in csv
import os
import csv

file_path = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

#create lists
months = []
moneyplz = []
track_changes = []
money_month = []

with open(file_path) as file:

    budget_datafile = csv.reader(file, delimiter= ',')

    bank_headers = next(budget_datafile)

    for row in budget_datafile:
        #TOTAL MONTHS
        months.append(row[0])
        total_months = len(months)

        #PROFITS AND LOSSES
        moneyplz.append(row[1])
        moneyplz_int = [int(x) for x in moneyplz]
        total_stack = sum(moneyplz_int)
        
    # AVERAGE OF PROFIT/LOSS
    for i in range (len(moneyplz_int)-1):
        track_changes.append(moneyplz_int[i+1]-moneyplz_int[i])
    change_avg = sum(track_changes)/len(track_changes)
    #INCREASE/DECREASE
    big_money = max(track_changes)
    small_money = min(track_changes)   


    print('Financial Analysis')
    print('--------------------------------------')
    print(f'Total Months: {total_months}')
    print(f'Total: ${total_stack}')
    print (f'Average Change: ${round(change_avg,2)}')
    print(f'Greatest Increase in Profits: ${big_money}') 
    print(f'Greatest Decrease in Profits: ${small_money}') 







       
   
    







