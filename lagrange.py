import numpy as np

g_func = []
base_array = []
time = []
due_date = []
weight = []
final_start = []
beginning_times = []

delta = [[]]
pi = []
store_L = []

machines = 2
init_days = 8
Lbar = 1000
L = 0

def initialize(file):
	with open(file, "r") as ins:
		for line in ins:
			data = line.strip().split(',')
			base_array.append(data)
			time.append(int(data[0]))
			due_date.append(int(data[1])-1)
			weight.append(int(data[2]))
	init_delta()
	init_g_func()
	init_begin_times()
	init_pi()
	init_final_start()
	init_store_L()


def init_delta():
	global delta
	delta = [[0 for i in range(init_days)] for j in range(len(time))]

def init_pi():
	global pi
	pi = [0.5 for i in range(init_days)]

def init_final_start():
	for i in range(len(time)):
		final_start.append(init_days - time[i] + 1)

def init_g_func():
	global g_func
	g_func = [0 for i in range(init_days)]
	print(g_func)

def init_begin_times():
	global beginning_times
	beginning_times = [0 for i in range(init_days)]

def init_store_L():
	global store_L
	store_L = [0 for i in range(init_days)]

def compute_tardiness(start_day, i):
	done_date = start_day + time[i] - 1
	days_overdue = done_date - due_date[i]
	if days_overdue < 0:
		days_overdue = 0
	return days_overdue
	
def calculate_lowest_L():
	global store_L
	for i in range(len(final_start)):
		#i = index of which task
		current_end_time = final_start[i]
		min_value = 1000
		start_day = 0
		#print(i)
		for j in range(current_end_time):
			#j = start_day
			calc_weight = weight[i] * compute_tardiness(j, i) + sum_pi(j, i)
			#print(calc_weight)
			if calc_weight <= min_value:
				min_value = calc_weight
				start_day = j
		store_L[i] = min_value
		beginning_times[i] = start_day
		update_delta(start_day, i)


def update_delta(start_day, task_id):
	global delta
	for i in range(time[task_id]):
		delta[task_id][start_day + i] = 1

def sum_pi(start_day, index):
	sum_of_pi = 0
	for i in range(time[index]):
		sum_of_pi = sum_of_pi + pi[start_day + i]
	return sum_of_pi

def update_g_func():
	global g_func
	for i in range(len(delta[0])):
		total_sum = 0
		for j in range(len(delta)):
			total_sum = delta[j][i] + total_sum
		g_func[i] = total_sum - machines

def step_size(greekL, optimal, nL):
	divider = np.dot(g_func, g_func)
	alpha = greekL * (optimal - nL) / divider
	return alpha

def update_pi():
	global pi
	update_L()
	for i in range(len(pi)):
		g_value = g_func[i]
		if g_value < 0:
			g_value = 0.1
		pi[i] = pi[i] + step_size(1, Lbar, L) * g_value

def update_L():
	global L
	total_L = 0
	for i in range(len(store_L)):
		total_L = total_L + store_L[i]
	total_pi = 0
	for i in range(len(pi)):
		total_pi = total_pi + pi[i] * machines
	L = total_L - total_pi

def update_LBar():
	global Lbar
	Lbar = L

def printSchedule():
	for i in range(len(delta)):
		print(delta[i])

def greedy_heuristic():
	return 0

def objective_function():
	return 0

if __name__=='__main__':
	initialize('sample.txt')
	for i in range(20):
		print("iteration number "+str(i))
		calculate_lowest_L()
		update_g_func()
		update_pi()
		update_LBar()
		printSchedule()
		print(pi)
		print(beginning_times)
		print()
		init_delta()
		init_begin_times()



	