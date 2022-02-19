import abc


from grapherty.definitions.graph_context import GraphContext


class Datum(abc.ABC):
    @classmethod
    async def calculate(cls, ctx: GraphContext):
        """Function to calculate the actual value, it may require other dependencies on runtime if necessary"""
        ...
