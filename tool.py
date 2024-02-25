import requests


def get_names(drivers):
    return [driver["abbreviation"] for driver in drivers]


driver_url = "https://f1fantasytoolsapi-szumjzgxfa-ew.a.run.app/race-results/drive?season=2023"
response = requests.get(driver_url)

if response.status_code != 200:
    raise Exception(f"failed to fetch url. {response.status_code}")

drivers = response.json()
points = get_names(drivers)

print(points)
