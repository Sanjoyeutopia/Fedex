
# %%
import pandas as pd

# Load the dataset (make sure to update the path to where your CSV file is located)
df = pd.read_csv('/path/to/your/csv/fedex_employee_data.csv')

# %%
# Function to filter employees by department
def filter_employees_by_department(department):
    return df[df['Department'] == department]

# Function to calculate average years of service
def average_years_of_service(department=None):
    if department:
        return df[df['Department'] == department]['Years of Service'].mean()
    else:
        return df['Years of Service'].mean()

# %%
# Example usage

# Filter employees in the 'Logistics' department
logistics_employees = filter_employees_by_department('Logistics')
logistics_employees.head()  # Displaying the first few records

# %%
# Calculate average years of service for all employees
avg_years_all = average_years_of_service()
print(f"Average Years of Service (All Departments): {avg_years_all:.2f}")

# Calculate average years of service for 'Logistics' department
avg_years_logistics = average_years_of_service('Logistics')
print(f"Average Years of Service (Logistics): {avg_years_logistics:.2f}")
