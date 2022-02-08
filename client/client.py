import socket
import os

IP = socket.gethostbyname(socket.gethostname())
PORT = 7777
ADDRESS = (IP, PORT)
FORMAT = 'utf-8'
SIZE = 1000000


def create_connection():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        print(f'Tentando conexao com o servidor em {ADDRESS}...\n')
        client.connect(ADDRESS)
        print('Conectado!\n')
        return client
    except:
        print(f'Erro ao se conectar com o servidor em {ADDRESS}.\n')
        return -1


def send_file(client, filename):
    try:
        client.send(filename.encode(FORMAT))

        if(not os.path.isfile('./'+filename)):
            print('Arquivo nao existe.\n')
            client.send('-1'.encode(FORMAT))
            return "Arquivo não existente. Verifique se não há erro de digitação e se o arquivo se encontra na pasta."
        else:
            client.send(str(os.path.getsize('./'+filename)).encode(FORMAT))

        with open(filename, 'rb') as file:
            client.send(file.read())

        print(f'Dados de {filename} enviados.\n')
        return "Arquivo enviado com sucesso!"
    except:
        print('Erro ao enviar arquivo.\n')
        return "Erro ao enviar arquivo."


def get_file(client, filename):

    try:
        client.send(filename.encode(FORMAT))

        filesize = int(client.recv(SIZE).decode(FORMAT))

        if(filesize == -1):
            print('Arquivo nao existe.\n')
            return "Arquivo não existente no servidor. Verifique se não há erro de digitação. Utilize a função de listagem para saber os nomes dos arquivos."

        with open(filename, 'wb') as file:
            file.write(client.recv(filesize))

        print(f'Dados de {filename} recebidos.\n')
        return "Arquivo recebido com sucesso!"
    except:
        print('Erro ao receber arquivo.\n')
        return "Erro ao receber arquivo."
