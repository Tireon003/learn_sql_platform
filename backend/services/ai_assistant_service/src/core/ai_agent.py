from typing import Literal

from pydantic_ai import Agent
from src.consts import Consts

import logging

from typing_extensions import cast

logger = logging.getLogger(__name__)


class AiAssistant:

    def __init__(self, model: str) -> None:
        self._agent = Agent(
            model=model,  # type: ignore
            system_prompt=Consts.PROMPT,
        )

    async def generate_answer(self, question: str) -> str:
        answer = ""
        try:
            response = await self._agent.run(user_prompt=question)
            answer = response.data
        except Exception as e:
            logger.error(
                "Error while processing request: %s",
                str(e),
            )
            answer = "Ошибка при обработке запроса, повторите снова."
        finally:
            return answer
