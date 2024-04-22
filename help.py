class HtmlTag:
    def __init__(self, tag, inline=False):
        self.tag = tag
        self.inline = inline
        # self.level = -1
        self.new_line = "\n"

    level = -1

    def __enter__(self):
        self.__class__.level += 1
        print('  ' * self.__class__.level + f"<{self.tag}>", end=f"{self.new_line * (not self.inline)}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('  ' * self.__class__.level * (not self.inline) + f"</{self.tag}>")
        self.__class__.level -= 1

    def print(self, text):
        self.__class__.level += 1
        print(f"{'  ' * (not self.inline) * self.level}{text}", end=f"{self.new_line * (not self.inline)}")
        self.__class__.level -= 1


with HtmlTag('body') as _:
    with HtmlTag('h1') as header:
        header.print('Поколение Python')
    with HtmlTag('p') as section:
        section.print('Cерия курсов по языку программирования Python от команды BEEGEEK')

with HtmlTag('body') as _:
    with HtmlTag('h1', True) as header:
        header.print('Поколение Python')
    with HtmlTag('p', True) as section:
        section.print('Cерия курсов по языку программирования Python от команды BEEGEEK')
