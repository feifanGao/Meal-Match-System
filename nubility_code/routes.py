from flask import render_template, request, redirect, url_for, abort, session
from server import app
import src.sys
'''
Main Pages
'''

@app.route('/',methods=["GET","POST"])
def home():
    if request.method == 'GET':
        ingredients = request.args.get('ingredient')
        if (ingredients != None):
            result = src.sys.recommExplorer(ingredients)
            return render_template("base.html",result=result)
        return render_template("base.html")

@app.route('/Register',methods=["POST","GET"])
def Register():
    if request.method == 'GET':
            return render_template('Register.html')

    else:
        user_name = request.form.get('User_Name')
        email = request.form.get('Email')
        password = request.form.get('Password')
        src.sys.register(user_name,email,password)
        return render_template('Register.html',msg = 'Register successfully!')


@app.route('/page2',methods=["GET","POST"])
def page2():
    return render_template('page2.html')

@app.route('/Search',methods=["GET","POST"])
def Search():
    return render_template('search.html')

#@app.route('/create',methods=["GET","POST"])
#def Create():
    #return render_template('Create.html')

@app.route('/Login',methods=["GET",'POST'])
def Login():
        if request.method == 'GET':
            return render_template('Login.html')
        else:
            email = request.form.get('Email')
            password = request.form.get('Password')
            result = src.sys.login(email,password)
            if (result != None):
                session['email'] = result
                return redirect('/')
            else:
                return render_template('Login.html', ermsg = 'Login Failed!')


@app.route('/Logout')
def Logout():
    if 'email' in session:
        session['email'] = None
    return render_template('Login.html', ermsg = 'Logout successfully')


@app.route('/action_page.php',methods=["POST","GET"])
def select():
    # ingredients = {'ingredients':[]}
    # i=1
    # while(i<5):
    #     v = request.args.get(i)
    #     i+=1
    #     if(v==None): continue
    #     ingredients['ingredients'].append(v)

    ingredients = {'ingredients':None}
    v1 = request.args.get('v1')
    v2 = request.args.get('v2')
    v3 = request.args.get('v3')
    v4 = request.args.get('v4')
    v5 = request.args.get('v5')
    v6 = request.args.get('v6')
    v7 = request.args.get('v7')
    d1 = request.args.get('D1')
    d2 = request.args.get('D2')
    d3 = request.args.get('D3')
    d4 = request.args.get('D4')
    d5 = request.args.get('D5')
    d6 = request.args.get('D6')
    d7 = request.args.get('D7')
    d8 = request.args.get('D8')
    d9 = request.args.get('D9')
    d10 = request.args.get('D10')
    d11 = request.args.get('D11')
    d12 = request.args.get('D12')
    d13 = request.args.get('D13')
    d14 = request.args.get('D14')
    d15 = request.args.get('D15')
    d16 = request.args.get('D16')
    f1 = request.args.get('F1')
    f2 = request.args.get('F2')
    f3 = request.args.get('F3')
    f4 = request.args.get('F4')
    f5 = request.args.get('F5')
    f6 = request.args.get('F6')
    f7 = request.args.get('F7')
    f8 = request.args.get('F8')
    f9 = request.args.get('F9')
    f10 = request.args.get('F10')
    f11 = request.args.get('F11')
    f12 = request.args.get('F12')
    f13 = request.args.get('F13')
    f14 = request.args.get('F14')
    f15 = request.args.get('F15')
    m1 = request.args.get('M1')
    m2 = request.args.get('M2')
    m3 = request.args.get('M3')
    m4 = request.args.get('M4')
    m5 = request.args.get('M5')
    m6 = request.args.get('M6')
    m7 = request.args.get('M7')
    m8 = request.args.get('M8')
    m9 = request.args.get('M9')
    m10 = request.args.get('M10')
    m11 = request.args.get('M11')
    m12 = request.args.get('M12')
    m13 = request.args.get('M13')
    m14 = request.args.get('M14')
    m15 = request.args.get('M15')
    p1 = request.args.get('P1')
    p2 = request.args.get('P2')
    p3 = request.args.get('P3')
    p4 = request.args.get('P4')
    p5 = request.args.get('P5')
    p6 = request.args.get('P6')
    p7 = request.args.get('P7')
    p8 = request.args.get('P8')
    p9 = request.args.get('P9')
    p10 = request.args.get('P10')
    alist = []

    if v1!=None: alist.append(v1)
    if v2!=None: alist.append(v2)
    if v3!=None: alist.append(v3)
    if v4!=None: alist.append(v4)
    if v5!=None: alist.append(v5)
    if v6!=None: alist.append(v6)
    if v7!=None: alist.append(v7)
    if d1!=None: alist.append(d1)
    if d2!=None: alist.append(d2)
    if d3!=None: alist.append(d3)
    if d4!=None: alist.append(d4)
    if d5!=None: alist.append(d5)
    if d6!=None: alist.append(d6)
    if d7!=None: alist.append(d7)
    if d8!=None: alist.append(d8)
    if d9!=None: alist.append(d9)
    if d10!=None: alist.append(d10)
    if d11!=None: alist.append(d11)
    if d12!=None: alist.append(d12)
    if d13!=None: alist.append(d13)
    if d14!=None: alist.append(d14)
    if d15!=None: alist.append(d15)
    if d16!=None: alist.append(d16)
    if f1!=None: alist.append(f1)
    if f2!=None: alist.append(f2)
    if f3!=None: alist.append(f3)
    if f4!=None: alist.append(f4)
    if f5!=None: alist.append(f5)
    if f6!=None: alist.append(f6)
    if f7!=None: alist.append(f7)
    if f8!=None: alist.append(f8)
    if f9!=None: alist.append(f9)
    if f10!=None: alist.append(f10)
    if f11!=None: alist.append(f11)
    if f12!=None: alist.append(f12)
    if f13!=None: alist.append(f13)
    if f14!=None: alist.append(f14)
    if f15!=None: alist.append(f15)
    if m1!=None: alist.append(m1)
    if m2!=None: alist.append(m2)
    if m3!=None: alist.append(m3)
    if m4!=None: alist.append(m4)
    if m5!=None: alist.append(m5)
    if m6!=None: alist.append(m6)
    if m7!=None: alist.append(m7)
    if m8!=None: alist.append(m8)
    if m9!=None: alist.append(m9)
    if m10!=None: alist.append(m10)
    if m11!=None: alist.append(m11)
    if m12!=None: alist.append(m12)
    if m13!=None: alist.append(m13)
    if m14!=None: alist.append(m14)
    if m15!=None: alist.append(m15)
    if p1!=None: alist.append(p1)
    if p2!=None: alist.append(p2)
    if p3!=None: alist.append(p3)
    if p4!=None: alist.append(p4)
    if p5!=None: alist.append(p5)
    if p6!=None: alist.append(p6)
    if p7!=None: alist.append(p7)
    if p8!=None: alist.append(p8)
    if p9!=None: alist.append(p9)
    if p10!=None: alist.append(p10)

    ingredients['ingredients'] = alist
    result = src.sys.recipe(ingredients)
    return render_template('Recipe.html',result = result,alist = alist)

