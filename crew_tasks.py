from crewai import Task

from agents.data_analyst_agent import data_analyst_agent
from agents.data_scientist_agent import data_scientist_agent

profile_task = Task(
    description="Profile uploaded dataset",
    expected_output="Dataset profiling report",
    agent=data_analyst_agent
)

quality_task = Task(
    description="Find data quality issues",
    expected_output="Quality report",
    agent=data_analyst_agent
)

kpi_task = Task(
    description="Recommend KPIs",
    expected_output="KPI list",
    agent=data_analyst_agent
)

ml_task = Task(
    description="Recommend ML use cases",
    expected_output="Machine learning report",
    agent=data_scientist_agent
)