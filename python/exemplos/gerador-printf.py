contra = ''
with open ('programa-c.c', 'w') as f:
	f.write('#include <stdio.h>\n')
	f.write('\n')
	f.write('int main(){\n')
	for c in range(1,101):
		f.write('	printf("Linha {}\{}n");\n'.format(c, contra))
	f.write('}')
