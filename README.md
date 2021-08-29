# "Casares News" API
Api that scrapes and provides the last news of the city of Carlos Casares by semantic way (RDF format).

## Usage

Consume the articles by: https://casares-news.herokuapp.com/articles/

Indicate the file format using the content-type header. Supports `JSON-LD`, `rdf/xml`, `turtle`, `n-triples` and `n3`.

E.g.: Get the lastest 5 news in JSON-LD format
```bash
ARTICLES="https://casares-news.herokuapp.com/articles/"
HEADER="Content-Type: application/ld+json" 

curl "$ARTICLES?start=0&offset=5" -H $HEADER
```

You can see other examples in the frontend app: https://pastorsin.github.io/casares-news/

## Local execution
### Requirements

- [Heroku](https://devcenter.heroku.com/articles/heroku-cli)
- [Pip](https://pip.pypa.io/en/stable/installation/)

### Install
1. Install dependencies and perform the initial migrations

```bash
make install
```

2. *Optional*: Generate a private key for the webpush notifications

```bash
make webpush-gen
```

3. *Optional*: Put the generated key in the .env file

```bash
WP_PRIVATE_KEY=<enter_private_key>
```

### Run

Run the server and the scrappers

```bash
make app
```

Run only the server

```bash
make server
```

Run only the scrappers

```bash
make scrap
```

### Clean

Remove the generated files

```bash
make clean
```