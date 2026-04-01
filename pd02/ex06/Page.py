#!/usr/bin/python3

from elements import Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br, Text, Elem

class Page:
    def __init__(self, element):
        if not isinstance(element, Elem):
            raise Elem.ValidationError()
        self.element = element

    def __str__(self):
        html = str(self.element)
        if isinstance(self.element, Html):
            return "<!DOCTYPE html>\n" + html
        return html

    def write_to_file(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            file.write(str(self))

    def is_valid(self):
        return self._is_valid_node(self.element)


    def _is_valid_node(self, node):
        if isinstance(node, Text):
            return True
        if not isinstance(node, Elem):
            return False

        allowed_types = (
            Html, Head, Body, Title, Meta, Img,
            Table, Th, Tr, Td,
            Ul, Ol, Li,
            H1, H2, P, Div, Span, Hr, Br
        )
        if not isinstance(node, allowed_types):
            return False

        if not self._check_node_rule(node):
            return False

        for child in node.content:
            if not self._is_valid_node(child):
                return False
        return True

    def _check_node_rule(self, node):
        content = node.content

        if isinstance(node, Html):
            return (
                len(content) == 2 and
                isinstance(content[0], Head) and
                isinstance(content[1], Body)
            )

        if isinstance(node, Head):
            return len(content) == 1 and isinstance(content[0], Title)

        if isinstance(node, (Body, Div)):
            allowed = (H1, H2, Div, Table, Ul, Ol, Span, Text)
            return all(isinstance(child, allowed) for child in content)

        if isinstance(node, (Title, H1, H2, Li, Th, Td)):
            return len(content) == 1 and isinstance(content[0], Text)

        if isinstance(node, P):
            return all(isinstance(child, Text) for child in content)

        if isinstance(node, Span):
            return all(isinstance(child, (Text, P)) for child in content)

        if isinstance(node, (Ul, Ol)):
            return len(content) >= 1 and all(isinstance(child, Li) for child in content)

        if isinstance(node, Tr):
            if len(content) < 1:
                return False
            has_th = all(isinstance(child, Th) for child in content)
            has_td = all(isinstance(child, Td) for child in content)
            return has_th or has_td

        if isinstance(node, Table):
            return len(content) >= 1 and all(isinstance(child, Tr) for child in content)

        return True


def run_tests():
    valid_page = Page(
        Html([
            Head([Title(Text("Hello ground!"))]),
            Body([
                H1(Text("Oh no, not again!")),
                Div([
                    Span([
                        Text("inside span"),
                        P(Text("paragraph inside span"))
                    ])
                ]),
                Table([
                    Tr([Th(Text("Name")), Th(Text("Age"))]),
                    Tr([Td(Text("Arthur")), Td(Text("42"))])
                ]),
                Ul([
                    Li(Text("first")),
                    Li(Text("second"))
                ])
            ])
        ])
    )

    invalid_head = Page(
        Html([
            Head([Title(Text("A")), Title(Text("B"))]),
            Body([H1(Text("ok"))])
        ])
    )

    invalid_tr_mixed = Page(
        Html([
            Head([Title(Text("Table test"))]),
            Body([
                Table([
                    Tr([Th(Text("A")), Td(Text("B"))])
                ])
            ])
        ])
    )

    print("[valid_page]", valid_page.is_valid())
    print("[invalid_head]", invalid_head.is_valid())
    print("[invalid_tr_mixed]", invalid_tr_mixed.is_valid())
    print("\nRendered valid page:\n")
    print(valid_page)
    valid_page.write_to_file("page.html")
    print("\nFile written: page.html")


if __name__ == '__main__':
    run_tests()