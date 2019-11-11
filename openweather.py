import requests
import sys


apikey = 'f193c0e61ed85d15bdea31e2e6dd0f1f'
weather_url = "http://api.openweathermap.org/data/2.5/weather"  # get kondisi saat ini
    # weather_url = "http://api.openweathermap.org/data/2.5/forecast" # get untuk peramalannya

def getWeather(city_name):
    # print(weather_url)
	r = requests.get(weather_url, params={'q': city_name, 'APPID': apikey})
	r.url  # `requests` help us encode the URL in the correct format
	r.status_code  # 200 means success
	result = r.json()
	return print(result) #print akan menjadi stdout pada backend django


if __name__ == "__main__":
	# Ketika file.py ini dieksekusi, kode berikut akan dijalankan
    a = str(sys.argv[1]) #argument yang dipassing di cast dalam bentuk string
    getWeather(a) #jalankan fungsi getWeather
