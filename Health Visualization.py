# python3 "Health Visualization.py" (type this in the terminal to run this script)
#python3 -m pip install matplotlib (run in the terminal)
# "pip install matplotlib", to install the  library 
# "shift + enter" to run selected lines of code
# "shift + /" to comment/uncomment
#  "Ctrl+Shift+P" to open the command palette
import random
import matplotlib.pyplot as plt

# Define some constants
NUM_INDIVIDUALS = 1000
STUDY_PERIOD = [2009, 2019] 
HEALTH_STATES = ['Mild', 'Moderate', 'Severe', 'Critical']
CARE_TYPES = ['Home', 'Institutional']

# Generate random health data frame
individuals = []
random.seed(123) #for reproducibility
for i in range(NUM_INDIVIDUALS):
    birth_year = random.randint(1920, 2000)
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
health_state_counts = {state: 0 for state in HEALTH_STATES} #initializing a dictionary that counts from 0
for individual in individuals:
    health_state_counts[individual['initial_health_state']] += 1

############################################################################
## Age summary statistics
ages = [individual['age'] for individual in individuals] 
#using 'list comprehension' to iterate through 'individuals' to create the 'ages' list
#which contains the 'ages' of individuals in the individuals list 
mean_age = sum(ages) / len(ages)
median_age = sorted(ages)[len(ages) // 2] #finds the middle index (using integer division)
age_range = max(ages) - min(ages)
std_dev_age = (sum((x - mean_age) ** 2 for x in ages) / len(ages)) ** 0.5
#for each 'x' calculate the square difference from the 'mean_age' 
#take the square root of the variance to get the 'standard deviation of age' 

print(f"Mean Age: {mean_age}")
print(f"Median Age: {median_age}")
print(f"Age Range: {age_range}")
print(f"Standard Deviation of Age: {std_dev_age}")
print()
print()
#######################################################################################
# Gender summary statistics
gender_counts = {'Male': 0, 'Female': 0}
for individual in individuals:
    gender_counts[individual['gender']] += 1
print(gender_counts)

total_individuals = len(individuals)
proportion_male = (gender_counts['Male'] / total_individuals) * 100
proportion_female = (gender_counts['Female'] / total_individuals) * 100

print(f"Count of Males: {gender_counts['Male']}")
print(f"Count of Females: {gender_counts['Female']}")
print(f"Proportion of Males: {proportion_male}%")
print(f"Proportion of Females: {proportion_female}%")

#####################################################################################
# Plotting the Age distribution
# Create age categories
age_categories = {'0-40': 0, '41-65': 0, '66-90': 0, '90+': 0}
for age in ages:
    if age <= 40:
        age_categories['0-40'] += 1
    elif age <= 65:
        age_categories['41-65'] += 1
    elif age <= 90:
        age_categories['66-90'] += 1
    else:
        age_categories['90+'] += 1

## line plot for Age distribution
ages = [individual['age'] for individual in individuals]
plt.figure(figsize=(10, 5))
plt.plot(list(age_categories.keys()), list(age_categories.values()))
plt.xlabel('Age')
plt.ylabel('Number of Individuals')
plt.title('Line graph: Age Categories')
#plt.savefig('age_distr_individulas1.png')
plt.show()

## histogram  for Age distribution
plt.hist(ages)
#plt.hist(ages, bins=range(0, 100, 5), color='skyblue', edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Number of Individuals')
plt.title('Histogram: Age Distribution of Individuals')
#plt.savefig('age_distr_individulas2.png')
plt.show()

## bar chat  for Age distribution
plt.bar(age_categories.keys(), age_categories.values(), color='red', edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Number of Individuals')
plt.title('Bar chart: Age Distribution of Individuals')
#plt.savefig('age_distr_individulas3.png')
plt.show()

########################################################################################
# Plotting the Initial Distribution of Health States

## line plot _Initial Distribution of Health States
plt.plot(health_state_counts.keys(), health_state_counts.values())
plt.xlabel('Health State')
plt.ylabel('Number of Individuals')
plt.title('Line graph: Initial Distribution of Health States')
#plt.savefig('initial_distr_individulas1.png')
plt.show()

# bar chart_Initial Distribution of Health States
#plt.figure(figsize=(10, 5))
plt.bar(health_state_counts.keys(), health_state_counts.values()) 
plt.xlabel('Health State')
plt.ylabel('Number of Individuals')
plt.title('Bar chart: Initial Distribution of Health States')
#plt.savefig('initial_distr_individulas2.png')  # Save the plot to a file
plt.show()

# pie chart__Initial Distribution of Health States
plt.figure(figsize=(8, 8))
plt.pie(health_state_counts.values(), labels=health_state_counts.keys(), autopct='%1.1f%%') 
plt.title('Pie chart: Initial Distribution of Health States')
#plt.savefig('initial_distr_individulas3.png')
plt.show()


################################################################################
# Plotting the Distribution  of CARE TYPE

# Count initial health states
counts_care_type = {care: 0 for care in CARE_TYPES} #initializes a dictionary with keys 'Home' and 'Institution' counting from 0
for individual in individuals:
    care_type = individual['care_type']
    if care_type is not None: #check if care_type != None
        counts_care_type[care_type] += 1
print(counts_care_type.keys())
print(counts_care_type.values())

#create a bar chart
plt.bar(counts_care_type.keys(), counts_care_type.values(), color='green', edgecolor='black')
plt.xlabel('Care Type')
plt.ylabel('Number of Individuals')
plt.title('Bar Chart: Care Type Distribution')
#plt.savefig('care_type_distr.png')
plt.show()

# Create a pie chart
plt.pie(counts_care_type.values(), labels=counts_care_type.keys(), autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightgreen'])
plt.title('Pie Chart - Care Type Distribution')
#plt.savefig('care_type_distribution_pie.png')
plt.show()


########################################################################################
# Plotting the Distribution of Gender

# bar chart_ _Gender Distribution
plt.bar(gender_counts.keys(), gender_counts.values(), color='lightgreen')
plt.xlabel('Gender')
plt.ylabel('Number of Individuals')
plt.title('Bar chart: Distribution of Gender')
#plt.savefig('gender_distr_individulas1.png')  # Save the plot to a file
plt.show()

# pie chart _Gender Distribution
plt.pie(gender_counts.values(), labels=gender_counts.keys(), autopct='%1.1f%%', 
        colors=['lightgreen', 'lightblue', 'lightcoral', 'lightyellow'])
plt.title('Pie chart: Gender Distribution')
#plt.savefig('gender_distr_individulas2.png')
plt.show()

#########################################################################
# Plot 5: Comparison Plot - Age, Initial Health State, Care Type, and Gender
plt.figure(figsize=(15, 6))

# Plotting Age distribution
plt.subplot(1, 4, 1)
plt.bar(age_categories.keys(), age_categories.values(), color='skyblue', edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Number of Individuals')
plt.title('Age Distribution of Individuals')

# Plotting Initial Health State distribution
plt.subplot(1, 4, 2)
plt.bar(health_state_counts.keys(), health_state_counts.values(), color='lightblue')
plt.xlabel('Health State')
plt.ylabel('Number of Individuals')
plt.title('Health State Distribution')

# # Plotting Care Type distribution
plt.subplot(1, 4, 3)
plt.bar(counts_care_type.keys(), counts_care_type.values(), color='lightcoral', edgecolor='black')
plt.xlabel('Care Type')
plt.ylabel('Number of Individuals')
plt.title('Care Type Distribution')

# Plotting Gender Distribution
plt.subplot(1, 4, 4)
plt.bar(gender_counts.keys(), gender_counts.values(), color='red')
plt.xlabel('Gender')
plt.ylabel('Number of Individuals')
plt.title('Initial Distribution of Health States')

plt.tight_layout()  # Adjust subplots to fit into the figure area.
plt.savefig('comparison_plot.png')
plt.show()