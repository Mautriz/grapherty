from asyncio import Task
from typing import Any


class Resolvers:
    resolver_map = {}

    def __init__(self) -> None:
        pass

    def set(self, k, v: Task[Any]):
        self.resolver_map[k] = v

    def has(self, k):
        return k in self.resolver_map

    async def get_key_result(self, k):
        return await self.resolver_map[k]

    async def get_keys_result(self, keys: list[Any]) -> dict[Any, Any]:
        return {k: await self.get_key_result(k) for k in keys}

    async def get_complete_result(self):
        return {k: await v for k, v in self.resolver_map.items()}
