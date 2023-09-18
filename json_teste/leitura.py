import json

with open ('json_teste/novo.json') as abrir_arquivo:
  objeto_json = json.load(abrir_arquivo)

print(objeto_json)
print(type(objeto_json))