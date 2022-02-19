import grapherty
import pytest

from grapherty.definitions import Graph
from grapherty.properties.one import PropertyOne
from grapherty.properties.three import PropertyThree
from grapherty.properties.two import PropertyTwo


def test_version():
    assert grapherty.__version__ == "0.0.1"


@pytest.mark.asyncio
async def test_properties():
    assert await Graph.resolve_tree(
        [
            PropertyThree,
            PropertyTwo,
            PropertyTwo,
            PropertyTwo,
            PropertyThree,
            PropertyThree,
            PropertyThree,
            PropertyThree,
            PropertyThree,
            PropertyThree,
            PropertyThree,
            PropertyTwo,
            PropertyTwo,
            PropertyTwo,
            PropertyOne,
        ],
        {"name": "CIAOOO!!!!"},
    ) == {
        PropertyThree: "ao",
        PropertyTwo: " assurdo in incredibile",
        PropertyOne: "ciao sono mauro",
    }
