from agents.research_agent.agent import ResearchAgent


def test_valid_topic():

    agent = ResearchAgent()

    result = agent.run("History of Artificial Intelligence")

    assert result["status"] == "success"
    assert result["research"]["topic"] == "History of Artificial Intelligence"



def test_empty_topic():

    agent = ResearchAgent()

    result = agent.run("")

    assert result["status"] == "error"
    assert result["error"]["code"] == "INVALID_TOPIC"



def test_output_structure():

    agent = ResearchAgent()

    result = agent.run("Space Exploration")

    assert "agent" in result
    assert "research" in result
    assert "metadata" in result
