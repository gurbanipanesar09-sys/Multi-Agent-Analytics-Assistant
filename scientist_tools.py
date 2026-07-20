import pandas as pd
from crewai.tools import tool

@tool("Recommend ML Problem Type")
def recommend_ml_problem_type(text):
    """Recommend the type of machine learning problem based on text keywords."""
    text = text.lower()
    if "churn" in text:
        return "Classification"
    elif "sales" in text:
        return "Forecasting"
    elif "price" in text:
        return "Regression"
    elif "segment" in text:
        return "Clustering"
    return "Regression"

@tool("Suggest Feature Engineering")
def suggest_feature_engineering():
    """Suggest standard feature engineering operations to clean up and prepare model matrices."""
    return [
        "Rolling Average",
        "Date Features",
        "Lag Variables",
        "One Hot Encoding",
        "Normalization",
        "Interaction Features"
    ]

@tool("Detect ML Data Risks")
def detect_ml_data_risks(df: pd.DataFrame) -> list:
    """Analyze data profile elements to flag potential data pipeline structural leaks or volume issues."""
    risks = []
    if df.isnull().sum().sum() > 0:
        risks.append("Missing Values")
    if df.duplicated().sum() > 0:
        risks.append("Duplicate Records")
    if len(df) < 100:
        risks.append("Very Small Dataset")
    return risks

@tool("Recommend Evaluation Metrics")
def recommend_evaluation_metrics(problem):
    """Recommend standard model metric matrices based on specific objective problem configurations."""
    if problem == "Classification":
        return ["Accuracy", "Precision", "Recall", "F1 Score", "ROC AUC"]
    elif problem == "Regression":
        return ["MAE", "RMSE", "R²"]
    elif problem == "Forecasting":
        return ["MAPE", "RMSE"]
    return []

@tool("Create ML Pipeline Plan")
def create_ml_pipeline_plan():
    """Create a structured, step-by-step pipeline workflow layout for machine learning models."""
    return [
        "Data Collection",
        "Data Cleaning",
        "Feature Engineering",
        "Train Test Split",
        "Model Training",
        "Evaluation",
        "Deployment",
        "Monitoring"
    ]