@app.route('/RecipeInformation',methods=["GET","POST"])
def Information():

    recipe = request.args.get('recipe')
    result = src.sys.getrecipebyname(recipe)
    return render_template('RecipeInformation.html',recipe=recipe,result=result)


@app.route('/add',methods=["POST","GET"])
def Create():
    #get recipe name
    name = request.args.get('name')
    #get meal type
    mtype = request.args.get('type')
    #get ingredients
    ingredients = {'ingredients':None}
    v1 = request.args.get('v1')
    v2 = request.args.get('v2')
    v3 = request.args.get('v3')
    v4 = request.args.get('v4')
    v5 = request.args.get('v5')
    v6 = request.args.get('v6')
    v7 = request.args.get('v7')
    d1 = request.args.get('D1')
    d2 = request.args.get('D2')
    d3 = request.args.get('D3')
    d4 = request.args.get('D4')
    d5 = request.args.get('D5')
    d6 = request.args.get('D6')
    d7 = request.args.get('D7')
    d8 = request.args.get('D8')
    d9 = request.args.get('D9')
    d10 = request.args.get('D10')
    d11 = request.args.get('D11')
    d12 = request.args.get('D12')
    d13 = request.args.get('D13')
    d14 = request.args.get('D14')
    d15 = request.args.get('D15')
    d16 = request.args.get('D16')
    f1 = request.args.get('F1')
    f2 = request.args.get('F2')
    f3 = request.args.get('F3')
    f4 = request.args.get('F4')
    f5 = request.args.get('F5')
    f6 = request.args.get('F6')
    f7 = request.args.get('F7')
    f8 = request.args.get('F8')
    f9 = request.args.get('F9')
    f10 = request.args.get('F10')
    f11 = request.args.get('F11')
    f12 = request.args.get('F12')
    f13 = request.args.get('F13')
    f14 = request.args.get('F14')
    f15 = request.args.get('F15')
    m1 = request.args.get('M1')
    m2 = request.args.get('M2')
    m3 = request.args.get('M3')
    m4 = request.args.get('M4')
    m5 = request.args.get('M5')
    m6 = request.args.get('M6')
    m7 = request.args.get('M7')
    m8 = request.args.get('M8')
    m9 = request.args.get('M9')
    m10 = request.args.get('M10')
    m11 = request.args.get('M11')
    m12 = request.args.get('M12')
    m13 = request.args.get('M13')
    m14 = request.args.get('M14')
    m15 = request.args.get('M15')
    p1 = request.args.get('P1')
    p2 = request.args.get('P2')
    p3 = request.args.get('P3')
    p4 = request.args.get('P4')
    p5 = request.args.get('P5')
    p6 = request.args.get('P6')
    p7 = request.args.get('P7')
    p8 = request.args.get('P8')
    p9 = request.args.get('P9')
    p10 = request.args.get('P10')
    alist = []

    if v1!=None: alist.append(v1)
    if v2!=None: alist.append(v2)
    if v3!=None: alist.append(v3)
    if v4!=None: alist.append(v4)
    if v5!=None: alist.append(v5)
    if v6!=None: alist.append(v6)
    if v7!=None: alist.append(v7)
    if d1!=None: alist.append(d1)
    if d2!=None: alist.append(d2)
    if d3!=None: alist.append(d3)
    if d4!=None: alist.append(d4)
    if d5!=None: alist.append(d5)
    if d6!=None: alist.append(d6)
    if d7!=None: alist.append(d7)
    if d8!=None: alist.append(d8)
    if d9!=None: alist.append(d9)
    if d10!=None: alist.append(d10)
    if d11!=None: alist.append(d11)
    if d12!=None: alist.append(d12)
    if d13!=None: alist.append(d13)
    if d14!=None: alist.append(d14)
    if d15!=None: alist.append(d15)
    if d16!=None: alist.append(d16)
    if f1!=None: alist.append(f1)
    if f2!=None: alist.append(f2)
    if f3!=None: alist.append(f3)
    if f4!=None: alist.append(f4)
    if f5!=None: alist.append(f5)
    if f6!=None: alist.append(f6)
    if f7!=None: alist.append(f7)
    if f8!=None: alist.append(f8)
    if f9!=None: alist.append(f9)
    if f10!=None: alist.append(f10)
    if f11!=None: alist.append(f11)
    if f12!=None: alist.append(f12)
    if f13!=None: alist.append(f13)
    if f14!=None: alist.append(f14)
    if f15!=None: alist.append(f15)
    if m1!=None: alist.append(m1)
    if m2!=None: alist.append(m2)
    if m3!=None: alist.append(m3)
    if m4!=None: alist.append(m4)
    if m5!=None: alist.append(m5)
    if m6!=None: alist.append(m6)
    if m7!=None: alist.append(m7)
    if m8!=None: alist.append(m8)
    if m9!=None: alist.append(m9)
    if m10!=None: alist.append(m10)
    if m11!=None: alist.append(m11)
    if m12!=None: alist.append(m12)
    if m13!=None: alist.append(m13)
    if m14!=None: alist.append(m14)
    if m15!=None: alist.append(m15)
    if p1!=None: alist.append(p1)
    if p2!=None: alist.append(p2)
    if p3!=None: alist.append(p3)
    if p4!=None: alist.append(p4)
    if p5!=None: alist.append(p5)
    if p6!=None: alist.append(p6)
    if p7!=None: alist.append(p7)
    if p8!=None: alist.append(p8)
    if p9!=None: alist.append(p9)
    if p10!=None: alist.append(p10)
    ingredients = " ".join(str(i) for i in alist)

    #get cooking time
    time = request.args.get('cooking_time')

    #get hints
    hints = request.args.get('hints')
    #get email
    email = session['email']
    #get url
    url = request.args.get('url')
    src.sys.addrecipe(name,mtype,ingredients,time,hints,email,url)
    result = src.sys.recommContributor()
    return render_template("Create.html",result = result)

@app.route('/myrecipe',methods=["POST","GET"])
def list():
    email = session['email']
    result = src.sys.getrecipe(email)
    mealname = request.args.get('mealtodel')
    src.sys.delete(mealname,email)
    result = src.sys.getrecipe(email)
    return render_template("list.html",result=result)

    # else:
    #     email = session['email']
    #     mealname = request.args.get('mealtodel')
    #     src.sys.delete(mealname,email)
    #     result = src.sys.getrecipe(email)
    #     return render_template("list.html",result=result)


# TEST1
@app.route('/reminder_e',methods=["POST","GET"])
def suggest():
    ingredients = request.args.get('ingredient')
    result = src.sys.recommExplorer(ingredients)
    return render_template("reminder_e.html",result=result)



# TEST2
@app.route('/reminder_c',methods=["POST","GET"])
def remind():
    r = src.sys.recommContributor()
    return r
