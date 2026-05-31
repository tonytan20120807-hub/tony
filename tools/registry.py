from tools.tools import *

TOOLS = {
    "formula": formula,
    "prism": prism,
    "sphere": sphere,
    "cylinder": cylinder,
    "pyramid": pyramid,
    "cone": cone
}

TOOL_DESCRIPTIONS = {
    "formula": "Show the formulas of the solid. args: solid:str",
    "prism": "Give the volume and the surface area of rectangular prism. args: width:float, length:float, height:float",
    "sphere": "Give the volume and the surface area of sphere. args: radius:float",
    "cylinder": "Give the volume and the surface area of cylinder. args: radius:float, height:float",
    "pyramid": "Give the volume of rectangular pyramid. args: width:float, length:float, height: float",
    "cone": "Give the volume and the surface area of cone. args: radius:float, height:float, slantheight:float"
}