from typing import List
import pandas as pd
from datetime import date, timedelta


CONFIRMED_CASES_URL = f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv "

confirmed_cases = pd.read_csv(CONFIRMED_CASES_URL, error_bad_lines=False)

def poland_cases_by_date(day: int, month: int, year: int = 2020) -> int:
    return confirmed_cases.loc[confirmed_cases["Country/Region"] == "Poland"][f"{month}/{day}/{str(year-2000)}"].values[0]

def top5_countries_by_date(day: int, month: int, year: int = 2020) -> List[str]:
    topfive = confirmed_cases.groupby("Country/Region").sum()
    return list(topfive.sort_values(by=[f"{month}/{day}/{str(year-2000)}"], ascending=False).head(5).index)

def no_new_cases_count(day: int, month: int, year: int = 2020) -> int:
    yesterday = date(year, month, day) - timedelta(days=1)
    yesterday_str = f"{yesterday.month}/{yesterday.day}/{str(yesterday.year)[:2]}"
    date_str = f"{month}/{day}/{str(year)[:2]}"
    output = (confirmed_cases.loc[confirmed_cases[date_str] != confirmed_cases[yesterday_str]]).shape[0]
    return output
