#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re
import sys


def main():
    doc = sys.stdin.read()

    doc = strip_apparatus(doc)
    doc = strip_verses(doc)
    doc = strip_marks(doc)

    doc = lines(doc)

    print doc


def strip_apparatus(doc):
    regex = re.compile(r'\n.*(WH|RP|NIV|Treg).*\n.*\n.*\n')
    return re.sub(regex, ' ', doc)


def strip_verses(doc):
    doc = re.sub(r'\d:\d', '', doc)
    doc = re.sub(r'\d+', '', doc)
    regex = re.compile(r'\n_+ Other Endings.*', re.DOTALL)
    doc = re.sub(regex, '', doc)
    return doc


def strip_marks(doc):
    doc = re.sub(r'⸀|⸂|⸃|⸁', '', doc)
    return doc


def lines(doc):
    doc = re.sub(r'\n ', '\n', doc)
    doc = re.sub(r'\n', "\n\n", doc)
    return doc


if __name__ == "__main__":
    main()
