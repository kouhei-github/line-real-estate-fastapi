import uuid, os
from schemas.index import FollowWebHook
from repositories.users.interface import UserRepositoryModule, UserRepository
from repositories.company.interface import CompanyRepositoryModule, CompanyRepository
from injector import Injector
from injector import Injector
from linebot import LineBotApi

async def follow_use_case(body: FollowWebHook) -> str:
    print(body)

    print(f"body.destination: {body.destination}")

    # 会社
    company_injector = Injector([CompanyRepositoryModule()])
    company_repository = company_injector.get(CompanyRepository)
    company = company_repository.find_by_line_user_id(body.destination)

    # line sdk
    bot = LineBotApi(company.channel_access_token)

    # user
    profile = bot.get_profile(body.events[0].source.userId)
    injector = Injector([UserRepositoryModule()])
    _injection = injector.get(UserRepository)
    # 存在するか確認
    user = _injection.find_by_line_user_id(profile.user_id)
    if user is None:
        res = _injection.register(
            profile.user_id,
            profile.display_name,
            profile.picture_url,
            company
        )
    return body.events[0].source.userId
