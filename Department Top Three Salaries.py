import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # Drop duplicates within the same department for salary
    duplicate = employee.drop_duplicates(["salary", "departmentId"])
    
    # Sort the employees by salary in descending order
    df_sorted = duplicate.sort_values(by=["salary"], ascending=False)
    
    # Select top 3 employees per department based on salary
    df_groupby = df_sorted.groupby("departmentId").head(3)
    
    # Merge with the department table to get department names
    df = employee.merge(department, how="left", left_on="departmentId", right_on="id")
    
    # Merge again to keep only the top 3 earners per department
    merging = df.merge(df_groupby[["salary", "departmentId"]], how="inner", on=["departmentId", "salary"])
    
    # Rename the columns appropriately
    merging = merging.rename(columns={"name_y": "Department", "name_x": "Employee", "salary": "Salary"})
    
    # Return only the required columns
    return merging[["Department", "Employee", "Salary"]]
