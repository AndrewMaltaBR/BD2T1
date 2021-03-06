#   Autor: Andrew Malta e Gabriel Vassoler
#   Obs: usar Python 3.x - ACENTOS NÃO SÃO ACEITOS EM AMBIENTE WINDOWS
#   Comandos:
#       COMANDO TABELA (ARGUMENTO1, ARGUMENTO2)
#       create table cliente (id int, nome varchar(30))
#       insert into cliente (4898, "Joao")
#       delete from cliente where id = 4898
#		select * from cliente -> lista todos os registros
#		show table cliente -> mostra os campos da tabela
#       exit

import Validator
import Executer

print('\nWelcome to best SGBD on universe! Enjoy it xD')
print('Based on Postgres 8.0')
while(True):
	try:
		cmd = input('>>> ')
	except EOFError:
		break
	cmd = Validator.Read(cmd) # valida o comando
	if(isinstance(cmd,list)): # verifica se retornou uma lista
		Executer.Read(cmd) # executa o comando
		#break # usar apenas para testar um comando específico como parâmetro
