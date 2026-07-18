import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    class_counts = courses.groupby('class', as_index=False).size()
    
    filtered_classes = class_counts[class_counts['size'] >= 5]
    
    return filtered_classes[['class']]