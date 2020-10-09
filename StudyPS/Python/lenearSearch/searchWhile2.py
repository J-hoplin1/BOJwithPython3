from typing import Any, Sequence

def seq_search(a : Sequence, key : Any) -> int: 
    for e in range(len(a)):
        if a[e] == key:
            return e:
        else:
            return -1
