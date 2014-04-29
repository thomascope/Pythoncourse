thomas={'age':29}
thomas['gender'] = 'male'
thomas['name'] = 'keith'

for count in range(len(thomas.keys())):
    print('For key %s the value is %s' %(thomas.keys()[count],thomas.values()[count]))

print('Or, all together now:')
print(thomas.keys())
print(thomas.values())