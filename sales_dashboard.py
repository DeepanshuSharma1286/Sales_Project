import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV (must be in the same folder as script)
df = pd.read_csv("sales.csv")

# Preview
print("✅ First 5 rows:")
print(df.head())

# Summary statistics
print("\n📊 Summary Statistics:")
print(df.describe())

# Example analysis: Top 5 by 'Weight(Pounds)' (if column exists)
if 'Weight(Pounds)' in df.columns:
    top5 = df.sort_values('Weight(Pounds)', ascending=False).head(5)
    print("\n🏆 Top 5 entries by Weight(Pounds):")
    print(top5)

# Plot histogram of a numeric column
if 'Height(Inches)' in df.columns:
    df['Height(Inches)'].plot(kind='hist', bins=10, title="Height Distribution")
    plt.xlabel("Height (Inches)")
    plt.show()

# Scatter plot: Height vs Weight
if 'Height(Inches)' in df.columns and 'Weight(Pounds)' in df.columns:
    sns.scatterplot(x='Height(Inches)', y='Weight(Pounds)', data=df)
    plt.title("Height vs Weight")
    plt.show()

# Optional: Save the dataset as a new CSV (merged/cleaned)
df.to_csv("sales_cleaned.csv", index=False)
print("\n✅ Cleaned CSV saved as 'sales_cleaned.csv'")
