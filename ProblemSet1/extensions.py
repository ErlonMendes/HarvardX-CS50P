file = input("File name: ").lower().strip()
p = file.rfind(".")
if file[p+1:] == "gif" or file[p+1:] == "jpeg" or file[p+1:] == "png":
    print(f"image/{file[p+1:]}")
elif file[p+1:] == "jpg":
    print("image/jpeg")
elif file[p+1:] == "pdf" or file[p+1:] == "zip":
    print(f"application/{file[p + 1:]}")
elif file[p+1:] == "txt":
    print("text/plain")
else:
    print("application/octet-stream")
