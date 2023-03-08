from utilities import breakoutPoints, timeHandler


class Tide:
    """class to model the high or low tide occuring on a particular day"""

    def __init__(self, lowData: str, sunriseSunset: str):
        self.lowData = lowData
        self.sunriseSunset = sunriseSunset

    @property
    def sunrise(self):
        """sunrise time (i.e. 7:00AM)"""
        try:
            return timeHandler(self.sunriseSunset.split(" ")[0])
        except:
            pass

    @property
    def sunset(self):
        """sunset time (i.e. 7:00PM)"""
        try:
            return timeHandler(self.sunriseSunset.split(" ")[1])
        except:
            pass

    @property
    def lowTidesDuringDay(self):
        """list of low tide magnitudes occuring during the day"""
        # note - if not both times, then we're dealing with a summary entry that we want to ignore
        if self.sunrise and self.sunset:
            return {
                k: v
                for (k, v) in breakoutPoints(self.lowData)
                if self.sunrise <= k <= self.sunset
            }
        else:
            return {}
