import difflib

def compare_files(file1, file2):
  """Compares two text files and returns a list of differences.

  Args:
    file1: The first text file.
    file2: The second text file.

  Returns:
    A list of differences between the two files. Each difference is a tuple of
    three elements: the line number, the text in the first file, and the text in
    the second file.
  """

  with open(file1, "r") as f1:
    lines1 = f1.readlines()

  with open(file2, "r") as f2:
    lines2 = f2.readlines()

  differences = []
  for i, line1 in enumerate(lines1):
    if line1 != lines2[i]:
      differences.append((i + 1, line1, lines2[i]))

  return differences


def main():
  file1 = input("Enter the path to the first file: ")
  file2 = input("Enter the path to the second file: ")

  differences = compare_files(file1, file2)

  if differences:
    print("The following differences were found between the two files:")
    for difference in differences:
      print("Line {}: {} {}".format(*difference))
  else:
    print("The two files are identical.")


if __name__ == "__main__":
  main()