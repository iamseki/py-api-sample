from requests import sessions, RequestException
import time
import csv
import signal
import sys

file = open("ISSposition.tsv", "w")

def signal_handler(sig, frame):
    print("\nExit process gracefuly\nClosing tsv file...")
    file.close()
    sys.exit(0)



try:
    signal.signal(signal.SIGINT, signal_handler)

    writer = csv.writer(file, delimiter='\t')
    writer.writerow(["SN", "latitude", "longitude", "maps"])

    lines = 1

    while(True):
        with sessions.Session() as session:
            res = session.get("https://api.wheretheiss.at/v1/satellites/25544")
            limit = res.headers['X-Rate-Limit-Remaining']

            data = res.json()

            latitude = data["latitude"]
            longitude = data["longitude"]

            maps = "https://maps.google.com/maps?q=" + \
                str(latitude)+","+str(longitude)+"&z=4"


            # Limit rate from ISS Api is ~350 requests in 5 minutes
            # Its API allow us to do one request per second
            if int(limit) > 5:
                print("Tracking international space station:")
                print("It's above us in this location: " + maps)
                writer.writerow([lines, latitude, longitude, maps])
                time.sleep(1)
                lines += 1
                continue
            break

    file.close()
except RequestException as e:
    print(e)
