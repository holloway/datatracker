# Copyright The IETF Trust 2012-2019, All Rights Reserved
#!/usr/bin/env python

if __name__ == "__main__":
    import io
    import os
    import json
    from collections import Counter
    from itertools import chain

    def make_path(num):
        return os.path.join(
            os.path.dirname(__file__),
            f"visited-urls.json-{num}.json",
        )
    
    def get_json(num):
        return io.open(make_path(num), 'r', encoding='utf-8')

    print("test", make_path(1858))

    visited_urls_sets = [
        set(json.load(get_json(1858))),
        set(json.load(get_json(1859))),
        set(json.load(get_json(1861))),
        set(json.load(get_json(1862))),
        set(json.load(get_json(1864))),
    ]
    
    # via https://www.geeksforgeeks.org/python-symmetric-difference-of-multiple-sets/
    freq = Counter(chain.from_iterable(visited_urls_sets))
    
    # getting frequency count == x 
    res = list({idx for idx in freq if freq[idx] == 5})
    res.sort()
    
    print(res)

    print(len(res)  / 5)
