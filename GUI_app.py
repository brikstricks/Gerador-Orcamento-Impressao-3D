# Iniciando o aplicativo
from PySide6.QtWidgets import QApplication, QWidget, QVBoxlayout, QLineEdit, QPushButton, QTextEdit, QLabel

# Função que será chamada ao clicar no botão

def gerar_pdf_gui():
    titulo = titulo_input.text()
    arte = arte_input.text()
    resumo.setText(f"Título: {titulo}\nArte aplicada: {arte}\n(PDF ainda não gerado)")

#Criar a aplicação
app = QApplication([])

#Janela Principal
window = QWidget()
window.setWindowTitle("Orcamentos Printaí 3D")
window.setGeometry(300, 300, 600, 500) # posição e tamanho da janela

#Layout vertical
layout = QVBoxlayout()

#Campo valor da arte aplicada
