# Import package
import scipy.io 
#import scipy.io as mt
# Load MATLAB file: mat
mat = scipy.io.loadmat('albeck_gene_expression.mat')
#mat = mt.loadmat('albeck_gene_expression.mat')

# Print the datatype type of mat
print(type(mat))

#for key in mat.keys():
#    print(mat[key])