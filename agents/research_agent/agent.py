class ResearchAgent:

    def __init__(self):
        self.name = "Research Agent"
        self.version = "1.0"

    def validate_output(self, output):

        required_fields = [
            "agent",
            "version",
            "status",
            "research",
            "metadata"
        ]

        for field in required_fields:
            if field not in output:
                return False

        return True


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


        if self.validate_output(research_output):
            return research_output

        return {
            "agent": self.name,
            "status": "error",
            "error": {
                "code": "INVALID_OUTPUT",
                "message": "Output validation failed",
                "details": ""
            }
        }
