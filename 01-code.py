import io
try:
    file = open('data_1.txt','r')
    data = file.read()
    print(data)
except FileNotFoundError:
    print("File not found")
    print("Creating file")
    file = open('data_1.txt','w')
except io.UnsupportedOperation:
    print("Change File Mode")
except BaseException:
    print("Some Error")
finally:
    print("Finally Executed")
    file.close()
