def scale_variable(value, min_in, max_in, min_out, max_out):
    # Calculate the normalized value within the input range
    normalized_value = (value - min_in) / (max_in - min_in)

    # Scale the normalized value to the output range
    scaled_value = (normalized_value * (max_out - min_out)) + min_out

    return scaled_value

# Example usage
input_value = 141
scaled_value = scale_variable(input_value, 120, 180, 0, 180)
print(scaled_value)