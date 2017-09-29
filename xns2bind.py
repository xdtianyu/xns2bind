#!/bin/env python3

import xml.etree.ElementTree as x


def parse(file):

    name = file[:-3]

    tree = x.parse(file)
    root = tree.getroot()

    for child in root:
        if child.tag == 'rdata':
            sub = child[0].text + '.'

            if sub == '@.':
                sub = ''

            print(sub + name, '\t', child[5].text, '\tIN\t', child[1].text, '\t', child[3].text)


if __name__ == "__main__":
    import sys
    parse("".join(sys.argv[1:]))
