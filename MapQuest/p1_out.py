import p1_maps

class Steps:
    def __init__(self, locationList):
        self.jsonData = p1_maps.getDirectionsData(locationList)

    def getInfo(self):

        if self.jsonData["route"]["routeError"]["errorCode"] == 2:
            yield "\nNO ROUTE FOUND"
        elif self.jsonData["route"]["routeError"]["errorCode"] == -400:
            yield "\nDIRECTIONS\n"+self.jsonData["route"]["legs"][0]["origNarrative"]

            manSize = len(self.jsonData["route"]["legs"][0]["maneuvers"])
            for i in range(manSize):
                yield self.jsonData["route"]["legs"][0]["maneuvers"][i]["narrative"]
        else:
            yield "\nMAPQUEST ERROR"

class TotalTime:
    def __init__(self, locationList):
        self.jsonData = p1_maps.getDirectionsData(locationList)

    def getInfo(self):

        if self.jsonData["route"]["routeError"]["errorCode"] == 2:
            yield "\nNO ROUTE FOUND"
        elif self.jsonData["route"]["routeError"]["errorCode"] == -400:
            yield "\nTOTAL TIME: %d minutes" % (self.jsonData["route"]["legs"][0]["time"]/60)
        else:
            yield "\nMAPQUEST ERROR"

class TotalDistance:
    def __init__(self, locationList):
        self.jsonData = p1_maps.getDirectionsData(locationList)

    def getInfo(self):

        if self.jsonData["route"]["routeError"]["errorCode"] == 2:
            yield "\nNO ROUTE FOUND"
        elif self.jsonData["route"]["routeError"]["errorCode"] == -400:
            yield "\nTOTAL DISTANCE: %d miles" % self.jsonData["route"]["legs"][0]["distance"]
        else:
            yield "\nMAPQUEST ERROR"

class LatLong:
    def __init__(self, locationList):
        self.locationList = locationList
        self.jsonData = p1_maps.getDirectionsData(locationList)

    def getInfo(self):

        if self.jsonData["route"]["routeError"]["errorCode"] == 2:
            yield "\nNO ROUTE FOUND"
        elif self.jsonData["route"]["routeError"]["errorCode"] == -400:
            print("\nLATLONGS")
            for i in self.locationList:
                latLng = (p1_maps.getGeocodingData(i))["results"][0]["locations"][0]["latLng"]
                lat = ("%.2f" % latLng["lat"] + "N") if latLng["lat"] > 0 else ("%.2f" % ((-1.0)*(latLng["lat"])) + "S")
                lng = ("%.2f" % latLng["lng"] + "E") if latLng["lng"] > 0 else ("%.2f" % ((-1.0)*(latLng["lng"])) + "W")
                yield lat + " " + lng

        else:
            yield "\nMAPQUEST ERROR"

class Elevation:
    def __init__(self, locationList):
        self.locationList = locationList
        self.jsonData = p1_maps.getDirectionsData(locationList)
    def getInfo(self):

        if self.jsonData["route"]["routeError"]["errorCode"] == 2:
            yield "\nNO ROUTE FOUND"
        elif self.jsonData["route"]["routeError"]["errorCode"] == -400:
            print("\nELEVATIONS")

            for i in self.locationList:
                latLngDict = (p1_maps.getGeocodingData(i))["results"][0]["locations"][0]["latLng"]
                latLng = str(latLngDict["lat"])+ "," +str(latLngDict["lng"])
                yield (p1_maps.getElevationData(latLng))["elevationProfile"][0]["height"]

        else:
            yield "\nMAPQUEST ERROR"