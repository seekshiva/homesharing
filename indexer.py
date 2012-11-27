import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("root", help="absolute root path of your media files")
parser.add_argument("-s", "--saveto", help="Saves the mp4 files found to the file specified here. Else, it will be sent to the Standard Output")
args = parser.parse_args()
print "The root is set to: ", args.root


if args.saveto:
    print "Files will be saved to: ", args.saveto
    wfile = open(args.saveto, "w")
    wfile.write("var movies = {\n")
else:
    print "Output will be sent to Standard I/O"

print

for dirname, dirnames, filenames in os.walk(args.root):
    for filename in filenames:
        ext = os.path.splitext(filename)[1][1:]
        
        if ext == "mp4":
            path = "/".join(dirname.split("/")[:-1])[9:]
            title = dirname.split("/")[-1]
            img = 5
            try:
                list = os.listdir(dirname).index("folder.jpg")
                img = 1
            except:
                img = 0
            
            
            if args.saveto:
                wfile.write('    "%s": {\n'%title)
                wfile.write('        "title": "%s",\n'%title)
                wfile.write('        "path": "%s",\n'%os.path.join(path, title))
                wfile.write('        "file": "%s",\n'%filename)
                if img==1:
                    wfile.write('        "art": "folder.jpg"\n')
                else:
                    wfile.write('        "art": undefined\n')
                    

                wfile.write('    },\n')
                
            print title
            print "path:\t", os.path.join(path, title)
            print "file:\t", filename
            if img == 1:
                print "art :\tfolder.jpg"
            else:
                print "art :\tnone"
            print
            
print

if args.saveto:
    wfile.write('}')
    wfile.close()
