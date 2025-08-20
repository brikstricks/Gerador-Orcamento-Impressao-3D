# Printaí 3D — Gerador de Orçamentos (PDF)

Script em **Python** para coletar dados de peças de impressão 3D, somar **Matéria Prima**, adicionar **Arte aplicada** (mão de obra) e gerar um **relatório em PDF** com cabeçalho *Printaí 3D* e **título do projeto**.

---

## ✨ Principais recursos

* Entrada interativa (CLI) para cadastrar **uma ou múltiplas peças**.
* Tabela com colunas: **Nome da peça**, **Tipo/Cor Filamento**, **Tempo de impressão**, **Peso estimado (g)**, **Matéria Prima (R\$)**.
* Cálculo automático: **Total de Matéria Prima**, **Arte aplicada** e **Total final** (*Investimento criativo + Matéria Prima + Arte aplicada*).
* Geração de PDF com **cabeçalho fixo** da Homemade3D e **título do projeto**.
* Formatação de moeda em **R\$** (duas casas decimais).

---

## 📂 Estrutura sugerida do projeto

```

> **Observação:** o nome da pasta pode conter espaços (ex.: `Automação Python`). No PowerShell, se precisar referenciar o caminho completo, use aspas: `"P:\Automação Python\venv\Scripts\Activate.ps1"`.

---

## 🧰 Requisitos

* **Python** 3.10+ (recomendado)
* **Sistema operacional**: Windows, macOS ou Linux
* **Bibliotecas Python**:

  * [`fpdf2`](https://pypi.org/project/fpdf2/) (utilizada com `from fpdf import FPDF`)

> Conteúdo mínimo de `requirements.txt`:

```
fpdf2
```

---

## ⚙️ Configuração do ambiente (VS Code + venv)

1. **Abra a pasta do projeto no VS Code**: `File > Open Folder...`.
2. **Abra o terminal integrado** (\`Ctrl + \`\`\`).
3. **Crie o ambiente virtual**:

   ```powershell
   python -m venv venv
   ```
4. **Ative o ambiente virtual (PowerShell)**:

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

   Se o Windows bloquear scripts, rode **apenas nesta sessão**:

   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   .\venv\Scripts\Activate.ps1
   ```

   Alternativa sem mexer na política (via `cmd`):

   ```powershell
   .\venv\Scripts\activate.bat
   ```
5. **Instale as dependências**:

   ```powershell
   pip install -r requirements.txt
   ```

   ou diretamente:

   ```powershell
   pip install fpdf2
   ```
6. **Selecione o interpretador do venv no VS Code**:

   * `Ctrl + Shift + P` → **Python: Select Interpreter** → escolha `./venv/Scripts/python.exe`.

---

## ▶️ Como executar

No terminal (com o `venv` ativo):

```powershell
python first_step.py
```

O programa irá:

1. Perguntar o **Título do projeto**.
2. Entrar em um **loop de cadastro** de peças (você pode adicionar quantas quiser):

   * **Nome da peça**
   * **Tipo/Cor Filamento**
   * **Tempo de impressão** (texto livre, ex.: `3h 20min`)
   * **Peso estimado (g)**
   * **Matéria Prima (R\$)** (aceita vírgula ou ponto; ex.: `15,90` ou `15.90`)
   * Ao final de cada peça: *“Adicionar outra peça? (s/n)”*
3. Solicitar o valor de **Arte aplicada (R\$)**.
4. Exibir um **resumo** na tela.
5. Perguntar se deseja **gerar o PDF**.
6. Salvar o arquivo como:

   ```
   Printaí 3D - <Título do projeto>.pdf
   ```

---

## 🧮 Regras de cálculo

* **Total Matéria Prima** = soma da coluna *Matéria Prima (R\$)* de todas as peças.
* **Total Final** (*Investimento criativo + Matéria Prima + Arte aplicada*) =

  ```
  Total Matéria Prima + Arte aplicada
  ```

---

## 🧾 Formato do PDF

