#  File: Geometry.py
#  Description: Returns if shapes intersect or not
#  Student Name: Nick Lee
#  Student UT EID: bl26395
#  Partner Name: Wendy Zhang
#  Partner UT EID: wz4393
#  Course Name: CS 313E
#  Unique Number: 52240
#  Date Created: 2-9-21
#  Date Last Modified: 2-12-21

import math
import sys

class Point (object):
    # constructor with default values
    def __init__ (self, x = 0, y = 0, z = 0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
    # create a string representation of a Point
    # returns a string of the form (x, y, z)
    def __str__ (self):
        return '(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'
    # get distance to another Point object
    # other is a Point object
    # returns the distance as a floating point number
    def distance (self, other):
        return math.hypot(self.x - other.x, self.y - other.y, self.z - other.z)
    # test for equality between two points
    # other is a Point object
    # returns a Boolean
    def __eq__ (self, other):
        tol = 1.0e-6
        return (abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol) and (abs(self.z - other.z) < tol)

class Sphere (object):
    # constructor with default values
    def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
        self.center = Point(x, y, z)
        self.radius = float(radius)
        self.extreme = [[x - radius, x + radius], [y - radius, y + radius], [z - radius, z + radius]]
    # returns string representation of a Sphere of the form:
    # Center: (x, y, z), Radius: value
    def __str__ (self):
        str_center = 'Center: '+'('+ str(self.center.x) +', ' + str(self.center.y) + ', ' + str(self.center.z) + ')'
        str_radius = 'Radius: ' + str(self.radius)
        return  str_center + ', ' + str_radius
    # compute surface area of Sphere
    # returns a floating point number
    def area (self):
        return 4 * math.pi * self.radius ** 2
    # compute volume of a Sphere
    # returns a floating point number
    def volume (self):
        return 4 / 3 * math.pi * self.radius ** 3
    # determines if a Point is strictly inside the Sphere
    # p is Point object
    # returns a Boolean
    def is_inside_point (self, p):
        return self.radius > (self.center.distance(p))
    # determine if another Sphere is strictly inside this Sphere
    # other is a Sphere object
    # returns a Boolean
    def is_inside_sphere (self, other):
        dist_centers = self.center.distance(other.center)
        # distance between centers plus the radius of the other should be smaller than self.radius
        return (dist_centers + other.radius) < self.radius

    # determine if a Cube is strictly inside this Sphere
    # determine if the eight corners of the Cube are strictly
    # inside the Sphere
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube (self, a_cube):
        # if all cube edges are within the sphere return True
        num_inside = 0
        for point in a_cube.edges:
            diff_dist = self.center.distance(point)
            if diff_dist < self.radius:
                num_inside += 1
        if num_inside == 8:
            return True
        else:
            return False

    # determine if a Cylinder is strictly inside this Sphere
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cyl(self, a_cyl):
        # define the Cylinder as a box and find a min and max of the cylinder
        x_extreme = [a_cyl.center.x - a_cyl.radius, a_cyl.center.x + a_cyl.radius]
        y_extreme = [a_cyl.center.y - a_cyl.radius, a_cyl.center.y + a_cyl.radius]
        z_extreme = [a_cyl.center.z - a_cyl.height / 2, a_cyl.center.z + a_cyl.height / 2]
        print(x_extreme, y_extreme, z_extreme)
        point1 = Point(x_extreme[0], y_extreme[0], z_extreme[0])
        point2 = Point(x_extreme[0], y_extreme[1], z_extreme[0])
        point3 = Point(x_extreme[1], y_extreme[0], z_extreme[0])
        point4 = Point(x_extreme[1], y_extreme[1], z_extreme[0])
        point5 = Point(x_extreme[0], y_extreme[0], z_extreme[1])
        point6 = Point(x_extreme[0], y_extreme[1], z_extreme[1])
        point7 = Point(x_extreme[1], y_extreme[0], z_extreme[1])
        point8 = Point(x_extreme[1], y_extreme[1], z_extreme[1])
        points = [point1, point2, point3, point4, point5, point6, point7, point8]
        num_points = 0
        #if all 8 points of the box is inside the sphere return True
        for point in points:
            print(point)
            if self.is_inside_point(point):
                num_points += 1
        if num_points == 8:
            return True
        else:
            return False

    # determine if another Sphere intersects this Sphere
    # other is a Sphere object
    # two spheres intersect if they are not strictly inside
    # or not strictly outside each other
    # returns a Boolean
    def does_intersect_sphere (self, other):
        # the distance between the center needs to be smaller than the sum of the radius
        if not self.is_inside_sphere(other):
            dist_centers = self.center.distance(other.center)
            return dist_centers <= self.radius + other.radius
        else:
            return False

    # determine if a Cube intersects this Sphere
    # the Cube and Sphere intersect if they are not
    # strictly inside or not strictly outside the other
    # a_cube is a Cube object
    # returns a Boolean
    def does_intersect_cube (self, a_cube):
        # return true if at least one point is inside the sphere
        sphere_cube = Cube(self.center.x, self.center.y, self.center.z, self.radius)
        if not self.is_inside_cube(a_cube):
            if sphere_cube.does_intersect_cube(a_cube) or a_cube.does_intersect_cube(sphere_cube):
                return True
            else:
                return False
        else:
            return False
    # return the largest Cube object that is circumscribed
    # by this Sphere
    # all eight corners of the Cube are on the Sphere
    # returns a Cube object
    def circumscribe_cube (self):
        # the forumula for radius of sphere to side of Cube
        side = self.radius * 2 / math.sqrt(3)
        return Cube(self.center.x, self.center.y, self.center.z, side)

class Cube (object):
    # Cube is defined by its center (which is a Point object)
    # and side. The faces of the Cube are parallel to x-y, y-z,
    # and x-z planes.
    def __init__ (self, x = 0, y = 0, z = 0, side = 1):
        self.center = Point(x, y, z)
        self.side = float(side)
        half = side/2
        self.point1 = Point(x - half, y - half, z - half)
        self.point2 = Point(x + half, y - half, z - half)
        self.point3 = Point(x + half, y + half, z - half)
        self.point4 = Point(x - half, y + half, z - half)
        self.point5 = Point(x - half, y - half, z + half)
        self.point6 = Point(x + half, y - half, z + half)
        self.point7 = Point(x + half, y + half, z + half)
        self.point8 = Point(x - half, y + half, z + half)
        self.edges = [self.point1, self.point2, self.point3, self.point4,
                      self.point5, self.point6, self.point7, self.point8]
        self.extreme = [[x-half,x+half], [y-half,y+half], [z-half,z+half]]
    # string representation of a Cube of the form:
    # Center: (x, y, z), Side: value
    def __str__ (self):
        str_center = 'Center: ' + '(' + str(self.center.x) + ', ' + str(self.center.y) + ', ' + str(self.center.z) + ')'
        str_side = 'Side: ' + str(self.side)
        return str_center + ', ' + str_side
    # compute the total surface area of Cube (all 6 sides)
    # returns a floating point number
    def area (self):
        return float(self.side ** 2 * 6)
    # compute volume of a Cube
    # returns a floating point number
    def volume (self):
        return float(self.side ** 3)
    # determines if a Point is strictly inside this Cube
    # p is a point object
    # returns a Boolean
    def is_inside_point (self, p):
        if (self.extreme[0][0] < p.x < self.extreme[0][1] and
            self.extreme[1][0] < p.y < self.extreme[1][1] and
            self.extreme[2][0] < p.z < self.extreme[2][1]):
            return True
        else:
            return False

    # determine if a Sphere is strictly inside this Cube
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere (self, a_sphere):
        if (self.extreme[0][0] < a_sphere.center.x - a_sphere.radius and
            self.extreme[0][1] > a_sphere.center.x + a_sphere.radius and
            self.extreme[1][0] < a_sphere.center.y - a_sphere.radius and
            self.extreme[1][1] > a_sphere.center.y + a_sphere.radius and
            self.extreme[2][0] < a_sphere.center.z - a_sphere.radius and
            self.extreme[2][1] > a_sphere.center.z + a_sphere.radius):
            return True
        else:
            return False

    # determine if another Cube is strictly inside this Cube
    # other is a Cube object
    # returns a Boolean
    def is_inside_cube (self, other):
        if (self.extreme[0][0] < other.extreme[0][0] and
            self.extreme[0][1] > other.extreme[0][1] and
            self.extreme[1][0] < other.extreme[1][0] and
            self.extreme[1][1] > other.extreme[1][1] and
            self.extreme[2][0] < other.extreme[2][0] and
            self.extreme[2][1] > other.extreme[2][1]):
            return True
        else:
            return False

    # determine if a Cylinder is strictly inside this Cube
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cylinder (self, a_cyl):
        x_extreme = [a_cyl.center.x - a_cyl.radius, a_cyl.center.x + a_cyl.radius]
        y_extreme = [a_cyl.center.y - a_cyl.radius, a_cyl.center.y + a_cyl.radius]
        z_extreme = [a_cyl.center.z - a_cyl.height / 2, a_cyl.center.z + a_cyl.height / 2]
        point1 = Point(x_extreme[0], y_extreme[0], z_extreme[0])
        point2 = Point(x_extreme[0], y_extreme[1], z_extreme[0])
        point3 = Point(x_extreme[1], y_extreme[0], z_extreme[0])
        point4 = Point(x_extreme[1], y_extreme[1], z_extreme[0])
        point5 = Point(x_extreme[0], y_extreme[0], z_extreme[1])
        point6 = Point(x_extreme[0], y_extreme[1], z_extreme[1])
        point7 = Point(x_extreme[1], y_extreme[0], z_extreme[1])
        point8 = Point(x_extreme[1], y_extreme[1], z_extreme[1])
        points = [point1, point2, point3, point4, point5, point6, point7, point8]
        num_points = 0
        for point in points:
            if self.is_inside_point(point):
                num_points += 1
        if num_points == 8:
            return True
        else:
            return False

    # determine if another Cube intersects this Cube
    # two Cube objects intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cube object
    # returns a Boolean
    def does_intersect_cube (self, other):
        num_point = 0
        for point in other.edges:
            if self.extreme[0][0] <= point.x <= self.extreme[0][1] and \
                    self.extreme[1][0] <= point.y <= self.extreme[1][1] and \
                    self.extreme[2][0] <= point.z <= self.extreme[2][1]:
                num_point += 1
        if num_point > 0:
            return True
        else:
            return False

    # determine the volume of intersection if this Cube
    # intersects with another Cube
    # other is a Cube object
    # returns a floating point number
    def intersection_volume (self, other):
        if self.does_intersect_cube(other):
            # x side
            if self.extreme[0][0] <= other.extreme[0][0] <= self.extreme[0][1]:
                x_side = self.extreme[0][1] - other.extreme[0][0]
            elif self.extreme[0][0] <= other.extreme[0][1] <= self.extreme[0][1]:
                x_side = other.extreme[0][1] - self.extreme[0][0]
            # y side
            if self.extreme[1][0] <= other.extreme[1][0] <= self.extreme[1][1]:
                y_side = self.extreme[1][1] - other.extreme[1][0]
            elif self.extreme[1][0] <= other.extreme[1][1] <= self.extreme[1][1]:
                y_side = other.extreme[1][1] - self.extreme[1][0]
            # z side
            if self.extreme[2][0] <= other.extreme[2][0] <= self.extreme[2][1]:
                z_side = self.extreme[2][1] - other.extreme[2][0]
            elif self.extreme[2][0] <= other.extreme[2][1] <= self.extreme[2][1]:
                z_side = other.extreme[2][1] - self.extreme[2][0]
            return x_side * y_side * z_side
        else:
            return 0


    # return the largest Sphere object that is inscribed
    # by this Cube
    # Sphere object is inside the Cube and the faces of the
    # Cube are tangential planes of the Sphere
    # returns a Sphere object
    def inscribe_sphere (self):
        return Sphere(self.center.x, self.center.y, self.center.z, self.side/2)

class Cylinder (object):
    # Cylinder is defined by its center (which is a Point object),
    # radius and height. The main axis of the Cylinder is along the
    # z-axis and height is measured along this axis
    def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
        self.z = float(z)
        self.radius = float(radius)
        self.height = float(height)
        self.center = Point(x,y,z)
    # returns a string representation of a Cylinder of the form:
    # Center: (x, y, z), Radius: value, Height: value
    def __str__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
        str_center = 'Center: ' + '(' + str(self.center.x) + ', ' + str(self.center.y) + ', ' + str(self.center.z) + ')'
        str_radius = 'Radius: ' + str(self.radius)
        str_height = 'Height: ' + str(self.height)
        return str_center + ', ' + str_radius + ', ' + str_height
    # compute surface area of Cylinder
    # returns a floating point number
    def area (self,radius = 1, height = 1):
        return float(2*math.pi* self.radius * (self.radius + self.height))
    # compute volume of a Cylinder
    # returns a floating point number
    def volume (self,radius = 1, height = 1):
        return float(math.pi* self.radius ** 2 * self.height)
    def is_inside_point (self, p):
        # 1/2height is a scalar and centerz-z is a vector.
        # the negative is the direction so we need to do an absolute value of the subtracted result
        center_xy = Point(self.center.x,self.center.y)
        point_xy = Point(p.x,p.y)
        return self.radius > (center_xy.distance(point_xy)) and (1/2)*self.height>(abs(self.center.z-p.z))
    def is_inside_cube (self, a_cube):
        for point in a_cube.edges:
            if not self.is_inside_point(point):
                return False
        return True
    # determine if a Sphere is strictly inside this Cylinder
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere (self, a_sphere):
        # calculate the sphere
        centerxy=Point(self.center.x, self.center.y)
        pointxy=Point(a_sphere.center.x, a_sphere.center.y)
        dist_centers = centerxy.distance(pointxy)
        return (dist_centers + a_sphere.radius) < self.radius and \
               (1/2)*self.height > (abs(self.center.z-a_sphere.center.z)+a_sphere.radius)
    # determine if another Cylinder is strictly inside this Cylinder
    # other is Cylinder object
    # returns a Boolean
    def is_inside_cylinder (self, other):
        centerxy = Point(self.center.x, self.center.y)
        pointxy = Point(other.center.x, other.center.y)
        dist_centers = centerxy.distance(pointxy)
        return self.radius > (dist_centers + other.radius) and \
               (1/2 * self.height) > (abs(self.center.z-other.z)+other.height/2)

    # determine if another Cylinder intersects this Cylinder
    # two Cylinder object intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cylinder object
    # returns a Boolean
    def does_intersect_cylinder (self, other):
        if not self.is_inside_cylinder(other):
            centerxy = Point (self.center.x,self.center.y)
            pointxy=Point(other.center.x,other.center.y)
            dist_centers = centerxy.distance(pointxy)
            if dist_centers <= self.radius+ other.radius:
                z1=[self.z-self.height/2,self.z+self.height/2] #self
                z2=[other.z-other.height/2,other.z+other.height/2] #other
                if z1[0]<=z2[0]<=z1[1] or z1[0]<=z2[1]<=z1[1]:
                    return True
                else:
                    return False
            return False
        return False
def main():
    # read the coordinates of the first Point p
    p = sys.stdin.readline().strip().split()
    p_x = float(p[0])
    p_y = float(p[1])
    p_z = float(p[2])
    # create a Point object
    pobj = Point(p_x, p_y, p_z)
    # read the coordinates of the second Point q
    q = sys.stdin.readline().strip().split()
    q_x = float(q[0])
    q_y = float(q[1])
    q_z = float(q[2])
    # create a Point object
    qobj = Point(q_x, q_y, q_z)
    # read the coordinates of the center and radius of sphereA
    sphereA = sys.stdin.readline().strip().split()
    sphereAx = float(sphereA[0])
    sphereAy = float(sphereA[1])
    sphereAz = float(sphereA[2])
    sphereAr = float(sphereA[3])
    # create a Sphere object
    sphereAobj = Sphere(sphereAx, sphereAy, sphereAz, sphereAr)
    # read the coordinates of the center and radius of sphereB
    sphereB = sys.stdin.readline().strip().split()
    sphereBx = float(sphereB[0])
    sphereBy = float(sphereB[1])
    sphereBz = float(sphereB[2])
    sphereBr = float(sphereB[3])
    # create a Sphere object
    sphereBobj = Sphere(sphereBx, sphereBy, sphereBz, sphereBr)
    # read the coordinates of the center and side of cubeA
    cubeA = sys.stdin.readline().strip().split()
    cubeAx = float(cubeA[0])
    cubeAy = float(cubeA[1])
    cubeAz = float(cubeA[2])
    cubeAside = float(cubeA[3])
    # create a Cube object
    cubeAobj = Cube(cubeAx, cubeAy, cubeAz, cubeAside)
    # read the coordinates of the center and side of cubeB
    cubeB = sys.stdin.readline().strip().split()
    cubeBx = float(cubeB[0])
    cubeBy = float(cubeB[1])
    cubeBz = float(cubeB[2])
    cubeBside = float(cubeB[3])
    # create a Cube object
    cubeBobj = Cube(cubeBx, cubeBy, cubeBz, cubeBside)
    # read the coordinates of the center, radius and height of cylA
    cylA = sys.stdin.readline().strip().split()
    cylAx = float(cylA[0])
    cylAy = float(cylA[1])
    cylAz = float(cylA[2])
    cylAradius = float(cylA[3])
    cylAheight = float(cylA[4])
    # create a Cylinder object
    cylAobj = Cylinder(cylAx, cylAy, cylAz, cylAradius, cylAheight)
    # read the coordinates of the center, radius and height of cylB
    cylB = sys.stdin.readline().strip().split()
    cylBx = float(cylB[0])
    cylBy = float(cylB[1])
    cylBz = float(cylB[2])
    cylBradius = float(cylB[3])
    cylBheight = float(cylB[4])
    # create a Cylinder object
    cylBobj = Cylinder(cylBx, cylBy, cylBz, cylBradius, cylBheight)

    # print if the distance of p from the origin is greater
    # than the distance of q from the origin
    if pobj.distance(Point()) > qobj.distance(Point()):
        t = 'is'
    else:
        t = 'is not'
    print("Distance of Point p from the origin", t, "greater than the distance of Point q from the origin")

    # print if Point p is inside sphereA
    if sphereAobj.is_inside_point(pobj):
        t = 'is'
    else:
        t = 'is not'
    print("Point p", t, "inside sphereA")

    # print if sphereB is inside sphereA
    if sphereAobj.is_inside_sphere(sphereBobj):
        t = 'is'
    else:
        t = 'is not'
    print("sphereB", t, "inside sphereA")

    # print if cubeA is inside sphereA
    if sphereAobj.is_inside_cube(cubeAobj):
        t = 'is'
    else:
        t = 'is not'
    print("cubeA", t, "inside sphereA")
    # print if cylA is inside sphereA
    if sphereAobj.is_inside_sphere(cylAobj):
        t = 'is'
    else:
        t = 'is not'
    print("cylA", t, "inside sphereA")
    # print if sphereA intersects with sphereB
    if sphereBobj.does_intersect_sphere(sphereAobj):
        t = 'does'
    else:
        t = 'does not'
    print("sphereA", t, "intersect sphereB")
    # print if cubeB intersects with sphereB
    if sphereBobj.does_intersect_cube(cubeBobj):
        t = 'does'
    else:
        t = 'does not'
    print("cubeB", t, "intersect sphereB")
    # print if the volume of the largest Cube that is circumscribed
    # by sphereA is greater than the volume of cylA
    circum_cube = sphereAobj.circumscribe_cube()
    if circum_cube.volume() > cylAobj.volume():
        t = 'is'
    else:
        t = 'is not'
    print("Volume of the largest Cube that is circumscribed by sphereA", t, "greater than the volume of cylA")

    # print if Point p is inside cubeA
    if cubeAobj.is_inside_point(pobj):
        t = 'is'
    else:
        t = 'is not'
    print("Point p", t, "inside cubeA")

    # print if sphereA is inside cubeA
    if cubeAobj.is_inside_sphere(sphereAobj):
        t = 'is'
    else:
        t = 'is not'
    print("sphereA", t, "inside cubeA")

    # print if cubeB is inside cubeA
    if cubeAobj.is_inside_cube(cubeBobj):
        t = 'is'
    else:
        t = 'is not'
    print("cubeB", t, "inside cubeA")
    # print if cylA is inside cubeA
    if cubeAobj.is_inside_cylinder(cylAobj):
        t = 'is'
    else:
        t = 'is not'
    print("cylA", t, "inside cubeA")
    # print if cubeA intersects with cubeB
    if cubeAobj.does_intersect_cube(cubeBobj) or cubeBobj.does_intersect_cube(cubeAobj):
        t = 'does'
    else:
        t = 'does not'
    print("cubeA", t, "intersect cubeB")
    # print if the intersection volume of cubeA and cubeB
    # is greater than the volume of sphereA
    if cubeAobj.intersection_volume(cubeBobj) > sphereAobj.volume():
        t = 'is'
    else:
        t = 'is not'
    print("Intersection volume of cubeA and cubeB", t, "greater than the volume of sphereA")

    # print if the surface area of the largest Sphere object inscribed
    # by cubeA is greater than the surface area of cylA
    if cubeAobj.inscribe_sphere().area() > cylAobj.area():
        t = 'is'
    else:
        t = 'is not'
    print("Surface area of the largest Sphere object inscribed by cubeA", t, "greater than the surface area of cylA")
    # print if Point p is inside cylA
    if cylAobj.is_inside_point(pobj):
        t = 'is'
    else:
        t = 'is not'
    print("Point p", t, "inside cylA")
    # print if sphereA is inside cylA
    if cylAobj.is_inside_sphere(sphereAobj):
        t = 'is'
    else:
        t = 'is not'
    print("sphereA", t, "inside cylA")
    # print if cubeA is inside cylA
    if cylAobj.is_inside_cube(cubeAobj):
        t = 'is'
    else:
        t = 'is not'
    print("cubeA", t, "inside cylA")
    # print if cylB is inside cylA
    if cylAobj.is_inside_cylinder(cylBobj):
        t = 'is'
    else:
        t = 'is not'
    print("cylB", t, "inside cylA")
    # print if cylB intersects with cylA
    if cylAobj.does_intersect_cylinder(cylBobj):
        t = 'does'
    else:
        t = 'does not'
    print("cylB", t, "intersect cylA")

if __name__ == "__main__":
  main()