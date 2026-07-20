import pandas as pd

from function_tools.scientist_tools import *

df = pd.DataFrame(
    {
        "Sales": [10, 20, 30]
    }
)

print(recommend_ml_problem_type("Predict churn"))

print()

print(suggest_feature_engineering())

print()

print(detect_ml_data_risks(df))

print()

print(recommend_evaluation_metrics("Classification"))

print()

print(create_ml_pipeline_plan())