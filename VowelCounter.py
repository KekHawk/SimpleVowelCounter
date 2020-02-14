userInput = input("Word to count vowels:\n").lower()

vowelsCount = {vowel: userInput.count(vowel) for vowel in ("a", "e", "i", "o", "u")}

for vowelKey, vowelValue in vowelsCount.items():
    print("{}: {}".format(vowelKey, vowelValue))
print("Total: {}".format(sum(vowelsCount.values())))

