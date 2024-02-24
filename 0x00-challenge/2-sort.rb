# Sample input array with mixed types
input_array = ARGV.map { |arg| arg.match?(/^\d+$/) ? arg.to_i : arg }

# Separate numbers and strings
numbers = input_array.select { |item| item.is_a?(Integer) }
strings = input_array.reject { |item| item.is_a?(Integer) }

# Sort numbers and strings individually
sorted_numbers = numbers.sort
sorted_strings = strings.sort

# Combine sorted numbers and strings
sorted_array = sorted_numbers + sorted_strings

# Output the sorted array
puts sorted_array
