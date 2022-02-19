import asyncio
import logging
from typing import Type

from grapherty.definitions.graph_context import GraphContext

from . import Resolvers, Datum, Input


class Graph:
    @staticmethod
    async def resolve_tree(properties: list[Type[Datum]], input: Input):
        # Qui sarebbe da aggiungerci vecchie proprietà tramite chiamate a db, anch'esse come task in modo che il resto dei calcoli inizino comunque
        ctx = GraphContext(resolvers=Resolvers(), input=input)
        await Graph.resolve_many(properties, ctx)

        return await ctx.resolvers.get_complete_result()

    @staticmethod
    async def resolve_many(properties: list[Type[Datum]], ctx: GraphContext):
        await asyncio.gather(*[Graph.resolve(prop, ctx) for prop in properties])
        return await ctx.resolvers.get_keys_result(properties)

    @staticmethod
    async def resolve(datum: Type[Datum], ctx: GraphContext):
        # Proprietà con task di risoluzione già lanciato
        if ctx.resolvers.has(datum):
            return await ctx.resolvers.get_key_result(datum)

        logging.info(
            f"sto ricalcolando la classe {datum} con resolvers {ctx.resolvers}, len: {len(ctx.resolvers.resolver_map.items())}"
        )

        # Una volta acquisito tutto il necessario, inizia a calcolare la proprietà attuale
        resolver_task = asyncio.get_event_loop().create_task(datum.calculate(ctx))
        ctx.resolvers.set(datum, resolver_task)

        # Aspetta la risoluzione del
        return await resolver_task
