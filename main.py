
from cpf_cnpj import CpfCnpj
from validate_docbr import CNPJ

#cpf_um = Cpf("13473507644")
#print(cpf_um)

exemplo_cnpj = "35379838000112"
exemplo_cpf = "13473507644"

documento = CpfCnpj(exemplo_cnpj,'cnpj')
print(documento)
documento = CpfCnpj(exemplo_cpf,'cpf')
print(documento)