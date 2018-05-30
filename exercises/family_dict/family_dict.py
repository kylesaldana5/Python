my_family = {
    'mom':{
        'name': 'Ronda',
        'age': 46
    },
    'dad':{
        'name': 'Leonard',
        'age': 51
    },
    'sister':{
        'name': 'Megan',
        'age': 26
    },
    'brother':{
        'name': 'Ryan',
        'age': 23
    }
}

for key, fam in my_family.items():
    print(" {1} is my {0} and is {2} years old".format(key,fam['name'], fam['age']))