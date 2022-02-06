import PySimpleGUI as sg
sg.theme("DarkPurple7")


def pedir_arquivo():
    # ----------- Tela para pedir arquivos -----------
    layout = [
        [sg.Text("Digite o nome do arquivo no campo abaixo e confirme clicando no botão", expand_x=True)],
        [sg.InputText(expand_x=True)],
        [sg.Submit("Requisitar"), sg.Cancel("Cancelar")]
    ]

    # ----------- Criando janela para requisitar arquivos -----------
    window = sg.Window("Requisitar arquivo", layout, size=(
        500, 400), element_justification="c")

    # ----------- Manipulador de eventos -----------
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cancelar":
            break
        if event == "Requisitar":
            print("faz alguma coisa")
    window.close()


def listar_arquivos():
    # ----------- Tela para pedir arquivos -----------
    layout = [
        [sg.Text("Aqui estão os nomes de todos os arquivos no sevidor", expand_x=True)],
        # Colocar a lista de arquivos aqui
        [sg.Button("Voltar")]
    ]

    # ----------- Criando janela para requisitar arquivos -----------
    window = sg.Window("Lista de arquivos", layout, size=(
        500, 400), element_justification="c")

    # ----------- Manipulador de eventos -----------
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Voltar":
            break
    window.close()


def enviar_arquivo():
    # ----------- Tela para pedir arquivos -----------
    layout = [
        [sg.Text("Selecione o arquivo a ser enviado", expand_x=True)],
        [sg.FileBrowse("Selecionar")],
        # Nome do arquivo aqui
        [sg.Button("Enviar"), sg.Button("Cancelar")]
    ]

    # ----------- Criando janela para requisitar arquivos -----------
    window = sg.Window("Enviar arquivo", layout, size=(
        500, 400), element_justification="c")

    # ----------- Manipulador de eventos -----------
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cancelar":
            break
        if event == "Enviar":
            print("faz algo")
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