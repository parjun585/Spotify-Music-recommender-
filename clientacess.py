import requests

# Spotify credentials
client_id = 'TYPE THE CLIENT ID'
client_secret = 'TYPE YOUR CLIENT SECRET GENERATED'

# Spotify token endpoint
url = 'https://accounts.spotify.com/api/token'

# Request payload and headers
data = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret
}

headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

# Sending the POST request to get the access token
response = requests.post(url, data=data, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    token = response.json().get('access_token')
    print(f"Access Token: {token}")
else:
    print(f"Failed to retrieve access token. Status code: {response.status_code}")
    print(response.json())
