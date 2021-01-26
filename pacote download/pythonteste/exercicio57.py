sex = str(input('Enter your gender: [M/F] ')).strip().upper()[0]
while sex not in 'MmFf':
    sex = str(input('Error, please try again: ')).strip().upper()[0]
print('Sex {} succesfully registred!'.format(sex))
