from .service import AiGenerationService
from src.consts import Consts
from src.core import AiAssistant


def get_service() -> AiGenerationService:
    assistant = AiAssistant(model=Consts.LLM_MODEL)
    service = AiGenerationService(assistant=assistant)
    return service
