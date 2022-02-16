from grapherty.definitions import Datum


class PropertyOne(Datum):
    @classmethod
    async def do_calculate(cls, dependencies, resolvers):
        return "ciao sono mauro"
