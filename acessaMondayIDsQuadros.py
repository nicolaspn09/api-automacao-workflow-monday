import requests

api_key = 'REMOVED_FOR_GITHUB'

url = 'https://api.monday.com/v2'
headers = {'Authorization': api_key, 'Content-Type': 'application/json'}

query = '''
{
  boards(limit: 10000) {
    id
    name
  }
}
'''

response = requests.post(url=url, json={'query': query}, headers=headers)

if response.status_code == 200:
    boards = response.json()['data']['boards']
    for board in boards:
        print(f"ID: {board['id']}, Nome: {board['name']}")
else:
    print('Falha ao buscar os quadros:', response.text)