from crew_setup import crew

print("✅ Crew created successfully!")
print("Number of agents:", len(crew.agents))

for agent in crew.agents:
    print("-", agent.role)