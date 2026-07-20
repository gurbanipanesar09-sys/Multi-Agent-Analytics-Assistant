from crewai.tools import tool
import pandas as pd

@tool("Profile DataFrame")
def profile_dataframe(df):
    """Return basic dataset statistics."""
    return {
        "row_count": len(df),
        "column_count": len(df.columns),
        "columns": list(df.columns),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "missing_values": df.isnull().sum().to_dict(),
        "duplicates": int(df.duplicated().sum()),
        "sample": df.head().to_dict(orient="records")
    }


def suggest_kpi_metrics(domain):
    """Suggest KPIs based on business domain."""
    if domain.lower() == "ecommerce":
        return [
            "Revenue",
            "Average Order Value",
            "Retention Rate",
            "Customer Lifetime Value",
            "Conversion Rate"
        ]

    elif domain.lower() == "finance":
        return [
            "Profit",
            "Operating Margin",
            "Cash Flow",
            "ROI"
        ]

    elif domain.lower() == "healthcare":
        return [
            "Patient Satisfaction",
            "Average Stay",
            "Readmission Rate"
        ]

    return ["Total Records", "Growth Rate"]


def generate_dashboard_layout():
    return {
        "Overview": [
            "Total Revenue",
            "Total Customers",
            "Transactions"
        ],
        "Charts": [
            "Revenue Trend",
            "Top Products",
            "Customer Distribution"
        ],
        "Tables": [
            "Top Customers",
            "Recent Transactions"
        ]
    }


def validate_sql_safety(query):
    blocked = [
        "DELETE",
        "DROP",
        "UPDATE",
        "ALTER",
        "TRUNCATE"
    ]

    query_upper = query.upper()

    found = [
        word
        for word in blocked
        if word in query_upper
    ]

    return {
        "safe": len(found) == 0,
        "blocked_commands": found
    }


def explain_query_result(result):
    return f"""
The query executed successfully.

Returned {len(result)} rows.

The data can be used for reporting and dashboard creation.
"""