import matplotlib.pyplot as plt

# Data
x = ['Commission', 'Parliament', 'Council']
y = [0.51, 0.57, 0.44]

# Set y-axis range from 0 to 1
plt.ylim(0, 1)

# Create a customized line plot
plt.plot(x, y, color='green', linestyle='-', linewidth=2, marker='o', markersize=10, markerfacecolor='red')

# Add labels and title
plt.ylabel('Bindingness')
plt.title('Bindingness Trend Between Directive Versions')

# Annotate the values of the data points
for i in range(len(x)):
    plt.text(x[i], y[i] + 0.03, f'{y[i]:.2f}', ha='center', fontsize=12, color='black')

# Calculate the differences
if len(y) > 1:
    diff_1_2 = y[1] - y[0]  # Difference between Commission and Parliament
    plt.text(0.5, (y[0] + y[1]) / 2 + 0.05, f'{diff_1_2:.2f}', ha='center', fontsize=12, color='blue')

if len(y) > 2:
    diff_2_3 = y[2] - y[1]  # Difference between Parliament and Council
    plt.text(1.5, (y[1] + y[2]) / 2 + 0.05, f'{diff_2_3:.2f}', ha='center', fontsize=12, color='blue')

# Highlight the differences
plt.fill_between(x, y, color='lightgray', alpha=0.3)  # Shade the area under the line

# Show the plot
plt.show()

