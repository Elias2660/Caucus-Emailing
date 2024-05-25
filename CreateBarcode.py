
import code128
from PIL import Image, ImageDraw, ImageFont

def createBarcode(code:int, out_filename: str):
    
    # Get barcode value
    barcode_param = str(code)

    # Create barcode image
    barcode_image = code128.image(barcode_param, height=100)

    # Create empty image for barcode + text
    top_bott_margin = 80
    l_r_margin = 10
    new_height = barcode_image.height + int(2 * top_bott_margin)
    new_width = barcode_image.width + (2* l_r_margin)
    new_image = Image.new( 'RGB', (new_width, new_height), (255, 255, 255))

    # put barcode on new image
    barcode_y = 100
    new_image.paste(barcode_image, (0, barcode_y))

    # object to draw text
    draw = ImageDraw.Draw(new_image)

    # Define custom text size and font
    h1_size = 40
    footer_size = 20

    h1_font = ImageFont.truetype("Open_Sans/static/OpenSans_Condensed-Medium.ttf", h1_size)
    footer_font = ImageFont.truetype("Open_Sans/static/OpenSans-Regular.ttf", footer_size)

    # Define custom text
    company_name = 'Junior Prom Ticket Barcode'
    center_barcode_value = (barcode_image.width / 2) - len(barcode_param) * 5.75

    # Draw text on picture
    draw.text( (l_r_margin, 20), company_name, fill=(0, 0, 0), font = h1_font)
    draw.text( (center_barcode_value, (new_height - footer_size - 40)), barcode_param, fill=(0, 0, 0), font=footer_font)

    # save in file 
    new_image.save(f'{out_filename}', 'PNG')
    
if __name__ == "__main__":
    createBarcode((122344521312166789), "barcode.png")
