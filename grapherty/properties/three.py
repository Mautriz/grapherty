from grapherty.definitions.datum import Datum
from grapherty.definitions.graph import Graph
from grapherty.definitions.graph_context import GraphContext

from . import PropertyTwo


class PropertyThree(Datum):
    @classmethod
    async def calculate(cls, ctx: GraphContext):
        if ctx.input["name"]:
            await Graph.resolve(PropertyTwo, ctx)
            return "ao"
        else:
            print(f"resolvers no two: {ctx.resolvers}")
            return "XD"
