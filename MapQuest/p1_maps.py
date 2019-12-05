import requests

key = "BA844HbqlDMVtOePiVLlOskI77D3VEM0"
directions = "http://open.mapquestapi.com/directions/v2/route"
elevation = "http://open.mapquestapi.com/elevation/v1/profile"
geocoding = "http://open.mapquestapi.com/geocoding/v1/address"

# direction data in json format
def getDirectionsData(locationList):
    payload = {}

    payload["key"] = key
    for i in range(len(locationList)):
        if(i == 0): payload["from"] = locationList[i]
        else:
            payload["to"] = locationList[i]

    # Replace <directions> with type of url/instruction
    r = requests.get(directions, params = payload)

    return r.json()

# elevation data in json format
# Note: latAndLongPair is a list of two elements
def getElevationData(latAndLongPair):
    payload = {}

    payload["key"] = key
    payload["shapeFormat"] = "raw"
    payload["latLngCollection"] = latAndLongPair
    r = requests.get(elevation, params = payload)

    return r.json()
# geocoding data in json format
def getGeocodingData(location):
    payload = {}

    payload["key"] = key
    payload["location"] = location
    r = requests.get(geocoding, params = payload)

    return r.json()
