#from cpf_cnpj import Documento
#from TelefonesBr import TelefonesBr
#from datas_br import DatasBr
from acesso_cep import BuscaEndereco


# Pegar dados CEP
cep = 31741377
objeto_cep = BuscaEndereco(cep)

bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(bairro, cidade, uf)



'''
# Datas
cadastro = DatasBr()
print(cadastro)

hoje = DatasBr()
print(hoje.tempo_cadastro())

# Telefones
telefone = "553187227409"
telefone_objeto = TelefonesBr(telefone)
print(telefone_objeto)

# CPF/CNPJ
exemplo_cnpj = "35379838000112"
exemplo_cpf = "13473507644"
documento = Documento.cria_documento(exemplo_cnpj)
print(documento)
documento = Documento.cria_documento(exemplo_cpf)
print(documento)
'''