from crewai import Agent

data_analyst_agent = Agent(
    role="Data Analyst",
    goal="Profile datasets, recommend KPIs, validate SQL, and design dashboards.",
    backstory="BI analyst skilled in analytics, reporting, and business insights.",
    verbose=True,
    allow_delegation=False
)