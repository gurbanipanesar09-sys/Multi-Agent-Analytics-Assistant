import streamlit as st
import pandas as pd
import tempfile

from function_tools.supervisor_tools import (
    classify_user_request,
    create_agent_work_plan,
    estimate_context_usage
)

from mcp_server.tools.csv_profile_tools import mcp_profile_csv
from mcp_server.tools.data_quality_tools import mcp_detect_data_quality_issues
from mcp_server.tools.kpi_tools import mcp_generate_kpi_catalog
from mcp_server.tools.ml_tools import (
    mcp_recommend_ml_use_cases,
    mcp_feature_engineering_suggestions
)
from mcp_server.tools.report_tools import mcp_generate_report_markdown


st.set_page_config(
    page_title="Gurbani Panesar Project 2",
    layout="wide"
)

st.title("Multi-Agent Analytics Assistant")
st.caption("Built using CrewAI, Function Tools, MCP Tools and Streamlit")

with st.sidebar:
    st.header("Project Info")
    st.write("Submitted By: Gurbani Panesar")
    st.write("Project 2")
    st.divider()

    st.subheader("Agents")
    st.success("Supervisor Agent")
    st.success("Data Analyst Agent")
    st.success("Data Scientist Agent")

    st.divider()
    st.metric("Function Tools", 15)
    st.metric("MCP Tools", 6)
    st.metric("Agents", 3)

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

prompt = st.chat_input("Ask your analytics question")

if uploaded_file is not None:
    df_preview = pd.read_csv(uploaded_file)
    st.subheader("Dataset Preview")
    st.dataframe(df_preview.head())

    uploaded_file.seek(0)

if uploaded_file is not None and prompt:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as temp:
        temp.write(uploaded_file.getbuffer())
        filepath = temp.name

    intent = classify_user_request.run(prompt)
    plan = create_agent_work_plan.run(intent["intent"])

    profile = mcp_profile_csv(filepath)
    quality = mcp_detect_data_quality_issues(filepath)
    kpis = mcp_generate_kpi_catalog("ecommerce", profile["column_names"])
    ml = mcp_recommend_ml_use_cases(profile["column_names"])
    features = mcp_feature_engineering_suggestions()

    report = mcp_generate_report_markdown(
        profile,
        quality,
        kpis,
        ml,
        features
    )

    usage = estimate_context_usage.run(report)

    st.success("Analysis completed successfully!")

    col1, col2, col3 = st.columns(3)
    col1.metric("Rows", profile["rows"])
    col2.metric("Columns", profile["columns"])
    col3.metric("Duplicates", profile["duplicates"])

    tab1, tab2, tab3 = st.tabs(
        ["Final Report", "Timeline", "Delegation Trace"]
    )

    with tab1:
        st.markdown(report)

        st.download_button(
            "Download Report",
            report,
            file_name="analytics_report.md",
            mime="text/markdown"
        )

    with tab2:
        steps = [
            "User uploaded dataset",
            "Supervisor classified request",
            "Work plan created",
            "MCP profile tool executed",
            "Data quality checked",
            "KPI catalog generated",
            "ML use cases recommended",
            "Final report created"
        ]

        for step in steps:
            st.info(step)

    with tab3:
        st.json(intent)
        st.json(plan)

    with st.expander("Dataset Profile"):
        st.json(profile)

    with st.expander("Data Quality Issues"):
        st.json(quality)

    with st.expander("KPI Catalog"):
        st.json(kpis)

    with st.expander("ML Use Cases"):
        st.json(ml)

    with st.expander("Feature Engineering Suggestions"):
        st.json(features)

    st.sidebar.metric("Estimated Tokens", usage["estimated_input_tokens"])