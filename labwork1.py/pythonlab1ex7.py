def remove_dollar_sign(s):
    return s.replace("$", "")
text = input("Something with $: ")
result = remove_dollar_sign(text)
print(result)