from bottle import run, get, response, request, post, delete, put
import json
import uuid # 1 billion per second will take 200
import re

items = [
  {"id":"1", "name":"a"},
  {"id":"2", "name":"b"},
  {"id":"3", "name":"c"}
]

##############################
# decorator
@get("/")
def _():
  return "Home"

@get("/test")
def _():
  user_name = "Elisha"
  if not re.match("^[a-zA-Z]*$", user_name):
    return "not a valid name"
  return "congrats valid name"


  # user_phone = "02345678"
  # if not re.match("^[1-9][0-9]{7}$", user_phone):  # true or false // ^starts - $ends
  #   return "not a valid phone" 
  # return "congrats valid phone"





##############################
@get("/items")
# @get("/items/")
def _():
  response.content_type = "application/json; charset: UTF-8"
  return json.dumps(items)
  # return str(items)

##############################
@get("/items/<item_id>")
def _(item_id):
  
  # VALIDATION
  if not item_id:
    response.status = 400
    return "item_id is missing"

  for item in items:
    if item["id"] == item_id:
      return item

  response.status = 400    
  return "Item not found"




##############################7
# Query strings
# Every other variable after the 1st one start with & (ampersant)
# 127.0.0.1:4444/test?id=1&name=a
# from postman pass the following variables to the server via 
# Query String      year, school-name, age
# The server will reply with this:
# Hi, you are at KEA. The year is 2022 and you are 20 years old
#                ___              ____             __

#Frindly URL
# @get("/test")
# def _():
#   year = request.params.get("year")
#   school_name = request.params.get("school-name") 
#   age = request.params.get("age") 
#   return f"Hi year: {year} school name: {school_name} age: {age}"

##############################
# 127.0.0.1:4444/friendly/brand/xxxx/color/xxx
@get("/friendly/brand/<brand_name>/color/<item_color>")
def _(brand_name, item_color):
  return f"You brand: {brand_name} color is: {item_color}"



##############################
@post("/items")
def update_item():

  # VALIDATION
  if not request.forms.get("item_name"):
    response.status = 400
    return "item_name is missing"
  if len(request.forms.get("item_name")) < 2:
    response.status = 400
    return "item_name must be at least 2 characters"
  if len(request.forms.get("item_name")) > 20:
    response.status = 400
    return "item_name must be less than 20 characters"

  item_id = str( uuid.uuid4() )
  item_name = request.forms.get("item_name")
  item_price = request.forms.get("item_price")
  item = {"id":item_id, "name":item_name, "item_price": item_price}
  items.append(item)

  # print("#"*30)
  # print( type(item_id) )
  return item


# ##############################
# @delete("/items/<item_id>")
# def _(item_id):
#   # VALIDATE
#   for item in items:
#     if item["id"] == item_id:
#       items.pop()
#       return "item deleted"

#   # No item found
#   return "item not found"

##############################
@delete("/items/<item_id>")
def _(item_id):
  #VALIDATION
  # for item in items:
  #   item = [item for item in items if item['id'] == item_id]
  #   if item:
  #     items.remove(item[0])
  #     return f'An element with an id: "{item_id}" was deleted!'
  # #No item found
  #   return f'Ooops no element found with id: "{item_id}"!'

#Delete with enumerate function
  for index, item in enumerate(items):
    if item['id'] == item_id:
      items.pop(index)
      return 'item deleted'

  return 'item not found'

##############################
      

##############################
#KWARGS
# ports 0 to 65535
# ports 0 to 1024 are reserved
run(host="127.0.0.1", port=4444, debug=True, reloader=True)







