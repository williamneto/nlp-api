
# nlp-api

API para utilização de modelos de processamento de linguagem natural. Utiliza modelos disponíveis no HuggingFace para realizar tarefas como criação e classificação de texto. Atualmente utiliza apenas o modelo egonrp/gpt2-medium-wikiwriter-squadv11-portuguese`

### Executar

São apenas dois componentes: a API e o banco de dados MongoDB.
Com o docker-compose monte as imagens e execute os dois containers destes componentes:

```
docker-compose build
docker-compose up
```

Por padrão a API estará ouvindo a porta 8000, mas é possível alterar isso nos arquivos `docker-compose.yml`e `api/Dockerfile

### Endpoints

Ao executar a API, uma documentação interativa disponível em `/doc` por onde é possível realizar as requisições

#### GET - /session/start

Inicia uma seção e retorna um ID de seção. Não recebe nenhum argumento.

#### POST - /session/complete

Geração de texto (completion). Recebe um objeto com os parâmetros da requisição:
```
{
  "session_id": "string",
  "prompt": "string",
  "type": "in",
  "use_history": false,
  "model": "egonrp/gpt2-medium-wikiwriter-squadv11-portuguese"
}
```
- session_id - Id da seção retornado na requisição de inicialização de seção
- prompt - Texto inicial para geração de texto
- type -
- use_history - Combinar prompt com histórico de atualizações. Implementação incompleta
- model - Modelo de processamento a ser utilizado. 


