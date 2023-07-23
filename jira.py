import base64
import requests

# Set up your credentials
user = 'ar.solutioner@gmail.com'
api_token = 'ATATT3xFfGF0wNTYnQDS41rli3fvF_rx1t0iu71t9GVix1eJe5ket6SsgBO5eUaw3V5SkqIZhsvKto7r80R_tFQJwHMLN12WoD9GSGhB5ALg-Se4kKduwzRNnIBR2FsfJbvkztbrnx9QsqZStNbS8H_z9Z3nJaDu6WP20Iv63VPDcMyCIInurEw=B6BA136E' # Replace this with your actual token
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
