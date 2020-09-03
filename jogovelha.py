Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def inicializar():
	tab = [ ]
	for i in range(3):
		linha = [ ]
		for j in range(3):
			linha.append(".")
		tab.append(linha)
	return tab

def main( ):
	jogo = inicializar( )
	print (jogo)

if __name__ == "__main__":
	main()
