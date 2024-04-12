
import requests

# Define the endpoint URL
url = "https://api.devrev.ai/works.create"

# Define the headers
headers = {
    "Authorization": "eyJhbGciOiJSUzI1NiIsImlzcyI6Imh0dHBzOi8vYXV0aC10b2tlbi5kZXZyZXYuYWkvIiwia2lkIjoic3RzX2tpZF9yc2EiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOlsiamFudXMiXSwiYXpwIjoiZG9uOmlkZW50aXR5OmR2cnYtdXMtMTpkZXZvLzFjcVlsVVZxZGQ6ZGV2dS8xIiwiZXhwIjoxNzQ0NDEwNDc3LCJodHRwOi8vZGV2cmV2LmFpL2F1dGgwX3VpZCI6ImRvbjppZGVudGl0eTpkdnJ2LXVzLTE6ZGV2by9zdXBlcjphdXRoMF91c2VyL29pZGN8cGFzc3dvcmRsZXNzfGVtYWlsfDY2MTc4MjYzYWUzNGQ1MDRjZmJkYzBlMyIsImh0dHA6Ly9kZXZyZXYuYWkvYXV0aDBfdXNlcl9pZCI6Im9pZGN8cGFzc3dvcmRsZXNzfGVtYWlsfDY2MTc4MjYzYWUzNGQ1MDRjZmJkYzBlMyIsImh0dHA6Ly9kZXZyZXYuYWkvZGV2b19kb24iOiJkb246aWRlbnRpdHk6ZHZydi11cy0xOmRldm8vMWNxWWxVVnFkZCIsImh0dHA6Ly9kZXZyZXYuYWkvZGV2b2lkIjoiREVWLTFjcVlsVVZxZGQiLCJodHRwOi8vZGV2cmV2LmFpL2RldnVpZCI6IkRFVlUtMSIsImh0dHA6Ly9kZXZyZXYuYWkvZGlzcGxheW5hbWUiOiI0bm0yMGlzMDQ2IiwiaHR0cDovL2RldnJldi5haS9lbWFpbCI6IjRubTIwaXMwNDZAbm1hbWl0LmluIiwiaHR0cDovL2RldnJldi5haS9mdWxsbmFtZSI6IjRubTIwaXMwNDZAbm1hbWl0LmluIiwiaHR0cDovL2RldnJldi5haS9pc192ZXJpZmllZCI6dHJ1ZSwiaHR0cDovL2RldnJldi5haS90b2tlbnR5cGUiOiJ1cm46ZGV2cmV2OnBhcmFtczpvYXV0aDp0b2tlbi10eXBlOnBhdCIsImlhdCI6MTcxMjg3NDQ3NywiaXNzIjoiaHR0cHM6Ly9hdXRoLXRva2VuLmRldnJldi5haS8iLCJqdGkiOiJkb246aWRlbnRpdHk6ZHZydi11cy0xOmRldm8vMWNxWWxVVnFkZDp0b2tlbi8xMUh0NWt1cXkiLCJvcmdfaWQiOiJvcmdfbXhUQ3p4bTFkNm1NZkJFWiIsInN1YiI6ImRvbjppZGVudGl0eTpkdnJ2LXVzLTE6ZGV2by8xY3FZbFVWcWRkOmRldnUvMSJ9.ghCGSwxKi00BnyUdq7l2_gDSuc58eEsSwjF5dpYv7PZE8R7Q38UB-W69KGz6K1c6a9wlAErliUZ9RhHhAaU88GWqP51GifaUFVRin3Lhe19VqkhZHgsWyOZmqytLedGqKhC8Yya-ZVqxdpkh-vok1-K-f-zQzAmSq4zf9hH0uYIfz6ZzQW6DvnVUfl6vHct9sswn5X7PkR0fnKyMGdj0LD_dTgj0p8WH74932M0O4_itmw4v2YcOJvTp333K63-TMNN_8MKtRduS85cKWfO8_Hg-sFuHo1GpwZ_1xCIIA_-NqR3Yolq4K9EzC4cfaNqCyTNcF9IjtZiWziP7hQSxaA",
    "Content-Type": "application/json"
}

# Define the payload for creating an issue
payload = {
    "type": "ticket",
    "applies_to_part": "PROD-1",
    "owned_by": ["DEVU-1"],
    "title": "My DevRev Ticket"
}

# Make the POST request to create the issue
response = requests.post(url, json=payload, headers=headers)

# Check the response
if response.status_code == 201:
    print("Ticket created successfully!")
    print("Response:", response.json())  # Print the response JSON
else:
    print("Failed to create ticket. Status code:", response.status_code)
    print("Error message:", response.text)