
# This entrypoint file to be used in development. Start by reading README.md
from arithmetic_arranger import arithmetic_arranger
from unittest import main

x = arithmetic_arranger(["32 + 698"])
print(x)
