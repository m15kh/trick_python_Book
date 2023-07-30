import struct

# Define the format string for the data (unsigned integer and a float)
format_string = "I f"

# Create a Struct object with the format string
data_struct = struct.Struct(format_string)

# Data to pack
unsigned_int_value = 42
float_value = 3.14

# Pack the data into binary format
packed_data = data_struct.pack(unsigned_int_value, float_value)

# Print the packed binary data
print("Packed data:", packed_data)

# Unpack the data back into Python values
unpacked_data = data_struct.unpack(packed_data)
print("Unpacked data:", unpacked_data)
