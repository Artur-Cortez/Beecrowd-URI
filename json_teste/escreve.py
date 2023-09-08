import json

py_dicionario = {
  "nome": "",
  "email": "",
  "fone": ""
}

with open("json_teste/exemplo.json", "w") as arquivo:
  json.dump(py_dicionario, arquivo)



