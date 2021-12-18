sum_of_numbers = 0

f = [x for x in open('day8-input.txt').read().strip().split('\n')]

for line in f:
  wires, output = line.split(' | ')
  wires = wires.split()
  output = output.split()

  displays = {0: '', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
  
  # find the obvious -> 1, 4, 7, 8
  # find len 5 -> 2, 3, 5
  # find len 6 -> 0, 6, 9
  len5 = []
  len6 = []

  for w in wires:
      l = len(w)
      if l == 2: displays[1] = set(w)
      if l == 3: displays[7] = set(w)
      if l == 4: displays[4] = set(w)
      if l == 5: len5.append(set(w))
      if l == 6: len6.append(set(w))
      if l == 7: displays[8] = set(w)

  for w in len6:
      if displays[4].issubset(set(w)): 
          displays[9] = set(w)
      else:
          if displays[7].issubset(set(w)):
              displays[0] = set(w)
          else:
              displays[6] = set(w)

  # then we sort the [2,3,5] group
  for w in len5:
      if displays[7].issubset(set(w)): 
          displays[3] = set(w)
      else:
          if len(set(w).intersection(displays[4])) == 2:
              displays[2] = set(w)
          else:
              displays[5] = set(w)

  digits = ''
  for n in output:
      s = set(n)
      for i, key in enumerate(displays.values()):
          if s == key:
              digits = digits + str(i)
  sum_of_numbers += int(digits)
print(sum_of_numbers)