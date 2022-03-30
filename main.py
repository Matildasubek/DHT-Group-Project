'''
Swagger API specification and a corresponding running implementation in Python programming language for an AC system
Code an Air Conditioning System API in python.

You must create a Swagger API specification and a corresponding running implementation in Python programming language.
The body parameters of the request and the response object are implemented as JSON objects. The specification and
implementation of the API must include all described functions including the required error handling covering client
side errors in case of values of ingoing parameters outside of the specified bounds.

The OR Air Conditioning System API should provide the following functions:

       1. Provide the current temperature in degree C and degree F.
       2. Provide the current humidity in percent.
       3. Provide the currently set target temperature in degree C and degree F.
       4. Provide the currently set target humidity in percent.
       5. Set the target temperature to a specific level in degree C.
       6. Do not accept values above 20 degree C and below 5 degree C.
       7. Set the target humidity to a specific level in percent.
       8. Manage a set of presets that consist of name, target humidity and temperature.
       9. Add a operation to create a preset.
       10. Add a operation to list all existing presets.
       11. Add a operation to remove a preset by name.
       12. Add a operation to select and activate a preset by name.

Group 9: Esskaros Marian, Haas Amelie, Larios Edina, Nwawudu Sixtus, Semenova Svetlana, Subek Simon Matilda
'''

#Importing the necessary packages
from flask import Flask, abort, Response #flask is a library to use an API
from flask_restful import Api, Resource, reqparse #Import of API, resources and request/parse

#To initalize the server
app = Flask(__name__)
'''
The Flask web application framework is assigned to the "app" variable.
The __name__ variable (two underscores before and after) is a special Python variable, it gets its value depending on
how we execute the containing script.
'''
api = Api(app)
'''
The API is assigned to the variable "api" with the previously assigned "app" as value 
'''

#################################################### Temperature API ####################################################
currentTemperatureValueInC = 27
targetTemperatureValueInC = 22
'''
our reference temperature and humidity is based on the HVAC guidelines for DACH (Deutschland, Oesterreich, Schweiz)
(Quelle: Deutsche Gesellschaft für Krankenhaush*giene)
'''

# Function to convert Fahrenheit degrees to Celsius degrees
def ConvertToF(TemperatureInC):
    return (TemperatureInC * 9/5) + 32

#Assigning the current and target temperatures with values in a dictionary
currentTemperatureJson = {"current Temperature": {"in Celsius degree": currentTemperatureValueInC, "in Fahrenheit degree":ConvertToF(currentTemperatureValueInC)}}
TargetTemperatureJson = {"target Temperature": {"in Celsius degree": targetTemperatureValueInC, "in Fahrenheit degree":ConvertToF(targetTemperatureValueInC)}}

# 1. Provide the current temperature in °C and °F
class TemperatureIs(Resource): #created a class for the current (room) temperature
    def get(self):
        '''
        The get method retrieves a specific information from the server and prints it on the website.
        Because dictionaries are compatible with the JSON-format, the dictionary is displayed in JSON format.
        :return: The current temperature should be shown here in degree Celsius and in degree Fahrenheit.
        '''
        return currentTemperatureJson # when this class is called upon, it will return the assigned variable "currentTemperatureJson"

# 3. Provide the currently set target temperature in °C and °F
class TemperatureTarget(Resource): # created a class for the desired (target) temperature
    def get(self):
        '''
        The get method retrieves a specific information from the server and prints it on the website.
        Because dictionaries are compatible with the JSON-format, the dictionary is displayed in JSON format.
        :return: The currently set target temperature should be shown here.
        '''
        return TargetTemperatureJson # when this class is called upon, it will return the assigned variable "TargetTemperatureJson"

# 5. Set the target temperature to a specific level in °C
    def put(self):
        '''
        The put method allows the user to add new information through the test-file.
        This new information needs to be in a specific format so the api is able to parse it to the server.
        :return: If the entered temperature is between 5 and 20 degrees Celsius, it is set as the new target temperature
        and is displayed.
        If the entered temperature is NOT between 5 and 20 degrees Celsius, a message is displayed, saying an invalid
        value has been entered.
        '''
        targetTemperature_put_args = reqparse.RequestParser() #activating the parsing function
        targetTemperature_put_args.add_argument("New target temperature in Celsius", type=float,
                                     help="What's the target temperature in Celsius?")
        # from the response (from the secondary test script) the new target temperature is parsed
        args = targetTemperature_put_args.parse_args() # the parsed variable targetTemperature_put_args is "switched" to
        #the new "args" variable
        """
        targetTemperature_put_args is the variable defined to contain the newly entered information. 
        It is equal to the reqparse from the RequestParser. The following lines define the arguments which are uploaded 
        through the new information. The argument parsed needs to be called "New target temperature in Celsius" 
        and consist of a value of the type=float.  
        The variable args is defined as a dictionary of the newly implemented information.
        """
