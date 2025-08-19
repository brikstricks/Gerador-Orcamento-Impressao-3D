from fpdf import FPDF
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QTextEdit

def gerar_pdf(titulo, arte, peca, filamento, tempo):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Orçamento Printaí 3D", ln=1, align="C")

    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"Título: {titulo}", ln=1)
    pdf.cell(0, 10, f"Arte aplicada: {arte}", ln=1)
    pdf.cell(0, 10, f"Peça: {peca}", ln=1)
    pdf.cell(0, 10, f"Filamento: {filamento}", ln=1)
    pdf.cell(0, 10, f"Tempo: {tempo}", ln=1)

    pdf.output("orcamento_interface.pdf")


def gerar_pdf_gui():
    titulo = titulo_input.text()
    arte = arte_input.text()
    peca = peca_input.text()
    filamento = filamento_input.text()
    tempo = tempo_input.text()

    # Exibe no resumo
    resumo.setText(
        f"Título: {titulo}\n"
        f"Arte aplicada: {arte}\n"
        f"Peça: {peca}\n"
        f"Filamento: {filamento}\n"
        f"Tempo: {tempo}\n\n"
        f"✅ PDF Gerado: orcamento_interface.pdf"
    )

    # Gera o PDF real
    gerar_pdf(titulo, arte, peca, filamento, tempo)


# Criar a aplicação
app = QApplication([])

# Janela Principal
window = QWidget()
window.setWindowTitle("Orçamentos Printaí 3D")
window.setGeometry(400, 200, 800, 600)

# Layout vertical
layout = QVBoxLayout()

# Inputs
titulo_input = QLineEdit()
titulo_input.setPlaceholderText("Título do Projeto")
layout.addWidget(titulo_input)

arte_input = QLineEdit()
arte_input.setPlaceholderText("Valor da Arte")
layout.addWidget(arte_input)

peca_input = QLineEdit()
peca_input.setPlaceholderText("Nome da Peça")
layout.addWidget(peca_input)

filamento_input = QLineEdit()
filamento_input.setPlaceholderText("Tipo/Cor do Filamento")
layout.addWidget(filamento_input)

tempo_input = QLineEdit()
tempo_input.setPlaceholderText("Tempo de Impressão")
layout.addWidget(tempo_input)

# Campo para resumo
resumo = QTextEdit()
resumo.setReadOnly(True)
layout.addWidget(resumo)

# Botão
botao_gerar = QPushButton("Gerar PDF")
botao_gerar.clicked.connect(gerar_pdf_gui)
layout.addWidget(botao_gerar)

# Aplicar layout e mostrar janela
window.setLayout(layout)
window.show()

# Rodar aplicação
app.exec()
