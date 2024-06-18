# python3 "Health Visualization.py (type this in the terminal to run this script)
import random
#python3 -m pip install matplotlib (run in the terminal)
import matplotlib.pyplot as plt

# Define constants
NUM_INDIVIDUALS = 100
STUDY_PERIOD = [2009, 2019] 
HEALTH_STATES = ['Mild', 'Moderate', 'Severe', 'Critical']
CARE_TYPES = ['Home', 'Institutional']

# Generate random health data
individuals = []
for i in range(NUM_INDIVIDUALS):
    birth_year = random.randint(1940, 2000)
    gender = random.choice(['Male', 'Female'])
    initial_health_state = random.choice(HEALTH_STATES)
    age = 2019 - birth_year
    care_type = random.choice(CARE_TYPES) if age > 65 else None
    visit_requests = random.randint(1, 5) # number of doctor visits randomly chosen between 1 and 5. 

# Individual: A dictionary containing the data for an individual, with keys ‘birth_year’, 
# ‘gender’, ‘initial_health_state’, ‘age’, ‘care_type’, and ‘visit_requests’.

    individual = {
        'birth_year': birth_year,
        'gender': gender,
        'initial_health_state': initial_health_state,
        'age': age,
        'care_type': care_type,
        'visit_requests': visit_requests
    }
    individuals.append(individual) # Adds the individual’s dictionary to the individuals list.

# Count initial health states
health_state_counts = {state: 0 for state in HEALTH_STATES}
for individual in individuals:
    health_state_counts[individual['initial_health_state']] += 1

############################################################################
## Age summary statistics
ages = [individual['age'] for individual in individuals]
mean_age = sum(ages) / len(ages)
median_age = sorted(ages)[len(ages) // 2]
age_range = max(ages) - min(ages)
std_dev_age = (sum((x - mean_age) ** 2 for x in ages) / len(ages)) ** 0.5

print(f"Mean Age: {mean_age}")
print(f"Median Age: {median_age}")
print(f"Age Range: {age_range}")
print(f"Standard Deviation of Age: {std_dev_age}")

# Gender summary statistics
gender_counts = {'Male': 0, 'Female': 1}
for individual in individuals:
    gender_counts[individual['gender']] += 1

total_individuals = len(individuals)
proportion_male = (gender_counts['Male'] / total_individuals) * 100
proportion_female = (gender_counts['Female'] / total_individuals) * 100

print(f"Count of Males: {gender_counts['Male']}")
print(f"Count of Females: {gender_counts['Female']}")
print(f"Proportion of Males: {proportion_male}%")
print(f"Proportion of Females: {proportion_female}%")

# Plot_1 bar chart_Initial Distribution of Health States
plt.figure(figsize=(10, 5))
plt.bar(health_state_counts.keys(), health_state_counts.values(), color='skyblue')
plt.xlabel('Health State')
plt.ylabel('Number of Individuals')
plt.title('Initial Distribution of Health States')
plt.savefig('initial distr health state.png')  # Save the plot to a file
plt.show()
#plt.close()  # Close the plot to free up memory


# Plot_2 pie chart__Initial Distribution of Health States
plt.figure(figsize=(8, 8))
plt.pie(health_state_counts.values(), labels=health_state_counts.keys(), autopct='%1.1f%%', 
        colors=['lightgreen', 'lightblue', 'lightcoral', 'lightyellow'])
plt.title('Initial Distribution of Health States')
plt.savefig('pie_chart_initial_distr.png')
plt.show()

#Plot_3 Age distribution for the histogram
ages = [individual['age'] for individual in individuals]
plt.figure(figsize=(10, 5))
plt.hist(ages, bins=range(0, 100, 5), color='skyblue', edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Number of Individuals')
plt.title('Age Distribution of Individuals')
plt.savefig('age_distr_individulas.png')
plt.show()

# Plot 4: Bar Chart - Care Type distribution
# care_type_counts = {care_type: 0 for care_type in CARE_TYPES}
# for individual in individuals:
#     if individual['care_type'] != 'None':
#         care_type_counts[individual['care_type']] += 1

# # CARE TYPE COUNT
# care_type_counts = {'Home': 0, 'Institutional': 1} #'Home', 'Institutional'
# for individual in individuals:
#     care_type_counts[individual['care_type']] += 1

# plt.figure(figsize=(10, 5))
# plt.bar(care_type_counts.keys(), care_type_counts.values(), color='skyblue', edgecolor='black')
# plt.xlabel('Care Type')
# plt.ylabel('Number of Individuals')
# plt.title('Care Type Distribution')
# plt.savefig('care_type_distr.png')
# plt.show()


# CARE TYPE COUNT
# care_type_counts = {'Home': 0, 'Institutional': 0}  # Initialize counts for 'Home' and 'Institutional'
# for individual in individuals:
#     if individual['care_type'] != 'None':  # Only count if the care type is not 'None'
#         care_type_counts[individual['care_type']] += 1

# plt.figure(figsize=(10, 5))
# plt.bar(care_type_counts.keys(), care_type_counts.values(), color='skyblue', edgecolor='black')
# plt.xlabel('Care Type')
# plt.ylabel('Number of Individuals')
# plt.title('Care Type Distribution')
# plt.savefig('care_type_distr.png')
# plt.show()

# Plot 5: Comparison Plot - Age, Initial Health State, and Care Type
plt.figure(figsize=(15, 5))

# Plotting Age distribution
plt.subplot(1, 3, 1)
plt.hist(ages, bins=range(0, 100, 5), color='skyblue', edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Number of Individuals')
plt.title('Age Distribution')

# Plotting Initial Health State distribution
plt.subplot(1, 3, 2)
plt.bar(health_state_counts.keys(), health_state_counts.values(), color='skyblue')
plt.xlabel('Health State')
plt.ylabel('Number of Individuals')
plt.title('Health State Distribution')

# # Plotting Care Type distribution
# plt.subplot(1, 3, 3)
# plt.bar(care_type_counts.keys(), care_type_counts.values(), color='skyblue', edgecolor='black')
# plt.xlabel('Care Type')
# plt.ylabel('Number of Individuals')
# plt.title('Care Type Distribution')

plt.tight_layout()  # Adjust subplots to fit into the figure area.
plt.savefig('comparison_plot.png')
plt.show()