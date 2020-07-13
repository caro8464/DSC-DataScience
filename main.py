import numpy as np
import pandas as pd

def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(str)
        return True
    except (TypeError, ValueError):
        pass
 
    return False


csv_to_clean = pd.read_csv("dsm-beuth-edl-demodata-dirty.csv")

# minimize Dataredundancy by removing empty lines and duplicated ones
csv_to_clean = csv_to_clean.drop_duplicates(subset=["email", "full_name"])
csv_to_clean = csv_to_clean.dropna(how="all")
csv_to_clean = csv_to_clean.reset_index()

for index,row in csv_to_clean.iterrows():
  # set consecutive IDs beginning with 1, since some are missing set them too
  csv_to_clean.at[index, 'id'] = index + 1
  
  # check for invalid age entries, only positive integers make sense 
  if is_number(row.age):
    age_as_int = int(row.age)
    if age_as_int != abs(age_as_int):
      # csv_to_clean.at[index, 'age'] = abs(age_as_int)
      pass
  else:
    # If age is not a number set it to 0 to signal that change is needed but also be compatible to programmes expecting a number
    csv_to_clean.at[index, 'age'] = 0

csv_to_clean['id'] = csv_to_clean['id'].astype(int)    
columns =  ["id", "full_name", "first_name", "last_name", "email", "gender", "age"]
csv_to_clean.to_csv("dsm-beuth-edl-demodata-cleaned.csv", index=False, columns=columns)

# KAGGLE CHALLENGE LINKS IN README