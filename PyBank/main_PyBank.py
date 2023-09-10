#Importing the operating system and csv capailities
import os, csv

#Importing a fix to the date structure
from datetime import date

csvpath = os.path.join("C:\\Users\\Brian Keffer\\GW Bootcamp\\python-challenge\\PyBank\\Resources\\budget_data.csv")

months = []
profit_losses = []

with open(csvpath, encoding= "UTF-8") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter= ",")
    csv_header = next(csvreader)

    total_months = 0
    difference = 0
    total_difference = 0
    net = 0
    previous_row = 0 
    greatest_increase = 0
    increase_month = ''
    greatest_decrease = 0
    decrese_month = ''
    
    for row in csvreader:
        

        #had to make everything in the profit/loss column an int to avoid error
        #profit_loss below iterates through the rows
        profit_loss = int(row[1])
        net = net + profit_loss
        difference = profit_loss - previous_row
        previous_row = profit_loss

        # It's important to have the differnce definition within the iteration we can accurately latch onto
        # the correct min and max
        if difference > greatest_increase:
            greatest_increase = difference
            increase_month = row[0]

        if difference < greatest_decrease:
            greatest_decrease = difference
            decrease_month = row[0]

        #This line is needed to determine the average change below. len(months) gives the same value as
        # the total_months variable
        if len(months) > 0:
            total_difference = total_difference + difference

        #Counting the months
        if row[0] != row[1]:
            total_months = total_months + 1

        #Adding the cells into their lists
        #This needs to happen at the bottom of the iteration instead of the top like I originally had
        #The new month specifically needs to be added after all the work is done for that iteration 
        months.append(row[0])
        profit_losses.append(row[1])

    #Outside of iteration
    average_change = round(total_difference / (len(months)-1),2)

output_file = os.path.join("C:\\Users\\Brian Keffer\\GW Bootcamp\\python-challenge\\PyBank\\Analysis\\Results_PyBank.txt")
with open(output_file, 'w') as text_file:

    #\n means to end line
    analysis = (f'Financial Analysis\n'
                  '-----------------------------\n'
                  f'Total Months: {total_months}\n'
                  f'Total: ${net}\n'
                  f'Average Change : ${average_change}\n'
                  f'Greatest Increase in Profits: {increase_month} (${greatest_increase})\n'
                  f'Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})\n')
    
    #Must be printed in the terminal
    print(analysis)
    text_file.write(analysis)

#Checking with prints

#print(total_months)
#print(months)
#print(net)
#print(greatest_increase)
#print(greatest_decrease)
#print(increase_month)
#print(decrease_month)
#print(average_change)