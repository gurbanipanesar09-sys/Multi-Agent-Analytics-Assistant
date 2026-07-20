from crewai import Agent

supervisor_agent = Agent(
    role="Analytics Supervisor",
    goal="Coordinate analytics agents and produce final validated reports.",
    backstory="Senior analytics coordinator responsible for delegation and validation.",
    verbose=True,
    allow_delegation=True
)
