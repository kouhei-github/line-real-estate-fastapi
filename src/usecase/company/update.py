from schemas.index import CompanySchema
from repositories.company.interface import CompanyRepositoryModule, CompanyRepository
from injector import Injector
from models.index import Company

async def update_use_case(company_id: int, message_id: int) -> Company:
    # user
    injector = Injector([CompanyRepositoryModule()])
    company_repository = injector.get(CompanyRepository)
    response = company_repository.update_message(company_id, message_id)
    return response