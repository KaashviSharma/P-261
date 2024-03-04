import requests
import json
equation = input("Enter your equation : ")
result = "https://newton.now.sh/api/v2//simplify/"+equation
data = requests.get(result).json()
print("Operation for given equation : ", data['operation'])
print("Expression for given eqation : ", data['expression'])
print("Results of given equatin : ", data['result'])