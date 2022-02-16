import asyncio
from typing import Type

from . import Resolvers, Datum, Input


class Graph:
    @classmethod
    async def resolve_depedency_tree(cls, properties: list[Type[Datum]], input: Input):

        # Qui sarebbe da aggiungerci vecchie proprietà tramite chiamate a db, anch'esse come task in modo che il resto dei calcoli inizino comunque
        resolvers = Resolvers()

        await asyncio.gather(*[prop.resolve(resolvers) for prop in properties])
        return await resolvers.get_complete_result()
