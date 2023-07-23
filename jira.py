import base64
import requests

# Set up your credentials
user = 'ar.solutioner@gmail.com'
api_token = 'ATATT3xFfGF0yGS-A_Gn2HAnii-dcjH4ZMcHVcJVnF3vmI8mue8dO7R6aw9xWPeTsnpC599qa-slhk5Bh_6uXUk-2SUcQyG9fo1chgApe56ofgwY251NF7080JzHj0Wo3mcVCbjOZTMtzpoi0KlnvDE0JPPs7SZ9QyIRjgsHZdGDYglIUGwUT6E=97A1304A' # Replace this with your actual token
site = 'https://arsolutioner.atlassian.net'

# Encode the user:api_token to base64
credentials = base64.b64encode(f"{user}:{api_token}".encode()).decode()
print(credentials)

# Prepare headers for the request
headers = {
    'Authorization': f'Basic {credentials}',
    'Accept': 'application/json'
}

# Make a GET request to the Jira API
response = requests.get(f'{site}/rest/api/3/myself', headers=headers)

# Check if the request was successful
if response.status_code == 200:
    print("Request was successful. Here's the user info:")
    user_info = response.json()
    
    # Pretty print the JSON
    import json
    print(json.dumps(user_info, indent=4))
else:
    print(f"Request failed with status code: {response.status_code}")
