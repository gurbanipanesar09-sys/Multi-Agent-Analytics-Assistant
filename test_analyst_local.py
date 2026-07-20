import pandas as pd

from function_tools.analyst_tools import *

df = pd.DataFrame(
    {
        "Revenue": [100, 200, 300],
        "Orders": [2, 3, 4]
    }
)

print(profile_dataframe(df))

print()

print(suggest_kpi_metrics("ecommerce"))

print()

print(generate_dashboard_layout())

print()

print(validate_sql_safety("SELECT * FROM sales"))

print()

print(explain_query_result(df))