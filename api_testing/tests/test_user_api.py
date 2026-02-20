import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_all_users():
    url = f"{BASE_URL}/users"
    response = requests.get(url)
    print(response.status_code)

    data = response.json()

    for user in data:
        print(user["name"])

def test_create_user():
    url = f"{BASE_URL}/users"

    payload = {"name" : "Pavan", "email" : "pavan@test.com"}
    response = requests.post(url, json=payload)
    print(response.status_code)
    data = response.json()
    print(data)
    assert data["name"] == "Pavan"
    assert data["email"] == "pavan@test.com"