* **Cabeçalho**: `Printaí 3D` (centralizado) + `Projeto: <Título>`.
* **Tabela** (largura fixa por coluna) com as 5 colunas definidas.
* **Linhas finais**:

  * `Total Matéria Prima` → valor somado
  * `Arte aplicada` → valor informado
  * `Investimento Total` → soma final

> *(Opcional futuro)*: adicionar **logo** no cabeçalho (requer imagem `.png/.jpg` e pequeno ajuste no código).

---

## 🔎 Validações e comportamento

* **Moeda**: aceita entrada com `,` ou `.` e converte internamente para número.
* **Campos obrigatórios**: todos os campos de peça são solicitados a cada inclusão.
* **Repetição**: após cada peça, o programa pergunta se deseja adicionar outra.
* **Saída**: apenas **PDF** (sem geração de `.xlsx`).

---

## 🧪 Exemplo (execução simplificada)

```
Título do projeto: Suporte de Parede PS5

--- Nova peça ---
Nome da peça: Base
Tipo/Cor Filamento: PLA Preto
Tempo de impressão: 5h 30min
Peso estimado (g): 120
Matéria Prima (R$): 18,50
Adicionar outra peça? (s/n): s

--- Nova peça ---
Nome da peça: Tampa
Tipo/Cor Filamento: PLA Preto
Tempo de impressão: 3h 10min
Peso estimado (g): 80
Matéria Prima (R$): 12,00
Adicionar outra peça? (s/n): n

Valor da Arte aplicada (R$): 35,00

Resumo: Matéria Prima = R$ 30,50, Arte = R$ 35,00, Total = R$ 65,50
Gerar PDF? (s/n): s
PDF gerado: Printaí 3D - Suporte de Parede PS5.pdf
```

---

## 🧯 Solução de problemas (Troubleshooting)

**1) `ModuleNotFoundError: No module named 'fpdf'`**

* Instale a lib dentro do venv: `pip install fpdf2`.
* Teste: `python -c "from fpdf import FPDF; print('OK')"` → deve imprimir `OK`.

**2) VS Code mostra `Import "fpdf" could not be resolved from source`**

* Selecione o interpretador correto: `Ctrl + Shift + P` → *Python: Select Interpreter* → `./venv/Scripts/python.exe`.
* Reinicie o VS Code.

**3) Erro ao ativar venv: `...não está assinado digitalmente`**

* Rode apenas nesta sessão: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` e ative novamente.
* Alternativa: `./venv/Scripts/activate.bat` (via `cmd`).

**4) PDF sem acentuação correta (caso futuro)**

* A fonte padrão do `fpdf2` pode não suportar todos os caracteres. Solução: registrar fonte TTF com suporte a UTF-8 (ex.: DejaVuSans). *(Podemos implementar se necessário.)*

---

## 🛣️ Roadmap (melhorias futuras)

* Inserir **logo da Homemade3D** no cabeçalho do PDF.
* Quebra de linha automática e ajuste de altura para textos longos.
* Formatação de moeda no padrão `pt-BR` com separador de milhar.
* Exportar também **JSON/CSV** para histórico.
* Parâmetros por **linha de comando** (`--titulo`, `--saida`, etc.).
* Cálculo automático de **Matéria Prima** com base em **tempo** e **peso** (regras configuráveis).
* Testes automatizados e *CI* simples no GitHub Actions.

---

## 📜 Licença

Sugestão: **MIT License**. (Ajuste conforme sua preferência.)

---

## 👤 Autor

* **Pablo Lacerda Casagni** — *Printaí 3D*

---

## 🤝 Contribuição

Sinta-se à vontade para abrir *issues* e *pull requests*. Para mudanças maiores, descreva o que pretende alterar e o motivo.

---

## 📝 Nota sobre o código

O script principal utiliza `fpdf2` com `from fpdf import FPDF`. Caso você renomeie arquivos/pastas, lembre-se de atualizar referências nos comandos do README.
