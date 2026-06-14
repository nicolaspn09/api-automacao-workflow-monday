import requests
import json

api_key = 'REMOVED_FOR_GITHUB'  # Substitua pelo seu token de API
board_id = 4859790701  # Substitua pelo ID do quadro que você deseja consultar

url = 'https://api.monday.com/v2'
headers = {'Authorization': api_key, 'Content-Type': 'application/json'}

# Ajustado para o tipo de dado correto [ID!]
query = '''
query ($boardId: [ID!]) {
  boards(ids: $boardId) {
    columns {
      id
      title
      type
    }
  }
}
'''

variables = {'boardId': [str(board_id)]}  # Converte o ID do quadro para string antes de usar

response = requests.post(url=url, json={'query': query, 'variables': variables}, headers=headers)

if response.status_code == 200:
    print('Colunas do quadro:')
    columns = response.json()['data']['boards'][0]['columns']
    for column in columns:
        print(f"ID: {column['id']}, Título: {column['title']}, Tipo: {column['type']}")
else:
    print('Falha ao buscar informações sobre as colunas:', response.text)