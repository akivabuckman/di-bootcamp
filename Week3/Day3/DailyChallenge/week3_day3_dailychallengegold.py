letters = list("abcdefghijklmnopqrstuvwxyz")
print(letters)

task = input("encode or decode? ")
message = input("message: ")
shift = int(input("shift: "))
if task == "decode":
    shift *= -1  # changes direction of shift if task is to decode

output = ""
for i in message:
    if i in letters:
        print(letters.index(i))
        output += letters[
            (letters.index(i) + shift) % 26]    # finds letter index in alphabet, adds shift, returns letter
                                                # of shifted index
    else:  # for non-letters like spaces and punctuation
        output += i
print(output)
