# NumPy - Trigonometric Functions
import numpy as np

# angles in radians
angles = np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2])

# Trigonometric functions
sin_ang = np.sin(angles)
cos_ang = np.cos(angles)
tan_ang = np.tan(angles)

# Inverse trigonometric functions
arcsin_ang = np.arcsin(sin_ang)
arccos_ang = np.arccos(cos_ang)
arctan_ang = np.arctan(tan_ang)

# Hyperbolic functions
sinh_ang = np.sinh(angles)
cosh_ang = np.cosh(angles)
tanh_ang = np.tanh(angles)

# Convert degrees to radians and back
degrees = np.array([0, 30, 45, 60, 90])
radians = np.deg2rad(degrees)
degrees_back = np.rad2deg(radians)

print("Sine:", sin_ang)
print("Cosine:", cos_ang)
print("Tangent:", tan_ang)
print("Arcsine:", arcsin_ang)
print("Arccosine:", arccos_ang)
print("Arctangent:", arctan_ang)
print("Hyperbolic Sine:", sinh_ang)
print("Hyperbolic Cosine:", cosh_ang)
print("Hyperbolic Tangent:", tanh_ang)
print("Radians:", radians)
print("Degrees:", degrees_back)
