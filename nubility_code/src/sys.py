import csv
import operator
def register(user_name,email,password):
    if(user_name != None and password != None and email != None):
        with open("user.csv","a+") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([user_name,email,password])

def login(email,password):
    if(email != None and password != None):
        r = csv.reader(open("user.csv"))
        lines = [l for l in r]
        for i in  lines:
            if (i[1] == email and i[2] == password) :
                return i[1]
    return None


def recipe(ingredients):
    r = csv.reader(open("recipe.csv"))
    recipes = {}
    ingre = set(ingredients['ingredients'])
    id = 0
    for i in r:
        ingredient_need = list(i[2].split(" "))
        if(ingre < set(ingredient_need)):
            id = id + 1
            result = {}
            result['aname'] = i[0]
            result['type'] = i[1]
            result['ingredients'] = i[2]
            result['cooktime'] = i[3]
            result['hint'] = i[4]
            result['contributor'] = i[5]
            result['url'] = i[6]
            recipes[id] = result
    return recipes

def addrecipe(name,mtype,ingredients,time,hints,email,url):
    if(name != None and mtype != None and ingredients != None and time != None and hints != None and email != None):
        with open("recipe.csv","a+") as csvfile:
            writer = csv.writer(csvfile)
            if(url != None):
                writer.writerow([name,mtype,ingredients,time,hints,email,url])
            else:
                writer.writerow([name,mtype,ingredients,time,hints,email,"https://thestayathomechef.com/wp-content/uploads/2014/10/How2Bto2Bboil2Beggs2B10-500x375.jpg"])
def getrecipe(email) :
    r = csv.reader(open("recipe.csv"))
    recipes = {}
    id = 0
    for i in r:
        if(email == i[5]):
            id = id + 1
            result = {}
            result['aname'] = i[0]
            result['type'] = i[1]
            result['ingredients'] = i[2]
            result['cooktime'] = i[3]
            result['hint'] = i[4]
            result['contributor'] = i[5]
            result['url'] = i[6]
            recipes[id] = result
    return recipes

def getrecipebyname(name) :
    r = csv.reader(open("recipe.csv"))
    recipes = {}
    id = 0
    for i in r:
        if(name == i[0]):
            id = id + 1
            result = {}
            result['aname'] = i[0]
            result['type'] = i[1]
            result['ingredients'] = i[2]
            result['cooktime'] = i[3]
            result['hint'] = i[4]
            result['contributor'] = i[5]
            result['url'] = i[6]
            recipes[id] = result
    return recipes

def delete(mealname,email):
    if(mealname != None and email != None):
        r = csv.reader(open("recipe.csv"))
    else:
        return
    lines = [l for l in r]
    for i in  lines:
        if (i[0] == mealname and i[5] == email) :
            lines.remove(i)
            break
    writer = csv.writer(open("recipe.csv","w"))
    writer.writerows(lines)

# arg:      list of ingredients in running list
# return:   list of recommend ingeidients for Explorer
def recommExplorer(ingredient):
    r = csv.reader(open("recipe.csv"))
    lines = [x for x in r]
    result1 = {}
    result = []
    ingredients = list(ingredient.split(" "))
    for i in lines:
        ingredient_recomm = list(i[2].split(" "))
        if set(ingredients).issubset(set(ingredient_recomm)):
            diff = list(set(ingredient_recomm).difference(set(ingredients)))
            result = list(set(result).union(set(diff)))
    result1['recomm_ingredients'] = result
    return result1

# arg:      viod
# return:   list of recommend ingeidients for Contributor
def recommContributor():
    result2 = {}
    e = csv.reader(open("recipe.csv"))
    lines = [i for i in e]
    usedIngredient = []
    for i in lines:
        ingredient_inRecipe = list(i[2].split(" "))
        usedIngredient = list(set(usedIngredient).union(set(ingredient_inRecipe)))
    r = csv.reader(open("ingredients.csv"))
    allIngredient = [x[0] for x in r]
    result = list(set(allIngredient).difference(set(usedIngredient)))
    result2['unuesd_ingredients'] = result
    return result2
