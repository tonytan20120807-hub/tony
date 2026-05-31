from core.state import STATE

import math

def formula(solid: str):
    for formula in STATE["formula"]:
        if formula["name"]==solid:
            return formula
        return "Formula for solid not found"
    
def prism(width: float,length: float, height: float):
    volume = width*length*height
    surface_area = 2.0*(width*length+width*height+length*height)
    return f"the volume is {volume}, the surface area is {surface_area}"

def sphere(radius: float):
    volume = (4.0/3.0)*math.pi*radius^3.0
    surface_area = 4.0*math.pi*radius^2.0
    return f"the volume is {volume}, the surface area is {surface_area}"

def cylinder(radius: float, height: float):
    volume = math.pi*radius^2.0*height
    surface_area = 2.0*math.pi*radius^2.0+2.0*math.pi*radius*height
    return f"the volume is {volume}, the surface area is {surface_area}"

def pyramid(width: float,length: float, height: float):
    volume = (1.0/3.0)*width*length*height
    return f"the volume is {volume}"

def cone(radius: float, height: float, slantheight: float):
    volume = (1.0/3.0)*math.pi*radius^2.0*height
    surface_area = math.pi*radius*(radius+slantheight)
    return f"the volume is {volume}, the surface area is {surface_area}"