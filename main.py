filename = input("Enter filename: ")
try:
    infile = open(filename, "r")
    line = infile.readline()
    value = int(line)
except FileNotFoundError:
    print("Error '"+filename+"' file not found")
except ValueError:
    print("Error '"+line+"' cannot be converted to an interger")