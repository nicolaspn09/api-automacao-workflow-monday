import requests
import json


def busca_informacoes_quadro():
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


def obter_id_coluna():
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


def insere_informacoes():
    api_key = 'REMOVED_FOR_GITHUB'
    board_id = 4859790701
    group_id = 'novo_grupo__1'

    url = 'https://api.monday.com/v2'
    headers = {'Authorization': api_key, 'Content-Type': 'application/json'}

    mutation = '''
    mutation ($boardId: ID!, $groupId: String!, $itemName: String!, $columnValues: JSON!) {
    create_item (board_id: $boardId, group_id: $groupId, item_name: $itemName, column_values: $columnValues) {
        id
    }
    }
    '''

    column_values = {
        'label__1': {"label": "RPA"},
        'text1': {"texto__1": "RPA"}, 
        'status': {"label": "Parado"}  # StatusColumn
    }

    # Convertendo diretamente no ponto de inserção para evitar conversões intermediárias
    variables = {
        'boardId': str(board_id),
        'groupId': group_id,
        'itemName': 'X-alface',
        'columnValues': json.dumps(column_values)  # Serialização direta
    }

    # Usando json para passar os dados diretamente, garantindo a formatação correta
    response = requests.post(url=url, json={
        'query': mutation,
        'variables': variables
    }, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        if 'errors' not in response_data:
            print('Novo item criado com sucesso.')
            print(response_data)
        else:
            print('Erro ao criar item:')
            print(response_data['errors'])
    else:
        print('Falha ao criar novo item:', response.text)


if __name__ == "__main__":
    busca_informacoes_quadro()
    #obter_id_coluna()
    #Oinsere_informacoes()