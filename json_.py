import json
# person={"name":"sudhanshu","age":30,}
# personJson=json.dumps(person,indent=4,sort_keys=True)
# print(personJson)

# with open('person.json','w')as file:
#     json.dump(person,file,indent=4)

# person=json.loads(personJson)
# print(person)

# with open('person.json','r')as file:
#     person=json.load(file)
#     print(person)

class User:
    def __init__(self,name,age):
        self.name=nameself.age=age

user=User('Max',27)

def encode_user(o):
    if isinstance(o,user):
        return {"User1":"hAihs"}