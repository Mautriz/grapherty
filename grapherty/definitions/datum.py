import abc
import asyncio

from asyncio import Task
from typing import Any, Type
from . import Resolvers

DatumClassList = list[Type["Datum"]]


class Datum(abc.ABC):
    is_property = False

    @classmethod
    async def resolve(cls, resolvers: Resolvers):
        # Proprietà con task di risoluzione già lanciato
        if resolvers.has(cls):
            return await resolvers.get_key_result(cls)

        print(f"sto ricalcolando la classe {cls} con resolvers {resolvers}")

        # Risolve le dipendenze in modo ricorsivo e le aggiunge in resolvers
        dependencies = await cls.dependencies()
        dependencies_resolvers = [datum.resolve(resolvers) for datum in dependencies]
        await asyncio.gather(*dependencies_resolvers)

        # Una volta acquisito tutto il necessario, inizia a calcolare la proprietà attuale
        resolver_task = asyncio.get_event_loop().create_task(cls.calculate(resolvers))
        resolvers.set(cls, resolver_task)

        # Aspetta la risoluzione della proprietà corrente
        return await resolver_task

    @classmethod
    async def calculate(cls, resolved):
        """Function to calculate the actual value, it may require other dependencies on runtime if necessary"""
        return None

    @classmethod
    async def dependencies(cls) -> DatumClassList:
        """This function is called pre-calculate"""
        return []
