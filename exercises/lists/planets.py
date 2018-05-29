planet_list = ["Mercury", "Mars"]
planet_list.append( "Saturn") 
print(planet_list)
planet_list.append('Jupiter')
print(planet_list)
planet_list.extend(['Mars', 'The Sun'])
print(planet_list)
planet_list.insert(1, "Venus")
print(planet_list)
planet_list.insert(2, "Earth")
planet_list.append('Jupiter')
print(planet_list)
planet_list.append('Pluto')
print(planet_list)
rocky_arr = planet_list[0:4]
print(f'rocky_arr {rocky_arr}')
del planet_list[9]
print(planet_list)

#space craft tuple
spaceCraft = (('Apollo, Earth'),('Cassini', 'Saturn'))
for planet in planet_list:
    for craft in spaceCraft:
        landing = []
        if spaceCraft[0] == planet:
            landing.append(spaceCraft[1])