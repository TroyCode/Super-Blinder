import time

class Words:
  def __init__(self):
    self.count_list = []

  def add_list(self, word_array, time):
    for word in word_array:
      is_inside = False
      for item in self.count_list:
        if word in item["Name"]:
          is_inside = True
          item["Count"] = item["Count"] + 1
          item["Times"].append(int(time))
      if not is_inside:
        new_item = {"Name": word, "Count": 1, "Times": [int(time)]}
        self.count_list.append(new_item)

  def dic_sort(self):
    from operator import itemgetter
    self.count_list = sorted(self.count_list, key=itemgetter('Count'))
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





