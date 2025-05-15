import logging

from sqlalchemy.ext.asyncio import AsyncSession

from schemas.statistic import ActiveStatistic
from utils.utils import to_snake


class StatisticService:
    def __init__(self):
        self.logger = logging.getLogger(to_snake(self.__class__.__name__))

    async def active_statistic(self, session: AsyncSession) -> ActiveStatistic:
        self.logger.debug('Fetching statistic for active users/commands')
        return ActiveStatistic(active_users=0, active_commands=0)


statistic_service = StatisticService()
