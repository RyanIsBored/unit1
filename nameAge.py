#Ryan Jones
#1/22/18

fullname= input( 'Your full name: ')
firstname, lastname = fullname.split()
age= int(input( 'Enter your age: '))
print( 'Your first name has',(len(firstname)), 'letters.')
print( 'Your last name has',(len(lastname)), 'letters.')
nextyear= (age++1)
print( 'Next year you will be',(nextyear), 'years old.')