# 6. Do not accept values above 20 °C and below 5 °C
        if args["New target temperature in Celsius"] < 5 or args["New target temperature in Celsius"] > 20:
            return {"Error": "Invalid temperature value! Temperature must be between 5 and 20 degree Celsius!"},406
        else:
            targetTemperatureValueInC = args["New target temperature in Celsius"]
            return {"New target temperature in Celsius": targetTemperatureValueInC}
        '''
        args["New target temperature in Celsius"] looks into the dictionary args which we defined above and searches for
        the parameter "New target temperature in Celsius". If this value is <5 or >20, an Error message is returned.
        If that entered value is between 5 and 20, the targetTemperatureValueInC, which has been defined in line 44, 
        is set to a the new value that has been parsed.
        '''

api.add_resource(TemperatureIs, "/temperature")
api.add_resource(TemperatureTarget, "/temperature/target")
'''
For the implementation of the current and target temperature, an url path has to be defined and the classes 
TemperatureIs and TargetTemperature have to be created.
Here the temperatures can be called and amended.
'''
#################################################### Temperature API ####################################################

##################################################### Humidity API ######################################################
CurrentHumidity = 50
targetHumidity = 35
'''
our reference temperature and humidity is based on the HVAC guidelines for DACH (Deutschland, Österreich, Sweiz)
(Resource: Deutsche Gesellschaft für Krankenhaushygiene)
'''

# 2. Provide the current humidity in percent
class HumidityIs(Resource):
    def get(self):
        '''
        The get method retrieves a specific information from the server and prints it on the website.
        Because dictionaries are compatible with the JSON-format, the dictionary is displayed in JSON format.
        :return: The current humidity should be shown here in percent.
        '''
        return {"Current humidity in Percent": CurrentHumidity}

# 4. Provide the currently set target humidity in percent
class TargetHumidity(Resource):
    def get(self):
        '''
        The get method retrieves a specific information from the server and prints it on the website.
        Because dictionaries are compatible with the JSON-format, the dictionary is displayed in JSON format.
        :return: The currently set target humidity should be shown here in percent.
        '''
        return {"Target humidity in Percent": targetHumidity}

# 7. Set the target humidity to a specific level in percent
    def put(self):
        '''
        The put method allows the user to add new information through the test-file.
        This new information needs to be in a specific format so the api is able to parse it to the server.
        :return: If the entered humidity is between 0 and 100 percent, it is set as the new target humidity
        and is displayed.
        If the entered humidity is NOT between 0 and 100 percent, a message is displayed, saying an invalid
        value has been entered.
        '''
        targetHumidity_put_args = reqparse.RequestParser()
        targetHumidity_put_args.add_argument("New target humidity in percent", type=float,
                                     help="What's the target humidity in percentage?")
        args = targetHumidity_put_args.parse_args()
        '''     
        targetHumidity_put_args is the variable defined to contain the newly entered information. 
        It is equal to the reqparse from the RequestParser. The following lines define the arguments which are uploaded 
        through the new information. The argument parsed needs to be called "New target humidity in percent" 
        and consist of a value of the type=float.  
        The variable args is defined as a dictionary of the newly implemented information.
        '''
#BONUS: Do not accept values above 100 % and below 0 %
        if args["New target humidity in percent"] < 0 or args["New target humidity in percent"] > 100:
            return {"Error": "Invalid humidity value! Humidity value must be between 0 and 100 percent!"},406
        else:
            targetHumidity = args["New target humidity in percent"]
            return {"New target humidity in percent": targetHumidity}
        '''
        args["New target humidity in percent"] looks into the dictionary args which we defined above and searches for
        the parameter "New target humidity in percent". If this value is <0 or >100, an Error message is returned.
        If that entered value is between 0 and 100, the targetHumidity, which has been defined in line 125, 
        is set to a the new value that has been parsed.
        '''

api.add_resource(HumidityIs, "/humidity")
api.add_resource(TargetHumidity, "/humidity/target")
'''
For the implementation of the current and target humidity, an url path has to be defined and the classes
HumidityIs and TargetHumidity have to be created.
Here the Humidity can be called and amended.
'''
##################################################### Humidity API ######################################################

###################################################### Preset API #######################################################
# 8. Manage a set of presets that consist of name, target humidity and temperature
presetDic = {"1":{"temperature": 20, "Humidity": 99, "IsActivated":False },
             "2":{"temperature": 10, "Humidity": 88, "IsActivated":False },
             "3":{"temperature": 0, "Humidity": 77, "IsActivated":False },}
'''
With the "presetDic" we implement a dictionary to store saved sets. Three programs are already given.
the programs' activity is set to False by default.
'''

# 10. Add an operation to list all existing presets
class Preset(Resource):
    def get(self):
        '''
        The get method retrieves a specific information from the server and prints it on the website.
        Because dictionaries are compatible with the JSON-format, the dictionary is displayed in JSON format.
        :return: All implemented and saved presets should be shown here.
        '''
        return presetDic
