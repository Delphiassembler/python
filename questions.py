import requests
for value in range (4):

  response = requests.get('https://nmap.org/')
  response1 = requests.get('https://google.com/')
  response2 = requests.get('https://duckduckgo.com/')
  response3 = requests.get('https://www.ixquick.com/')
  response4 = requests.get('https://ya.ru/')
  values = [response, response1, response2, response3, response4]
  for value in values:
    print(response.status_code)
