from typing import Optional, Union, List, Dict

CacheDict = Dict[int, int]
CacheType = Union[List[int], CacheDict]


def eating_cookies(n: int, cache: Optional[CacheType] = None) -> int:
    # a base case if n is less than zero
    if n < 0:
        return 1

    # build the cache if cache is empty
    if cache == None:
        cache = {key: 0 for key, value in enumerate(range(n+1))}
        cache[0] = 1

    # if found in cache
    # use that instead
    if cache[n] > 0:
        return cache[n]
    # otherwise, add the small cases to the cache
    elif n == 1:
        cache[n] = 1
    elif n == 2:
        cache[n] = 2
    elif n == 3:
        cache[n] = 4
    # build the permutations of n in the cache
    else:
        cache[n] = eating_cookies(
            n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)

    # return permutation from the cache
    return cache[n]
