#Python program: Weather system

import requests

choice = ''
save = []
searched = False

print('\033[0;32mWelcome to this weather program!\033[0m')
print('\033[0;36mEnter numbers to select actions.\033[0m')
print()

class main:
    def __init__(api_key):  #Initialize
        api_key = 'e3e17e44b9c86ed9c4398c45a14a0512'
    def get_weather():  #This part of code asks user to enter a city, then get data from OpenWeatherMap and analyze it, at last show the information to the user.
        global searched, city, country, description, temperature, humidity, pressure
        city = input('\033[0;35mPlease enter city name: \033[0m')
        print('\033[0;34mLoading data...please wait.\033[0m')
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        if response.status_code == 200:
            searched = True
            data = response.json()
            print()
            country = data['sys']['country']
            description = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            pressure = data['main']['pressure']
            print('\033[0;36mWeather in',city+':\033[0m')
            print('Country:',country)
            print('Description:',description)
            print('Temperature:',str(temperature)+'°C')
            print('Humidity:',str(humidity)+'%')
            print('Pressure:',str(pressure)+'hPa')
            print()
        else:
            searched = False
            print('\033[0;31mThe city doesn’t exist, please check your spelling and try again.\033[0m')
    def save():  #This part of code works for saving process.
        global searched, city, country, description, temperature, humidity, pressure
        if searched == True:
            save.append([city, country, description, temperature, humidity, pressure])
            print('\033[0;32mSuccessfully saved!\033[0m')
        else:
            print('\033[0;31mYou haven’t searched anything yet!\033[0m')
    def show_save():  #This part of code works for showing all saves of the user.
        if len(save) == 0:
            print('\033[0;31mYou haven’t saved anything yet!\033[0m')
        else:
            print('\033[0;34mYour save:\033[0m')
            a = len(save)
            b = 0
            for i in range(a):
                print('\033[0;36mCompare to weather in',save[b][0]+':\033[0m')
                print('Country:',save[b][1])
                print('Description:',save[b][2])
                print('Temperature:',str(save[b][3])+'°C')
                print('Humidity:',str(save[b][4])+'%')
                print('Pressure:',str(save[b][5])+'hPa')
                print()
                b += 1
    def compare():  #This part of code allows user to compare current city's weather situation to all saved cities.
        if len(save) == 0:
            print('\033[0;31mYou haven’t saved anything yet!\033[0m')
        else:
            a = len(save)
            b = 0
            text = ''
            for i in range(a):
                if temperature - save[b][3] > 0:
                    text1 = '\033[0;32m(+'+str(round(temperature - save[b][3],2))+'°C)\033[0m'
                elif temperature - save[b][3] < 0:
                    text1 = '\033[0;31m(-'+str(round(save[b][3] - temperature,2))+'°C)\033[0m'
                elif temperature - save[b][3] == 0:
                    text1 = '\033[0;36m(=0°C)\033[0m'
                if humidity - save[b][4] > 0:
                    text2 = '\033[0;32m(+'+str(round(humidity - save[b][4],2))+'%)\033[0m'
                elif humidity - save[b][4] < 0:
                    text2 = '\033[0;31m(-'+str(round(save[b][4] - humidity,2))+'%)\033[0m'
                elif humidity - save[b][4] == 0:
                    text2 = '\033[0;36m(=0%)\033[0m'
                if pressure - save[b][5] > 0:
                    text3 = '\033[0;32m(+'+str(round(pressure - save[b][5],2))+'hPa)\033[0m'
                elif pressure - save[b][5] < 0:
                    text3 = '\033[0;31m(-'+str(round(save[b][5] - pressure,2))+'hPa)\033[0m'
                elif pressure - save[b][5] == 0:
                    text3 = '\033[0;36m(=0hPa)\033[0m'
                print('\033[0;36mWeather in',save[b][0]+':\033[0m')
                print('Country:',save[b][1])
                print('Description:',save[b][2])
                print('Temperature:',str(save[b][3])+'°C'+text1)
                print('Humidity:',str(save[b][4])+'%'+text2)
                print('Pressure:',str(save[b][5])+'hPa'+text3)
                print()
                b += 1
    def end():  #This part of code is to end the program.
        print('\033[0;32mProgram ended successfully.\033[0m')
        print('\033[0;36mThanks for using!\033[0m')
        
weather = main()

while choice != '5':  #This is the main loop, the whole program works based on it.
    api_key = 'e3e17e44b9c86ed9c4398c45a14a0512'
    print('\033[0;35mWhat you gonna do?\033[0m')
    print('1.Search the weather of a city    2.Save    3.Show your save    4.Compare to your save    5.End program')
    choice = input()
    if choice == '1':
        main.get_weather()
    elif choice == '2':
        main.save()
    elif choice == '3':
        main.show_save()
    elif choice == '4':
        main.compare()
    elif choice == '5':
        main.end()
    else:
        print('\033[0;31mInvalid input, please try again.\033[0m')