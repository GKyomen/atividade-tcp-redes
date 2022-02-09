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


    except:
        print(f'Erro ao se conectar com a porta {PORT}.\n')

    while(True):
        connection, addr = server.accept()
        print(f'Nova conexao em {addr}.\n')

        request = connection.recv(SIZE).decode(FORMAT)

        if(request == 'send'):
            recieve_file(connection)
        elif(request == 'get'):
            deliver_file(connection)
        elif(request == 'directory'):
            directory_files(connection)

    connection.close()

def recieve_file(connection):
    try:
        filename = connection.recv(SIZE).decode(FORMAT)

        filesize = int(connection.recv(SIZE).decode(FORMAT))

        if(filesize == -1):
            print('Arquivo nao existe.\n')
            return

        with open('./server/'+filename, 'wb') as file:
            file.write(connection.recv(filesize))

        print(f'Dados de {filename} recebidos.\n')
    except:
        print('Erro ao receber arquivo.\n')

def deliver_file(connection):
    try:
            
        filename = connection.recv(SIZE).decode(FORMAT)

        if(not os.path.isfile('./'+filename)):
            print('Arquivo nao existe.\n')
            connection.send('-1'.encode(FORMAT))
            return
        else:
            connection.send(str(os.path.getsize('./'+filename)).encode(FORMAT))

        with open(filename, 'rb') as file:
            connection.send(file.read())

        print(f'Dados de {filename} enviados.\n')
    except:
        print('Erro ao enviar o arquivo.\n')

def directory_files(connection):
    try:
        for root, dirs, files in os.walk('./'):
            if 'server.py' in files:
                files.remove('server.py')
            directory_list = []
            for file in files:
                directory_list.append(file)
            directory_list = str(directory_list)
            directory_list = directory_list.encode(FORMAT)
            connection.send(directory_list)
    except:
        print('Erro ao abrir a lista de arquivos disponíveis.')


if __name__ == "__main__":
    main()