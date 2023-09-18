import json

py_dicionario = {
  "nome": "Najuia",
  "email": "najuia@gmail.com",
  "fone": "66969-6969"
}

with open("json_teste/novo.json", "w") as arquivo:
  json.dump(py_dicionario, arquivo)



