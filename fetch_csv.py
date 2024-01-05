import pandas as pd
import os

# Folder containing all your Excel files
folder_path = 'C:/Users/Kshitiz/Students_Name'

# Initialize an empty DataFrame to store the combined data
combined_data = pd.DataFrame()

# Iterate over each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.xlsx'):
        file_path = os.path.join(folder_path, filename)

        # Read the Excel file
        df = pd.read_excel(file_path)

        # Extract the desired columns (e.g., "Name", "Fullname", "name")
        if "Name" in df.columns:
            selected_columns = ["Name"]
        elif "Fullname" in df.columns:
            selected_columns = ["fullName"]
        elif "name" in df.columns:
            selected_columns = ["name"]
        else:
            # Modify this based on your actual column names
            selected_columns = []

        # Append the selected columns to the combined data
        combined_data = combined_data.append(df[selected_columns], ignore_index=True)

# Save the combined data to a new Excel file
output_file_path = 'C:/Users/Kshitiz/Students_Name/Final Data/combined_data.xlsx'
combined_data.to_excel(output_file_path, index=False)

print(f"Combined data saved to {output_file_path}")
