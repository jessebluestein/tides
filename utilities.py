from datetime import time


def separateTimeVal(pt: str):
    """given a point, separate the time from the value.
    break on capital M, because both AM/PM have that char"""

    pts = pt.split("M")
    time = pts[0] + "M"  # put M back
    time = timeHandler(time)
    val = float(pts[1].replace("m", ""))
    return (time, val)


def breakoutPoints(pt: str):
    """given a string (i.e. 10:32AM0.25m 9:31PM0.92m) or (i.e. 11:42AM0.09m10:54PM1.02m),
    break out into n points (n=1-3)"""

    pts = pt.split(" ")  # could be 1-3 tides per day

    # need this to handle 1% of cases - sometimes space is omitted
    # super long string that contains multiple points but didn't split
    processedPts = []
    for pt in pts:
        if len(pt) > 15:
            pt = pt.replace("m", "m ")  # add in missing space
            subpts = pt.split(" ")
            for pt in subpts:
                if pt:
                    processedPts.append(pt)
        else:
            processedPts.append(pt)

    # return list of tuples where each tuple is (time, val)
    tuplesList = []
    for pt in processedPts:
        tuplesList.append(separateTimeVal(pt))

    return tuplesList


def timeHandler(tm: str):
    """given a time string (i.e. 6:59AM), convert to time object"""

    # strip am/pm, note if pm so we can add 12 hours later
    isPm = "PM" in tm
    tm = tm.replace("AM", "")
    tm = tm.replace("PM", "")

    # split into hours and mins, add 12 for pm times
    hm = tm.split(":")
    h = int(float(hm[0]))
    m = int(float(hm[1]))
    if isPm and h != 12:
        h += 12

    return time(h, m)
