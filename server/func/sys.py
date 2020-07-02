import re
import jwt
from . import data
def generate_uid():
    u_id = len(data.users) + 1
    return u_id;
def generate_token(u_id):
    token = jwt.encode({'u_id':u_id},data.secret,algorithm = 'HS256')
    token = bytes.decode(token)
    return token
def get_uid (email):
    for user in data.users:
        if data.users[user]['email'] == email:
            return data.users[user]['u_id']
def check_email(email):
    for user in data.users:
        if data.users[user]['email'] == email:
            return True
    return False
def check_password(email,password):
    for user in data.users:
        if data.users[user]['email'] == email:
            if data.users[user]['password'] == password:
                return True
    return False
def check_token(token):
    for i in data.active_tokens['token']:
        if i == token:
            return True
    return False
def sys_register(email,username,password):
    user_details = {
        'u_id' : None,
        'user_name' : None,
        'email' : None,
        'token': None,
        'logged' : None,
    }
    u_id = generate_uid()
    token = generate_token(u_id)
    user_details['u_id'] = u_id
    user_details['user_name'] = username
    user_details['email'] = email
    user_details['password'] = password
    user_details['token'] = token
    user_details['logged'] = False
    data.users[u_id] = user_details

    return{
        'u_id':u_id,
        'username':username,
        'email':email,
        'token':token

    }
def sys_login(email,password):
    for i in data.users:
        if data.users[i]['email'] == email and data.users[i]['logged'] == True:
            raise Exception('already login')


    if check_email(email) == False:
        raise ValueError ("email not belong to a user")
    elif check_password(email,password) == False:
        raise ValueError ("wrong password")

    u_id = get_uid(email)
    token = data.users[u_id]['token']
    data.users[u_id]['logged'] = True
    data.active_tokens['token'].append(token)
    result = 'login success'

    return{
        'u_id':u_id,
        'token':token,
        'logged':data.users[u_id]['logged'],
        'result':result
    }

def sys_logout(token):
    if check_token(token) == True:
        for user in data.users:
            if data.users[user]['token'] == token:
                data.users[user]['logged'] = False
        data.active_tokens['token'].remove(token)
        return True
    return False
