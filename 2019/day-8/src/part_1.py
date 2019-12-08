IMAGE_WIDTH = 25
IMAGE_HEIGHT = 6


def main() -> None:
    with open("day-8.in", "r") as image_file:
        image_string = str(image_file.readline().rstrip())

    pixels_per_image = IMAGE_HEIGHT * IMAGE_WIDTH

    min_layer = "0" * (pixels_per_image + 1)
    for i in range(0, len(image_string), pixels_per_image):
        layer = image_string[i : i + pixels_per_image]

        if layer.count("0") < min_layer.count("0"):
            min_layer = layer

    print(min_layer.count("1") * min_layer.count("2"))


if __name__ == "__main__":
    main()
