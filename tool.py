import requests


driver_url = "https://f1fantasytoolsapi-szumjzgxfa-ew.a.run.app/race-results/driver?season=2023"

response = requests.get(driver_url)

if response.status_code == 200:
    data = response.json()

    for driver in data:
        driver_name = driver["abbreviation"]

        print(driver_name)
        # print(driver["color"])
        # print(driver["constructor"])
        # print(driver["race_results"])

else:
    print(f"Could not fetch data. Status code {response.status_code} ")