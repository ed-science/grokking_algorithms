def count(list):
  return 0 if list == [] else 1 + count(list[1:])
