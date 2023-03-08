import requests
from bs4 import BeautifulSoup
from tide import Tide


def getTideData(locs: list):
    """get tide data for a list of locations"""

    for loc in locs:
        print(f"\n########## tide results for {loc} ##########\n")

        # send get request to url for each loc
        processedLoc = loc.replace(", ", "-")
        processedLoc = processedLoc.replace(" ", "-")
        url = f"https://www.tide-forecast.com/locations/{processedLoc}/tides/latest"
        response = requests.get(url)

        # parse html for successful requests (200 = success)
        if response.status_code == 200:
            # parse html from page for specific table we're interested in
            data = []
            soup = BeautifulSoup(response.text, "html.parser")
            table = soup.find("table", attrs={"class": "tide-table__table"})
            rows = table.findAll(lambda tag: tag.name == "tr")

            # assemble data
            for row in rows:
                cols = row.find_all("td")
                cols = [ele.text.strip() for ele in cols]
                data.append([ele for ele in cols if ele])

            data = [row for row in data if row]  # filter empty rows

            # variable amount of items in each row (day could have 1-3 high/low tides in summary on left)
            # going over rows backwards will allow us to match data up reliably
            data = [reversed(row) for row in data]

            # remove last row in data because it's too short and messes up transpose
            # last row is wind data, doesn't matter
            data.pop()

            data = list(zip(*data))  # transpose

            # analyze tide info
            for row in reversed(data):
                lowData = row[2]
                sunriseSunset = row[3]
                # create objects to work with data easier
                tide = Tide(lowData, sunriseSunset)
                if tide.lowTidesDuringDay:
                    for time, mag in tide.lowTidesDuringDay.items():
                        print(f"\tlow tide of {mag}m at {time:%I:%M %p}")
