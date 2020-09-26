from random import randint
from src.parser.wordreader import Reader


class Generator:

    @staticmethod
    def generate(split: bool) -> str:
        words, sup_limit = Reader.words()
        password = []

        for _ in range(4):
            word = words[randint(0, sup_limit)]
            word = word[:word.find('\n')]
            password.append(word)
        return '-'.join(password) if split else ''.join(password)


print(Generator.generate(True))
print(Generator.generate(False))
