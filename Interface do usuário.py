from datetime import datetime
from tkinter import *
from PIL import ImageTk,Image
import lookuptable
import requests
import json

def callApi():
	#inplementar a criação automatida da URL + esconder a chave da API
	response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=-22.25&lon=-45.7&lang=pt_br&units=metric&appid=Sua chave da API")
                                                                                                                               #Crie uma no Open wather map: https://openweathermap.org
	#Caso o pedido tenha uma respota retorna-a
	if response.status_code == 200:
		print("sucessfully fetched the data")
		clima = response.json()
		return clima
	else:
		print(f"there's a {response.status_code} error with your request")

clima = callApi()

def jsonCall(y):
	c = lookuptable.caminho2[y]
	#compara o input com as opções e retorna o valor correnspondente
	try:
		if(y == "descrição" or y == "icone"):
			a = lookuptable.caminho2[y]
			resposta = clima[a[0]][0][a[1]]
		else:
			a = lookuptable.caminho2[y]
			resposta = clima[a[0]][a[1]]
	except:
		resposta = "argumento invalido"

	#caso a resposta seja alguma data ou hora pasar de unix para utc
	if(y == "porSol" or y == "nascerSol"):
		resposta = datetime.fromtimestamp(int(resposta))
		resposta = resposta.strftime("%H:%M")
		return resposta

	return str(resposta)

#Inicia o TK com o nome de root (Não tem a ver com root de computador,  é só nome)
root = Tk()
size = (50, 50)

#Configuração da janela do TK
root.title("Clima")
#root.attributes("-fullscreen", True)
root.configure(bg="black")

#Inicia os label para texto colocar só a fonte e a cor do texto
imagem = Label(root, fg = "white", bg = "black")
temp = Label(root, font = ("impact" , 24), fg = "white", bg="black")
solPor = Label(root, font = ("impact" , 24), fg = "white", bg="black")
relogio = Label(root, font = ("impact" , 56), fg = "white", bg="black")
descrição = Label(root, font = ("impact" , 24), fg = "white", bg="black")
solNascer = Label(root, font = ("impact" , 24), fg = "white", bg="black")

#Envia tudo para o root do TK
relogio.pack()
#relogio.place(anchor = "ne")
temp.pack()
descrição.pack()
imagem.pack()
solNascer.pack()
solPor.pack()

#Espaço para os loops de refresh (after function)
def getTime():
	hora = datetime.now()
	hora = hora.strftime("%H:%M:%S")
	relogio.config(text = hora)
	root.after(250, getTime)

#talvez mudar a parte de atribuir o texto pracá ¯\_(ツ)_/¯
def atualizarClima():
	clima = callApi()
	print("Atualizar clima")
	#chamar a api de novo e pegar as informações de novo (testar 900000ms(15 min) e 1800000ms(30 min))
	descrição.config(text=jsonCall("descrição"))
	temp.config(text="Está fazendo " + jsonCall("temperatura") + " C°")
	solPor.config(text="O sol vai se por as: " + jsonCall("porSol"))
	solNascer.config(text="O sol nasceu as: " + jsonCall("nascerSol"))
	#espaço para a imagem
	
	icon = Image.open(lookuptable.icons[jsonCall("icone").strip("'")])
	img = ImageTk.PhotoImage(icon.resize(size))
	imagem.config(image = img)
	imagem.image = img

	root.after(900000, atualizarClima)

#Inicia o mainloop para chamar a janela e inicia os afters
root.after(0, getTime)
root.after(0, atualizarClima)
print("iniciando tk mainloop")
root.mainloop()
print("saiu do tk mainloop")