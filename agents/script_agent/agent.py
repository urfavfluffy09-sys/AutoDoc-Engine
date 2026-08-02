class ScriptAgent:

    def __init__(self):
        self.name = "Script Agent"
        self.version = "1.0"

    def validate_output(self, output):

        required_fields = [
            "agent",
            "version",
            "status",
            "script",
            "metadata"
        ]

        for field in required_fields:
            if field not in output:
                return False

        return True


    def run(self, research):

        if not research:
            return {
                "agent": self.name,
                "status": "error",
                "error": {
                    "code": "INVALID_RESEARCH",
                    "message": "Research data is required",
                    "details": ""
                }
            }

        script_output = {
            "agent": self.name,
            "version": self.version,
            "status": "success",
            "script": {
                "title": "",
                "hook": "",
                "introduction": "",
                "sections": [],
                "narration": "",
                "ending": ""
            },
            "metadata": {
                "confidence_score": 0
            }
        }

        if self.validate_output(script_output):
            return script_output

        return {
            "agent": self.name,
            "status": "error",
            "error": {
                "code": "INVALID_OUTPUT",
                "message": "Output validation failed",
                "details": ""
            }
        }
