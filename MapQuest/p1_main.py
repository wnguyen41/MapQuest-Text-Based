import p1_maps
import p1_out

def main():
    numOfLocat = int(input())
    if(numOfLocat >= 2):
        locationsList = []
        for i in range(numOfLocat):
            locationsList.append(input())

        numOfOut = int(input())
        outputList = []
        if(numOfOut < 1):
            print("Invalid number of outputs.")
        else:
            for i in range(numOfOut):
                outputList.append(input())

        for i in range(numOfOut):
            instr = outputList[i]

            if instr == "TOTALTIME":
                time = p1_out.TotalTime(locationsList)
                for i in time.getInfo():
                    print(i)

            elif instr == "TOTALDISTANCE":
                dist = p1_out.TotalDistance(locationsList)
                for i in dist.getInfo():
                    print(i)

            elif instr == "STEPS":
                steps = p1_out.Steps(locationsList)
                for i in steps.getInfo():
                    print(i)

            elif instr == "LATLONG":
                latlng = p1_out.LatLong(locationsList)
                for i in latlng.getInfo():
                    print(i)

            elif instr == "ELEVATION":
                elev = p1_out.Elevation(locationsList)
                for i in elev.getInfo():
                    print(i)

    else:
        print("Invalid number of locations.")

    print("\nDirections Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors")

main()