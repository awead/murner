# M-URN-er

Moves URNs by repointing them to other new locations.

## Development Setup

Start up the containers:

``` bash
docker compose up -d
```

Use the `development` service for testing:

``` bash
docker compose exec -it development pytest
```

## Using the Worker

Use the worker pod by calling the `runner.py` script:

``` bash
docker compose exec -it worker python src/runner.py
```

