# Gestão Rebanho

## 👨‍🎓 Integrantes: 
- Yuki Watanabe Kuramoto
- Ricardo Batah Leone
- Cayo Henrique Gomes do Amaral
- Guilherme Martins Ventura Vieira Romeiro

## 👩‍🏫 Professores:
### Tutor(a) 
- Lucas Gomes Moreira
### Coordenador(a)
- André Godoi


## 📜 Descrição

*Este projeto visa desenvolver um sistema simples, em Python, para a gestão de rebanhos bovinos com foco em rastreabilidade, voltado para pequenas propriedades rurais.*

### Funcionalidades
- Registro de animais (com dados como raça, sexo, data de nascimento e identificador único)
- Consulta e listagem dos animais registrados
- Registro de eventos no histórico do animal (ex: vacinação, venda)
- Exportação dos dados em formato JSON
- Integração com banco de dados Oracle (via cx_Oracle)
- Interface via terminal com menus intuitivos

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>.github</b>: Nesta pasta ficarão os arquivos de configuração específicos do GitHub que ajudam a gerenciar e automatizar processos no repositório.

- <b>assets</b>: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.

- <b>config</b>: Posicione aqui arquivos de configuração que são usados para definir parâmetros e ajustes do projeto.

- <b>document</b>: aqui estão todos os documentos do projeto que as atividades poderão pedir. Na subpasta "other", adicione documentos complementares e menos importantes.

- <b>scripts</b>: Posicione aqui scripts auxiliares para tarefas específicas do seu projeto. Exemplo: deploy, migrações de banco de dados, backups.

- <b>src</b>: Todo o código fonte criado para o desenvolvimento do projeto ao longo das 7 fases.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

## 🔧 Como executar o código

### Requisitos

- Python 3.8+
- Biblioteca `cx_Oracle`
- Oracle XE instalado ou servidor remoto disponível

```bash
pip install cx_Oracle
```

### Execução

```bash
python gestao_rebanho.py
```

## 🗃 Histórico de lançamentos

* 0.1.0 - 22/04/2024
    * 


## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
