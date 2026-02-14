import pandas as pd

data = {
    'Size': [500, 700, 1000, 1200, 1500, 800, 1100, 1400, 600, 1300],
    'Price': [52000, 71000, 105000, 118000, 152000, 82000, 109000, 141000, 60500, 133000]
}

df = pd.DataFrame(data)
df.to_csv('raw_data.csv', index=False)
print("File 'raw_data.csv' has been created successfully!")