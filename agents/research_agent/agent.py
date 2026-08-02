class ResearchAgent:

    def __init__(self):
        self.name = "Research Agent"

    def run(self, topic):
        return {
            "agent": self.name,
            "topic": topic,
            "status": "initialized"
        }
