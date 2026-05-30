import zipfile
filename = input("Enter file name: ")
file = open(filename, "w")
text = input("Enter file content: ")
file.write(text)
file.close()
with zipfile.ZipFile("files.zip", "w") as zipf:
    zipf.write(filename)
print("File zipped successfully")
with zipfile.ZipFile("files.zip", "r") as zipf:
    zipf.extractall("Extracted_Files")
print("File unzipped successfully")
[25bcs155@mepcolinux ex10]$python3 ex10d.py
Enter file name: sample.txt
Enter file content: welcome to python
File zipped successfully
File unzipped successfully
