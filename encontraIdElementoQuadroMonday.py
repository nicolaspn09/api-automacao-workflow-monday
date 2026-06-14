import requests
import json

api_key = 'REMOVED_FOR_GITHUB'  # Substitua pelo seu token de API
board_id = 4859790701  # Substitua pelo ID do quadro que você deseja consultar

url = 'https://api.monday.com/v2'
headers = {'Authorization': api_key, 'Content-Type': 'application/json'}

query = '''
query ($boardId: [ID!]) {
  boards(ids: $boardId) {
    id
    name
    groups {
      id
      title
    }
  }
}
'''

variables = {'boardId': [str(board_id)]}

response = requests.post(url=url, json={'query': query, 'variables': variables}, headers=headers)

if response.status_code == 200:
    response_data = response.json()
    print(json.dumps(response_data, indent=4))

    boards = response_data.get('data', {}).get('boards', [])
    if not boards:
        print("Nenhum quadro foi encontrado com o ID fornecido.")
    else:
        for board in boards:
            print(f"Quadro: {board['name']} (ID: {board['id']})")
            for group in board.get('groups', []):
                print(f"  Grupo: {group['title']} (ID: {group['id']})")
else:
    print('Falha ao buscar informações:', response.status_code, response.text)