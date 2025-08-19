from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QFormLayout,
    QLineEdit, QTextEdit, QPushButton, QMessageBox
)
from PySide6.QtGui import QIcon
import sys
import first_step  # importa a função gerar_pdf do seu script

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Printaí 3D - Gerador de PDF")
        self.setWindowIcon(QIcon("fundo_branco.jpg"))  # logo no canto da janela
        self.setGeometry(400, 200, 800, 600)

        layout = QVBoxLayout()

        # Layout de formulário
        form_layout = QFormLayout()

        # Campos de entrada
        self.pecas = QLineEdit()
        self.arte_aplicada = QTextEdit()
        self.material = QLineEdit()
        self.cliente = QLineEdit()
        self.obs = QTextEdit()

        form_layout.addRow("Peças:", self.pecas)
        form_layout.addRow("Arte Aplicada:", self.arte_aplicada)
        form_layout.addRow("Material:", self.material)
        form_layout.addRow("Cliente:", self.cliente)
        form_layout.addRow("Observações:", self.obs)

        layout.addLayout(form_layout)

        # Botão para gerar PDF
        self.btn_gerar = QPushButton("Gerar PDF")
        self.btn_gerar.clicked.connect(self.gerar_pdf_action)
        layout.addWidget(self.btn_gerar)

        self.setLayout(layout)

    def gerar_pdf_action(self):
        try:
            # Pegando os valores da interface
            dados = {
                "pecas": self.pecas.text(),
                "arte_aplicada": self.arte_aplicada.toPlainText(),
                "material": self.material.text(),
                "cliente": self.cliente.text(),
                "obs": self.obs.toPlainText(),
                "logo": "fundo_branco.jpg"
            }

            # Chamando a função do first_step.py
            first_step.gerar_pdf(dados)

            QMessageBox.information(self, "Sucesso", "PDF gerado com sucesso!")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Falha ao gerar PDF:\n{str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
