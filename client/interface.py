import client
import PySimpleGUI as sg
import os
import ntpath
sg.theme("DarkPurple7")


def pedir_arquivo():
    # ----------- Criando conexão -----------
    connection = client.create_connection()
    # ----------- Tela para pedir arquivos e tela de erro -----------
    layout = [
        [sg.Text("Digite o nome do arquivo no campo abaixo e confirme clicando no botão", expand_x=True)],
        [sg.InputText(expand_x=True, key="nome_arquivo")],
        [sg.Submit("Requisitar"), sg.Cancel("Cancelar")],
        [sg.Text("")],
        [sg.Text(key="resposta", size=(40, 0), justification='center')]
    ]

    err_layout = [
        [sg.Text("Houve um problema ao tentar conectar com o servidor :C")],
        [sg.Button("Voltar")]
    ]

    # ----------- Criando janela para requisitar arquivos -----------
    if (connection == -1):
        tela = err_layout
    else:
        tela = layout
    window = sg.Window("Requisitar arquivo", tela, size=(
        500, 400), element_justification="c")

    # ----------- Manipulador de eventos -----------
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cancelar" or event == "Voltar":
            break
        elif event == "Requisitar":
            nome = values["nome_arquivo"]
            if (nome == ""):
                window["resposta"].update("preencha o campo antes do envio")
            else:
                retorno = client.get_file(connection, nome)
                window["resposta"].update(retorno)
    client.end_connection(connection)
    window.close()


def listar_arquivos():
    # ----------- Criando conexão e pedindo lista de arquivos -----------
    connection = client.create_connection()
    if (connection != -1):
        lista = client.get_directory(connection)
    # ----------- Tela de erro se deu algum problema -----------
    if (connection == -1 or lista == -1):
        err_layout = [
            [sg.Text("Houve um problema ao tentar conectar com o servidor :C")],
            [sg.Button("Voltar")]
        ]
        window = sg.Window("Lista de arquivos", err_layout, size=(
            500, 400), element_justification="c")
    else:
        # ----------- Criando janela para listar arquivos -----------
        layoutLista = [
            [sg.Text(
                "Aqui estão os nomes de todos os arquivos no sevidor", expand_x=True)]

        ]
        layoutLista += [[sg.Text(f"{nome}")] for nome in lista]
        layoutLista += [[sg.Button("Voltar")]]
        layoutListaVazia = [
            [sg.Text("Não há arquivos no servidor nesse momento", expand_x=True)],
            [sg.Button("Voltar")]
        ]

        if (len(lista) == 0):
            tela = layoutListaVazia
        else:
            tela = layoutLista
        window = sg.Window("Lista de arquivos", tela, size=(
            500, 400), element_justification="c")

    # ----------- Manipulador de eventos -----------
    while True:
        event, _ = window.read()
        if event == sg.WIN_CLOSED or event == "Voltar":
            break
    client.end_connection(connection)
    window.close()


def enviar_arquivo():
    # ----------- Criando conexão -----------
    connection = client.create_connection()
    # ----------- Tela para enviar arquivos -----------
    layout = [
        [sg.Text("Selecione o arquivo a ser enviado", expand_x=True)],
        [sg.FileBrowse("Selecionar", key="seletor",
                       change_submits=True, initial_folder=os.getcwd())],
        [sg.Text(key="nome_arquivo")],
        [sg.Button("Enviar"), sg.Button("Cancelar")],
        [sg.Text(key="resposta", size=(40, 0), justification='center')]
    ]

    err_layout = [
        [sg.Text("Houve um problema ao tentar conectar com o servidor :C")],
        [sg.Button("Voltar")]
    ]

    # ----------- Criando janela para enviar arquivos -----------
    if (connection == -1):
        tela = err_layout
    else:
        tela = layout
    window = sg.Window("Enviar arquivo", tela, size=(
        500, 400), element_justification="c")

    # ----------- Manipulador de eventos -----------
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cancelar":
            break
        elif event == "seletor":
            _, tail = ntpath.split(values["seletor"])
            window["nome_arquivo"].update(tail)
        elif event == "Enviar":
            nome_arquivo = values["seletor"]
            if (nome_arquivo == ""):
                window["nome_arquivo"].update(
                    "Antes, selecione um arquivo para enviar")
            else:
                _, tail = ntpath.split(values["seletor"])
                print(f"aqui\n{tail}")
                retorno = client.send_file(connection, tail)
                window["resposta"].update(retorno)
    window.close()


