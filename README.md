# Laboratorio 04 — xUnit y Cobertura de Código

Bubble sort en Python 3 (POO) probado con `unittest` y medido con Coverage.py.

```
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python3 -m unittest discover -s tests -t . -v
coverage run --branch --source=src -m unittest discover -s tests -t .
coverage report -m
coverage html
```
