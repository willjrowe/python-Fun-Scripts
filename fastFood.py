import datetime
import sys
args = sys.argv
if ((args[1]).lower()=='yesterday'):
    Current_Date_Formatted = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime ('%m/%d/%Y')
    args.remove('yesterday')
else:    
    Current_Date_Formatted = datetime.datetime.today().strftime ('%m/%d/%Y') 
f = open('fastFoodList.txt','a')
f.write('\n'+Current_Date_Formatted+': '+args[1]+' - '+args[2])
print('Your eating habits have been updated')