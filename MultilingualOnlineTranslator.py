import requests
from bs4 import BeautifulSoup
from argparse import ArgumentParser

def parse_command_line_args():
    parser = ArgumentParser()
    parser.add_argument(dest = "lang1",
                    help='from which language to translate')
    parser.add_argument(dest = "lang2",
                    help='to which language to translate or all')
    parser.add_argument(dest = "word",
                    help="which word to translate")
    args = parser.parse_args()
    return args


def input_data(error=False):
    greeting = '''Hello, you're welcome to the translator. Translator supports: 
1. Arabic
2. German
3. English
4. Spanish
5. French
6. Hebrew
7. Japanese
8. Dutch
9. Polish
10. Portuguese
11. Romanian
12. Russian
13. Turkish
Type the number of your language:\n'''
    dict = {'1': 'arabic',
            '2': 'german',
            '3': 'english',
            '4': 'spanish',
            '5': 'french',
            '6': 'hebrew',
            '7': 'japanese',
            '8': 'dutch',
            '9': 'polish',
            '10': 'portuguese',
            '11': 'romanian',
            '12': 'russian',
            '13': 'turkish'
            }
    lang1 = input(greeting)
    if lang1 not in dict():
        error = True
        return "", "", "", error
    lang2 = input("Type the number of language you want to translate to or \"0\" to translate to all languages:\n")
    if lang2 not in dict():
        error = True
        return "", "", "", error
    word = input('Type the word you want to translate:\n')

    lang1 = dict[lang1]
    if lang2 == '0':
        lang2 = []
        for key in dict:
            if dict[key] != lang1:
                lang2.append(dict[key])
    else:
        lang2 = dict[lang2]
    return lang1, lang2, word, error


def request(lang1, lang2, word):
    url = lang1 + '-' + lang2
    url = 'https://context.reverso.net/translation/{0}/{1}'.format(url, word)
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    return r


def clean_data(r):
    soup = BeautifulSoup(r.content, 'html.parser')
    # words = soup.find_all('a', {'class': 'translation indication ltr dict mobile-hidden no-pos'})
    words = soup.find('div', {'id': 'translations-content'})
    if words:
        words = words.text.split()[:5]
    sentences = soup.find_all('span', {'class': 'text'})
    # elements = [line for line in soup.find_all('span', class_='text')
    #                if 'ltr' in line.parent['class'] or 'rtl' in line.parent['class']]
    return words, sentences


def clean_sentences(sentences):
    res = []
    for i in range(len(sentences)):
        if len(sentences[i].text.split()) < 4:
            continue
        if 'Reverso' in sentences[i].text:
            continue
        if 'Download our free app' in sentences[i].text:
            continue
        sentence = sentences[i].text.strip()
        res.append(sentence)
        if len(res) == 10:
            break
    return res


def print_translations(lang, words, sentences, word=False):
    print()
    print(lang[0].upper() + lang[1:] + ' Translations:')
    if not word:
        for word in words:
            print(word)
    elif words:
        print(words[0])
        with open(f'{word}.txt', 'a') as f:
            f.write(lang[0].upper() + lang[1:] + ' Translations:\n')
            f.write(words[0] + '\n\n')
    print()
    if not word:
        print(lang[0].upper() + lang[1:] + ' Examples:')
        for i, sentence in enumerate(sentences):
            if i % 2 == 1:
                print(sentence)
                print()
            else:
                print(sentence + ':')
    elif sentences:
        print(lang[0].upper() + lang[1:] + ' examples:')
        print(sentences[0] + ':')
        print(sentences[1])
        print()
        with open(f'{word}.txt', 'a') as f:
            f.write(lang[0].upper() + lang[1:] + ' examples:\n')
            f.write(sentences[0] + ':\n')
            f.write(sentences[1]+ '\n\n')

def main():
    # f_l, t_l, w = sys.argv[1:4]
    args = parse_command_line_args()
    if args:
        all = ['arabic', 'german', 'english', 'spanish', 'french',
                    'hebrew', 'japanese', 'dutch', 'polish', 'portuguese',
                    'romanian', 'russian', 'turkish']
        if args.lang1 not in all:
            print(f"Sorry, the program doesn't support {args.lang1}")
            return
        all.append('all')
        if args.lang2 not in all:
            print(f"Sorry, the program doesn't support {args.lang2}")
            return
        all.remove('all')
        lang1 = args.lang1
        if args.lang2 == 'all':
            all.remove(lang1)
            lang2 = all
        else:
            lang2 = args.lang2
        word = args.word
    else:
        lang1, lang2, word, error = input_data()
        if error:
            print("Sorry, the program doesn't support this language")
            return
    if not isinstance(lang2, list):
        r = request(lang1, lang2, word)
        if r.status_code != 200 and r.status_code != 404:
            print("Something wrong with your internet connection")
            return
        if r.status_code == 404:
            print(f"Sorry, unable to find {word}")
            return
        words, sentences = clean_data(r)
        sentences = clean_sentences(sentences)
        print_translations(lang2, words, sentences)
    else:
        for lang in lang2:
            r = request(lang1, lang, word)
            if r.status_code != 200 and r.status_code != 404:
                print("Something wrong with your internet connection")
                return
            if r.status_code == 404:
                print(f"Sorry, unable to find {word}")
                return
            words, sentences = clean_data(r)
            sentences = clean_sentences(sentences)
            print_translations(lang, words, sentences, word)


if __name__ == '__main__':
    main()
