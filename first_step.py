from fpdf import FPDF

# Função auxiliar para adicionar linhas na tabela
def adicionar_linha(pdf, dados, larguras, multiline_idx=None):
    if multiline_idx is None:
        multiline_idx = []

    x, y = pdf.get_x(), pdf.get_y()  # posição inicial
    altura = 10
    max_y = y

    for i, (valor, largura) in enumerate(zip(dados, larguras)):
        if i in multiline_idx:
            pdf.multi_cell(largura, altura, str(valor), border=1, align="C")
            max_y = max(max_y, pdf.get_y())
            pdf.set_xy(x + largura, y)
        else:
            pdf.cell(largura, altura, str(valor), border=1, align="C")
        x += largura
    pdf.set_xy(pdf.get_x() - sum(larguras), max_y)

# Função para gerar o PDF
def gerar_pdf(titulo, pecas, soma, arte, total, logo_path=None):
    pdf = FPDF()
    pdf.add_page()

    # Cabeçalho
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Homemade3D", ln=1, align="C")

    if logo_path:
        pdf.image(logo_path, x=10, y=8, w=20)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, f"Projeto: {titulo}", ln=1, align="C")
    pdf.ln(10)

    # Cabeçalho da tabela
    pdf.set_font("Arial", "B", 10)
    colunas = ["Peça", "Filamento", "Tempo", "Peso (g)", "Matéria Prima (R$)"]
    larguras = [40, 40, 30, 30, 40]
    for col, largura in zip(colunas, larguras):
        pdf.cell(largura, 10, col, border=1, align="C")
    pdf.ln()

    # Conteúdo da tabela
    pdf.set_font("Arial", "", 10)
    for peca in pecas:
        dados = [
            peca['nome'], 
            peca['filamento'], 
            peca['tempo'], 
            peca['peso'], 
            f"R$ {peca['materia']:.2f}"
        ]
        adicionar_linha(pdf, dados, larguras, multiline_idx=[0,1,4])

    # Linhas finais de resumo
    pdf.ln(5)
    pdf.cell(0, 10, f"Total Matéria Prima: R$ {soma:.2f}", ln=1, align="C")
    pdf.cell(0, 10, f"Arte aplicada: R$ {arte:.2f}", ln=1, align="C")
    pdf.cell(0, 10, f"Investimento Total: R$ {total:.2f}", ln=1, align="C")

    # Salvar PDF
    nome_arquivo = f"Homemade3D - {titulo}.pdf"
    pdf.output(nome_arquivo)
    print(f"PDF gerado: {nome_arquivo}")

# Loop de entrada interativa
def main():
    pecas = []
    titulo = input("Título do projeto: ")

    while True:
        print("\n--- Nova peça ---")
        nome = input("Nome da peça: ")
        filamento = input("Tipo/Cor Filamento: ")
        tempo = input("Tempo de impressão: ")
        peso = float(input("Peso estimado (g): "))
        materia = float(input("Matéria Prima (R$): ").replace(",", "."))

        pecas.append({
            "nome": nome,
            "filamento": filamento,
            "tempo": tempo,
            "peso": peso,
            "materia": materia
        })

        cont = input("Adicionar outra peça? (s/n): ").lower()
        if cont != "s":
            break

    arte = float(input("Valor da Arte aplicada (R$): ").replace(",", "."))
    soma = sum(p['materia'] for p in pecas)
    total = soma + arte

    gerar_pdf(titulo, pecas, soma, arte, total, logo_path=None)

if __name__ == "__main__":
    main()
