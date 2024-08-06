content = ["today's weather is nice"]
filename = ['rando.txt']
for contents, filenames in zip(content, filename):
    file = open(f"../pystuff/{filenames}", "w")
    file.write(contents)