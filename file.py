
my_file = open("HelloWorld.txt", "wb");
print "File Name = ", my_file.name;

print "File STARTS HERE --------!"
my_file.write("Hello World! My name is Pranjal and this a sample file created by python code");

my_file.close();


my_file = open("HelloWorld.txt", "rb");
print my_file.read();
my_file.close();
