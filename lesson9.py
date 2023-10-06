my_dictionary = {}

days_in_month = {'Jan':31,
                 'Feb':28,
                 'Mar':31}

#prints number of days 
print(days_in_month['Jan'])
#prints array/dictionary
print(days_in_month)
#prints months
print(days_in_month.keys())
#prints days
print(days_in_month.values())
#print (key, value) pairs
print(days_in_month.items())
#test if key is present
print("Is Feb present: ", 'Feb' in days_in_month)
print("Is Sat present: ", 'Sat' in days_in_month)
#adding new values
#days_in_month['Apr'] = 20
#print(days_in_month)
#changing values
#days_in_month['Apr'] = 30
#print(days_in_month)
#combining dictionaries
days_in_month2 = {'Apr':30,
                 'May':31,
                 'Jun':30}
days_in_month.update(days_in_month2)
print(days_in_month.items())

#removing values
#del days_in_month['Apr']
odds = {1:'one', 3:'three', 5:'five'}
evens = {2: 'two', 4:'four', 6:'six'}
odds.clear()
print("After clearing odds:")
print(odds)
#del evens
#print("After clearing evens:")
#print(evens)

#accessing values
#should get 'None'
print(days_in_month.get('January'))
#replaces 'None' with 'January not present'
print(days_in_month.get('January', 'January not present'))
