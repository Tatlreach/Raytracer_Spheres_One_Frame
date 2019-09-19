import vec3
import ray

import vec3_test

from random import random

import camera

# vec3_test.test_vec3()

# ordered TODOs
#   create a vec3 class
#   test all it's funcs in main

#   create ray class
#   test all it's funcs in main

#   find how write to file

#   write fadeBlueBackround func

#   how to gen rand numbers

#   create render loop

#   loop writing fadeBlueBackround func to file

#   write 

def give_fade_blue_down(ray):
	# goal color is vec3(.5, .7, 1.0)	//blue
	# start is white(1,1,1)
	# r's original y val goes from -1, 1
		# 1 then *.5, to go 0-1
	unit_direction = vec3.unit_vector( ray.direction() )
	percent = 0.5*(1.0 + unit_direction.e[1])

	return vec3.lerp( vec3.vec3(in_list=[1.0, 1.0, 1.0]), vec3.vec3(in_list=[0.5, 0.7, 1.0]), percent)

def color(ray, world=None, reflects_left=25):
    return give_fade_blue_down(ray=ray)


sample_count = 1
cam = camera.camera()

with open('testPPM.ppm', 'w') as image_file:
    width = 200
    height = 100
#	fWidth = float(width)
#	fHeight = float(height)
    print_count=4000

    image_file.write("P3\n{w} {h}\n255\n".format(w=width, h=height))
    for i in range((height-1), -1,-1):
        for j in range(width):
            col = vec3.vec3(in_list=[0.0, 0.0, 0.0])
            for s in range(sample_count):
                # x_percent = (j + random()) / width
                # y_percent = (i + random()) / height

                x_percent = j / width
                y_percent = i / height

                r = cam.get_ray(x_percent = x_percent, y_percent = y_percent)
                col += color(ray = r)
            
            col.idiv_float(sample_count)
            if (print_count > 0):
                print_count-=1
                print("{red} {green} {blue}\n".format(red=col[0], green=col[1], blue=col[2]))

            ir = int(255.99 * col[0])
            ig = int(255.99 * col[1])
            ib = int(255.99 * col[2])
            image_file.write("{red} {green} {blue}\n".format(red=ir, green=ig, blue=ib))

#	///give background fade white to blue upward

#	//pixel coordinates
#		//x goes from 0 to 4
#		//y goes from 0 to 2
#		//z is set at -1
