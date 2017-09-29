#!/bin/env python3

import xml.etree.ElementTree as x


def parse(file):

    name = file[:-3]

    tree = x.parse(file)
    root = tree.getroot()

    for child in root:
        if child.tag == 'rdata':
            sub = child[0].text + '.'
            rr_pref = child[4].text + '\t'

            if sub == '@.':
                sub = ''

            if rr_pref == 'N/A\t':
                rr_pref = ''

            print(sub + name + '\t' + child[5].text + '\tIN\t' + child[1].text + '\t' + rr_pref + child[3].text)


if __name__ == "__main__":
    import sys
    parse("".join(sys.argv[1:]))
