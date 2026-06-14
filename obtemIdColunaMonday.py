import requests
import json

api_key = 'REMOVED_FOR_GITHUB'  # Substitua pelo seu token de API
board_id = 4859790701  # Substitua pelo ID do quadro que você deseja consultar

url = 'https://api.monday.com/v2'
headers = {'Authorization': api_key, 'Content-Type': 'application/json'}

query = '''
query ($boardId: ID!) {
  boards(ids: [$boardId]) {
    columns {
      id
      title
      type
    }
  }
}
'''

variables = {'boardId': str(board_id)}

response = requests.post(url=url, json={'query': query, 'variables': variables}, headers=headers)

if response.status_code == 200:
    response_data = response.json()
    print(json.dumps(response_data, indent=4))  # Print the full response data formatted
    
    # Extrair e imprimir os IDs e títulos das colunas
    columns = response_data.get('data', {}).get('boards', [])[0].get('columns', [])
    for column in columns:
        print(f"ID da Coluna: {column['id']}, Título: {column['title']}, Tipo: {column['type']}")
else:
    print('Falha ao buscar as colunas:', response.text)
