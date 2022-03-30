# Hospital-Airconditioning-System-API

Swagger API specification and a corresponding running implementation in Python. The body parameters of the request and the response object are implemented as JSON objects. 
The OR Air Conditioning System API provide the following functions:

Provide the current temperature in °C and °F.
Provide the current humidity in percent.
Provide the currently set target temperature in °C and °F.
Provide the currently set target humidity in percent.
Set the target temperature to a specific level in °C.
Do not accept values above 20 °C and below 5 °C.
Set the target humidity to a specific level in percent.
Manage a set of presets that consist of name, target humidity and temperature.
Add a operation to create a preset.
Add a operation to list all existing presets.
Add a operation to remove a preset by name.
Add a operation to select and activate a preset by name.
