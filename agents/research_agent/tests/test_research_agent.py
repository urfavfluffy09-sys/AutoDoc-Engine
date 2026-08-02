from agents.research_agent.agent import ResearchAgent


def test_agent_initialization():

    agent = ResearchAgent()

    result = agent.run("Artificial Intelligence")

    assert result["status"] == "initialized"
