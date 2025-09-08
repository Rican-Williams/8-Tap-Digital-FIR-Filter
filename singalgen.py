import numpy as np
import matplotlib.pyplot as plt


# this function is used to perform the transformotion from a signed binary to the signed decimal representation


def todecimal(x, bits):
    assert len(x) <= bits
    n = int(x, 2)
    s = 1 << (bits - 1)
    return (n & s - 1) - (n & s )




# compute a binary representation of the filter coefficients
# number of coefficients
tap = 8
# for computing first scale, we want to represent filter coefficent
# as 8 bit numbers
N1 = 8
# this is used to convert the filter inputs to  16-bit signed values
N2 = 16
# this is the output bit width
N3 = 32






real_coeff = (1/tap);


# bit representation of the coefficients
coeff_bit = np.binary_repr(int(real_coeff*(2**(N1-1))),N1)


# double check, invert, it should be equal to real_coeff
todecimal(coeff_bit, N1)/(2**(N1-1))


#generate a test noisy signal
timeVector = np.linspace(0, 2*np.pi, 100)
output=np.sin(2*timeVector)+np.cos(3*timeVector)+0.3*np.random.randn(len(timeVector))
plt.plot(output)
plt.show()


#convert to intergers
# this list contains the N2 - bit signed represntation of the sin sequence
list1 = []
for number in output:
    list1.append(np.binary_repr(int(number*(2**(N1-1))),N2))


print( list1[:100])
print("Total entries:", len(list1))




# save the converted sequence to the data file
with open ('input.data', 'w') as file:
    for number in list1:
        file.write(number + '\n')


# after this line, you need to run the vivado code


# from here, we read the filtered values, convert them to decimal rep and plot the filtered results


read_b=[]


# read data
with open ("save.data") as file:
    for line in file:
        read_b.append(line.rstrip('\n'))


# this list contains the converted values
n_l=[]
