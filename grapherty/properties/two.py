from grapherty.definitions import Datum, DatumClassList
from grapherty.definitions.graph_context import GraphContext
from . import PropertyOne


class PropertyTwo(Datum):
    @classmethod
    async def do_calculate(cls, ctx: GraphContext, dependencies: dict):
        return dependencies[PropertyOne] + " assurdo in incredibile"

    @classmethod
    async def dependencies(cls, ctx) -> DatumClassList:
        return [PropertyOne]
