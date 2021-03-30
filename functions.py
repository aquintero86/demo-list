import json
from sqlalchemy import inspect, and_
from model import User

#convert the object to a list
def query_row(ob):
    item_list = []   
    for item in ob:
            new_item = {c.key: getattr(item, c.key) for c in inspect(item).mapper.column_attrs}
            new_item = json.dumps(new_item)
            new_item = json.loads(new_item)
            item_list.append(new_item)  
    return item_list


#function that validates the POST parameters
def query_obj(data):
    firstName = data.get("firstName",None)
    lastName = data.get("lastName",None) 
    email = data.get("email",None) 
    print(firstName)
    print(lastName)
    print(email)
    #validate if all variables comes with values
    if firstName is not None and firstName != '' and lastName is not None and lastName != '' and email is not None and email != '':
        ob = User.query.filter(and_(User.first_name == firstName, User.last_name == lastName, User.email == email)).\
        limit(data['row']).offset((data['num_page'] - 1) *data['row']) 
    #validate if only firstName comes with values                     
    elif firstName is not None and firstName != '':
        ob = User.query.filter(User.first_name.like('%'+ firstName+'%')).limit(data['row']).offset((data['num_page'] - 1) *data['row'])
     #validate if only lastname comes with values 
    elif lastName is not None and lastName != '':
        ob = User.query.filter(User.last_name.like('%'+ lastName+'%')).limit(data['row']).offset((data['num_page'] - 1) *data['row'])
     #validate if only email comes with values 
    elif email is not None and email != '':
        ob = User.query.filter(User.email.like('%'+ email+'%')).limit(data['row']).offset((data['num_page'] - 1) *data['row'])    
    else :
        ob = User.query.limit(data['row']).offset((data['num_page'] - 1) *data['row'])
        
    return ob