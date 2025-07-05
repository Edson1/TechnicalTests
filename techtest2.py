import os, json, requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/ASEAN"
FILE_NAME = "density_data.json"

# get the wiki page
response = requests.get(URL)
soup = BeautifulSoup(response.content, "html.parser")

# find the wikitables
tables = soup.find_all("table", {"class": "sortable wikitable plainrowheaders"})
##print(tables[0])

# Get the 'Urban areas' table rows, skip header row (first row)
data_rows = tables[0].find_all("tr")[1:] 

countries_dictionary = {}

for row in data_rows:
    ##print(row)
    cols_td = row.find_all("td")
    cols_th = row.find_all("th")

    country = cols_td[2].get_text(strip=True)
    core_city = cols_th[1].get_text(strip=True)
    population_text = cols_td[0].get_text(strip=True).replace(",", "")
    area_text = cols_td[1].get_text(strip=True).replace(",", "")

    try:
        population = int(population_text)
        area = float(area_text)
        density = round(population / area, 2)
    except ValueError:
        continue

    ##add new country
    if country not in countries_dictionary:
        countries_dictionary[country] = {
            "cities": [],
            "total_population": 0,
            "total_area": 0.0,
            "population_density": 0.0
        }

    ##add new city to its country
    countries_dictionary[country]["cities"].append({
        "name": core_city,
        "population": population,
        "area": area,
        "density": density
    })

    ##add totals for each country
    countries_dictionary[country]["total_population"] += population
    countries_dictionary[country]["total_area"] += area

##to calculate population density for all countries 
all_population = 0
all_area = 0.0

# Calculate overall density for each country
for country in countries_dictionary:
    total_population = countries_dictionary[country]["total_population"]
    total_area = countries_dictionary[country]["total_area"]

    all_population += total_population
    all_area += total_area

    countries_dictionary[country]["population_density"] = round(total_population / total_area, 2)
    print(f"Country: {country}, Density: {countries_dictionary[country]["population_density"]}")

countries_dictionary["all_population"] = all_population
countries_dictionary["all_area"] = round(all_area, 2)
countries_dictionary["population_density"] = round(all_population / all_area, 2)

# Convert to JSON string
new_data_json = json.dumps(countries_dictionary, indent=2)
print(new_data_json)

print(f"File name: {FILE_NAME}")

# Read old data in existing file
previous_data_json = ""
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        previous_data_json = f.read()

# Compare new data with existing file data, save only if data has changed
if new_data_json != previous_data_json:
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        f.write(new_data_json)
    print("Data updated in file.")
else:
    print("No data changes found.")

