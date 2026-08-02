from agents.script_agent.agent import ScriptAgent


def test_valid_research():

    agent = ScriptAgent()

    research = {
        "topic": "Artificial Intelligence"
    }

    result = agent.run(research)

    assert result["status"] == "success"


def test_empty_research():

    agent = ScriptAgent()

    result = agent.run({})

    assert result["status"] == "error"


def test_output_structure():

    agent = ScriptAgent()

    research = {
        "topic": "Artificial Intelligence"
    }

    result = agent.run(research)

    assert "script" in result
    assert "metadata" in result
