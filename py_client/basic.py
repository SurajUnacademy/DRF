import requests   # it does http request for us ( explaination 2. Rest Api)

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/"

# 1. requests.get() is the form of api which is in the library requests but its a actual method that's built into it ( this is just library api not rest api)
# ex: Phone -> camera -> every APP uses camera -> uses API -> to grab Camera

#2. Rest Api ->  they have to do with the internet more like web based api -> doesn't mean it has to go across internet but it going to use http request 
# http request -> HTML (get)
# Rest API http requests -> JSON (or xml) => meant basically software to communicate with not for humans ( no html to saw humans )


get_response = requests.post(endpoint, json = {"title": "Hello world", "content": "abc content"})
# print(get_response.text) #print raw text response (scrapped data using python requests)
# print(get_response.status_code)
print(get_response.json())

# JavaScript Object notation ~ python dictionary

