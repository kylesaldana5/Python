stockDict = { 'GM': 'General Motors', 'CAT':'Caterpillar', 'EK':"Eastman Kodak" }

purchases = [ ('GM', 25, "10-22-2016", 500), ("CAT", 100, "11-05-17", 10), ("HE", 35, "05-05-16", 20), ("EK", 35, "05-25-16", 40), ("EK", 35, "10-15-16", 70)]

for purchase in purchases:
    for key, name in stockDict.items():
        if purchase[0] == key:
            total = purchase[1] * purchase[3]
            print(f"total stock purchase {name} {total}")
        
            

