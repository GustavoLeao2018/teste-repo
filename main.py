from marko import *

remarcacao = Markdown()


entrada = open('entrada.md', 'r+')
saida = open('saida.html', 'w+')

saida.write('''
<!DOCTYPE html>
	<html lang="pt-br">
		<head>
			<meta charset="utf-8"/>
			<title>Pacotes</title>

			<style>
				@import "css/estilo.css";
			</style>
		</head>
		<body>

''')
for linha in entrada.readlines():
	saida.write(remarcacao(linha))

saida.write('''

		</body>
	</html>
''')
entrada.close()
saida.close()
