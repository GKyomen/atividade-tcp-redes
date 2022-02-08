import socket
import os

IP = socket.gethostbyname(socket.gethostname())
PORT = 7777
ADDRESS = (IP, PORT)
FORMAT = 'utf-8'
SIZE = 1000000

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        print(f'Tentando conexao com o servidor em {ADDRESS}...\n')
        client.connect(ADDRESS)
        print('Conectado!\n')
    except:
        print(f'Erro ao se conectar com o servidor em {ADDRESS}.\n')

    send_file(client)

    client.close()


def send_file(client):
    filename = str(input('Insira o nome do arquivo: '))

    try:
        client.send(filename.encode(FORMAT))

        if(not os.path.isfile('./'+filename)):
            print('Arquivo nao existe.\n')
            client.send('-1'.encode(FORMAT))
            return
        else:
            client.send(str(os.path.getsize('./'+filename)).encode(FORMAT))

        with open(filename, 'rb') as file:
            client.send(file.read())

        print(f'Dados de {filename} enviados.\n')
    except:
        print('Erro ao enviar arquivo.\n')


def get_file(client):
    filename = str(input('Insira o nome do arquivo: '))

    try:
        client.send(filename.encode(FORMAT))

        filesize = int(client.recv(SIZE).decode(FORMAT))

        if(filesize == -1):
            print('Arquivo nao existe.\n')
            return

        with open(filename, 'wb') as file:
            file.write(client.recv(filesize))

        print(f'Dados de {filename} recebidos.\n')
    except:
        print('Erro ao receber arquivo.\n')

if __name__ == "__main__":
    main()