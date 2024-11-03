import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data from the file
data = {
    'Company': ['Exxon', 'Chevron', 'Shell', 'BP'],
    'Scope 1 (MtCO2e)': [92, 52, 50, 31.1],
    'Scope 2 (MtCO2e)': [8, 4, 7, 1],
    'Scope 1,2, and 3 (MtCO2e)': [638, 745, 1147, 347]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Reshape the data for plotting
melted_data = df.melt(id_vars='Company', 
                      value_vars=['Scope 1 (MtCO2e)', 'Scope 2 (MtCO2e)', 'Scope 1,2, and 3 (MtCO2e)'], 
                      var_name='Emissions Type', 
                      value_name='Emissions (MtCO2e)')

# Set plot size
plt.figure(figsize=(12, 6))

# Create bar plot
bar_plot = sns.barplot(data=melted_data, x='Company', y='Emissions (MtCO2e)', hue='Emissions Type')

# Add title and labels
bar_plot.set_title('Monetised Scope 1, 2, and Total Emissions by Company for 2023')
bar_plot.set_ylabel('Emissions (MtCO2e)')
bar_plot.set_xlabel('Company')

# Show legend and plot
plt.legend(title='Emissions Type')
plt.tight_layout()
plt.show()
