import argparse
import api_call

##########################################################################
# This app is a console based script to get weather information,
# To initialize it run the main script with the desired parameters
# Examples:
#     python weather_app.py current Madrid,ES --units "imperial"
#     python weather_app.py forecast Santander,ES --days 4 --units "metric"

# Run "python weather_app.py --help" for further information.
##########################################################################


# Preparing the arguments
parser = argparse.ArgumentParser()

parser.add_argument(
    "cronologicalTime",
    type=str,
    help="current/forecast",
    default="current"
)

parser.add_argument(
    "location",
    type=str,
    help="City to forecast, EX: Irvine,US",
    default="Santander,ES"
)

parser.add_argument(
    "--days",
    type=int,
    choices=range(1,6),
    help="How many days",
    default=1
)
parser.add_argument(
    "--units",
    type=str,
    choices=["metric","imperial"],
    help="metric/imperial",
    default="metric"
)

# Storing the arguments
inputs = parser.parse_args()

# Invoking the function that is going to call the API
api_call.call(inputs.cronologicalTime,inputs.location,inputs.days,inputs.units)
