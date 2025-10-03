from impyrial.length.api import convert_unit

# Make sure unit checking is working by trying examples
print('The following line should run:')
result1 = convert_unit(10, 'in', 'yd')
print(result1)

print('The following line should cause an error:')
result2 = convert_unit(10, 'lb', 'yd')
print(result2)
