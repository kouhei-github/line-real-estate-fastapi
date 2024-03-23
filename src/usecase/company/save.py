from schemas.index import CompanySchema
from repositories.company.interface import CompanyRepositoryModule, CompanyRepository
from injector import Injector

async def save_use_case(body: CompanySchema) -> str:
    # user
    injector = Injector([CompanyRepositoryModule()])
    company_repository = injector.get(CompanyRepository)
    response = company_repository.save(
        company_name=body.name,
        company_line_id=body.line_id,
        channel_access_token=body.channel_access_token,
    )
    return response