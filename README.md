
# nlp-api

API para utilização de modelos de processamento de linguagem natural. Utiliza modelos disponíveis no HuggingFace para realizar tarefas como criação e classificação de texto. Atualmente utiliza apenas o modelo egonrp/gpt2-medium-wikiwriter-squadv11-portuguese`

### Executar

São apenas dois componentes: a API e o banco de dados MongoDB.
Com o docker-compose monte as imagens e execute os dois containers destes componentes:

```
docker-compose build
docker-compose up
```

Por padrão a API estará ouvindo a porta 8000, mas é possível alterar isso nos arquivos `docker-compose.yml`e `api/Dockerfile`

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

#### POST - /session/classify
Classificação de texto. Utiliza por padrão o modelo `PrachiPatel/text_emotion_classification`
```
{
  "session_id": "string",
  "prompt": "string",
  "type": "in",
  "model": ""
}
```

Label0=sad Label1=joy Label2=love Label3=anger Label4=fear Label5=Surprise label6=neutral

#### POST - /session/analyse_sentiment
Analise de sentimento. utiliza por padrão o modelo `cardiffnlp/xlm-roberta-base-tweet-sentiment-pt`
```
{
  "session_id": "string",
  "prompt": "string",
  "type": "in",
  "model": ""
}
```

#### POST /train
```
{
  "data_training_args": {
    "dataset_name": "jvanz/querido_diario",
    "dataset_config_name": "gpt2-medium-wikiwriter-squadv11-querido-diario-portuguese",
    "model_name_or_path": "egonrp/gpt2-medium-wikiwriter-squadv11-portuguese"
  },
  "output_dir": "./llms/trained/gpt2-medium-wikiwriter-squadv11-querido-diario-portuguese",
  "overwrite_output_dir": true,
  "do_train": true,
  "do_eval": true
}
```