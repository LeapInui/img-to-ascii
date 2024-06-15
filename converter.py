from PIL import Image

def convert(image_path, new_width = 150, threshold = 150):
    image = Image.open(image_path) # 

    width, height = image.size
    ratio = height / width
    new_height = int(ratio * new_width) // 2
    image = image.resize((new_width, new_height))

    image = image.convert("L") # Convert to greyscale
    pixels = image.getdata()

    character_list = []

    for pixel in pixels:
        if pixel < threshold:
            character_list.append(" ")
        else:
            character_list.append(".")

    characters = "".join(character_list)

    rows = []
    pixel_count = len(characters)

    for i in range(0, pixel_count, new_width):
        row = characters[i: i + new_width]
        rows.append(row)
    
    ascii_image = "\n".join(rows)

    return ascii_image

if __name__ == "__main__":
    image_path = "resources/image.jpg" # Path name here!!

    file = open("output.txt", "w")
    file.write(convert(image_path, 200, 170)) # Can mess around with values to potentially achieve better or worse results
    print("File created")
