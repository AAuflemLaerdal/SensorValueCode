import matplotlib.pyplot as plt

def read_list_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read all lines from the file into a list
            lines = file.readlines()
            
            # Optionally, remove any leading/trailing whitespaces or newline characters
            # and convert the list items to lowercase (for example)
            cleaned_list = [line.strip().lower() for line in lines]
            
            return cleaned_list
            
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
        return []
    except Exception as e:
        print("An error occurred:", e)
        return []

# Replace 'my_list.txt' with the path to your text file containing the list
file_path = 'Test1.txt'
my_list = read_list_from_file(file_path)

# Split each string in the list on every space and create a new list of strings
split_list = [string.split() for string in my_list]

# Flatten the list of lists to get a single list of strings
flat_list = [item for sublist in split_list for item in sublist]

# Convert each string element to a float and create the final list of floats
SensorValue_list = [float(num) for num in flat_list]

# Print the resulting list of floats
print(len(SensorValue_list))

# Calculate the power value ((5 * 8) / 9600)
power_value = (5 * 8) / 9600

# Initialize the result_list with the first element as 0
time_list = [0]

# Calculate the rest of the elements using a loop
for i in range(0, 23511):
    next_element = time_list[-1] + power_value
    time_list.append(next_element)

# Print the first 10 elements of the result list
print(len(time_list))

def moving_average(data, window_size):
    smoothed_data = []
    for i in range(len(data) - window_size + 1):
        window = data[i:i+window_size]
        average = sum(window) / window_size
        smoothed_data.append(average)
    return smoothed_data

window_size = 50
smoothedPressure_list = moving_average(SensorValue_list, window_size)
smoothedTime_list = moving_average(time_list, window_size)
print(len(smoothedPressure_list))
print(len(smoothedTime_list))

#----------------------------------------------------------|Plot|-------------------------------------------------

plt.plot(smoothedTime_list[:8000], smoothedPressure_list[:8000], linestyle='-')

# Add a horizontal line at y=80
plt.axhline(y=80, color='red', linestyle='--', label='Pressure Threshold')

# Add labels and title to the graph
plt.xlabel('Time [s]')
plt.ylabel('Pressure Value')
plt.title('Test 1')
plt.legend()

# Display the graph
plt.show()