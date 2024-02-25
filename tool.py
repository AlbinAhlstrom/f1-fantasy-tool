import requests


def get_ids(drivers):
    return {driver["abbreviation"]: id for id, driver in enumerate(drivers)} 


def get_results(drivers):
    return [driver["race_results"] for driver in drivers]

def get_driver_results(name, results):
    print()


driver_url = "https://f1fantasytoolsapi-szumjzgxfa-ew.a.run.app/race-results/driver?season=2023"
response = requests.get(driver_url)

if response.status_code != 200:
    raise Exception(f"failed to fetch url. {response.status_code}")

drivers = response.json()
points = get_ids(drivers)

print(points)
