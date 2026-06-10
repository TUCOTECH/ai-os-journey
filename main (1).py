
name = 'tuco'
if name == 'alice' :
    print('hi , alice')
else :
    print('hello , stranger')

name = 'carol'
age = 3000

if name == 'Alice' :
    print('hi , Alice')
elif age < 12 :
    print('You are not Alice , kiddo')
elif age > 100:
    print( 'You are not Alice, grannie')
elif age > 2000:
    print('unlike You , Alice is not an undead immortal vampire.')
    
    
name = 'carol'
age = 3000

if name == 'Alice' :
    print('hi , Alice')
elif age < 12 :
    print('You are not Alice , kiddo')
else:
    print('You are niether Alice nor a little kid')


today_is_opposite_day = True

# set say_it_is_opposite_day based on today_is_opposite_day:
if today_is_opposite_day == True :
    say_it_is_opposite_day = True
else:
    say_it_is_opposite_day = False
    
# if it is opposite day , toggle say_it_is_opposite_day:    
if today_is_opposite_day == True:
    say_it_is_opposite_day = not say_it_is_opposite_day

# say what day it is :
if say_it_is_opposite_day == True:
    print('Today is opposie day ')
else:
    print('Today is not opposite day')

spam = input("input integer >>")
spam = int(spam)

if spam == 1 :
    print('Hello')
elif spam == 2 :
    print('Howdy')
else :
    print('Greetings')