import requests


BASE = "http://127.0.0.1:5000/"


testdata = [{"name": "Joe Schmoe", "email_address": "joeschmoe@gmail.com", "password": "XcT00y4W"},
{"name": "Billy Bob Thornton", "email_address": "bobthebuilder22@gmail.com", "password": "willybobthornton"},
{"name": "Shawn Don", "email_address": "smcginester@gmail.com", "password": "newpassword"}]


for i in range(len(testdata)):
    response = requests.put(BASE + "helloworld/" + str(i), testdata[i])
    print(response.json())

input()
response = requests.get(BASE + "helloworld/17")
print(response.json())

input()
response = requests.delete(BASE + "helloworld/0")
print(response)
