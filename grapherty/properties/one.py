from grapherty.definitions import Datum


class PropertyOne(Datum):
    @classmethod
    async def calculate(cls, resolvers):
        print("Sto venendo calcolato, sono proprietà numero 1")

        return "ciao sono mauro"
