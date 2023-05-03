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
