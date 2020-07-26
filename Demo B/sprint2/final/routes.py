from flask import render_template, request, redirect, url_for, abort, session
from server import app
import src.sys
'''
Main Pages
'''

@app.route('/',methods=["GET","POST"])
def home():
    email = request.args.get('email')
    password = request.args.get('password')
    print(email)
    print(password)
    return render_template('base.html')

@app.route('/Register',methods=["POST","GET"])
def Register():
    user_name = request.args.get('User_Name')
    email = request.args.get('Email')
    password = request.args.get('Password')
    src.sys.register(user_name,email,password)
    return render_template('Register.html')


@app.route('/page2',methods=["GET","POST"])
def page2():
    return render_template('page2.html')

@app.route('/Search',methods=["GET","POST"])
def Search():
    return render_template('search.html')

@app.route('/create',methods=["GET","POST"])
def Create():
    return render_template('Create.html')


@app.route('/Login',methods=["POST","GET"])
def Login():
    email = request.args.get('Email')
    password = request.args.get('Password')
    src.sys.login(email,password)
    return render_template('Login.html')

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
    d1 = request.args.get('D1')
    d2 = request.args.get('D2')
    d3 = request.args.get('D3')
    d4 = request.args.get('D4')
    d5 = request.args.get('D5')
    d6 = request.args.get('D6')
    d7 = request.args.get('D7')
    f1 = request.args.get('F1')
    f2 = request.args.get('F2')
    f3 = request.args.get('F3')
    m1 = request.args.get('M1')
    m2 = request.args.get('M2')
    m3 = request.args.get('M3')
    m4 = request.args.get('M4')
    m5 = request.args.get('M5')
    p1 = request.args.get('P1')
    p2 = request.args.get('P2')
    alist = []

    if v1!=None: alist.append(v1)
    if v2!=None: alist.append(v2)
    if v3!=None: alist.append(v3)
    if v4!=None: alist.append(v4)
    if d1!=None: alist.append(d1)
    if d2!=None: alist.append(d2)
    if d3!=None: alist.append(d3)
    if d4!=None: alist.append(d4)
    if d5!=None: alist.append(d5)
    if d6!=None: alist.append(d6)
    if d7!=None: alist.append(d7)
    if f1!=None: alist.append(f1)
    if f2!=None: alist.append(f2)
    if f3!=None: alist.append(f3)
    if m1!=None: alist.append(m1)
    if m2!=None: alist.append(m2)
    if m3!=None: alist.append(m3)
    if m4!=None: alist.append(m4)
    if m5!=None: alist.append(m5)
    if p1!=None: alist.append(p1)
    if p2!=None: alist.append(p2)


    ingredients['ingredients'] = alist
    result = src.sys.recipe(ingredients)
    return render_template('Recipe.html',result = result)
