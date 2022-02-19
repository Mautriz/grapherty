from grapherty.definitions import Datum
from grapherty.definitions.graph import Graph
from grapherty.definitions.graph_context import GraphContext
from . import PropertyOne


class PropertyTwo(Datum):
    @classmethod
    async def calculate(cls, ctx: GraphContext):
        property_one = await Graph.resolve(PropertyOne, ctx)
        print(f"property_one: {property_one}")
        return " assurdo in incredibile"
