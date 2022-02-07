from asyncio.windows_events import NULL
import socket

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

        ## nao sei se eh necessario
        response = client.recv(SIZE).decode(FORMAT)

        if(response is NULL):
            print('Erro ao enviar nome do arquivo.\n')
            return
        else:
            print(response)

        with open(filename, 'rb') as file:
            for data in file.readlines():
                client.send(data)

            print(f'Dados de {filename} enviados.\n')
    except:
        print('Erro ao enviar arquivo.\n')


def get_file(client):
    filename = str(input('Insira o nome do arquivo: '))

    try:
        client.send(filename.encode(FORMAT))

        with open(filename, 'wb') as file:
            while 1:
                data = client.recv(SIZE)
                if not data:
                    break
                file.write(data)

            print(f'Dados de {filename} recebidos.\n')
    except:
        print('Erro ao receber arquivo.\n')

if __name__ == "__main__":
    main()