from bottle import error, get, run, request, redirect, static_file, post, view  
import uuid

items = [
    {"id":"c9cdddca-1b0f-4a05-99ce-c163e207447f", "name": "a", "price": 10},
    {"id":"63f67edc-cb82-4599-8176-0fb50c205b31", "name": "b", "price": 20},
    {"id":"fc3cf9aa-c938-4839-a86b-b464c981e8b8", "name": "c", "price": 30}
]

# must have an id and email
users = [
    {"id": "382983923", "email": "hello@yahoo.fr"}
]

####################################
#getting the css file 
@get("/app.css")
def _():
    return static_file("app.css", root=".")
####################################
@get("/")
@view("index")
def _():
    return
####################################
@get("/items")
@view("items")
def _():
    return dict(items=items)
####################################
@get("/signup")
@view("signup")
def _():
    return
####################################
@get("/login")
@view("login")
def _():
    return

####################################
@post("/delete-item")
def _():
    item_id = request.forms.get("item_id")
    for index, item in enumerate(items):
        if item['id'] == item_id:
            items.pop(index)
            return redirect("/items")
    return redirect("/items")


@post("/signup")
def _():
  user_id = str( uuid.uuid4() )
  user_email = request.forms.get("user_email")
  user = {"id":user_id, "email":user_email}
  users.append(user)

  # print("#"*30)
  # print( type(item_id) )

  return redirect("/users")

####################################
@get("/users")
@view("users")
def _():

    return dict(users=users)



####################################
@error(404)
@view("404")
def _(error):
    print(error)
    return




run(host="127.0.0.1", port=1111, debug=True, reloader=True, server="paste")