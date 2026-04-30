# Arquitetura Multicamadas

## Arquitetura do Projeto

Apresentação (View)
Templates HTML responsáveis pela interface com o usuário.

Controlador (Controller)
Responsável por orquestrar as requisições e preparar os dados para a View.

Aplicação (Service)
Camada onde ficam as regras de negócio (ex: filtros e lógica de datas para banners).

Persistência (Infrastructure / Repository)
Responsável pelo acesso aos dados e comunicação com a “base de dados”.

Entidades / Rotas
Ponto de entrada da aplicação Flask, gerenciando o ciclo de vida das requisições.

## Feature Nova

Marketing Sazonal (Banner Dinâmico)
Implementação de uma regra de negócio na camada de aplicação que exibe banners promocionais com base no mês atual do sistema.

# Como Executar o Projeto

1. Criar o ambiente virtual
```
   python -m venv venv
```
2. Ativar o ambiente (Windows)
```
   .\venv\Scripts\activate
```
3. Instalar dependências
```
   pip install -r requirements.txt
```
4. Rodar a aplicação
```
   python app.py
```
Acesse no navegador:
[http://127.0.0.1:5000](http://127.0.0.1:5000)

## Executar Testes BDD

```
behave
```

# Observações

* Estrutura organizada em múltiplas camadas para melhor manutenção e escalabilidade.
* Separação clara de responsabilidades entre regras de negócio, controle e acesso a dados.
* Nova feature de marketing adicionada sem impacto direto nas demais camadas, seguindo boas práticas de arquitetura.
