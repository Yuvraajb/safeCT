import csv
import numpy as np

# Define realistic bounds for scaling (0 = worst, 100 = best)
REALISTIC_MIN = 0  # Lowest possible safety index (worst)
REALISTIC_MAX = 100  # Highest possible safety index (best)

# Read CSV data
csv_file = '/Users/yuvraaj/Desktop/SafeCT/safe_ct/dataset/train.csv'  # Replace with your CSV file path
data = []

# Define crime weights for each category (adjusted)
crime_weights = {
    "PORNOGRAPHY/OBSCENE MAT": 10,
    "FAMILY OFFENSES": 15,
    "LARCENY/THEFT": 30,
    "DISORDERLY CONDUCT": 12,
    "GAMBLING": 14,
    "SECONDARY CODES": 5,
    "BRIBERY": 18,
    "LIQUOR LAWS": 10,
    "BURGLARY": 35,
    "VEHICLE THEFT": 28,
    "ROBBERY": 50,  # Increased weight for more severe crime
    "SEX OFFENSES FORCIBLE": 55,  # Increased weight for more severe crime
    "VANDALISM": 20,
    "WEAPON LAWS": 40,
    "BAD CHECKS": 12,
    "WARRANTS": 18,
    "RUNAWAY": 8,
    "SEX OFFENSES NON FORCIBLE": 30,
    "FRAUD": 25,
    "SUICIDE": 60,  # Increased weight due to the severity of this category
    "TREA": 22,
    "EMBEZZLEMENT": 20,
    "STOLEN PROPERTY": 20,
    "RECOVERED VEHICLE": 10,
    "LOITERING": 5,  # Lower weight for less severe crimes
    "PROSTITUTION": 18,
    "DRUG/NARCOTIC": 40,
    "ARSON": 50,  # Increased weight for arson
    "NON-CRIMINAL": 2,
    "MISSING PERSON": 8,
    "EXTORTION": 30,
    "FORGERY/COUNTERFEITING": 28,
    "SUSPICIOUS OCC": 15,
    "OTHER OFFENSES": 12,
    "ASSAULT": 45,
    "TRESPASS": 15,
    "DRIVING UNDER THE INFLUENCE": 20,
    "DRUNKENNESS": 15,
    "KIDNAPPING": 60,  # Very high weight for kidnapping
}

# Step 1: Read the CSV file and collect crime categories
crime_categories = set()

