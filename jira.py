import requests

# Set up your credentials
credentials = 'YXIuc29sdXRpb25lckBnbWFpbC5jb206QVRBVFQzeEZmR0YwWFNFLU9OU0lvODNjeDdNU1VkWVJTYjdBQ2I4Vkg1SHo2OTM3NHZqM1c2YXJ0eU5icnNGNl9ZaEZZaGhudU1Vb3VRMEVpTmU0MEppMEpjV1I3czdtRmZuYVhaUndJeF9fVXgxNXhtdDFxM1B5UmZDZzY5UUFtanBaNnNkNUVxLUN4MzAtcmYtQUJUMDhORk1ERFk1UGFIZUNIeDZLU2g2a3A5c3Rfb3hOQzVzPTg3RUU5RjIw'
site = 'https://appsflyer.atlassian.net'

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
