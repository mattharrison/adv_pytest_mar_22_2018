import collections


import block as bl


import pytest


def test_hash():
    node = bl.Node('matt')
    gb, hash = node.process_txns([])
    assert hash.startswith('0')
    
