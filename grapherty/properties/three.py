from grapherty.definitions import Datum, DatumClassList
from . import PropertyTwo


class PropertyThree(Datum):
    @classmethod
    async def calculate(cls, resolved):
        if True:
            await PropertyTwo.resolve(resolved)
            return "ao"
        else:
            print(f"resolved no two: {resolved}")
            return "XD"

    @classmethod
    async def dependencies(cls) -> DatumClassList:
        return []
