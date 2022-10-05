from resDetails import Restaurant

print("Hello and how are you doing?")

print("I am good, wheres the menu?")


# CREATING THE MENU TO A TEXT FILE.
#menu = open('menu.txt', 'w')

#menu.writelines('Mukimo Beef ' '220' )
#menu = open('menu.txt', 'a')
#menu.write('\nPilau ' '125')
#menu.write('\nChips ' '100')
#menu.write('\nSausage ' '45')
#menu.write('\nSmokie ' '40')
#menu.write('\nTea ' '20')
#menu.write('\nBurger ' '500')
#menu.close()

#menu = open('menu.txt', 'r')


#for meals in menu.readlines():
 #   res = Restaurant("Kings Palace Restaurant", meals)
         # meals

#print(dish)
#print(res.menu)


#print(res.menu)

#hotel = Restaurant('Kings Palace Restaurant', meals)
#print(hotel.name)

meals =[
 'Mukimo Beef ' ' 220',
 'Pilau ' ' 125',
 'Chips ' ' 100',
 'Sausage ' ' 45',
 'Smokie ' ' 40',
 'Tea ' ' 20',
 'Burger ' ' 500'
]

print('Ohh you ordered for the menu, here it is.')
def hotel(meals):
    for meal in meals:
     print(meal)

print(hotel(meals))

preference = input('Serve me with: ')

# IF STATEMENTS TO KNOW THE PREFERENCE THE CUSTOMER WILL CHOOSE.
def prefer():
   if preference == 'Mukimo Beef':
    print('Here is your ' + preference + ' enjoy ' )
   elif preference == 'Pilau':
    print('Here is your ' + preference + ' enjoy ')
   elif preference == 'Chips':
    print('Here is your ' + preference + ' enjoy ')
   elif preference == 'Sausage':
     print('Here is your ' + preference + ' enjoy ')
   elif preference == 'Smokie':
     print('Here is your ' + preference + ' enjoy ')
   elif preference == 'Tea':
    print('Here is your ' + preference + ' enjoy ')
   elif preference == 'Burger':
    print('Here is your ' + preference + ' enjoy ')
   else:
    print('Sorry but we do not have your preference in our menu.')

print(prefer())

print('Would you like to be served with another thing?')

another_thing = input()
if another_thing == 'Yes':
    print(hotel(meals))
    preference = input('Can you serve me with: ')
    print(prefer())
elif another_thing == 'No':
    print('Alright sir have a good day.')
else:
    print('Its ok hope you are satisfied.')

print('Can you kindly leave your review before you go?\nIt will go a long way in assisting us to better our services and food.')
review = input()
print('Appreciated.')

#reviews = open('reviews.txt', 'w')

#APPENDS THE CUSROMERS REVIEWS ONTO THE REVIEWS.TXT FILE.

reviews = open('reviews.txt', 'a')

reviews.write('\n' + review)
reviews.close()























