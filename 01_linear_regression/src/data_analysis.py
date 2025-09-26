# data_analysis.py - Fixed version
import pandas as pd
import matplotlib.pyplot as plt
import os

def explore_data():
    try:
        # Exact file path
        file_path = '../data/Tehran-Houses-DIVAR.csv'
        
        print(f"🔍 Searching for file at: {file_path}")
        print(f"📁 Current directory: {os.getcwd()}")
        print(f"✅ File exists: {os.path.exists(file_path)}")
        
        # Read dataset
        df = pd.read_csv(file_path, encoding='utf-8')
        
        print("\n🎉 File read successfully!")
        print("📊 Dataset information:")
        print(f"Number of rows: {df.shape[0]}")
        print(f"Number of columns: {df.shape[1]}")
        
        print("\n📋 Columns:")
        print(df.columns.tolist())
        
        print("\n👀 Sample data (first 5 rows):")
        print(df.head())
        
        print("\n📈 Statistical information:")
        print(df.describe())
        
        print("\n🔍 Missing values:")
        missing_data = df.isnull().sum()
        print(missing_data[missing_data > 0])  # Only columns with missing data
        
        print("\n💾 Data types:")
        print(df.dtypes)
        
        return df
        
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        # More detailed error investigation
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    print("🚀 Starting data analysis...")
    df = explore_data()
    
    if df is not None:
        print("\n✅ Data analysis completed successfully!")
        print(f"📊 Data dimensions: {df.shape}")
        
        # Optional: Create some basic visualizations
        try:
            # Check if we have numeric columns for plotting
            numeric_columns = df.select_dtypes(include=['number']).columns
            
            if len(numeric_columns) >= 2:
                # Create a simple scatter plot if we have at least 2 numeric columns
                plt.figure(figsize=(10, 6))
                plt.scatter(df[numeric_columns[0]], df[numeric_columns[1]], alpha=0.5)
                plt.xlabel(numeric_columns[0])
                plt.ylabel(numeric_columns[1])
                plt.title(f'{numeric_columns[1]} vs {numeric_columns[0]}')
                plt.grid(True, alpha=0.3)
                plt.savefig('../data/first_analysis_plot.png')
                plt.show()
                print("📊 Basic visualization created and saved!")
                
        except Exception as e:
            print(f"⚠️ Could not create visualization: {e}")
            
    else:
        print("\n❌ Data analysis failed!")