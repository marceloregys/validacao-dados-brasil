from cpf_cnpj import Documento
from validate_docbr import CNPJ

#cpf_um = Cpf("13473507644")
#print(cpf_um)

exemplo_cnpj = "35379838000112"
exemplo_cpf = "13473507644"

documento = Documento.cria_documento(exemplo_cnpj)
print(documento)
documento = Documento.cria_documento(exemplo_cpf)
print(documento)