import requests
BASE = "http://127.0.0.1:5000/"

# 1. Provide the current temperature in °C and °F
#response = requests.get(BASE + "temperature")
#print(response.json())

# 3. Provide the currently set target temperature in °C and °F
#response = requests.get(BASE + "temperature/target")
#print(response.json())

# 2. Provide the current humidity in percent
#response = requests.get(BASE + "/humidity")
#print(response.json())

# 4. Provide the currently set target humidity in percent
#response = requests.get(BASE + "humidity/target")
#print(response.json())

# 5. Set the target temperature to a specific level in °C
#response = requests.put(BASE + "temperature/target", {"New target temperature in Celsius":888})
#print(response)
#response = requests.put(BASE + "temperature/target", {"New target temperature in Celsius":14})
#print(response.json())

# 7. Set the target humidity to a specific level in percent
#response = requests.put(BASE + "humidity/target", {"New target humidity in percent":87})
#print(response.json())
#response = requests.put(BASE + "humidity/target", {"New target humidity in percent":120})
#print(response.json())

# 10. Add an operation to list all existing presets
#response = requests.get(BASE + "preset")
#print(response.json())

# 9. Add an operation to create a preset
#response = requests.put(BASE + "preset", {"temperature": 19, "humidity": 95 } )
#print(response.json())
#response = requests.put(BASE + "preset", {"temperature": 12, "humidity": 15 } )
#print(response.json())

# 12. Add an operation to select and activate a preset by name
#response = requests.post(BASE + "preset", {"preset ID":"1", "isActivated": "True"} )
#print(response.json())
#response = requests.post(BASE + "preset", {"preset ID":"6", "isActivated": "True"} )
#print(response.json())
#response = requests.post(BASE + "preset", {"preset ID":"1", "isActivated": "False"} )
#print(response.json())

# 11. Add an operation to remove a preset by name
#response = requests.delete(BASE + "preset/1")
#print(response.json())
#response = requests.delete(BASE + "/preset/p1")
#print(response.json())
