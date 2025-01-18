from src.core import AiAssistant


class AiGenerationService:

    def __init__(self, assistant: AiAssistant):
        self.assistant = assistant

    async def process_question(self, question_text: str) -> str:
        answer = await self.assistant.generate_answer(question_text)
        return answer
