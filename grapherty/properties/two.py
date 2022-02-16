from grapherty.definitions import Datum, DatumClassList
from grapherty.definitions import Resolvers
from . import PropertyOne


class PropertyTwo(Datum):
    @classmethod
    async def calculate(cls, resolvers: Resolvers):
        return await resolvers.get_key_result(PropertyOne) + " assurdo in incredibile"

    @classmethod
    async def dependencies(cls) -> DatumClassList:
        return [PropertyOne]
