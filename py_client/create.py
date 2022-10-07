import requests

endpoint = 'http://127.0.0.1:8000/api/products/'

data = {
    "title": "This field is done",
    "content": "I was welcomed to the Turing Committee through a welcome call by Blessing Akubude.I was taken through "
               "a general overview of Turing and how the training phase works. ",

}
get_response = requests.post(endpoint, json=data)
print(get_response.json())

