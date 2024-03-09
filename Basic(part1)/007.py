name = input("Name of the file and extension: ")
fname = name.split(".")
print(f'The extension of the file is: '+ repr(fname[-1]))