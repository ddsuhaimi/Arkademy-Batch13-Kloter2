from itertools import permutations


def findSame(strings_list):
  is_perm_word_exist = False
  has_been_found = [False for i in range(len(strings_list))]
  for i in range(len(strings_list)):
    # comparator = strings_list[i+1:]
    word = strings_list[i]
    perm_list = [''.join(p) for p in permutations(word)]
    same_word = []
    for j in range(i+1, len(strings_list)):
      if strings_list[j] in perm_list and not has_been_found[j]:
        same_word.append(strings_list[j])
        has_been_found[j] = True
        is_perm_word_exist = True
        # print(i, j, word, strings_list[j])
    same_word.insert(0, word)
    if len(same_word) > 1:
      print(same_word)
      
  if not is_perm_word_exist:
    print('Tidak ditemukan!')
    

findSame(['cat', 'listen', 'code', 'act', 'silent', 'tac'])
# ['cat', 'act', 'tac']
# ['listen', 'silent']

findSame(['try', 'fired', 'dark']) 
# Tidak ditemukan!