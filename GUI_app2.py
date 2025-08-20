# app.py
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QFormLayout,
    QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QHeaderView,
    QFileDialog, QMessageBox, QLabel
)
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

import first_step  # nosso módulo de PDF (gerar_pdf)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Printaí 3D — Gerador de Orçamentos")

        self.setWindowIcon(QIcon("fundo_branco.jpg"))

        self.logo_path = "fundo_branco.jpg"  # caminho default da logo (pode trocar pelo botão)
        self._build_ui()

    def _build_ui(self):
        cw = QWidget()
        layout = QVBoxLayout(cw)

        # --- Formulário superior: Título + Arte aplicada ---
        form = QFormLayout()
        self.input_titulo = QLineEdit()
        self.input_titulo.setPlaceholderText("Ex.: Suporte de Parede PS5")
        form.addRow("Título do projeto:", self.input_titulo)

        self.input_arte = QLineEdit()
        self.input_arte.setPlaceholderText("Ex.: 35,00")
        form.addRow("Arte aplicada (R$):", self.input_arte)

        layout.addLayout(form)

        # --- Tabela de peças ---
        self.table = QTableWidget(0, 5)
        self.table.setHorizontalHeaderLabels(["Peça", "Filamento", "Tempo", "Peso (g)", "Matéria Prima (R$)"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().setVisible(False)
        self.table.setAlternatingRowColors(True)
        layout.addWidget(self.table)

        # Linha de botões para a tabela
        hbtn = QHBoxLayout()
        btn_add = QPushButton("Adicionar peça")
        btn_add.clicked.connect(self.add_row)
        hbtn.addWidget(btn_add)

        btn_rem = QPushButton("Remover selecionadas")
        btn_rem.clicked.connect(self.remove_selected_rows)
        hbtn.addWidget(btn_rem)

        hbtn.addStretch()
        layout.addLayout(hbtn)

        # Botão principal de geração
        btn_generate = QPushButton("Gerar PDF")
        btn_generate.setStyleSheet("font-weight: bold; padding: 8px;")
        btn_generate.clicked.connect(self.on_generate_pdf)
        layout.addWidget(btn_generate)

        # Dica
        tip = QLabel("Dica: use vírgula ou ponto nos valores. Linhas em branco serão ignoradas.")
        tip.setStyleSheet("color: gray;")
        layout.addWidget(tip)

        self.setCentralWidget(cw)

        # Começa com 1 linha em branco para ajudar o usuário
        self.add_row()

    # ---------- Ações da UI ----------
    def add_row(self):
        r = self.table.rowCount()
        self.table.insertRow(r)
        # cria itens editáveis em cada coluna
        for c in range(self.table.columnCount()):
            self.table.setItem(r, c, QTableWidgetItem(""))

    def remove_selected_rows(self):
        rows = sorted({idx.row() for idx in self.table.selectedIndexes()}, reverse=True)
        for r in rows:
            self.table.removeRow(r)

    def select_logo(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Selecionar logo (PNG/JPG)", "", "Imagens (*.png *.jpg *.jpeg)")
        if file_path:
            self.logo_path = file_path
            # Atualiza o ícone da janela também
            self.setWindowIcon(QIcon(self.logo_path))
            QMessageBox.information(self, "Logo selecionada", f"Logo atualizada:\n{file_path}")

    def on_generate_pdf(self):
        titulo = self.input_titulo.text().strip()
        arte_txt = self.input_arte.text().strip().replace(",", ".") or "0"

        if not titulo:
            QMessageBox.warning(self, "Atenção", "Informe o título do projeto.")
            return

        # Lê as linhas da tabela e monta a lista de peças
        pecas = []
        for r in range(self.table.rowCount()):
            nome = self._cell_text(r, 0)
            filamento = self._cell_text(r, 1)
            tempo = self._cell_text(r, 2)
            peso_txt = self._cell_text(r, 3)
            materia_txt = self._cell_text(r, 4)

            # Ignora linhas totalmente vazias
            if not any([nome, filamento, tempo, peso_txt, materia_txt]):
                continue

            # Validação simples
            try:
                peso = float((peso_txt or "0").replace(",", "."))
                materia = float((materia_txt or "0").replace(",", "."))
            except ValueError:
                QMessageBox.warning(self, "Atenção", f"Digite somente números {r+1}. Verifique Peso/Materia Prima.")
                return

            # Campos essenciais
            if not nome or not filamento or not tempo or not peso_txt or not materia_txt:
                QMessageBox.warning(self, "Atenção", f"Verifique o preenchimento de todos os campos! {r+1}.")
                return

            pecas.append({
                "nome": nome,
                "filamento": filamento,
                "tempo": tempo,
                "peso": peso,
                "materia": materia
            })

        if not pecas:
            QMessageBox.warning(self, "Atenção", "Adicione pelo menos uma peça.")
            return

        # Arte aplicada
        try:
            arte = float(arte_txt)
        except ValueError:
            QMessageBox.warning(self, "Atenção", "Informe um valor numérico válido para Arte aplicada.")
            return

        # Cálculos
        soma_materia = sum(p["materia"] for p in pecas)
        total_final = soma_materia + arte

        # Chama o gerador de PDF do módulo first_step
        try:
            caminho_pdf = first_step.gerar_pdf(
                titulo=titulo,
                pecas=pecas,
                soma_materia=soma_materia,
                arte_aplicada=arte,
                total_final=total_final,
                logo_path=self.logo_path  # usa a logo selecionada (ou a default)
            )
            QMessageBox.information(self, "Sucesso", f"PDF gerado com sucesso!\n\n{caminho_pdf}")
        except Exception as e:
            QMessageBox.critical(self, "Erro ao gerar PDF", str(e))

    def _cell_text(self, row, col):
        item = self.table.item(row, col)
        return (item.text().strip() if item else "")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.resize(900, 600)
    win.show()
    sys.exit(app.exec())
