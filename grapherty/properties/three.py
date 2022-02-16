from grapherty.definitions import Datum, DatumClassList
from grapherty.definitions.graph_context import GraphContext
from grapherty.definitions.resolvers import Resolvers
from . import PropertyTwo


class PropertyThree(Datum):
    @classmethod
    async def do_calculate(cls, ctx: GraphContext, dependencies):
        if ctx.input["name"]:
            await PropertyTwo.resolve(ctx)
            return "ao"
        else:
            print(f"resolvers no two: {ctx.resolvers}")
            return "XD"

    @classmethod
    async def dependencies(cls, ctx) -> DatumClassList:
        return []
