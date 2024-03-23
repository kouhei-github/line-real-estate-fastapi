from .abstruct import AbstractCompanyDatabase
from models.index import Company
from config.index import get_db
from sqlalchemy.orm import Session
from schemas.index import CompanySchema

class CompanyRDBMS(AbstractCompanyDatabase):
    def __init__(self):
        self.db: Session = next(get_db())

    def save(self, data: CompanySchema) -> dict:
        company = Company(
            name=data.name,
            line_id=data.line_id,
            channel_access_token=data.channel_access_token
        )

        self.db.add(company)
        self.db.commit()
        self.db.refresh(company)
        return {"message": "Company created"}

    def update_message(self, id: int, message_id: int) -> Company:
        company = self.db.query(Company).get(id)
        company.message_id = message_id

        self.db.commit()
        self.db.refresh(company)
        return company

    def find_by_line_id(self, line_id: str) -> Company:
        record = self.db.query(Company).filter(Company.line_id == line_id).first()
        self.db.close()
        return record

    def find_by_id(self, id: int) -> Company:
        record = self.db.query(Company).get(id)
        self.db.close()
        return record