import os

f = input("Enter file name : ");
f,ext = os.path.splitext(f);
print(ext);
