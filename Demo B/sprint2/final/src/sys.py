import csv
import operator
def register(user_name,email,password):
    if(user_name != None and password != None and email != None):
        with open("user.csv","a+") as csvfile: 
            writer = csv.writer(csvfile)
            writer.writerow([user_name,email,password,False])

def login(email,password):
    if(email != None and password != None):
        r = csv.reader(open("user.csv"))
        lines = [l for l in r]
        for i in  lines:
            if (i[1] == email and i[2] == password) :
                i[3] = True
                break
        writer = csv.writer(open("user.csv","w"))
        writer.writerows(lines)

def recipe(ingredients):
    r = csv.reader(open("recipe.csv"))
    recipes = {}
    id = 0 
    for i in r:
        ingredient_need = list(i[2].split(" "))
        if(ingredient_need == ingredients['ingredients']):
            id = id + 1
            result = {
                'aname':None,

                'type':None,

                'ingredients':None,

                'cooktime':None,
                
                'hint':None

            }
            result['aname'] = i[0]
            result['type'] = i[1]
            result['ingredients'] = i[2]
            result['cooktime'] = i[3]
            result['hint'] = i[4]
            recipes[id] = result
    return recipes

        

