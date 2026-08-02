from agents.script_agent.agent import ScriptAgent


def test_script_agent():

    agent = ScriptAgent()

    result = agent.run({})

    assert result["status"] == "initialized"
