import asyncio
from typing import Type

from grapherty.definitions.graph_context import GraphContext

from . import Resolvers, Datum, Input


class Graph:
    @classmethod
    async def resolve_depedency_tree(cls, properties: list[Type[Datum]], input: Input):
        # Qui sarebbe da aggiungerci vecchie proprietà tramite chiamate a db, anch'esse come task in modo che il resto dei calcoli inizino comunque
        ctx = GraphContext(resolvers=Resolvers(), input=input)

        await asyncio.gather(*[prop.resolve(ctx) for prop in properties])
        return await ctx.resolvers.get_complete_result()
