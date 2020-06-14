import numpy as np
import matplotlib.pyplot as plt

def convolution(in_data, response):
    '''Basic algorithm
    When h having m data, x having p data, then
    
    y[ni] = x[ni-(m-1)]h[m-1] + x[ni-m]h[m-2]  + ... + x[ni-1]h[1] + x[ni]h[0] 
    
    where ni is 0 to m+p-2
    '''
    # In the following calculation,
    # make sure len(x) > len(h)
    if response.size > in_data.size:
        x, h = response, in_data
    else:
        x, h = in_data, response
        
    # Initalization 
    x_len = x.size
    h_len = h.size
    out_data = np.zeros(x_len + h_len - 1)
    
    # Padding zero to arrays
    zero_after = np.zeros(out_data.size - x_len)
    zero_before = np.zeros(h_len - 1)
    
    x = np.concatenate([zero_before, x, zero_after])
    out_data = np.concatenate([zero_before, out_data])
    
    # Calculation
    for i in range(zero_before.size, out_data.size):
        for j in range(h_len):
            out_data[i] += h[j]*x[i-j]
       
    return out_data[zero_before.size:]  # remove initial padding


if __name__ == '__main__':
    # Input data
    x = np.array([0, -1, -1.2, 2, 1.3, 1.3, 0.6, 0, -0.8])
    # Impulse response
    h = np.array([1, -0.5, -0.3, -0.1])
    result = convolution(x, h)
    print(result)
    
    # Show graph
    plt.subplot(3,1,1)
    plt.plot(x, 'rx')
    plt.subplot(3,1,2)
    plt.plot(h,'gx')
    plt.subplot(3,1,3)
    plt.plot(result,'bx')
    plt.show()
    