# -*- coding: utf-8 -*-
# <nbformat>4</nbformat>

# <markdowncell>

# # Variables
# * point_index
# * school_id
# * color
# * radius
# * starting_x_position
# * starting_y_position
# * ending_x_position
# * ending_y_position

# <codecell>

import random
import pandas as pd

# <codecell>

main_school_enrollment = 450
size_of_plot = 300
space_between_areas = 50
default_radius = '4'
color_list = ['#cf2030', '#ff7300', '#ffcc00', '#69c242', '#64bbe3']
target_color = color_list[4]
n_colors = len(color_list)

# <codecell>

def create_random_percentages(length_of_list):
    r = [random.random() for i in range(1,length_of_list + 1)]
    s = sum(r)
    r = [round(i/s,2) for i in r]
    if sum(r) != 1:
        create_random_percentages(length_of_list)
    return r

# <codecell>

def test_color_length(new_color_list, total_number):
    if len(new_color_list) < total_number:
        diff = total_number - len(new_color_list)
        fill_array = [color_list[i] for i in range(0, diff)]
        return fill_array

# <codecell>

def create_color_list(percentage_list, total_number, color_list):
    colors = []
    for i, per in enumerate(percentage_list):
        count = round(total_number * per)
        color = [color_list[i]]
        list_of_colors = color * count
        for color in list_of_colors:
            colors.append(color)
    if len(colors) < total_number:
        colors = test_color_length(colors, total_number)
    if len(colors) > total_number:
        colors = colors[0: total_number]
    random.shuffle(colors)
    return colors

# <codecell>

def make_data(enrollment, 
              school_name,
              starting_min_x,
              starting_max_x, 
              starting_min_y,
              starting_max_y, 
              color_list = color_list,
              n_colors = n_colors):
    school_percentages = create_random_percentages(n_colors)

    point_index = range(0, enrollment)
    school_id = [school_name] * enrollment
    colors = create_color_list(school_percentages, enrollment, color_list)
    radius = [default_radius] * enrollment
    starting_x_position = [random.randint(starting_min_x, starting_max_x) for x in range(0,enrollment)]
    starting_y_position = [random.randint(starting_min_y, starting_max_y) for x in range(0,enrollment)]
    
    data = pd.DataFrame({'point_index': point_index,
             'school_id': school_id,
             'color': colors,
             'radius': radius,
             'starting_x_position': starting_x_position,
             'starting_y_position': starting_y_position})
    return data

# <markdowncell>

# # Make data for main school

# <codecell>

main_school_data = make_data(main_school_enrollment, 
                             'main',
                             starting_min_x = 0,
                             starting_max_x = 300, 
                             starting_min_y = 0,
                             starting_max_y = 300)

# <codecell>

# Shift blue points to the right
main_school_data['ending_x_position'] = main_school_data.starting_x_position
main_school_data.loc[main_school_data.color == target_color, 'ending_x_position'] = main_school_data.starting_x_position + size_of_plot + space_between_areas
main_school_data['ending_y_position'] = main_school_data.starting_y_position

# <codecell>

# Make one student bigger than the others
main_school_data.loc[main_school_data.point_index == 0, 'radius'] = 10

# <codecell>

# Check and export
assert(len(main_school_data) == main_school_enrollment)
main_school_data.to_csv('data/main_school_data.csv', index = False)

# <markdowncell>

# # Make data for 3 other schools

# <codecell>

school_1_enrollment = 225
school_1_data = make_data(school_1_enrollment, 
                          'sch1',
                         starting_min_x = 0,
                         starting_max_x = 100, 
                         starting_min_y = 300,
                         starting_max_y = 400)
school_1_data['ending_x_position'] = school_1_data.starting_x_position
school_1_data.loc[school_1_data.color == target_color, 'ending_x_position'] = school_1_data.starting_x_position + size_of_plot + space_between_areas
school_1_data['ending_y_position'] = school_1_data.starting_y_position

# <codecell>

school_2_enrollment = 500
school_2_data = make_data(school_2_enrollment, 
                          'sch2',
                         starting_min_x = 150,
                         starting_max_x = 250, 
                         starting_min_y = 150,
                         starting_max_y = 250)
school_2_data['ending_x_position'] = school_2_data.starting_x_position
school_2_data.loc[school_2_data.color == target_color, 'ending_x_position'] = school_2_data.starting_x_position + size_of_plot + space_between_areas
school_2_data['ending_y_position'] = school_2_data.starting_y_position

# <codecell>

school_3_enrollment = 300
school_3_data = make_data(school_3_enrollment, 
                          'sch3',
                         starting_min_x = 0,
                         starting_max_x = 100, 
                         starting_min_y = 0,
                         starting_max_y = 100)
school_3_data['ending_x_position'] = school_3_data.starting_x_position
school_3_data.loc[school_3_data.color == target_color, 'ending_x_position'] = school_3_data.starting_x_position + size_of_plot + space_between_areas
school_3_data['ending_y_position'] = school_3_data.starting_y_position

# <codecell>

new_positions = range(0, len(other_school_data[other_school_data.color == target_color])*10, 10)
new_positions = [x + (random.randrange(-1000,1000,1)/10) for x in new_positions]

other_school_data = pd.concat([school_1_data, school_2_data, school_3_data])
other_school_data.loc[other_school_data.color == target_color, 'ending_y_position'] = [random.randint(0,350) for x in range(len(new_positions))]
other_school_data.to_csv('data/other_school_data.csv', index = False)

other_school_data['line_x_position'] = other_school_data.ending_x_position
other_school_data.loc[other_school_data.color == target_color, 'line_x_position'] = new_positions
other_school_data['line_y_position'] = other_school_data.ending_y_position
other_school_data.loc[other_school_data.color == target_color, 'line_y_position'] = 450

# <codecell>

# Find 50 most similar students to main student
main_student_position = 15

# <codecell>

other_school_line_data = other_school_data.loc[other_school_data.color == target_color]
other_school_line_data.to_csv('data/other_school_line_data.csv', index = False)

# <codecell>

other_school_line_data

# <codecell>


