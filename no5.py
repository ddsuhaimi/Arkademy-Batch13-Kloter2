def ganti_kata(word, a, b):
  result = []
  for letter in word:
    if letter == a:
      result.append(b)
    else:
      result.append(letter)
  return result

print(ganti_kata('purwakarta', 'a', 'o'))
      