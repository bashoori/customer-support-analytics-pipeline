import pandas as pd
from pathlib import Path


def load_customer_messages(file_path):
    """Load customer messages from a CSV file."""
    """It reads a CSV, checks that the required columns exist, removes rows with missing customer messages, and displays the result."""
    
    df = pd.read_csv(file_path)

    required_columns = ["ticket_id", "customer_message"]

    if not all(col in df.columns for col in required_columns):
        raise ValueError("CSV is missing required columns.")

    df = df.dropna(subset=["customer_message"])

    return df


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parents[1]
    file_path = project_root / "data" / "sample_customer_messages.csv"

    df = load_customer_messages(file_path)
    print(df.head())
    print(f"Loaded {len(df)} customer messages.")