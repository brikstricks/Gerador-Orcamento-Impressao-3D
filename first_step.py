from fpdf import FPDF
from datetime import datetime

def gerar_pdf(titulo, pecas, soma_materia, arte_aplicada, total_final, logo_path=None):
    pdf = FPDF()
    pdf.add_page()

    # Cabeçalho com logo centralizado
    if logo_path:
        logo_w = 50  # largura em mm
        pdf.set_y(10)
        pdf.set_x((210 - logo_w) / 2)  # centraliza horizontal (A4 = 210 mm)
        pdf.image(logo_path, w=logo_w)
        pdf.ln(logo_w * 0.2)  # espaço abaixo da logo

    # Título do cabeçalho
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Printaí", ln=1, align="C")
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, f"Projeto: {titulo}", ln=1, align="C")
    pdf.ln(5)

    # Cabeçalho da tabela
    pdf.set_font("Arial", "B", 10)
    colunas = ["Peça", "Filamento", "Tempo", "Peso (g)", "Matéria Prima (R$)"]
    larguras = [40, 40, 30, 30, 40]

    for col, largura in zip(colunas, larguras):
        pdf.cell(largura, 10, col, border=1, align="C")
    pdf.ln()

    # Conteúdo da tabela
    pdf.set_font("Arial", "", 10)
    for p in pecas:
        x_inicio = pdf.get_x()
        y_inicio = pdf.get_y()

        # Quebra de linha automática nos campos desejados
        pdf.multi_cell(larguras[0], 10, p['nome'], border=1, align="C")
        pdf.set_xy(x_inicio + larguras[0], y_inicio)
        pdf.multi_cell(larguras[1], 10, p['filamento'], border=1, align="C")
        pdf.set_xy(x_inicio + larguras[0] + larguras[1], y_inicio)
        pdf.cell(larguras[2], 10, p['tempo'], border=1, align="C")
        pdf.cell(larguras[3], 10, str(p['peso']), border=1, align="C")
        pdf.multi_cell(larguras[4], 10, f"R$ {p['materia']:.2f}", border=1, align="C")
        pdf.ln(0)

    # Linhas finais centralizadas
    pdf.ln(5)
    pdf.cell(0, 10, f"Total Matéria Prima: R$ {soma_materia:.2f}", ln=1, align="C")
    pdf.cell(0, 10, f"Arte aplicada: R$ {arte_aplicada:.2f}", ln=1, align="C")
    pdf.cell(0, 10, f"Investimento Total: R$ {total_final:.2f}", ln=1, align="C")

    # Salvar PDF com data/hora
    agora = datetime.now()
    timestamp = agora.strftime("%d-%m-%Y_%H-%M-%S")  # exemplo: 19-08-2025_14-30-00
    arquivo_saida = f"Printaí - {titulo} - {timestamp}.pdf"
    pdf.output(arquivo_saida)
    print(f"PDF gerado: {arquivo_saida}")


# -------------------------------
# Input do Título do projeto
# -------------------------------
titulo = input("Título do projeto: ")

# -------------------------------
# Loop de input interativo para peças
# -------------------------------
pecas = []
while True:
    print("\n--- Nova peça ---")
    nome = input("Nome da peça: ")
    filamento = input("Tipo/Cor Filamento: ")
    tempo = input("Tempo de impressão: ")
    peso = float(input("Peso estimado (g): "))
    materia = float(input("Matéria Prima (R$): ").replace(",", "."))

    pecas.append({
        'nome': nome,
        'filamento': filamento,
        'tempo': tempo,
        'peso': peso,
        'materia': materia
    })

    mais = input("Adicionar outra peça? (s/n): ").lower()
    if mais != 's':
        break

# -------------------------------
# Cálculos de totais
# -------------------------------
soma_materia = sum(p['materia'] for p in pecas)
arte_aplicada = float(input("Valor da Arte aplicada (R$): ").replace(",", "."))
total_final = soma_materia + arte_aplicada
# -------------------------------
# Geração do PDF
# -------------------------------
gerar_pdf(titulo, pecas, soma_materia, arte_aplicada, total_final, logo_path="fundo_branco.jpg")