with open(csv_file, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        crime_categories.add(row["Category"])

# Step 2: Process the data and assign the crime weights dynamically
with open(csv_file, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        record = {
            "month_year": row["Dates"],  # You can modify this if needed
            "location": row["PdDistrict"],  # Assuming location is in 'PdDistrict'
            "category": row["Category"],  # Storing the crime category
        }
        
        # Initialize crime count as 0 for each category
        for category in crime_categories:
            record[category] = 1 if row["Category"] == category else 0
        
        data.append(record)

# Step 3: Calculate the weighted crime scores for each record
weighted_scores = []
for record in data:
    weighted_score = 0
    for crime, weight in crime_weights.items():
        weighted_score += record.get(crime, 0) * weight
    record["weighted_crime_score"] = weighted_score
    weighted_scores.append(weighted_score)

# Step 4: Calculate mean and standard deviation
mean_score = np.mean(weighted_scores)
std_dev_score = np.std(weighted_scores)  # Corrected this line to calculate standard deviation

# Precompute min and max weighted scores for scaling
min_weighted_score = min(weighted_scores)
max_weighted_score = max(weighted_scores)

# Step 5: Normalize the scores using precomputed min and max to scale to 0-100
for record in data:
    weighted_score = record["weighted_crime_score"]
    
    # Scale Z-scores directly between 0 and 100
    scaled_score = (weighted_score - min_weighted_score) / (max_weighted_score - min_weighted_score) * 100
    
    # Round and assign the normalized crime safety index
    record["crime_safety_index"] = round(scaled_score)

# Step 6: Compute and output the total average crime safety index for each location
location_averages = {}

for record in data:
    location = record["location"]
    if location not in location_averages:
        location_averages[location] = []
    location_averages[location].append(record["crime_safety_index"])

# After calculating location_averages, add these coordinates for SF districts
district_coordinates = {
    'BAYVIEW': [37.7198, -122.3844],
    'CENTRAL': [37.8015, -122.4089],
    'INGLESIDE': [37.7149, -122.4362],
    'MISSION': [37.7634, -122.4099],
    'NORTHERN': [37.7804, -122.4232],
    'PARK': [37.7677, -122.4455],
    'RICHMOND': [37.7798, -122.4747],
    'SOUTHERN': [37.7751, -122.4093],
    'TARAVAL': [37.7337, -122.4762],
    'TENDERLOIN': [37.7841, -122.4143]
}

# Update the district_boundaries with greatly expanded coordinates
district_boundaries = {
    'BAYVIEW': [
        [37.6983, -122.4135], [37.7624, -122.3615], 
        [37.7544, -122.3480], [37.6935, -122.3685],
        [37.6983, -122.4135]
    ],
    'CENTRAL': [
        [37.7795, -122.4380], [37.8260, -122.4065],
        [37.8135, -122.3785], [37.7770, -122.3900],
        [37.7795, -122.4380]
    ],
    'INGLESIDE': [
        [37.6945, -122.4770], [37.7560, -122.4180],
        [37.7420, -122.4020], [37.6905, -122.4610],
        [37.6945, -122.4770]
    ],
    'MISSION': [
        [37.7410, -122.4480], [37.7950, -122.3950],
        [37.7820, -122.3820], [37.7280, -122.4250],
        [37.7410, -122.4480]
    ],
    'NORTHERN': [
        [37.7620, -122.4620], [37.8090, -122.4080],
        [37.7960, -122.3950], [37.7490, -122.4490],
        [37.7620, -122.4620]
    ],
    'PARK': [
        [37.7390, -122.4890], [37.7980, -122.4350],
        [37.7850, -122.4220], [37.7360, -122.4760],
        [37.7390, -122.4890]
    ],
    'RICHMOND': [
        [37.7510, -122.5210], [37.8090, -122.4470],
        [37.7960, -122.4340], [37.7480, -122.4980],
        [37.7510, -122.5210]
    ],
    'SOUTHERN': [
        [37.7550, -122.4480], [37.8050, -122.3950],
        [37.7920, -122.3820], [37.7420, -122.4350],
        [37.7550, -122.4480]
    ],
    'TARAVAL': [
        [37.7120, -122.5080], [37.7740, -122.4540],
        [37.7610, -122.4410], [37.7090, -122.4950],
        [37.7120, -122.5080]
    ],
    'TENDERLOIN': [
        [37.7680, -122.4380], [37.8050, -122.3920],
        [37.7920, -122.3850], [37.7550, -122.4310],
        [37.7680, -122.4380]
    ]
}

# Add interpolation points generation
def generate_grid_points(boundaries, num_points=10):
    min_lat = min(point[0] for point in boundaries)
    max_lat = max(point[0] for point in boundaries)
    min_lon = min(point[1] for point in boundaries)
    max_lon = max(point[1] for point in boundaries)
    
    lat_step = (max_lat - min_lat) / num_points
    lon_step = (max_lon - min_lon) / num_points
    
    grid_points = []
    for i in range(num_points + 1):
        for j in range(num_points + 1):
            lat = min_lat + i * lat_step
            lon = min_lon + j * lon_step
            grid_points.append([lat, lon])
    
    return grid_points

# Modify the grid point generation to create more interpolation points
def generate_interpolation_points(boundaries1, boundaries2, num_points=50):
    interpolated_points = []
    
    # Ensure both boundary lists have the same number of points
    def resample_boundary(boundary, target_points):
        resampled = []
        for i in range(target_points):
            index = int(i * len(boundary) / target_points)
            resampled.append(boundary[min(index, len(boundary) - 1)])
        return resampled
    
    # Resample boundaries to have consistent number of points
    b1 = resample_boundary(boundaries1, num_points)
    b2 = resample_boundary(boundaries2, num_points)
    
    # Create interpolation points
    for j in range(num_points + 1):
        interpolation_row = []
        for i in range(num_points + 1):
            # Linear interpolation between corresponding points
            lat = (b1[i][0] * (num_points - j) + b2[i][0] * j) / num_points
            lon = (b1[i][1] * (num_points - j) + b2[i][1] * j) / num_points
            interpolation_row.append([lat, lon])
        interpolated_points.extend(interpolation_row)
    
    return interpolated_points

# Modify location_data creation to include interpolation points between districts
location_data = []
districts = list(location_averages.keys())
for i, location in enumerate(districts):
    if location in district_coordinates and location in district_boundaries:
        # Individual district data
        grid_points = generate_grid_points(district_boundaries[location])
        
        # Interpolation points with neighboring districts
        interpolation_data = []
        if i > 0:  # Not the first district
            prev_district = districts[i-1]
            interpolation_points = generate_interpolation_points(
                district_boundaries[location], 
                district_boundaries[prev_district]
            )
            interpolation_data.append({
                'with_district': prev_district,
                'interpolation_points': interpolation_points
            })
        
        if i < len(districts) - 1:  # Not the last district
            next_district = districts[i+1]
            interpolation_points = generate_interpolation_points(
                district_boundaries[location], 
                district_boundaries[next_district]
            )
            interpolation_data.append({
                'with_district': next_district,
                'interpolation_points': interpolation_points
            })
        
        average_index = round(sum(location_averages[location]) / len(location_averages[location]))
        
        location_data.append({
            'location': location,
            'safety_index': average_index,
            'coordinates': district_coordinates[location],
            'boundaries': district_boundaries[location],
            'grid_points': grid_points,
            'interpolation_data': interpolation_data
        })

# Write the data to a JavaScript file
js_output = 'const safetyData = ' + str(location_data).replace("'", '"') + ';'
with open('/Users/yuvraaj/Desktop/safety_data.js', 'w') as f:
    f.write(js_output)

# Output the average crime safety index by location
print("Average Crime Safety Index by Location:")
for location, indexes in location_averages.items():
    average_index = sum(indexes) / len(indexes)
    print(f"Location: {location}, Average Crime Safety Index: {round(average_index)}")