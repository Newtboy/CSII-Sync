import copy

def power(base, exp): # {
    if (exp == 1): # {
        return base
    # }
    return base * power(base, exp-1)
# }

def alien_ears(n): # {
    even = n % 2 == 0
    return alien_ears_helper(n, even)
# }

def alien_ears_helper(n, even: bool): # {
    if (n == 1): # {
        return 2+int(not even);
    # }
    return (alien_ears_helper(n-1, not even)+ 2+int(not even))
# }

"""
The helper method of the recursion.
:param x: The x value in the 2D map (x values increase going to the right)
:param y: The y value in the 2D map (y values increase going downwards)
:param old_color: A 'color' value that is the color to be changed
:param new_color: The new 'color' value that we want to see
:param image: The 2D map we are using
"""
def flood_fill_helper(x: int, y: int, old_color, new_color, image:list[list]):
    # Base case: Check if out of bounds or the color matches the old color
    if (x > len(image)-1 or x < 0): # {
        return
    # }
    if (y > len(image[0])-1 or y < 0): # {
        return
    # }
    if (image[x][y] != old_color): # {
        return
    # }

    # General case: Change the color and then visit all adjacent pixels
    image[x][y] = new_color
    flood_fill_helper(x + 1, y, old_color, new_color, image)
    flood_fill_helper(x - 1, y, old_color, new_color, image)
    flood_fill_helper(x, y + 1, old_color, new_color, image)
    flood_fill_helper(x, y - 1, old_color, new_color, image)

def flood_fill(row, col, new_color, image):
    # If the starting pixel already has the new color, nothing needs to be done
    if image[row][col] == new_color:
        return image

    # Call our search, also giving the starting pixel's original color
    flood_fill_helper(row, col, image[row][col], new_color, image)

    return image
