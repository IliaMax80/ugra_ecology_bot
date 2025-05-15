from sqlalchemy.ext.asyncio import AsyncSession

from repositories.user_repository import user_repository
from schemas.user import UserInit, UserShort, UserAbout


class AccountService:
    async def register_account(self, session: AsyncSession, data: UserInit) -> UserShort:
        user = await user_repository.create_user(session, data)
        return user

    async def fill_about(self, session: AsyncSession, chat_id: int, data: UserAbout):
        user_id = (await user_repository.get_user_by_chat_id(session, chat_id)).id
        await user_repository.fill_about(session, user_id, data)


account_service = AccountService()
