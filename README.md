# Demo project to try stuff

Install base dependencies:
```
pip install -r requirements.txt
```


### poetry-multiproject-plugin
```
cd api
poetry install
poetry build-project
poetry run python3 run.py
```

Output
```json
{
  "id": 0,
  "name": "Misha"
}
```