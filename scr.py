import requests
#https://i.screenshotbin.com/i/1b2e05c8ca53419bb5341085b5591618.png
URL='andypi.co.uk'
#API_KEY='41dsithyeg6287szyiqi4bzyx0a0g0mp'

response = requests.post(
    "https://api.screenshotbin.com/v1/screenshot",
    auth=(API_KEY, ''),
    json={'url': URL}
)

print(response.json().get('url'))