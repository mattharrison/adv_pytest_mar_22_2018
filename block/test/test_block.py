import collections


import block as bl


import pytest


def test_hash():
    node = bl.Node('matt')
    gb, hash = node.process_txns([])
    print(f'Genesis block {gb.todict()}, \nHash {hash}')
    assert hash.startswith('0')


def test_bad_difficulty():
    node = bl.Node('matt')
    with pytest.raises(TypeError):
        gb, hash = node.process_txns([], difficulty='1')
