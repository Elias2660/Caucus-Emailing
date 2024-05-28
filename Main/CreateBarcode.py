
import code128
from PIL import Image, ImageDraw, ImageFont, ImageOps



def createBarcode(code:int, out_filename: str):
    
    # Get barcode value
    barcode_param = str(code)

    # Create barcode image
    barcode_image = ImageOps.colorize(code128.image(barcode_param, height=100).convert("L"), black='#0629B0', white="white")

    # Create empty image for barcode + text
    top_bott_margin = 80
    l_r_margin = 10
    new_height = barcode_image.height +  top_bott_margin
    new_width = barcode_image.width + (2* l_r_margin)
    new_image = Image.new( 'RGB', (new_width, new_height), (255, 255, 255))

    # put barcode on new image
    barcode_y = 30
    new_image.paste(barcode_image, (int((new_width - barcode_image.width) / 2), barcode_y))

    # object to draw text
    draw = ImageDraw.Draw(new_image)
    
    # Define custom text size and font
    footer_size = 20
    
    footer_font = ImageFont.truetype("Open_Sans/static/OpenSans-Regular.ttf", footer_size)

    # Calculate the width of the text
    text_width= draw.textlength(barcode_param, font=footer_font)


    # Calculate the center of the barcode
    center_barcode = (barcode_image.width / 2)
    
    # Calculate the position of the text
    text_position = (center_barcode - (text_width / 2), (new_height - footer_size - 20))

    # Draw text on picture
    draw.text(text_position, barcode_param, fill=(6, 41, 176), font=footer_font)


    # save in file 
    new_image.save(f'{out_filename}', 'PNG')
    
    
    
if __name__ == "__main__":
    createBarcode((122344521312166789), "barcode.png")


