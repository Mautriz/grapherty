import abc
import asyncio

from typing import Any, Type

from grapherty.definitions.graph_context import GraphContext

DatumClassList = list[Type["Datum"]]


class Datum(abc.ABC):
    is_property = False

    @classmethod
    async def resolve(cls, ctx: GraphContext):
        # Proprietà con task di risoluzione già lanciato
        if ctx.resolvers.has(cls):
            return await ctx.resolvers.get_key_result(cls)

        print(
            f"sto ricalcolando la classe {cls} con resolvers {ctx.resolvers}, len: {len(ctx.resolvers.resolver_map.items())}"
        )

        # Una volta acquisito tutto il necessario, inizia a calcolare la proprietà attuale
        resolver_task = asyncio.get_event_loop().create_task(cls.calculate(ctx))
        ctx.resolvers.set(cls, resolver_task)

        # Aspetta la risoluzione della proprietà corrente
        return await resolver_task

    @classmethod
    async def calculate(cls, ctx: GraphContext):
        """Function to calculate the actual value, it may require other dependencies on runtime if necessary"""
        dependencies = await cls.resolve_dependencies(ctx)
        return await cls.do_calculate(ctx, dependencies)

    @classmethod
    async def do_calculate(cls, ctx: GraphContext, dependencies: dict[Any, Any]):
        ...

    @classmethod
    async def resolve_dependencies(cls, ctx: GraphContext):
        # Risolve le dipendenze in modo ricorsivo e le aggiunge in resolvers
        dependencies = await cls.dependencies(ctx)
        dependencies_resolvers = [datum.resolve(ctx) for datum in dependencies]
        await asyncio.gather(*dependencies_resolvers)
        return await ctx.resolvers.get_keys_result(dependencies)

    @classmethod
    async def dependencies(cls, ctx: GraphContext) -> DatumClassList:
        """This function is called pre-calculate"""
        return []
