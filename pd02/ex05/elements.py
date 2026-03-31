#!/usr/bin/python3

import elem as e


class Html(e.Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='html', attr=attr, content=content, tag_type='double')


class Head(e.Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='head', attr=attr, content=content, tag_type='double')


class Body(e.Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='body', attr=attr, content=content, tag_type='double')


class Title(e.Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='title', attr=attr, content=content, tag_type='double')


class Meta(e.Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='meta', attr=attr, content=content, tag_type='simple')


class Img(e.Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='img', attr=attr, content=content, tag_type='simple')


class Table(e.Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='table', attr=attr, content=content, tag_type='double')


class Th(e.Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='th', attr=attr, content=content, tag_type='double')


class Tr(e.Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='tr', attr=attr, content=content, tag_type='double')


class Td(e.Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='td', attr=attr, content=content, tag_type='double')


class Ul(e.Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='ul', attr=attr, content=content, tag_type='double')


class Ol(e.Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='ol', attr=attr, content=content, tag_type='double')


class Li(e.Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='li', attr=attr, content=content, tag_type='double')


class H1(e.Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='h1', attr=attr, content=content, tag_type='double')


class H2(e.Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='h2', attr=attr, content=content, tag_type='double')


class P(e.Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='p', attr=attr, content=content, tag_type='double')


class Div(e.Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='div', attr=attr, content=content, tag_type='double')


class Span(e.Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='span', attr=attr, content=content, tag_type='double')


class Hr(e.Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='hr', attr=attr, content=content, tag_type='double')


class Br(e.Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='br', attr=attr, content=content, tag_type='double')


def create_html():
    html = Html([
        Head([
            Title(e.Text("Hello ground!"))
        ]),
        Body([
            H1(e.Text("Oh no, not again!")),
            Img(attr={'src': 'http://i.imgur.com/pfp3T.jpg'})
        ])
    ])
    print(html)


if __name__ == '__main__':
    create_html()