print('Enter TB or GB for the advertised unit')
unit = input('>')
#calculate the amount that the advertiser lies
if unit == "TB" or 'tb':
    disperency = 1000000000000/109951162776
elif unit == 'GB' or 'gb':
    disperency = 1000000000/1073741824

print("what's the advertised capacity ?")
advertised_capacity = input('>')
advertised_capacity = float(advertised_capacity)

# calculate the real capacity round it to nearest hundreths
# and convert it to a string so that it can be concatenated:
real_capacity = str(round(advertised_capacity*disperency , 2))

print( 'The actual capcity is ' + real_capacity + '' + unit)