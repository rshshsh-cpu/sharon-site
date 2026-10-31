#!/usr/bin/env python3
"""Update Google rating and review count on the site.
Usage: python3 tools/update-reviews.py <rating> <count>   e.g. 5.0 51
Changes every element marked data-g="rating" / data-g="count" in index.html.
"""
import re, sys
rating, count = sys.argv[1], sys.argv[2]
float(rating); int(count)  # sanity check
p = 'index.html'
s = open(p, encoding='utf-8').read()
new = re.sub(r'(data-g="rating">)[^<]*', r'\g<1>' + f'{float(rating):.1f}', s)
new = re.sub(r'(data-g="count">)[^<]*', r'\g<1>' + str(int(count)), new)
if new == s:
    print('no change')
else:
    open(p, 'w', encoding='utf-8').write(new)
    print('updated')
