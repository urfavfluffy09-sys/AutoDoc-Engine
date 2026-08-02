class ResearchAgent:

    def __init__(self):
        self.name = "Research Agent"
        self.version = "1.0"

    def run(self, topic):

        if not topic or topic.strip() == "":
            return {
                "agent": self.name,
                "status": "error",
                "error": {
                    "code": "INVALID_TOPIC",
                    "message": "Research topic cannot be empty",
                    "details": ""
                }
            }

        research_output = {
            "agent": self.name,
            "version": self.version,
            "status": "success",
            "research": {
                "topic": topic,
                "overview": "",
                "key_points": [],
                "timeline": [],
                "important_entities": [],
                "sources": []
            },
            "metadata": {
                "confidence_score": 0
            }
        }

        return research_output
