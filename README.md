# tides

This script uses web scraping to grab data from `www.tide-forecast.com` and print out low tides that occur during the day at the locations entered in `entrypoint.py`. Please see the following instructions for running the script.

# Step 1: Setup Virtual Environment

It is recommended to run the script from a virtual environment. However, the user could also opt to install the dependencies directly to their machine without using a virtual environment, although this is not recommended.

```
python -m venv venv (windows)
python3 -m venv venv (mac)
```

# Step 2: Activate Virtual Environment

```
venv\Scripts\activate (windows)
source venv/bin/activate (mac)
```

# Step 3: Install Requirements (In Virtual Environment)

```
pip install -r requirements.txt
```

# Step 4: Call Script (From Root Directory)

Note - change `entrypoint.py` as required to input the desired locations.

```
python entrypoint.py
```