from main import getTideData

if __name__ == "__main__":
    # locations where we want to get tide info
    locs = [
        "Half Moon Bay, California",
        "Huntington Beach",  # note - omitting 'California' from this name to conform with site
        "Providence, Rhode Island",
        "Wrightsville Beach, North Carolina",
    ]

    getTideData(locs)
