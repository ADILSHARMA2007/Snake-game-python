import pandas as pd
df = pd.DataFrame({
    'City': ['New York', 'New York', 'London', 'London', 'Berlin'],
    'Population': [8175133, 8175133, 8982000, 8982000, 3769000],
    'Area': [789, 789, 1572, 1572, 891]
})

grouped = df.groupby('City').sum()  # Group by 'City' and sum 'Population' and 'Area'
print(grouped)
