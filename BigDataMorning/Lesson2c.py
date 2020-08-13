
# decision in strings
county = str(input('Which county are you from?'))

if county.lower() == 'meru':
    print('Go get  some oranges')

elif county.lower() == 'nairobi':
    print('Get some fish')

elif county.lower().endswith('k'):
    print('Thats might be my county')

else:
    print('Invalid County')