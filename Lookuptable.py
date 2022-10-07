#fazer o 04d e 04n (muitas núveins)

icons = {
		"01d":"images/Sun.png",
		"01n":"images/Moon.png",
		"02d":"images/PartlySunny.png",
		"02n":"images/PartlyMoon.png",
		"03d":"images/Cloud.png",
		"03n":"images/Cloud.png",
		"04d":"images/PartlySunny.png",
		"04n":"images/PartlyMoon.png",
		"09d":"images/Rain.png",
		"09n":"images/Rain.png",
		"10d":"images/Rain.png",
		"10n":"images/Rain.png",
		"11d":"images/Storm.png",
		"11n":"images/Storm.png",
		"13d":"images/Snow.png",
		"13n":"images/Snow.png",
		"50d":"images/Haze.png",
		"50n":"images/Haze.png"
		}


#And when we kill those God, they won't go to heaven nor hell for these were created to inprison us 
caminho = {
		"nascerSol":'clima["sys"]["sunrise"]',
		"porSol":'clima["sys"]["sunset"]',
		"temperatura":'clima["main"]["temp"]',
		"nuveins":'clima["weather"][0]["description"]',
		"icone":'clima["weather"][0]["icon"]'
}

caminho2 = {
		"nascerSol":("sys", "sunrise"),
		"porSol":("sys", "sunset"),
		"temperatura":("main", "temp")	,
		"descrição":("weather", "description"),
		"icone":("weather", "icon")
}
