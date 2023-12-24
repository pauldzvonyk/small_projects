import pandas
import os


class Definition:
    def __init__(self, term):
        self.term = term

    def get(self):
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, '../data.csv')
        df = pandas.read_csv(file_path)
        return tuple(df.loc[df['word'] == self.term]['definition'])


word = input('Enter a word: ')
answer = Definition(word).get()
print(answer)
print(type(answer))
