import sys
import pandas as pd
from fpdf import FPDF
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, 
                            QWidget, QPushButton, QLineEdit, QLabel, QTableWidget, 
                            QTableWidgetItem, QMessageBox, QDoubleSpinBox, QSpinBox,
                            QHeaderView, QFileDialog)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from datetime import datetime
import os

class OrcamentoPrintai3D(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pecas_dados = []  # Lista para armazenar as peças
        self.init_ui()
        
    def init_ui(self):
        """Inicializa a interface do usuário"""
        self.setWindowTitle("Printaí 3D - Sistema de Orçamentos")
        self.setGeometry(400, 200, 1000, 700)
        
        # Widget principal
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)
        
        # === SEÇÃO: DADOS DO PROJETO ===
        self.criar_secao_projeto(layout)
        
        # === SEÇÃO: ADICIONAR PEÇAS ===
        self.criar_secao_pecas(layout)
        
        # === TABELA DE PEÇAS ===
        self.criar_tabela_pecas(layout)
        
        # === SEÇÃO: VALORES FINAIS ===
        self.criar_secao_valores(layout)
        
        # === BOTÕES FINAIS ===
        self.criar_botoes_finais(layout)
        
    def criar_secao_projeto(self, layout):
        """Cria seção para dados do projeto e cliente"""
        # Título
        titulo = QLabel("📋 DADOS DO PROJETO")
        titulo.setFont(QFont("Arial", 14, QFont.Bold))
        layout.addWidget(titulo)
        
        # Layout horizontal para nome do projeto e cliente
        h_layout = QHBoxLayout()
        
        # Nome do projeto
        h_layout.addWidget(QLabel("Nome do Projeto:"))
        self.projeto_input = QLineEdit()
        self.projeto_input.setPlaceholderText("Ex: Miniaturas para RPG")
        h_layout.addWidget(self.projeto_input)
        
        # Nome do cliente
        h_layout.addWidget(QLabel("Cliente:"))
        self.cliente_input = QLineEdit()
        self.cliente_input.setPlaceholderText("Ex: João Silva")
        h_layout.addWidget(self.cliente_input)
        
        layout.addLayout(h_layout)
        
    def criar_secao_pecas(self, layout):
        """Cria seção para adicionar peças"""
        titulo = QLabel("\n🎯 ADICIONAR PEÇA")
        titulo.setFont(QFont("Arial", 14, QFont.Bold))
        layout.addWidget(titulo)
        
        # Layout para inputs das peças
        pecas_layout = QHBoxLayout()
        
        # Nome da peça
        pecas_layout.addWidget(QLabel("Nome:"))
        self.nome_peca_input = QLineEdit()
        self.nome_peca_input.setPlaceholderText("Ex: Miniatura Orc")
        pecas_layout.addWidget(self.nome_peca_input)
        
        # Tipo/Cor do filamento
        pecas_layout.addWidget(QLabel("Filamento:"))
        self.filamento_input = QLineEdit()
        self.filamento_input.setPlaceholderText("Ex: PLA Preto")
        pecas_layout.addWidget(self.filamento_input)
        
        # Tempo de impressão
        pecas_layout.addWidget(QLabel("Tempo (h):"))
        self.tempo_input = QDoubleSpinBox()
        self.tempo_input.setDecimals(1)
        self.tempo_input.setRange(0.1, 999.9)
        self.tempo_input.setValue(1.0)
        pecas_layout.addWidget(self.tempo_input)
        
        # Peso estimado
        pecas_layout.addWidget(QLabel("Peso (g):"))
        self.peso_input = QDoubleSpinBox()
        self.peso_input.setDecimals(1)
        self.peso_input.setRange(0.1, 9999.9)
        self.peso_input.setValue(10.0)
        pecas_layout.addWidget(self.peso_input)
        
        # Preço por grama (R$)
        pecas_layout.addWidget(QLabel("R$/g:"))
        self.preco_g_input = QDoubleSpinBox()
        self.preco_g_input.setDecimals(3)
        self.preco_g_input.setRange(0.001, 10.0)
        self.preco_g_input.setValue(0.05)  # 5 centavos por grama como padrão
        pecas_layout.addWidget(self.preco_g_input)
        
        # Botão adicionar
        btn_adicionar = QPushButton("➕ Adicionar Peça")
        btn_adicionar.clicked.connect(self.adicionar_peca)
        btn_adicionar.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; font-weight: bold; }")
        pecas_layout.addWidget(btn_adicionar)
        
        layout.addLayout(pecas_layout)
        
    def criar_tabela_pecas(self, layout):
        """Cria a tabela para mostrar as peças adicionadas"""
        titulo = QLabel("\n📊 PEÇAS DO ORÇAMENTO")
        titulo.setFont(QFont("Arial", 14, QFont.Bold))
        layout.addWidget(titulo)
        
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(6)
        self.tabela.setHorizontalHeaderLabels([
            "Nome da Peça", "Filamento", "Tempo (h)", 
            "Peso (g)", "R$/g", "Matéria Prima (R$)"
        ])
        
        # Ajustar largura das colunas
        header = self.tabela.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)  # Nome da peça ocupa mais espaço
        for i in range(1, 6):
            header.setSectionResizeMode(i, QHeaderView.ResizeToContents)
            
        layout.addWidget(self.tabela)
        
        # Botão remover peça selecionada
        btn_remover = QPushButton("❌ Remover Peça Selecionada")
        btn_remover.clicked.connect(self.remover_peca)
        btn_remover.setStyleSheet("QPushButton { background-color: #f44336; color: white; }")
        layout.addWidget(btn_remover)
        
    def criar_secao_valores(self, layout):
        """Cria seção dos valores finais"""
        titulo = QLabel("\n💰 VALORES FINAIS")
        titulo.setFont(QFont("Arial", 14, QFont.Bold))
        layout.addWidget(titulo)
        
        valores_layout = QHBoxLayout()
        
        # Total matéria prima
        valores_layout.addWidget(QLabel("Total Matéria Prima:"))
        self.total_materia_label = QLabel("R$ 0,00")
        self.total_materia_label.setStyleSheet("font-weight: bold; color: blue;")
        valores_layout.addWidget(self.total_materia_label)
        
        # Arte aplicada (mão de obra)
        valores_layout.addWidget(QLabel("Arte Aplicada (R$):"))
        self.arte_input = QDoubleSpinBox()
        self.arte_input.setRange(0, 9999.99)
        self.arte_input.setDecimals(2)
        self.arte_input.setValue(30.00)  # Valor padrão
        self.arte_input.valueChanged.connect(self.calcular_total)
        valores_layout.addWidget(self.arte_input)
        
        # Total final
        valores_layout.addWidget(QLabel("TOTAL FINAL:"))
        self.total_final_label = QLabel("R$ 0,00")
        self.total_final_label.setStyleSheet("font-weight: bold; font-size: 16px; color: green;")
        valores_layout.addWidget(self.total_final_label)
        
        layout.addLayout(valores_layout)
        
    def criar_botoes_finais(self, layout):
        """Cria botões para gerar PDF e limpar"""
        botoes_layout = QHBoxLayout()
        
        # Botão gerar PDF
        btn_pdf = QPushButton("📄 Gerar PDF do Orçamento")
        btn_pdf.clicked.connect(self.gerar_pdf)
        btn_pdf.setStyleSheet("QPushButton { background-color: #2196F3; color: white; font-weight: bold; padding: 10px; }")
        botoes_layout.addWidget(btn_pdf)
        
        # Botão limpar tudo
        btn_limpar = QPushButton("🗑️ Limpar Tudo")
        btn_limpar.clicked.connect(self.limpar_tudo)
        btn_limpar.setStyleSheet("QPushButton { background-color: #FF9800; color: white; font-weight: bold; padding: 10px; }")
        botoes_layout.addWidget(btn_limpar)
        
        layout.addLayout(botoes_layout)
        
    def adicionar_peca(self):
        """Adiciona uma peça à lista"""
        nome = self.nome_peca_input.text().strip()
        filamento = self.filamento_input.text().strip()
        tempo = self.tempo_input.value()
        peso = self.peso_input.value()
        preco_g = self.preco_g_input.value()
        
        if not nome or not filamento:
            QMessageBox.warning(self, "Atenção", "Preencha pelo menos o nome da peça e o filamento!")
            return
            
        # Calcular matéria prima
        materia_prima = peso * preco_g
        
        # Adicionar aos dados
        peca_data = {
            'nome': nome,
            'filamento': filamento,
            'tempo': tempo,
            'peso': peso,
            'preco_g': preco_g,
            'materia_prima': materia_prima
        }
        
        self.pecas_dados.append(peca_data)
        self.atualizar_tabela()
        self.calcular_total()
        
        # Limpar campos
        self.nome_peca_input.clear()
        self.filamento_input.clear()
        self.tempo_input.setValue(1.0)
        self.peso_input.setValue(10.0)
        
    def remover_peca(self):
        """Remove a peça selecionada da tabela"""
        linha_atual = self.tabela.currentRow()
        if linha_atual >= 0:
            self.pecas_dados.pop(linha_atual)
            self.atualizar_tabela()
            self.calcular_total()
        else:
            QMessageBox.information(self, "Info", "Selecione uma linha para remover!")
            
    def atualizar_tabela(self):
        """Atualiza a tabela com os dados das peças"""
        self.tabela.setRowCount(len(self.pecas_dados))
        
        for i, peca in enumerate(self.pecas_dados):
            self.tabela.setItem(i, 0, QTableWidgetItem(peca['nome']))
            self.tabela.setItem(i, 1, QTableWidgetItem(peca['filamento']))
            self.tabela.setItem(i, 2, QTableWidgetItem(f"{peca['tempo']:.1f}"))
            self.tabela.setItem(i, 3, QTableWidgetItem(f"{peca['peso']:.1f}"))
            self.tabela.setItem(i, 4, QTableWidgetItem(f"{peca['preco_g']:.3f}"))
            self.tabela.setItem(i, 5, QTableWidgetItem(f"R$ {peca['materia_prima']:.2f}"))
            
    def calcular_total(self):
        """Calcula e atualiza os totais"""
        total_materia = sum(peca['materia_prima'] for peca in self.pecas_dados)
        arte_aplicada = self.arte_input.value()
        total_final = total_materia + arte_aplicada
        
        self.total_materia_label.setText(f"R$ {total_materia:.2f}")
        self.total_final_label.setText(f"R$ {total_final:.2f}")
        
    def gerar_pdf(self):
        """Gera o PDF do orçamento"""
        if not self.pecas_dados:
            QMessageBox.warning(self, "Atenção", "Adicione pelo menos uma peça antes de gerar o PDF!")
            return
            
        projeto = self.projeto_input.text().strip() or "Projeto sem nome"
        cliente = self.cliente_input.text().strip() or "Cliente não informado"
        
        # Escolher onde salvar
        filename, _ = QFileDialog.getSaveFileName(
            self, "Salvar Orçamento", 
            f"Orcamento_{projeto.replace(' ', '_')}_{datetime.now().strftime('%d%m%Y_%H%M')}.pdf",
            "Arquivos PDF (*.pdf)"
        )
        
        if filename:
            self.criar_pdf(filename, projeto, cliente)
            QMessageBox.information(self, "Sucesso", f"PDF gerado com sucesso!\n{filename}")
            
    def criar_pdf(self, filename, projeto, cliente):
        """Cria o arquivo PDF"""
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        # === CABEÇALHO ===
        pdf.set_font("Arial", 'B', 20)
        pdf.set_text_color(0, 100, 200)  # Azul
        pdf.cell(0, 15, "Printaí 3D", ln=True, align='C')
        
        pdf.set_font("Arial", 'I', 12)
        pdf.set_text_color(100, 100, 100)  # Cinza
        pdf.cell(0, 8, "Impressão 3D Profissional", ln=True, align='C')
        pdf.ln(10)
        
        # === DADOS DO PROJETO ===
        pdf.set_text_color(0, 0, 0)  # Preto
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, f"ORÇAMENTO: {projeto.upper()}", ln=True)
        pdf.ln(5)
        
        pdf.set_font("Arial", '', 11)
        pdf.cell(40, 8, "Cliente:", 0, 0)
        pdf.set_font("Arial", 'B', 11)
        pdf.cell(0, 8, cliente, ln=True)
        
        pdf.set_font("Arial", '', 11)
        pdf.cell(40, 8, "Data:", 0, 0)
        pdf.cell(0, 8, datetime.now().strftime("%d/%m/%Y"), ln=True)
        pdf.ln(10)
        
        # === TABELA DE PEÇAS ===
        pdf.set_font("Arial", 'B', 10)
        pdf.set_fill_color(230, 230, 230)  # Cinza claro para cabeçalho
        
        # Cabeçalho da tabela
        pdf.cell(50, 8, "Nome da Peça", 1, 0, 'C', True)
        pdf.cell(35, 8, "Filamento", 1, 0, 'C', True)
        pdf.cell(20, 8, "Tempo(h)", 1, 0, 'C', True)
        pdf.cell(20, 8, "Peso(g)", 1, 0, 'C', True)
        pdf.cell(25, 8, "R$/g", 1, 0, 'C', True)
        pdf.cell(30, 8, "Matéria Prima", 1, 1, 'C', True)
        
        # Dados das peças
        pdf.set_font("Arial", '', 9)
        for peca in self.pecas_dados:
            pdf.cell(50, 6, peca['nome'][:20], 1, 0, 'L')  # Limita nome a 20 chars
            pdf.cell(35, 6, peca['filamento'][:15], 1, 0, 'C')
            pdf.cell(20, 6, f"{peca['tempo']:.1f}", 1, 0, 'C')
            pdf.cell(20, 6, f"{peca['peso']:.1f}", 1, 0, 'C')
            pdf.cell(25, 6, f"{peca['preco_g']:.3f}", 1, 0, 'C')
            pdf.cell(30, 6, f"R$ {peca['materia_prima']:.2f}", 1, 1, 'R')
        
        pdf.ln(10)
        
        # === TOTAIS ===
        total_materia = sum(peca['materia_prima'] for peca in self.pecas_dados)
        arte_aplicada = self.arte_input.value()
        total_final = total_materia + arte_aplicada
        
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(120, 8, "", 0, 0)  # Espaço
        pdf.cell(50, 8, f"Total Matéria Prima: R$ {total_materia:.2f}", 1, 1, 'R')
        
        pdf.cell(120, 8, "", 0, 0)
        pdf.cell(50, 8, f"Arte Aplicada: R$ {arte_aplicada:.2f}", 1, 1, 'R')
        
        pdf.set_font("Arial", 'B', 14)
        pdf.set_fill_color(200, 255, 200)  # Verde claro
        pdf.cell(120, 10, "", 0, 0)
        pdf.cell(50, 10, f"Total: R$ {total_final:.2f}", 1, 1, 'R', True)
        
        # === RODAPÉ ===
        pdf.ln(20)
        pdf.set_font("Arial", 'I', 8)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(0, 5, "Orçamento válido por 30 dias. Valores sujeitos a alteração sem aviso prévio.", ln=True, align='C')
        pdf.cell(0, 5, f"Gerado em {datetime.now().strftime('%d/%m/%Y às %H:%M')} pelo Sistema Printaí 3D", ln=True, align='C')
        
        # Salvar PDF
        pdf.output(filename)
        
    def limpar_tudo(self):
        """Limpa todos os campos e dados"""
        resposta = QMessageBox.question(
            self, "Confirmar", 
            "Tem certeza que deseja limpar todos os dados?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if resposta == QMessageBox.Yes:
            self.pecas_dados.clear()
            self.projeto_input.clear()
            self.cliente_input.clear()
            self.nome_peca_input.clear()
            self.filamento_input.clear()
            self.tempo_input.setValue(1.0)
            self.peso_input.setValue(10.0)
            self.preco_g_input.setValue(0.05)
            self.arte_input.setValue(30.00)
            self.atualizar_tabela()
            self.calcular_total()

def main():
    """Função principal"""
    app = QApplication(sys.argv)
    
    # Configurar fonte padrão
    font = QFont("Arial", 9)
    app.setFont(font)
    
    # Criar e mostrar a janela
    janela = OrcamentoPrintai3D()
    janela.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()