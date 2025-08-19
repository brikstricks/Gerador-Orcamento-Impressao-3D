# Iniciando o aplicativo
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QTextEdit, QLabel

# Função que será chamada ao clicar no botão

def gerar_pdf_gui():
    titulo = titulo_input.text()
    arte = arte_input.text()
    peca = peca_input.text()
    filamento = filamento_input.text()
    tempo = tempo_input.text()

    resumo.setText(f"Título: {titulo}\nArte aplicada: {arte}\nNome da peça: {peca}\nTipo Filamento/Cor: {filamento}\nTempo de impressão: {tempo}\n(PDF ainda não gerado)")

#Criar a aplicação
app = QApplication([])

#Janela Principal
window = QWidget()
window.setWindowTitle("Orcamentos Printaí 3D")
window.setGeometry(300, 300, 600, 500) # posição e tamanho da janela

#Layout vertical
layout = QVBoxLayout()

#Campo de Título do projeto
titulo_input = QLineEdit()
titulo_input.setPlaceholderText("Título do Projeto")
layout.addWidget(titulo_input)

#campo valor de arte aplicada
arte_input = QLineEdit()
arte_input.setPlaceholderText("Valor da Arte")
layout.addWidget(arte_input)

#campo valor de arte aplicada
peca_input = QLineEdit()
peca_input.setPlaceholderText("Nome da Peça")
layout.addWidget(peca_input)

#campo valor de arte aplicada
filamento_input = QLineEdit()
filamento_input.setPlaceholderText("Tipo/Cor do Filamento")
layout.addWidget(filamento_input)

#campo valor de arte aplicada
tempo_input = QLineEdit()
tempo_input.setPlaceholderText("Tempo de Impressão")
layout.addWidget(tempo_input)

#Campo para exibir resumo/interações
resumo = QTextEdit()
resumo.setReadOnly(True)
layout.addWidget(resumo)

#Botão para gerar PDF
botao_gerar = QPushButton("Gerar PDF")
botao_gerar.clicked.connect(gerar_pdf_gui)
layout.addWidget(botao_gerar)

#Aplicar layout e mostrar janela
window.setLayout(layout)
window.show()

#Rodar aplicação
app.exec()

