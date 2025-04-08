import sys
import matplotlib
matplotlib.use('Agg') 
import numpy as np
import matplotlib.pyplot as plt


marks = np.array([[85, 90, 88, 92, 78],   
                  [78, 83, 79, 85, 80],   
                  [90, 92, 88, 94, 86]])  

sums = np.sum(marks, axis=1)
averages = np.mean(marks, axis=1)


print("Student-wise marks sum and average:")
for i in range(3):
    print(f"Student {i+1}: Sum = {sums[i]}, Average = {averages[i]:.2f}")

x = np.arange(3) 
width = 0.35  

fig, ax = plt.subplots()

bars_sum = ax.bar(x - width/2, sums, width, label='Sum of Marks', color='b')
bars_avg = ax.bar(x + width/2, averages, width, label='Average Marks', color='g')

ax.set_xlabel('Students')
ax.set_ylabel('Marks')
ax.set_title('Sum and Average Marks of Students')
ax.set_xticks(x)
ax.set_xticklabels([f'Student {i+1}' for i in range(3)])
ax.legend()

plt.tight_layout()
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
