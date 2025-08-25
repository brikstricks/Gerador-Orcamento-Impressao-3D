# 🖨️ Sistema de Orçamentos Printaí 3D

Sistema completo para geração de orçamentos de impressão 3D com interface gráfica moderna e exportação em PDF profissional.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![PyQt5](https://img.shields.io/badge/PyQt5-Interface-green.svg)
![PDF](https://img.shields.io/badge/PDF-Export-red.svg)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow.svg)

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação](#-instalação)
- [Como Usar](#-como-usar)
- [Exemplos de Uso](#-exemplos-de-uso)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Contribuição](#-contribuição)
- [Solução de Problemas](#-solução-de-problemas)
- [Roadmap](#-roadmap)

## 🎯 Sobre o Projeto

O **Sistema Printaí 3D** é uma aplicação desktop desenvolvida em Python para automatizar a criação de orçamentos profissionais para serviços de impressão 3D. 

### ✨ Por que usar este sistema?

- **Facilidade**: Interface intuitiva para cadastro rápido de peças
- **Profissionalismo**: PDFs com logo e layout profissional
- **Precisão**: Cálculos automáticos de tempo, materiais e totais
- **Flexibilidade**: Valores personalizáveis por peça e mão de obra
- **Organização**: Tabelas estruturadas com todos os dados

## 🚀 Funcionalidades

### ✅ Implementadas

- **Interface Gráfica Moderna**: Desenvolvida com PyQt5
- **Cadastro de Peças**: 
  - Nome da peça
  - Tipo/cor do filamento
  - Tempo de impressão (horas e minutos)
  - Peso estimado
  - Valor individual por peça
- **Cálculos Automáticos**: Subtotais, total de peças e valor final
- **Arte Aplicada**: Campo configurável para mão de obra
- **Exportação PDF**: 
  - Logo personalizada da Printaí 3D
  - Layout profissional
  - Tabela organizada
  - Totais destacados
- **Validações**: Campos obrigatórios e verificações de erro
- **Interface Responsiva**: Tabela redimensionável e campos organizados

### 🔄 Em Desenvolvimento

- Banco de dados para histórico de orçamentos
- Templates de peças mais utilizadas
- Cadastro de clientes
- Relatórios de vendas
- Interface web (Flask/Django)

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Finalidade |
|------------|---------|------------|
| **Python** | 3.8+ | Linguagem principal |
| **PyQt5** | 5.15+ | Interface gráfica |
| **fpdf2** | Latest | Geração de PDFs |
| **pandas** | 1.3+ | Manipulação de dados |

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- **Python 3.8 ou superior**
- **pip** (gerenciador de pacotes Python)
- **Sistema operacional**: Windows, macOS ou Linux

### Como verificar se o Python está instalado:

```bash
python --version
# ou
python3 --version
```

Se não tiver o Python instalado, baixe em: https://python.org/downloads/

## 🔧 Instalação

### 1. Clone ou baixe o projeto

```bash
# Opção 1: Clone via git
git clone https://github.com/seu-usuario/printai-3d-orcamentos.git
cd printai-3d-orcamentos

# Opção 2: Baixe o arquivo .zip e extraia
```

### 2. Crie um ambiente virtual (recomendado)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install fpdf2 pandas PyQt5
```

### 4. Execute o programa

```bash
python printai_3d_orcamentos.py
```

## 📖 Como Usar

### 1. **Iniciando o Sistema**

Execute o arquivo principal e a interface será aberta:

![Interface Principal](docs/interface-principal.png)

### 2. **Preenchendo Dados do Projeto**

- **Nome do Projeto**: Ex: "Miniaturas RPG Mesa Redonda"
- **Cliente**: Nome do cliente ou empresa

### 3. **Adicionando Peças**

Para cada peça do orçamento:

1. **Nome da Peça**: Ex: "Miniatura Orc Guerreiro"
2. **Filamento**: Ex: "PLA Preto" ou "PETG Transparente"
3. **Tempo**: Selecione horas (0-99) e minutos (0-59)
4. **Peso**: Peso estimado em gramas
5. **Valor**: Preço que você cobrará por esta peça
6. Clique em **"➕ Adicionar Peça"**

### 4. **Configurando Valores Finais**

- **Arte Aplicada**: Valor da mão de obra (padrão: R$ 30,00)
- Os totais são calculados automaticamente

### 5. **Gerando o PDF**

1. Clique em **"📄 Gerar PDF do Orçamento"**
2. Escolha onde salvar o arquivo
3. O PDF será criado com logo e layout profissional

### 6. **Outras Opções**

- **❌ Remover Peça**: Selecione uma linha na tabela e clique no botão
- **🗑️ Limpar Tudo**: Remove todos os dados (pede confirmação)

## 💡 Exemplos de Uso

### Exemplo 1: Orçamento para Miniaturas de RPG

```
Projeto: "Set Miniaturas D&D"
Cliente: "João Silva"

Peças:
1. Miniatura Elfo Arqueiro    | PLA Verde  | 2h30min | 15g | R$ 25,00
2. Miniatura Anão Bárbaro     | PLA Cinza  | 3h15min | 22g | R$ 30,00
3. Dragão Boss                | PLA Preto  | 8h00min | 85g | R$ 80,00

Total Peças: R$ 135,00
Arte Aplicada: R$ 50,00
TOTAL FINAL: R$ 185,00
```

### Exemplo 2: Orçamento para Peças Funcionais

```
Projeto: "Peças Reposição Impressora"
Cliente: "TechLab Ltda"

Peças:
1. Engrenagem Motor X    | PETG Azul    | 1h45min | 8g  | R$ 15,00
2. Suporte Sensor Y      | ABS Preto    | 2h30min | 12g | R$ 20,00
3. Case Eletrônico       | PETG Branco  | 4h00min | 35g | R$ 45,00

Total Peças: R$ 80,00
Arte Aplicada: R$ 30,00
TOTAL FINAL: R$ 110,00
```

## 📁 Estrutura do Projeto

```
printai-3d-orcamentos/
│
├── printai_3d_orcamentos.py    # Arquivo principal
├── README.md                   # Documentação
├── requirements.txt            # Dependências
├── docs/                       # Documentação adicional
│   ├── interface-principal.png
│   └── exemplo-pdf.png
├── examples/                   # Exemplos de PDFs gerados
│   ├── orcamento-exemplo-1.pdf
│   └── orcamento-exemplo-2.pdf
└── venv/                      # Ambiente virtual (criado na instalação)
```

## 🤝 Contribuição

Contribuições são bem-vindas! Aqui está como você pode ajudar:

### Ideias para Contribuição:

- 🎨 Melhorias na interface
- 🐛 Correção de bugs
- 📚 Documentação adicional
- ✨ Novas funcionalidades
- 🧪 Testes automatizados

## 🆘 Solução de Problemas

### ❌ Erro: "ModuleNotFoundError: No module named 'PyQt5'"

**Solução:**
```bash
pip install PyQt5
```

### ❌ Erro: "ModuleNotFoundError: No module named 'fpdf'"

**Solução:**
```bash
pip install fpdf2
```

### ❌ Erro ao gerar PDF: "Permission denied"

**Causas possíveis:**
- PDF já está aberto em outro programa
- Pasta de destino sem permissão de escrita

**Solução:**
- Feche o PDF se estiver aberto
- Escolha outra pasta para salvar
- Execute como administrador (Windows)

### ❌ Interface não abre ou fica em branco

**Solução:**
```bash
# Reinstale o PyQt5
pip uninstall PyQt5
pip install PyQt5
```

### ❌ Caracteres especiais não aparecem no PDF

**Solução:**
- Evite acentos nos nomes das peças
- Use apenas caracteres ASCII no nome do projeto

### 🔍 Debug Mode

Para ver erros detalhados, execute:

```bash
python printai_3d_orcamentos.py
```

Os erros aparecerão no terminal.

## 🗺️ Roadmap

### Versão 1.1 (Próxima)
- [ ] Banco de dados SQLite para histórico
- [ ] Backup automático dos dados
- [ ] Templates de peças frequentes
- [ ] Configurações salvas do usuário

### Versão 1.2 (Futura)
- [ ] Cadastro completo de clientes
- [ ] Relatórios de vendas mensais
- [ ] Múltiplos templates de PDF
- [ ] Sistema de descontos automáticos

### Versão 2.0 (Longo Prazo)
- [ ] Interface web com Flask
- [ ] API REST para integração
- [ ] Sistema multi-usuário
- [ ] Dashboard de analytics

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor

**Desenvolvido com ❤️ para a comunidade de impressão 3D**

## 🙏 Agradecimentos

- Comunidade Python Brasil
- Desenvolvedores do PyQt5 e fpdf2
- Beta testers da versão inicial
- Makers e entusiastas da impressão 3D

---

⭐ **Se este projeto te ajudou, deixe uma estrela no repositório!**

📧 **Dúvidas?** Abra uma issue ou envie um email!

🚀 **Bora imprimir em 3D!**