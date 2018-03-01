# -*- coding: utf-8 -*-


def get_attr(obj, attr):
    """Safe getting object attribute"""
    try:
        return getattr(obj, attr)
    except AttributeError:
        return


def concat_attrs(obj, attrs):
    """Concat object attributes"""
    acc = []
    for attr in attrs:
        value = get_attr(obj, attr)
        if value:
            acc += value
    return tuple(acc)
