#!/usr/bin/python3

class Text(str):

    def __str__(self):

        result = super().__str__()
        result = result.replace('<', '&lt;')
        result = result.replace('>', '&gt;')
        result = result.replace('"', '&quot;')
        result = result.replace('\n', '\n<br />\n')
        return result


class Elem:

    class ValidationError(Exception):
        def __init__(self) -> None:
            super().__init__("incorrect behaviour.")

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        self.tag = tag
        self.attr = attr if attr else {}
        self.tag_type = tag_type
        
        if content is not None:
            if not Elem.check_type(content):
                raise Elem.ValidationError()
            if isinstance(content, list):
                self.content = [elem for elem in content if elem != Text('')]
            elif content != Text(''):
                self.content = [content]
            else:
                self.content = []
        else:
            self.content = []

    def __str__(self):
        if self.tag_type == 'double':
            content_str = self.__make_content()
            if content_str:
                return f"<{self.tag}{self.__make_attr()}>{content_str}</{self.tag}>"
            else:
                return f"<{self.tag}{self.__make_attr()}></{self.tag}>"
        elif self.tag_type == 'simple':
            return f"<{self.tag}{self.__make_attr()} />"

    def __make_attr(self):
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        if len(self.content) == 0:
            return ''
        result = '\n'
        for elem in self.content:
            result += '  ' + str(elem).replace('\n', '\n  ') + '\n'
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))

def create_html():
    html = Elem(tag='html')
    head = Elem(tag='head')
    title = Elem(tag='title', content=Text('Hello ground!'))

    head.add_content(title)
    html.add_content(head)
    
    body = Elem(tag='body')
    h1 = Elem(tag='h1', content=Text('Oh no, not again!'))
    img = Elem(tag='img', attr={'src': 'http://i.imgur.com/pfp3T.jpg'}, tag_type='simple')
    
    body.add_content(h1)
    body.add_content(img)
    html.add_content(body)
    
    print(html)

if __name__ == '__main__':
    create_html() 
