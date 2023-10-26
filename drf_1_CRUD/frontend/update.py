import requests

product_id = input("Enter the post id \n")

endpoint = f"http://127.0.0.1:8000/posts/update/{product_id}/"

data = {
    "title":"Hello world my old friend 1",
    "content":"my content",
 
}

get_response = requests.put(endpoint, json=data)
print(get_response.json())
