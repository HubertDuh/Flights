import pandas as pd
from pathlib import Path


def fixed_dataset() -> pd.DataFrame:
    flight_list= pd.concat(
        pd.read_csv(file, parse_dates=["firstseen", "lastseen", "day"])
        for file in Path("/Users/hubert/PycharmProjects/Flights/data_set").glob("flightlist_*.csv")
    )
    return flight_list