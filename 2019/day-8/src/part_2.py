IMAGE_WIDTH = 25
IMAGE_HEIGHT = 6


def main() -> None:
    with open("day-8.in", "r") as image_file:
        image_string = str(image_file.readline().rstrip())

    pixels_per_image = IMAGE_HEIGHT * IMAGE_WIDTH

    decoded_image = list("2" * pixels_per_image)
    for i in range(0, len(image_string), pixels_per_image):
        current_layer = image_string[i : i + pixels_per_image]

        for index, pixel in enumerate(list(current_layer)):
            # Replace 0 pixel with empty space for legibility
            if pixel == "0":
                pixel = " "
            if pixel == "1":
                pixel = "█"
            if decoded_image[index] == "2" and pixel != "2":
                decoded_image[index] = pixel

    for index in range(0, len(decoded_image), IMAGE_WIDTH):
        print("".join(decoded_image[index : index + IMAGE_WIDTH]))


if __name__ == "__main__":
    main()
