# 🍽️ Sistema de Gerenciamento de Restaurantes

Este projeto é uma aplicação em Python que simula um sistema de gerenciamento de restaurantes, utilizando os princípios da Programação Orientada a Objetos (POO). Nele, é possível cadastrar restaurantes, visualizar seus estados (ativos ou inativos), registrar avaliações e listar todas essas informações de forma estruturada.

## 📚 Conceitos Aplicados

Durante o desenvolvimento, foram aplicados diversos conceitos fundamentais de POO:

- **Criação de Classes e Instâncias**: Estruturação do sistema com entidades bem definidas como `Restaurante` e `Avaliação`.
- **Atributos com Underscore**: Utilização de underscore (`_`) para sinalizar atributos protegidos, como `_categoria` e `_ativo`.
- **Propriedades com `@property`**: Criação de propriedades controladas para acessar e modificar atributos de forma segura.
- **Métodos de Classe**: Implementação de métodos como `listar_restaurantes` para lidar com dados da classe como um todo.
- **Abstração**: Representação visual do estado do restaurante (ativo ou inativo) usando abstração com a propriedade `ativo`.
- **Relacionamento entre Classes**: Associação de múltiplas avaliações a um restaurante, demonstrando composição entre objetos.
- **Listagem e Apresentação de Dados**: Visualização de avaliações associadas a cada restaurante de forma organizada.
- **Importação de Arquivos**: Separação de responsabilidades com importação de classes entre arquivos como `main.py` e `restaurante.py`.

## 🚀 Funcionalidades

- Cadastrar restaurantes com nome e categoria.
- Ativar ou desativar restaurantes.
- Adicionar avaliações com nota e comentário.
- Listar todos os restaurantes cadastrados.
- Listar todas as avaliações de um restaurante específico.

## 🛠️ Tecnologias Utilizadas

- Python 3.13

