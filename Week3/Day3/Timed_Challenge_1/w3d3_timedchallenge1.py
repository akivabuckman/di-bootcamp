reverseinp= input("Input: ").split(' ')
reverseinp.reverse()
reversed = ""
for i in reverseinp:
    reversed += f"{i} "

print(reversed)