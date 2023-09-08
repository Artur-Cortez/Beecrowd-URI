import enum, datetime

class Pagamento(enum.Enum):
  EmAberto = 1
  PagoParcial = 2
  Pago = 3

class Boleto:
  def __init__(self, cod, emissao, venc, valor):
    self.__codBarras, self.__dataEmissao, self.__dataVencimento = '', datetime.datetime(2023, 1, 1), datetime.datetime(2023, 1, 1)
    self.__dataPagto, self.__valorBoleto, self.__valorPago, self.__situacaoPagamento = datetime.datetime(2023, 1, 1), 0.0, 0.0, 1

  def set_codBarras(self, codBarras):
    try:
      if codBarras.strip() != "":
        self.__codBarras = codBarras
      else: raise ValueError('codBarras não pode ser null')
    except ValueError: print(ValueError)

  def set_dataEmissao(self, dataEmissao):
    self.__dataEmissao = dataEmissao

  def set_dataVencimento(self, dataVencimento):
    self.__dataVencimento = dataVencimento
  
  def set_valorBoleto(self, valorBoleto):
    self.__valorBoleto = valorBoleto
  
  def pagar(self, valorPago):    
    self.__valorPago += valorPago
    if self.__valorBoleto - self.__valorPago <= 0:
      self.__situacaoPagamento = 3
      self.__dataPagto = datetime.datetime.now()
    else: self.__situacaoPagamento = 2

  def situacao(self):
    return Pagamento(self.__situacaoPagamento)

  def __str__(self):
    return f' Cód. de barras: {self.__codBarras}\n Data de Emissão: {self.__dataEmissao}\n Data de vencimento: {self.__dataVencimento}\n Data do último pagamento: {self.__dataPagto}\n Último valor pago: {self.__valorPago} Valor do boleto {self.__valorBoleto}\n Situação de pagamento: {self.__situacaoPagamento}'


class UI:
  def main():
    lista_boletos = []
    comandos = '''Comandos
--> emitir_boleto
--> pagar_boleto (codBarras)
--> situacao (codBarras)
  '''

    while True:
      entrada = input('')
  

UI.main()