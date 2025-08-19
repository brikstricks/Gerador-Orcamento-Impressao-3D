from PySide6.QtWidgets import QApplication, QWidget, QLabel

# Criar a aplicação
app = QApplication([])

# Criar uma janela principal
janela = QWidget()
janela.setWindowTitle("Printaí")
janela.setGeometry(100, 100, 400, 300)  # posição x, y e tamanho w x h

# Adicionar um widget (ex.: label)
label = QLabel("Aqui é a Printaí", janela)
label.move(150, 130)  # posição do label dentro da janela

# Mostrar a janela
janela.show()

# Rodar o app
app.exec()
