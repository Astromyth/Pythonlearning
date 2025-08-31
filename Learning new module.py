'''
#dictionary
____________________

dictionary={'a':'123', 'b':'143'}
dictionary['c']='567'
print(dictionary)
del (dictionary['a'])
print(dictionary)
print('g' in dictionary)
print(dictionary.keys())
print(dictionary.values())
print(dictionary.get('g','g not found' ))

'''

#list

list=[1,2,4,5]
list[3]='7'
print(list)
print(list[0:3:3])
a='john CeNa            '
b= a.capitalize()
print(b)
print(a.upper())
print(a.lower())
print(a.replace('john CeNa    ','U cant See me'))
print(a.find('D'))
print(a.lstrip())
print(a.rstrip())
print(a.split())
print(a.splitlines())
c='_'
print(c.join(a))
