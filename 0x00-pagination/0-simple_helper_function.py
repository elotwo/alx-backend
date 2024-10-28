#!/usr/bin/env python3
"""
this script is about pagination
"""


def index_range(page, page_size):
    """
    indext_range takes two arguiment to
    return start and end of a page
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
