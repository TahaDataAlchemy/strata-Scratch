import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # Sort by salary in descending order and remove duplicates
    unique_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False).reset_index(drop=True)
    
    # Return a DataFrame with NaN (null) if N is out of bounds
    if N > len(unique_salaries) or N <= 0:
        return pd.DataFrame({f"getNthHighestSalary({N})": [pd.NA]})
    
    # Return only the salary column of the N-th highest distinct salary with dynamic column name
    return pd.DataFrame({f"getNthHighestSalary({N})": [unique_salaries.iloc[N-1]]})

