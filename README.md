### Desafio de Automação proposta pela Inmetrics

## Preparando o ambiente

> ### Requisitos do sistema:

- Python 3.6 >

se  já possuir estes recursos instalados em sua máquina pule diretos para os passos abaixo:

> ### baixar as depêndecias do projeto

execute o comando abaixo na pasta raiz do projeto

```python
pip install -r requirements.txt
```
Deixei neste projeto um arquivo Dockefile, caso execute este projeto em um ambiente Docker não será necessário executar o comando acima.

> ### Estrutura do projeto

- feature: armazenamento dos gherkins.
- manager: armazenamento de arquivos que auxiliam a execução e orquestração do projeto.
- pages: criado para trabalhar com page-objects
- data: feito para o consumo de dados(imagens)
- steps: diretorio onde esta a implementação dos passos
- driver: onde fica armazenado o driver do selenium para execução dos testes (não é recomendado subir arquivos  exe no git, mas subi somente para o desafio)
- o arquivo enviroment.py é onde fica o setup inicial do projeto de automação.

> ### execução dos testes

execute o comando abaixo na pasta raiz do projeto para realizar a execução dos testes

```python
python -m Pyautomators
```
