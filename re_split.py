import re

# input = 100,000,000.000
regex_pattern = r"[,.]+"
print("\n".join(re.split(regex_pattern, input())))
