FPGA_0 = pd.Series(data[data['FPGA'] == 0]['TDC_CHANNEL'].value_counts())
FPGA_1 = pd.Series(data[data['FPGA'] == 1]['TDC_CHANNEL'].value_counts())
print("Series FPGA == 0 :\n" , FPGA_0)
print("\nSeries FPGA == 1 :\n" , FPGA_1)