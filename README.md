# Static site generator
This project is created through the boot.dev backend development course, it was a lot of fun and a great way to learn recursion and templating for static websites such as blogs!

This project generates static sites based on your markdown files. It will recursively generate pages based on all .md files in the content folder.

## Usage
1. Add markdown content in the ./content folder
2. Have a template.html file with your desired structure, must include a {{ Title }} and {{ Content }} for the templating
3. Static assets in the ./static folder (css and images for example)
4. run ```./main.sh```
5. This will start a server at localhost:8888 and looks something like this: ![image](https://github.com/Insanityandme/static-site-generator/assets/1380257/799f7793-49b3-4ccd-8f04-b53b150838f2)
6. Success! 
