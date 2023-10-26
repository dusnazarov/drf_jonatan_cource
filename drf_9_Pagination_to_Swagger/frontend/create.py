import requests

endpoint = "http://127.0.0.1:8000/posts/create/"

data = {
    "title":"This field is done",
    "content":"my content is created",
    
}

get_response = requests.post(endpoint, json=data)
print(get_response.json())