import requests
import json
import os

print("Welcome to WeatherApp ; Created by Abdullah Sarfraz\n")
quest = input("Please enter 'Temp' for Temperature of City only or write 'Info' for detailed weather information\n\n")
API_Key = "https://api.weatherapi.com/v1/current.json?key=1c5fac0fa37b4cbf89b180552230810&q="
if quest == "Temp":
    city = input("Please Enter the City name for Weather Information\n")
    url = f"{API_Key}{city}"

    W_Result = requests.get(url)
    # print(W_Result.text)
    F_w_result = json.loads(W_Result.text)
    # print(F_w_result.values())
    # print(F_w_result["current"]["temp_c"])
    temp = F_w_result["current"]["temp_c"]
    print("\n")
    print(f"Weather in {city} is {temp} degree\n")

    testing = f"Weather in {city} is {temp} degree"
    # command = f"Is str:str works {testing}"
    # print(command)
    command = f"echo {testing} | powershell -ExecutionPolicy Bypass -File text2speech.ps1"
    os.system(command)
elif quest == "Info":
    Info = input("Please enter the City name \n")
    url = f"{API_Key}{Info}"
    w_info = requests.get(url)
    f_w_info = json.loads(w_info.text)
    temp = f_w_info["current"]["temp_c"]
    moreInfo = f_w_info["current"]["last_updated"]
    localtime = f_w_info["location"]["localtime"]
    print("\n")
    print(f"Weather in {Info} is {temp} degree and it was last time update at {moreInfo}\n")
    print(f"\n\nCurrent time : {localtime}")
else:
    print("Please give valid input!")


