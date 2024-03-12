import uuid, os
from schemas.index import FollowWebHook
from repositories.users.interface import UserRepositoryModule, UserRepository
from injector import Injector
from linebot import LineBotApi

async def follow_use_case(body: FollowWebHook) -> str:
    print(body)

    # line sdkでuserのメールアドレスを取得する
    bot = LineBotApi(os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))

    profile = bot.get_profile(body.events[0].source.userId)
    injector = Injector([UserRepositoryModule()])
    _injection = injector.get(UserRepository)
    # 存在するか確認
    user = _injection.find_by_line_user_id(profile.user_id)
    if user is None:
        res = _injection.register(
            profile.user_id,
            str(uuid.uuid4()),
            "nH%n&CaninHn%4AC&A47inHC",
            profile.picture_url
        )
    return body.events[0].source.userId
