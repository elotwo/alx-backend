#!/usr/bin/env python3
def index_range(page, page_size):
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
