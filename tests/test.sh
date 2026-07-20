#!/bin/bash

# Cria o diretório exigido pelas regras do Harbor TB2
mkdir -p /logs/verifier

# Roda o pytest gerando o relatório ctrf.json no caminho obrigatório
pytest /tests/test_outputs.py -rA --ctrf /logs/verifier/ctrf.json

# Salva a nota no caminho /logs/verifier/reward.txt
if [ $? -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
