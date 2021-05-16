import ascii_magic
output= ascii_magic.from_image_file("Sour.jpg",columns=175,char=".")
ascii_magic.to_terminal(output)