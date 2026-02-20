import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)
print(response.status_code)

data = response.json()
print(data[0]["id"])

for users in data:
    print(users["name"], "->", users["email"])
    print(users["username"])