import socket
from sqlite3 import connect
import os

IP = socket.gethostbyname(socket.gethostname())
PORT = 7777
ADDRESS = (IP, PORT)
FORMAT = 'utf-8'
SIZE = 1000000


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # af_inet = IPv4 / sock_stream = TCP 
        
    try:
        print('Servidor iniciando...\n')
        server.bind(ADDRESS)

        server.listen(1)
        print('Ouvindo por conexoes...\n')

        connection, addr = server.accept()
        print(f'Nova conexao em {addr}.\n')

    except:
        print(f'Erro ao se conectar com a porta {PORT}.\n')

    directory_files()
    recieve_file(connection)

    connection.close()

def recieve_file(connection):
    try:
        filename = connection.recv(SIZE).decode(FORMAT)

        ## nao sei se eh necessario
        connection.send('Nome do arquivo recebido pelo servidor.\n'.encode(FORMAT))

        with open(filename, 'wb') as file: 
            while 1:
                data = connection.recv(SIZE)
                if not data:
                    break
                file.write(data)

            print(f'Dados de {filename} recebidos.\n')
    except:
        print('Erro ao receber arquivo.\n')

def deliver_file(connection):
    try:
            
        filename = connection.recv(SIZE).decode(FORMAT)

        with open(filename, 'rb') as file:
                for data in file.readlines():
                    connection.send(data)

                print(f'Dados de {filename} enviados.\n')
    except:
        print('Erro ao enviar o arquivo.\n')

def directory_files():
    try:
        for root, dirs, files in os.walk('./'):
            if 'server.py' in files:
                files.remove('server.py')
            for name in files:
                print(name)
    except:
        print('Erro ao abrir a lista de arquivos disponíveis')


if __name__ == "__main__":
    main()