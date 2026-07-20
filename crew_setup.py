from crewai import Crew, Process

from agents.supervisor_agent import supervisor_agent
from agents.data_analyst_agent import data_analyst_agent
from agents.data_scientist_agent import data_scientist_agent

from crew_tasks import profile_task, quality_task, kpi_task, ml_task

crew = Crew(
    agents=[
        supervisor_agent,
        data_analyst_agent,
        data_scientist_agent
    ],
    tasks=[
        profile_task,
        quality_task,
        kpi_task,
        ml_task
    ],
    process=Process.sequential,
    verbose=True
)