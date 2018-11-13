# Input sequences mERG

This python script generates a sequence (of custom length) of hexagonic inputs that can be used in [multifocal electroretinography](https://en.wikipedia.org/wiki/Electroretinography) studies or computational modeling of the human eye.

## Usage
Navigate to the directory the python script was put into. Then do:

```python
python generate.py *mode* *radius* *size_x* *size_y* *output_directory* *output_size*
```
- *mode* is the image type (e.g. RGB or 1 for 1-bit black-white, check [Pillow Documentation](https://pillow.readthedocs.io/en/5.3.x/handbook/concepts.html#modes) for more info)
- *radius* is the radius for each hexagon (all have the same)
- *size_x* and *size_y* the dimensions of the image
- *output_directory* is the directory the images will be saved in
- *output_size* is the name of the output image

## Showcase of images
##### This image is colored to better depict the rings of eccentricity
![Colored Hexagon](https://raw.githubusercontent.com/verrannt/Input_sequences_mERG/master/HexagonColored.png =200x)
##### This is how an image generated by the script looks that can be used as input
![BlackWhite Hexagon](https://raw.githubusercontent.com/verrannt/Input_sequences_mERG/master/HexagonBlackWhite1.png =200x)
