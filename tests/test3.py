import code128
import PIL

code128.image(12345).save("Hello World.png")  # with PIL present

with open("Hello World.svg", "w") as f:
        f.write(code128.svg("Hello World"))