from schemas.index import QuestionSchema
from repositories.question.interface import QuestionRepository, QuestionRepositoryModule
from injector import Injector

async def save_use_case(body: QuestionSchema) -> dict:
    # user
    injector = Injector([QuestionRepositoryModule()])
    question_repository = injector.get(QuestionRepository)
    response = question_repository.save(body.content, body.company_id)
    return response