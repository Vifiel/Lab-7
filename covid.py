import requests as rq

#NB вообще, сайт перестал выгружать новые данные, api всегда возвращает
#сводку от 7 мая 2021, но работать с ним это не особо мешает

generally = rq.get("https://api.covidtracking.com/v1/us/current.json").json()
hist = rq.get("https://api.covidtracking.com/v1/us/daily.json").json()
states = rq.get("https://api.covidtracking.com/v1/states/current.json").json()

date = str(generally[0]["date"])
date = f"{date[:4]}-{date[4:6]}-{date[6:]}"

most_positive_state = max(states, key=lambda x:x["positive"])["state"]

tested = generally[0]["totalTestResults"]

neg = generally[0]["negative"]

hosp = [i["hospitalized"] for i in hist[:100]]
hosp = [i if i else 0 for i in hosp]
average_hosp = sum(hosp)//len(hosp)

print(f"At the moment of {date} in US such ststistics about Covid-19 is avilable:\n")
print(f"Today tested {tested} people")
print(f"Of this tests {neg} are negative")
print(f"The most of positive tests are in {most_positive_state}")
print(f"Today hospitalised {hosp[0]} people")
print(f"Average hospitalisation per day for past 100 days: {average_hosp}")

