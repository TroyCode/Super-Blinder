class Words:
  def __init__(self):
    self.count_list = {}

  def add_list(self, word_array):
    for word in word_array:
      if self.count_list.get(word):
        self.count_list[word] = self.count_list[word] + 1
      else:
        self.count_list.setdefault(word, 1)

  def dic_sort(self):
    import operator
    self.count_list = sorted(self.count_list.items(), key=operator.itemgetter(1))
    self.count_list.reverse()
