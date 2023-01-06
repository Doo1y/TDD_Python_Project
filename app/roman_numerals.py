def parse(val):
  numerals_base = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
  }

  numerals_shortcut = {
    "IV": -2,
    "IX": -2,
    "XL": -20,
    "XC": - 20,
    "CD": -200,
    "CM": -200
  }
  total = 0
  # idx = 0, 1, 2, 3, 4...
  for idx in range(len(val)):
    total += numerals_base[val[idx]]
    if idx <= (len(val) - 2) and (val[idx] + val[idx + 1]) in numerals_shortcut:
      total += numerals_shortcut[val[idx] + val[idx + 1]]
  return total