from PersianStemmer import PersianStemmer

ps = PersianStemmer()

extra_words = []
with open('persian-stopwords/short', encoding='UTF-8') as my_file:
    for line in my_file:
        extra_words.append(line.replace('\n', ''))

extra_chars = ['\n', '\r']
with open('persian-stopwords/chars', encoding='UTF-8') as my_file:
    for line in my_file:
        extra_chars.append(line.replace('\n', ''))


def remove_extra_words(string):
    string = str(string)
    for char in extra_chars:
        string = string.replace(char, ' ')
    string = ps.run(string)

    edit_string_as_list = string.split()

    return [word for word in edit_string_as_list if word not in extra_words]
    # return edit_string_as_list
