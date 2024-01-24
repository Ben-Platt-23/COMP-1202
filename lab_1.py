import pandas as pd
import matplotlib.pyplot as plt

# Given data
data = {
    'Status': ['Admit', 'Reject', 'Admit', 'Reject', 'Admit', 'Reject', 'Admit', 'Reject', 'Admit', 'Reject',
               'Admit', 'Reject', 'Admit', 'Reject', 'Admit', 'Reject', 'Admit', 'Reject', 'Admit', 'Reject'],
    'Gender': ['Male', 'Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Female', 'Male', 'Male',
               'Female', 'Female', 'Male', 'Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Female'],
    'Department': ['Astronomy', 'Astronomy', 'Astronomy', 'Astronomy', 'Biology', 'Biology', 'Biology', 'Biology',
                   'Law', 'Law', 'Law', 'Law', 'Physics', 'Physics', 'Physics', 'Physics', 'Psychology', 'Psychology',
                   'Psychology', 'Psychology', 'Sociology', 'Sociology', 'Sociology', 'Sociology'],
    'Count': [512, 313, 89, 19, 22, 351, 24, 317, 138, 279, 131, 244, 353, 207, 17, 8, 120, 205, 202, 391, 53, 138, 94, 299]
}

df = pd.DataFrame(data)

# Pivot the data for grouped bar chart
pivot_df = df.pivot_table(index=['Department', 'Gender'], columns='Status', values='Count', aggfunc='sum')

# Plotting the grouped bar chart
fig, ax = plt.subplots(figsize=(12, 8))
pivot_df.plot(kind='bar', stacked=True, color=['blue', 'red'], ax=ax)

# Adding labels and title
plt.xlabel('Department and Gender')
plt.ylabel('Count')
plt.title('Distribution of Admissions by Department and Gender')

# Displaying the legend
plt.legend(title='Admission Status', loc='upper right')

# Show the plot
plt.show()
