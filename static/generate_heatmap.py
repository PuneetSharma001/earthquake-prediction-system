import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load your Excel spreadsheet
file_path = "all_month.csv"  # Ensure this file is in the same folder as this script
data = pd.read_excel(file_path)

# Step 2: Select relevant columns for the heatmap
columns = ['depth', 'mag', 'rms', 'gap', 'dmin']  # Adjust as needed based on your dataset
correlation_matrix = data[columns].corr()

# Step 3: Create the heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", cbar=True)
plt.title("Correlation Heatmap of Earthquake Data")

# Step 4: Save the heatmap image in the 'static' folder
heatmap_path = "static/correlation_heatmap.png"  # Ensure the 'static' folder exists
plt.savefig(heatmap_path)
print(f"Heatmap saved at: {heatmap_path}")
plt.show()
