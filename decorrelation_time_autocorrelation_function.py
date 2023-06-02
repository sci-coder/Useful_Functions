
""" Calculates decorrelation times for a signal"""

def calculate_decorrelation_time(data, threshold=0.1):
    # Compute autocorrelation function
    acf = np.corrcoef(data - np.mean(data), data - np.mean(data), mode='full')
    acf = acf[len(acf)//2:]  # Keep only the positive lags

    # Normalize ACF
    acf /= acf[0]  # Divide by the first element (maximum autocorrelation)

    # Plot ACF
    plt.plot(acf)
    plt.xlabel('Lag')
    plt.ylabel('Autocorrelation')
    plt.show()

    # Find decorrelation time
    decorrelation_time = np.where(acf < threshold)[0][0]

    return decorrelation_time
