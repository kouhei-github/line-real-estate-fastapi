from injector import inject, Module
from .rdbms_company import CompanyRDBMS

from .abstruct import AbstractCompanyDatabase
from schemas.index import UserAuth, UserOut, CompanySchema
from models.index import Company

class CompanyRepository(Module):
    @inject
    def __init__(self, repository: AbstractCompanyDatabase) -> None:
        if not isinstance(repository, AbstractCompanyDatabase):
            raise Exception("notify is not abstractTire.")
        self.repository = repository


    def save(self, company_name: str, company_line_id: str, channel_access_token: str) -> dict:
        print("MySQlに応募者の情報を登録しました")
        company = CompanySchema.parse_obj({
            "line_id": company_line_id,
            "name": company_name,
            "channel_access_token": channel_access_token
        })
        return self.repository.save(company)

    def update_message(self, company_id: int, message_id: int) -> Company:
        print("MySQlに応募者の情報を登録しました")
        return self.repository.update_message(company_id, message_id)

    def find_by_line_user_id(self, line_id: str) -> Company:
        return self.repository.find_by_line_id(line_id)
class CompanyRepositoryModule(Module):
    def configure(self, binder):
        # binder.bind(AbstractNotify, to=SlackNotification)
        binder.bind(AbstractCompanyDatabase, to=CompanyRDBMS)