file_path = "wonderwall.txt"  # Replace with the path to your .txt file

with open(file_path, 'r') as file:
        file_contents = file.read()
        print(file_contents)        

#separar lineas pares e impares 
lines = file_path.readline()
lineas_pares = []
lineas_impares = []
for i, lines in enumerate (lines):
        if i % 2 == 0:
        lineas_pares.append(lines)

        else
        lineas_impares.append(lines)

with open('pares.txt', 'w') as archivo_pares:
        archivo_pares.writelines(lineas_pares) 
        print(lineas_pares) 
# # Define the string containing multiple lines
# input_string = file_contents

# # # Define the keyword you want to search for in the lines
# # keyword = "keyword"

# # Split the string into lines
# lines = input_string.split('\n')

# # # Select lines containing the keyword
# # selected_lines = [line for line in lines if keyword in line]

# # # Join the selected lines back into a single string
# # result_string = '\n'.join(selected_lines)

# # Print or use the result_string as needed
# print(result_string)
