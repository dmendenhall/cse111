# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from code import InteractiveConsole
from random import randint
from turtle import width
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_cloud(canvas, 25, 325, 100)
    draw_cloud(canvas, 200, 250, 72)
    draw_ground(canvas, scene_width, scene_height)
    draw_pine_tree(canvas, 570, 172, 280)
    draw_pine_tree(canvas, 440, 80, 400)
    draw_new_pine(canvas, randint(200, 300), randint(280, 380))
    draw_new_pine(canvas, randint(50, 150), randint(250, 350))
    draw_new_pine(canvas, randint(600, 700), randint(250, 350))
    draw_sun(canvas, 650, 350, 120)

    draw_picket(canvas, 10, 0, 150, scene_width)
    # draw_grid(canvas, scene_width, scene_height, 100)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):
    # Draw the sky
    draw_rectangle(canvas, 0, scene_height / 2.5, scene_width, scene_height,
                   width=0, fill="Deep Sky Blue2")


def draw_sun(canvas, sun_left, sun_top, sun_radius):
    # Draw the sun
    draw_oval(canvas, sun_left, sun_top, sun_left +
              sun_radius, sun_top + sun_radius, fill="yellow2")


# def draw_cloud(canvas, cloud_left, cloud_top, cloud_radius)
def draw_cloud(canvas, cloud_left, cloud_top, cloud_radius):
    # Draw a cloud
    draw_oval(canvas, cloud_left, cloud_top, cloud_left + cloud_radius + 20,
              cloud_top + cloud_radius, outline="white", fill="white")
    draw_oval(canvas, cloud_left + 50, cloud_top + 50, cloud_left + 50 + cloud_radius + 20,
              cloud_top + 50 + cloud_radius, outline="white", fill="white")
    draw_oval(canvas, cloud_left + 80, cloud_top + 20, cloud_left + 80 + cloud_radius + 20,
              cloud_top + 20 + cloud_radius, outline="white", fill="white")


def draw_ground(canvas, scene_width, scene_height):
    # Draw the ground
    draw_rectangle(canvas, 0, 0, scene_width,
                   scene_height / 2.5, fill="green4")


def draw_pine_tree(canvas, center_x, bottom, height):
    # Draw the trunk of the tree
    trunk_width = height / 20
    trunk_height = height / 8
    left_trunk = center_x - trunk_width / 2
    bottom_trunk = bottom
    right_trunk = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height
    draw_rectangle(canvas, left_trunk, bottom_trunk,
                   right_trunk, trunk_top, fill="sienna4")

    # draw the skirt of the tree
    skirt_width = height / 2
    skirt_left = center_x - skirt_width / 2
    skirt_bottom = trunk_top
    skirt_center = center_x
    skirt_top = bottom + height
    skirt_right = center_x + skirt_width / 2
    draw_polygon(canvas, skirt_left, skirt_bottom, skirt_center,
                 skirt_top, skirt_right, skirt_bottom, fill="Dark Green")


def draw_new_pine(canvas, peak_x, peak_y):
    skirt_left = peak_x - 70
    skirt_right = peak_x + 70
    skirt_bottom = peak_y - 210
    trunk_left = peak_x - 10
    trunk_right = peak_x + 10
    trunk_bottom = peak_y - 260

    draw_rectangle(canvas, trunk_left, trunk_bottom,
                   trunk_right, skirt_bottom, fill="brown")

    draw_polygon(canvas, skirt_left, skirt_bottom, peak_x, peak_y,
                 skirt_right, skirt_bottom, fill="lime")


def draw_picket(canvas, center_x, bottom, height, width):
    # Draw a picket fence
    picket_width = int(height / 10)
    picket_left = center_x - picket_width / 2
    picket_bottom = bottom
    picket_top_middle = height + picket_width
    picket_right = center_x + picket_width / 2
    interval = 100
    for i in range(0, width, picket_width * 2):
        draw_polygon(canvas, picket_left + i, picket_bottom, picket_left + i, height, center_x + i,
                     picket_top_middle, picket_right + i, height, picket_right + i, bottom, fill="white")


def draw_grid(canvas, width, height, interval, color="light grey"):
    # Draw vertical lines
    label_y = 15
    for x in range(0, width, interval):
        draw_line(canvas, x, 0, x, height, fill=color)
        draw_text(canvas, x, label_y, f"{x}", fill=color)

    label_x = 15
    for y in range(0, height, interval):
        draw_line(canvas, 0, y, width, y, fill=color)
        draw_text(canvas, label_x, y, f"{y}", fill=color)


# Call the main function so that
# this program will start executing.
main()
