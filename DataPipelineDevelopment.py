import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

def run_etl_pipeline(input_file, output_file):
    # --- 1. EXTRACT ---
    print("Reading data...")
    df = pd.read_csv(input_file)
    
    # --- 2. TRANSFORM ---
    print("Transforming data...")
    
    # A. Handle Missing Values by replacing any missing value with mean of that column
    imputer = SimpleImputer(strategy='mean')
    
    # cleaning numeric columns
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numeric_cols] = imputer.fit_transform(df[numeric_cols])
    
    # B. Scaling
    # puts all numbers on a similar scale so the big value don't make the calculation too off 
    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    
    # --- 3. LOAD ---
    print(f"Loading cleaned data to {output_file}...")
    df.to_csv(output_file, index=False)
    print("Done!")

run_etl_pipeline('raw_data.csv', 'cleaned_data.csv')
