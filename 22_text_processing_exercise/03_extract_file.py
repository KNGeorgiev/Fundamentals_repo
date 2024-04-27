def extract_file(line):

    line = line.split("\\")
    file = line[-1].split(".")

    return print(f"File name: {file[0]}\n"
                 f"File extension: {file[1]}")


file_path = input()
extract_file(file_path)
