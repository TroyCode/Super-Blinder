import time

class Words:
  def __init__(self):
    self.count_list = {}

  def add_list(self, word_array):
    for word in word_array:
      if word in self.count_list:
        self.count_list[word] = self.count_list[word] + 1
      else:
        self.count_list.setdefault(word, 1)

  def dic_sort(self):
    import operator
    self.count_list = sorted(self.count_list.items(), key=operator.itemgetter(1))
    self.count_list.reverse()


class Times:
  def __init__(self):
    self.time_stamp = time.time()
    self.time_dic = {}

  def add_stamp(self, description):
    now = time.time()
    gap = now - self.time_stamp
    self.time_stamp = now
    self.time_dic[description] = gap

  def print_result(self):
    accu = 0.0
    for des in self.time_dic:
      accu = accu + self.time_dic[des]
      print "{des}: {gap}secs".format(
        des=des, 
        gap=round(self.time_dic[des], 1)) 
    print "total time: {}secs".format(round(accu, 1))





