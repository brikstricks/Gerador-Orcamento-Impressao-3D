# import pytest
# from GUI_app2 import OrcamentoPrintai3D

# def test_adicionar_peca(qtbot):
#     janela = OrcamentoPrintai3D()
#     qtbot.addWidget(janela)

#     # Preencher campos
#     janela.nome_peca_input.setText("Miniatura Orc")
#     janela.filamento_input.setText("PLA Preto")
#     janela.horas_input.setValue(1)
#     janela.minutos_input.setValue(30)
#     janela.peso_input.setValue(15.0)
#     janela.preco_peca_input.setValue(40.0)

#     # Clicar no botão "Adicionar"
#     qtbot.mouseClick(janela.findChild(type(janela).findChild, "➕ Adicionar Peça"), qtbot.MouseButton.LeftButton)

#     # Verificar se peça entrou na tabela
#     assert janela.tabela.rowCount() == 1
#     assert janela.tabela.item(0, 0).text() == "Miniatura Orc"
