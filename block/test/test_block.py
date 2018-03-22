import collections


import block as bl


import pytest


@pytest.fixture
def matt_node():
    node = bl.Node('matt')
    return node

def test_hash(matt_node):
    node = matt_node
    gb, hash = node.process_txns([])
    print(f'Genesis block {gb.todict()}, \nHash {hash}')
    assert hash.startswith('0')


def test_bad_difficulty(matt_node):
    #node = bl.Node('matt')
    node = matt_node
    with pytest.raises(TypeError):
        gb, hash = node.process_txns([], difficulty='1')

@pytest.mark.parametrize('uuid',
                         ['123', 'matt'])
def test_node(uuid):
    #for uuid in ['123', 'matt']:
    n = bl.Node(uuid)
    assert n.uuid == uuid
