moscow_weather={
    'city':'Moscow',
    'temperature':20
}
print(moscow_weather['city'])
moscow_weather['temperature']-=5
print(moscow_weather)
print(moscow_weather.get('country'))
print(moscow_weather.get('country','Россия'))
moscow_weather['date']='27.05.2019'
print(moscow_weather)
print(len(moscow_weather))