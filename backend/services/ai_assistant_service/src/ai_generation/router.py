from fastapi import (
    APIRouter,
    status,
    Query,
    Depends,
)
from starlette.responses import JSONResponse
from typing_extensions import Annotated

from .dependencies import get_service
from .service import AiGenerationService

router = APIRouter(
    prefix="/api/assist",
    tags=["assist"],
)


@router.get(
    path="/answer",
    summary="Endpoint gets question and gives answer to this one",
    status_code=status.HTTP_200_OK,
)
async def handle_question(
        question: Annotated[
            str,
            Query(min_length=10, max_length=200),
        ],
        service: Annotated[
            AiGenerationService,
            Depends(get_service),
        ],
) -> JSONResponse:
    data = await service.process_question(question)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "question": question,
            "answer": data,
        }
    )
