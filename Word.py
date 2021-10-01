def most_long_prefix_per_word(prefix):
    most_long_prefix = 0
    for pref in prefix:
        if len(pref) > most_long_prefix:
            most_long_prefix = len(pref)
    return most_long_prefix


class Word:
    def __init__(self, input_1: str, input_2: str):
        self.input_1 = int(input_1)
        self.input_2 = input_2.split(" ")
        self.size_word_input_2 = [len(i) for i in self.input_2]

    def is_1_length_prefix_word(self, mot: str):
        return not any(word != mot and word[0] == mot[0] for word in self.input_2)

    def list_prefix_per_word(self, word):
        prefix = []
        for word2 in self.input_2:
            i = 0
            current_prefix = ""

            while word2[i] == word[i] and word != word2:
                current_prefix += word2[i]
                i += 1
            prefix.append(current_prefix)

        return prefix

    def uniq_prefix(self):
        list_prefix = []
        for word in self.input_2:
            if self.is_1_length_prefix_word(word):
                list_prefix.append(1)
            else:
                prefix = self.list_prefix_per_word(word)
                most_long_prefix = most_long_prefix_per_word(prefix)

                list_prefix.append(most_long_prefix + 1)

        return [self.input_2[ind][:p] for ind, p in enumerate(list_prefix)]
