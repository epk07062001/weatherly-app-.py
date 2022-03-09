import tkinter as tk
#import Image, ImageTk
import requests


HEIGHT = 650
WIDTH = 800

def test_function(entry):
	print("This is the entry:", entry)

# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
# a4aa5e3d83ffefaba8c00284de6ef7c3

def format_response(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']

		final_str = 'City: %s \nConditions: %s \nTemperature (°c): %s ' % (name, desc, temp )
	except:
		final_str ='There was a problem retrieving the information of\n' + entry.get() +' or\n the  name you have entered is incorrect'  

	return final_str

def get_weather(city):
	weather_key = '9dd2670e265ea31c7510e8a7f8ffe767'  #api key 9dd2670e265ea31c7510e8a7f8ffe767

	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key, 'q': city, 'units': 'metric' , 'units1':'imperial'}
	response = requests.get(url, params=params)
	weather = response.json()

	label['text'] = format_response(weather)



root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

"""background_widget = tk.PhotoImage(file='weather.png')
background_label = tk.Label(root, image=background_widget)
background_label.place(relwidth=1, relheight=1)"""



frame = tk.Frame(root, bg='#ff3300', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=60)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=40,bg = 'yellow', command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#00ff00', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame , font = 75)
label.place(relwidth=1, relheight=1)

root.mainloop()
