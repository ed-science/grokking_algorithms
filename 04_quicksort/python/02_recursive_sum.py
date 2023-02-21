def sum(list):
  return 0 if list == [] else list[0] + sum(list[1:])
