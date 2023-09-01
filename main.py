import re
#from cpf_cnpj import Documento
#from validate_docbr import CNPJ
from TelefonesBr import TelefonesBr

telefone = "553187227409"

telefone_objeto = TelefonesBr(telefone)

print(telefone_objeto)


'''
exemplo_cnpj = "35379838000112"
exemplo_cpf = "13473507644"

documento = Documento.cria_documento(exemplo_cnpj)
print(documento)
documento = Documento.cria_documento(exemplo_cpf)
print(documento)
'''