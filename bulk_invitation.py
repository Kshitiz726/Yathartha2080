from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

folder_path = 'C:/Users/Kshitiz/Downloads/output'
if not os.path.exists(folder_path):
    os.mkdir(folder_path)

# Read the Excel file containing the names
df = pd.read_excel("C:/Users/Kshitiz/Downloads/Names.xlsx")

# # Convert the names to upper case
# df["Name"] = df["Name"].str.upper()

# Open the PSD file and convert it to RGB mode
template_path = "C:/Users/Kshitiz/Downloads/invitation.psd"
original_template = Image.open(template_path).convert("RGB")

# Specify the font and font size to be used
font_path = "C:/Users/Kshitiz/Downloads/HANDYMAN Regular/Six Hands Web Black.ttf"
font_size = 80

# Iterate over the names in the Excel file
for index, row in df.iterrows():
    # Create a fresh copy of the original template for each student
    template_copy = original_template.copy()

    # Create a draw object for the template copy
    draw = ImageDraw.Draw(template_copy)

    # Specify the font and font size
    font = ImageFont.truetype(font_path, font_size)

    # Get the size of the text using the ImageFont object
    text_width, text_height = draw.textsize(row["Name"], font=font)

    # Calculate the center position of the text
    y_offset = 50
    x = (template_copy.width - text_width) / 2
    y = (template_copy.height - text_height) / 2.25 + y_offset

    # Insert the name into the image
    draw.text((x, y), row["Name"], fill='#c92812', font=font)

    # Save the image with the inserted name as a PNG file
    output_path = f"{folder_path}/{row['Name']}.png"
    template_copy.save(output_path)


