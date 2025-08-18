from fpdf import FPDF

def ler_numero(prompt):
    v = input(prompt + " ")
    v = v.replace(',', '.').strip()
    return float(v)

def coletar_pecas():
    pecas = []
    while True:
        print("\n--- Nova peça ---")
        nome = input("Nome da peça: ")
        filamento = input("Tipo/Cor Filamento: ")
        tempo = input("Tempo de impressão: ")
        peso = input("Peso estimado (g): ")
        materia = ler_numero("Matéria Prima (R$):")
        pecas.append({'nome': nome, 'filamento': filamento, 'tempo': tempo, 'peso': peso, 'materia': materia})

        add = input("Adicionar outra peça? (s/n): ").lower()
        if add == 'n':
            break
    return pecas

def gerar_pdf(titulo, pecas, soma_materia, arte_aplicada, total):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Homemade3D", ln=1, align="C")
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"Projeto: {titulo}", ln=1, align="C")
    pdf.ln(10)

    # Cabeçalho da tabela
    pdf.set_font("Arial", "B", 10)
    colunas = ["Peça", "Filamento", "Tempo", "Peso (g)", "Matéria Prima (R$)"]
    larguras = [40, 40, 30, 30, 40]
    for col, largura in zip(colunas, larguras):
        pdf.cell(largura, 10, col, 1, 0, "C")
    pdf.ln()

    # Linhas da tabela
    pdf.set_font("Arial", "", 10)
    for p in pecas:
        pdf.cell(40, 10, p['nome'], 1)
        pdf.cell(40, 10, p['filamento'], 1)
        pdf.cell(30, 10, p['tempo'], 1)
        pdf.cell(30, 10, str(p['peso']), 1)
        pdf.cell(40, 10, f"R$ {p['materia']:.2f}", 1, ln=1)

    # Totais
    pdf.cell(140, 10, "Total Matéria Prima", 1)
    pdf.cell(40, 10, f"R$ {soma_materia:.2f}", 1, ln=1)

    pdf.cell(140, 10, "Arte aplicada", 1)
    pdf.cell(40, 10, f"R$ {arte_aplicada:.2f}", 1, ln=1)

    pdf.cell(140, 10, "Investimento Total", 1)
    pdf.cell(40, 10, f"R$ {total:.2f}", 1, ln=1)

    pdf.output(f"Homemade3D - {titulo}.pdf")

def main():
    titulo = input("Título do projeto: ")
    pecas = coletar_pecas()
    soma = sum(p['materia'] for p in pecas)
    arte = ler_numero("Valor da Arte aplicada (R$):")
    total = soma + arte
    print(f"\nResumo: Matéria Prima = R$ {soma:.2f}, Arte = R$ {arte:.2f}, Totsal = R$ {total:.2f}")

    gerar = input("Gerar PDF? (s/n): ").lower()
    if gerar == 's':
        gerar_pdf(titulo, pecas, soma, arte, total)
        print(f"PDF gerado: Homemade3D - {titulo}.pdf")

if __name__ == "__main__":
    main()
