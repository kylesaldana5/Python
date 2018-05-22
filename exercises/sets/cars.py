showroom = {'Jeep', 'Bentley', 'BMW', 'Aston Martin'}
print(len(showroom))
showroom.add('Jeep')
print(showroom)
showroom.update(['Mercedes', 'Audi'])
print(showroom)
showroom.discard('Bentley')
print(showroom)

junkyard = {'Jeep', 'BMW', 'Camery', 'Dodge'}
print(showroom.intersection(junkyard))
newShow = showroom.union(junkyard)
print(newShow)
newShow.discard('Dodge')
print(newShow)
