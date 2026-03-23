# 🎬 CineReserve API - Sistema de Reservas de Cinema

Uma API RESTful robusta desenvolvida em Django REST Framework para gerenciamento de um cinema, incluindo listagem de filmes, sessões, visualização de mapa de assentos em tempo real e um sistema seguro de reservas de ingressos.

## 🚀 Tecnologias Utilizadas
* **Python 3.11+**
* **Django & Django REST Framework (DRF)**
* **PostgreSQL:** Banco de dados relacional principal.
* **Redis:** Utilizado para gerenciamento em memória do bloqueio temporário de assentos (Time-To-Live) evitando *Race Conditions*.
* **JWT (JSON Web Tokens):** Autenticação segura nas rotas privadas.
* **Poetry:** Gerenciamento de pacotes e dependências.
* **Docker & Docker Compose:** Containerização de toda a aplicação e serviços.
* **drf-spectacular:** Geração de documentação automática (Swagger/OpenAPI).

## ⚙️ Principais Funcionalidades (Casos Implementados)
- [x] **TC.2:** Listagem de filmes e sessões aberta ao público.
- [x] **TC.4:** Mapa de assentos com status em tempo real (Disponível, Reservado, Comprado) e paginação global implementada.
- [x] **TC.5:** Bloqueio temporário de assentos por 10 minutos utilizando operação atômica (`SETNX`) no Redis.
- [x] **Checkout Seguro:** Uso de `transaction.atomic()` e `select_for_update()` no PostgreSQL para garantir a integridade da compra e evitar vendas duplicadas.

## 🐳 Como executar o projeto (Via Docker)

A maneira mais recomendada de rodar o projeto é utilizando o Docker, que subirá a API, o Banco de Dados e o Redis simultaneamente.

1. Clone o repositório:
```bash
git clone [https://github.com/RicardoWillyan007/CineReserve-API.git](https://github.com/RicardoWillyan007/CineReserve-API.git)
cd https://github.com/RicardoWillyan007/CineReserve-API.git