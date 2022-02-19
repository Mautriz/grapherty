from grapherty.definitions import Datum
from grapherty.definitions.graph_context import GraphContext


class PropertyOne(Datum):
    @classmethod
    async def calculate(cls, ctx: GraphContext):
        return "ciao sono mauro"
