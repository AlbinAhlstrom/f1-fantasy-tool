import requests

def get_ids(drivers):
    return {driver["abbreviation"]: id for id, driver in enumerate(drivers)} 

def get_results(drivers):
    return [driver["race_results"] for driver in drivers]

def get_driver_results(drivers, id):
    return drivers[id]["race_results"]

def get_points(drivers, name):
    driver_id = get_ids(drivers)[name]
    driver_results = get_driver_results(drivers, driver_id)
    fantasy_results = [result for result in driver_results if result['id'] == 'weekend_current_points'][0]
    results_per_race_list = fantasy_results['results_per_race_list']
    
    print(f"Points per race for {name}: {results_per_race_list}")

driver_url = "https://f1fantasytoolsapi-szumjzgxfa-ew.a.run.app/race-results/driver?season=2023"
response = requests.get(driver_url)

if response.status_code != 200:
    raise Exception(f"failed to fetch url. {response.status_code}")

drivers = response.json()
get_points(drivers, "VER")