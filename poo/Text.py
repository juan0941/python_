print("TEXO 1")
print("                                          ")


class Text:
    def __init__(self, type_, paragraphs):
        self.type_ = type_
        self.paragraphs = paragraphs
        self.text_name = False
        self.author_name = False

    def name_t(self):
        self.text_name = True
        print("El titulo del texto es: Ante la ley")

    def author(self):
        self.author_name = True
        print("El autor del tecto es: Franz Kafka")


Text1 = Text("narrativo", "8 parrafos")
print("El texto es de tipo:", Text1.type_)
print("El texto tiene", Text1.paragraphs)
Text1.name_t()
Text1.author()
# ////////////////////////////////////////////////////////////
print("                                          ")
print("TEXTO 2")
print("                                          ")


class story(Text):
    def __init__(self, type_, paragraphs, who_wrote_it, name_story):
        super().__init__(type_, paragraphs)
        self.who_wrote_it = who_wrote_it
        self.name_story = name_story

    def writer(self):
        print(f"El autor del cuento es {self.who_wrote_it}")

    def story(self):
        print(f"El nombre del cuento es {self.name_story}")


story1 = story("ficcion", "23 parrafos", "Oscar Wilde", "El Príncipe Feliz")
print("El genero del cuento es:", story1.type_)
print("El cuento tiene", story1.paragraphs)
story1.writer()
story1.story()
