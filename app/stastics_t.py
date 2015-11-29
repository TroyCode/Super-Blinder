import stastics

w = stastics.Words()
word_list = ["troy", "abc", "cnn", "cmd", "cnn"]
time = 50

w.add_list(word_list, time)

print w.count_list