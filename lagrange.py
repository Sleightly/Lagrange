import numpy as np


g_func = []


def read_data(file):
	with open(file, "r") as ins:
		array = []	
		for line in ins:
			data = line.strip().split(',')
			array.append(data)
		return array

machines = 2

def update_multiplier(iteration, greekL, optimal, nL):
	alpha = step_size(greekL, optimal, nL)
	pi_n1 = pi_n + alpha * g_func[pi_n]
	return pi_n 

def step_size(greekL, optimal, nL):
	divider = np.dot(g_func, g_func)
	alpha = greekL * (optimal - nL) / divider
	return alpha

array = read_data('data.txt')
print(array)