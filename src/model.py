import pandas as pd 
from sklearn.model_selection import train_test_split

def split_data(df):
    """
    Splits the DataFrame into features (X) and target (y),
    and then into training and testing sets

    Args: 
        df (pd.DataFrame): The Full, encoded dataset.

    Returns
        tuple: X_train, X_test, y_train, y_test
    """

    print("---DATA SPLITTING---")

    #Define target (y) and features (X)
    target_columns = 'price'

    #X contains everything except the price
    X = df.drop(columns=[target_columns])
    #y contains only the price
    y = df[target_columns]

    print(f"Target (y): {target_columns}")
    print(f"Features (X): {list(X.columns)}")

    #Split into train and test sets
    #test_size = 0.2 -> 20% of data goes to the 'Exam' (Test set)
    #random state = 42 -> Ensures the split is indentical every time we run the code
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state= 42)

    print(f"Training set size: {len(X_train)} rows (80%)")
    print(f"Testing set size: {len(X_train)} rows (20%)")

    return X_train, X_test, y_train, y_test