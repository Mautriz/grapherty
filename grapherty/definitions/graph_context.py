from dataclasses import dataclass

from grapherty.definitions.input import Input
from grapherty.definitions.resolvers import Resolvers


@dataclass
class GraphContext:
    resolvers: Resolvers
    input: Input