# 9. Add an operation to create a preset
    def put(self):
        '''
        The put method allows the user to add new information through the test-file.
        This new information needs to be in a specific format so the api is able to parse it to the server.
        :return: If both conditions are fulfilled the new preset is added to the
        existing preset dictionary and same updated dictionary is displayed.
        '''
        preset_put_args = reqparse.RequestParser()
        preset_put_args.add_argument("temperature", type=float)
        preset_put_args.add_argument("humidity", type=float)
        #preset_put_args.add_argument("preset ID", type=str)
        args = preset_put_args.parse_args()
        preset_id = int(max(presetDic.keys())) + 1
        preset_id = '%i' % preset_id
        print(preset_id)
        print(presetDic.keys())
        '''
        preset_put_args is the variable defined to contain the newly entered information. 
        It is equal to the reqparse from teh RequestParser. The following lines define the arguments which are uploaded 
        through the new information. One argument, e.g., of the parsed information needs to be called "temperature" and
        consist of a value of the type=float.  
        The variable args is defined as a dictionary of the newly implemented information.
        print(presetDic.keys()) prints and shows the titles of the dictionary entries in the original dictionary.
        '''
        if preset_id in presetDic.keys():
            return {"Error": "This ID already exist!"}, 400
        elif args["temperature"] < 5 or args["temperature"] > 20:
            return {"Error": "Invalid temperature value! Temperature must be between 5 and 20 degree Celsius!"}, 404
        elif args["humidity"] < 0 or args["humidity"] > 100:
            return {"Error": "Invalid humidity value! Humidity value must be between 0 and 100 percent!"}, 406
        else:
            presetDic[preset_id] = {"temperature": args["temperature"], "humidity": args["humidity"], "IsActivated":False}
            return presetDic
        '''
        The elif-function checks if the ID of the newly entered dataset already exists,  
        if the temperature is between 5°C and 20°C as required, and if the humidity is between 0 and 100 percent. 
        If the ID is already in use or the temperature is outside that range, a error-message is returned. If both 
        conditions are fulfilled the new preset is added to the existing preset dictionary and same updated dictionary 
        is displayed. 
        '''

# 12. Add an operation to select and activate a preset by name
    def post(self):
        '''
        The post method can be used to amend data which has already been stored.
        This function checks what preset is mentioned and what values the newly input values have and if the "
        isActivated" part is now true instead of false, it activates the preset and vice versa.
        :return: Depending on outcome of the conditions several returns are possible. Refers the user to a non existing
        preset, the program will tell him. otherwise the message Set activated or Set deactivated will be displayed.
        '''
        presetActivate_put_args = reqparse.RequestParser()
        presetActivate_put_args.add_argument("preset ID", type=str)
        presetActivate_put_args.add_argument("isActivated", type=str)
        activateArgs = presetActivate_put_args.parse_args()
        print(activateArgs)
        '''
        As in the put method the presetActivate is the variable where the new information is parsed to.
        Afterwards the arguments are defined by their title and value type. The activateArgs is the dictionary
        where the information is parsed to. This dictionary is printed after the definition and Parse.
        '''
        if activateArgs["preset ID"] not in presetDic.keys():
            return {"Error": "This ID does not exist!"}, 404
        else:
            nameInTheData = activateArgs["preset ID"]
            activation = activateArgs["isActivated"] == "True"
            '''A Boolean function cannot be used due to an error in the Flas library.
            Therefore the boolean value is converted into a string value'''
            presetDic[nameInTheData][activation] = activation
            return {"message": "Set status changed correctly!"}

        '''
        The condition for the activation of a set is that the set actually exists. 
        Therefore the "name" in the parsed dictionary activateArgs needs to also be in the existing 
        presentDic.key - values. If the name parsed is NOT in the presetDic, the the method returns an error message and
        aborts it. If the name parsed is in the present Dic, the activateArgs dictionary is divided into two variables: 
        The nameInTheData is defined as what is parsed under "name" and IsActivated is defined as what is parsed under 
        "isActivated". The presetDic dictionary is advised to look for for the name first and then the argument 
        IsActivated. The value of the argument IsActivated is set to the IsActivated variable, which is the parsed
        new information. 
        If it the value IsActivated is True, the message Set activated is displayed and if the value is not true, 
        therefore false, the message Set deactivated is displayed. 
        '''
api.add_resource(Preset, "/preset")
'''
For the implementation of the presets, an url path has to be defined and the class Preset has to be created.
Here the presets can be called, amended, added.
'''

# 11. Add an operation to remove a preset by name
class PresetManagement(Resource):
    def delete(self, preset_id):
        if preset_id not in presetDic:
            return {"Error":"Preset ID does not exist!"},404
        else:
            del presetDic[preset_id]
            return presetDic

api.add_resource(PresetManagement,"/preset/<preset_id>")
'''
For the implementation of the presets, an url path has to be defined and the class PresetManagement has to be created.
Here the presets can be deleted.
'''
###################################################### Preset API #######################################################

'''
This is a Python specific format to tell Python to start the code from here.
So in this case: the program (that will follow from the top) must run in debug mode
'''
if __name__ == "__main__":
    app.run(debug=True)

