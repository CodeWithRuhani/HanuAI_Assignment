import pandas as pd

def clean_data(input_path, output_path):
    print("🔹 Loading raw data...")

    try:
        df = pd.read_csv(input_path)
    except Exception as e:
        print(f" Error loading file: {e}")
        return

    print(f"Initial Shape: {df.shape}")

    # Step 1: Check Missing Values
    print("\n🔹 Missing values BEFORE cleaning:")
    print(df.isnull().sum())

    # Step 2: Remove Duplicates
    before_dup = df.shape[0]
    df = df.drop_duplicates()
    after_dup = df.shape[0]

    print(f"\n Removed {before_dup - after_dup} duplicate rows")

    # Step 3: Handle Missing Values
    df = df.fillna("Unknown")

    print("\n Missing values AFTER cleaning:")
    print(df.isnull().sum())

    # Step 4: Standardize Column Names
    df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")

    print("\n Updated Column Names:")
    print(list(df.columns))

    # Step 5: Save Cleaned Data
    try:
        df.to_csv(output_path, index=False)
        print(f"\n Cleaned data saved to: {output_path}")
    except Exception as e:
        print(f"Error saving file: {e}")

    return df


# MAIN EXECUTION
if __name__ == "__main__":
    clean_data(
        "../data/raw_data.csv",
        "../data/cleaned_data.csv"
    )