def main():
    # ----------- Telas do client principal -----------
    telaBoasVindas = [
        [sg.Text("Boas-vindas!")],
        [sg.Text("")],
        [sg.Text(
            "Esta é uma aplicação client feita para um servidor TCP para a atividade")],
        [sg.Text("da disciplina Redes de Computadores.")],
        [sg.Text("Atualmente, você está no menu principal.")],
        [sg.Text("Utilize os botões na parte inferior da janela para navegar pela aplicação.",
                 (60, None), justification="center")],
        *[[sg.Text("")] for _ in range(5)]
    ]

    telaFuncionalidades = [
        [sg.Text(
            "Basta clicar em um dos botões abaixo para abrir a tela da funcionalidade.\n\n")],
        [sg.Button("Requisitar arquivo", size=(
            20, 1), auto_size_button=False)],
        [sg.Button("Listar arquivos", size=(20, 1), auto_size_button=False)],
        [sg.Button("Transferir arquivo", size=(
            20, 1), auto_size_button=False)],
        *[[sg.Text("")] for _ in range(5)]
    ]

    telaCreditos = [
        [sg.Text("_"*20), sg.Text("Feito por: "), sg.Text("_"*20)],
        [sg.Text("")],
        [sg.Text("Nome:", (30, 1)), sg.Text("RA:", (6, 1))],
        [sg.Text("Gabriel da Silva Kyomen", (30, 1)),
         sg.Text("771008", (6, 1))],
        [sg.Text("Guilherme Milani de Oliveira", (30, 1)),
         sg.Text("771016", (6, 1))],
        [sg.Text("Marcos Antônio de Santana Júnior", (30, 1)),
         sg.Text("771040", (6, 1))],
        *[[sg.Text("")] for _ in range(5)]
    ]

    # ----------- Layout da janela principal -----------
    layout = [
        [sg.Column(telaBoasVindas, key="-COL1-", expand_x=True, element_justification="center"),
         sg.Column(telaFuncionalidades, visible=False, key="-COL2-",
                   expand_x=True, element_justification="center"),
         sg.Column(telaCreditos, visible=False, key="-COL3-", expand_x=True, element_justification="center")],
        [sg.Button("Tela inicial"),
         sg.Button("Funcionalidades"),
         sg.Button("Créditos")],
        [sg.Button("Fechar", button_color=("white", "red"))]
    ]

    # ----------- Criando janela principal -----------
    window = sg.Window("Client TCP", layout, size=(
        500, 400), element_justification="c")

    # ----------- Manipulador de eventos -----------
    layout = 1
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Fechar":
            break
        elif event == "Tela inicial":
            window[f"-COL{layout}-"].update(visible=False)
            layout = 1
            window[f"-COL{layout}-"].update(visible=True)
        elif event == "Funcionalidades":
            window[f"-COL{layout}-"].update(visible=False)
            layout = 2
            window[f"-COL{layout}-"].update(visible=True)
        elif event == "Créditos":
            window[f"-COL{layout}-"].update(visible=False)
            layout = 3
            window[f"-COL{layout}-"].update(visible=True)
        elif event == "Requisitar arquivo":
            pedir_arquivo()
        elif event == "Listar arquivos":
            listar_arquivos()
        elif event == "Transferir arquivo":
            enviar_arquivo()
    window.close()


if __name__ == "__main__":
    main()
