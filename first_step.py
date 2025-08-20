# first_step.py
from fpdf import FPDF
from datetime import datetime

def gerar_pdf(titulo, pecas, soma_materia, arte_aplicada, total_final, logo_path=None):
    """
    Gera o PDF do orçamento.
    Parâmetros:
      - titulo (str): título do projeto
      - pecas (list[dict]): lista de peças, cada uma com:
            {'nome': str, 'filamento': str, 'tempo': str, 'peso': float, 'materia': float}
      - soma_materia (float): soma de 'materia' de todas as peças
      - arte_aplicada (float): valor da arte aplicada
      - total_final (float): soma_materia + arte_aplicada
      - logo_path (str|None): caminho de arquivo da logo (opcional)
    Retorna:
      - caminho do arquivo PDF gerado (str)
    """
    pdf = FPDF()
    pdf.add_page()

    # Cabeçalho com logo centralizada (se houver)
    if logo_path:
        try:
            logo_w = 50  # largura em mm
            pdf.set_y(10)
            pdf.set_x((210 - logo_w) / 2)  # centraliza (A4 tem 210mm de largura)
            pdf.image(logo_path, w=logo_w)
            pdf.ln(logo_w * 0.2)  # pequeno espaço após a logo
        except Exception as e:
            # Se a imagem falhar, segue sem a logo
            print(f"[Aviso] Não foi possível carregar a logo ({logo_path}): {e}")

    # Título do cabeçalho
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Printaí 3D", ln=1, align="C")
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, f"Projeto: {titulo}", ln=1, align="C")

    # Data/hora
    pdf.set_font("Arial", "", 10)
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    pdf.cell(0, 8, f"Gerado em: {agora}", ln=1, align="C")
    pdf.ln(4)

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

        # Células com quebra automática para textos longos
        pdf.multi_cell(larguras[0], 10, str(p.get('nome', '')), border=1, align="C")
        pdf.set_xy(x_inicio + larguras[0], y_inicio)
        pdf.multi_cell(larguras[1], 10, str(p.get('filamento', '')), border=1, align="C")
        pdf.set_xy(x_inicio + larguras[0] + larguras[1], y_inicio)
        pdf.cell(larguras[2], 10, str(p.get('tempo', '')), border=1, align="C")
        pdf.cell(larguras[3], 10, f"{float(p.get('peso', 0)):.0f}", border=1, align="C")
        pdf.multi_cell(larguras[4], 10, f"R$ {float(p.get('materia', 0)):.2f}", border=1, align="C")
        pdf.ln(0)

    # Linhas finais centralizadas
    pdf.ln(5)
    pdf.set_font("Arial", "B", 11)
    pdf.cell(0, 8, f"Total Matéria Prima: R$ {soma_materia:.2f}", ln=1, align="C")
    pdf.cell(0, 8, f"Arte aplicada: R$ {arte_aplicada:.2f}", ln=1, align="C")
    pdf.cell(0, 10, f"Investimento Total: R$ {total_final:.2f}", ln=1, align="C")

    # Salvar PDF com data/hora no nome
    timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    arquivo_saida = f"Printaí - {titulo} - {timestamp}.pdf"
    pdf.output(arquivo_saida)
    print(f"✅ PDF gerado: {arquivo_saida}")
    return arquivo_saida
