#denomination.py
amount=int(input())
five_hundred_notes=amount//500
remaining_balance=amount%500
print("Five Hundred Notes (500): ",five_hundred_notes)
hundred_notes=remaining_balance//100
remaining_balance=remaining_balance%100
print("Hundred Notes (100):",hundred_notes)
fifty_notes=remaining_balance//50
remaining_balance=remaining_balance%50
print("Fifty Notes (50):",fifty_notes)
ten_notes=remaining_balance//10
remaining_balance=remaining_balance%10
print("Ten Notes (10):",ten_notes)
print(five_hundred_notes+hundred_notes+fifty_notes+ten_notes)
print(amount)
#output
#1250
#Five Hundred Notes (500):  2
#Hundred Notes (100): 2
#Fifty Notes (50): 1
#Ten Notes (10): 0
#5
#1250
