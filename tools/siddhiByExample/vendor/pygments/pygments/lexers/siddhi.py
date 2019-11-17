# -*- coding: utf-8 -*-
"""
    pygments.lexers.siddhi
    ~~~~~~~~~~~~~~~~~~~~~~

    Lexers for the Google Go language.

    :copyright: Copyright 2006-2015 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import re

from pygments.lexer import RegexLexer, bygroups, words
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation

__all__ = ['SiddhiLexer']


class SiddhiLexer(RegexLexer):
    """
    For `Go <http://golang.org>`_ source.

    .. versionadded:: 1.2
    """
    name = 'Siddhi'
    filenames = ['*.siddhi']
    aliases = ['siddhi']
    mimetypes = ['text/x-balsrc']

    flags = re.MULTILINE | re.UNICODE

    tokens = {
        'root': [
            (r'\n', Text),
            (r'\s+', Text),
            (r'\\\n', Text),  # line continuations
            (r'//(.*?)\n', Comment.Single),
            (r'/(\\\n)?[*](.|\n)*?[*](\\\n)?/', Comment.Multiline),
            (r'(import|package)\b', Keyword.Namespace),
            (r'(define|stream|table|aggregation|trigger|window|select|insert|into|function|plan|partition|delete|update|return|overwrite)\b', Keyword.Declaration),
            (words((
                'group', 'by', 'having', 'events', 'output', 'expired', 'current', 'snapshot', 'for', 'raw', 'of',
                'as', 'at', 'or', 'and', 'in', 'on', 'is', 'not', 'within', 'with', 'begin', 'end', 'null', 'every',
                'last', 'all', 'first', 'join', 'inner', 'outer', 'right', 'left', 'full', 'unidirectional'), suffix=r'\b'),
             Keyword),
            (r'(true|false|years|year|months|month|weeks|week|days|day|hours|hour|minutes|minute|min|seconds|second|sec|milliseconds|millisecond|millisec)\b', Keyword.Constant),

            (words(('println','parse'), suffix=r'\b(\()'),
             bygroups(Name.Builtin, Punctuation)),

            # function names
            #(r'.*\:(.*)\(', bygroups(Name.Builtin, Punctuation)),

            #annotations
            #(r'(@.*)\b(\{)', Punctuation),
                      
            (words((
                'int','float', 'long', 'string', 'bool', 'double', 'object'), suffix=r'\b'),
             Keyword.Type),
            # imaginary_lit
            (r'\d+i', Number),
            (r'\d+\.\d*([Ee][-+]\d+)?i', Number),
            (r'\.\d+([Ee][-+]\d+)?i', Number),
            (r'\d+[Ee][-+]\d+i', Number),
            # float_lit
            (r'\d+(\.\d+[eE][+\-]?\d+|'
             r'\.\d*|[eE][+\-]?\d+)', Number.Float),
            (r'\.\d+([eE][+\-]?\d+)?', Number.Float),
            # int_lit
            # -- octal_lit
            (r'0[0-7]+', Number.Oct),
            # -- hex_lit
            (r'0[xX][0-9a-fA-F]+', Number.Hex),
            # -- decimal_lit
            (r'(0|[1-9][0-9]*)', Number.Integer),
            # char_lit
            (r"""'(\\['"\\abfnrtv]|\\x[0-9a-fA-F]{2}|\\[0-7]{1,3}"""
             r"""|\\u[0-9a-fA-F]{4}|\\U[0-9a-fA-F]{8}|[^\\])'""",
             String.Char),
            # StringLiteral
            # -- raw_string_lit
            (r'`[^`]*`', String),
            # -- interpreted_string_lit
            (r'"(\\\\|\\"|[^"])*"', String),
            # Tokens
            (r'(<=|>=|'
             r'|->|==|!=|\.\.\.|[+\-*/%&])', Operator),
            (r'[|^<>=!()\[\]{}.,;:]', Punctuation),
            # identifier
            (r'[^\W\d]\w*', Name.Other),
            (r'(@.*)(?:\{)', Name.Decorator),
            (r'.*\:(.*)\(', Punctuation),
        ]
    }
