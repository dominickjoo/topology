import math
import itertools
from functools import reduce
import nt

# A homomorphism from Z^a into Z/bZ is represented as (a, b, [g_1, \ldots, g_a]), where the g_i are the images of the generators of Z^a
class Hom:
	def __init__(self, a, b, imgs):
		self.a = a
		self.b = b
		self.imgs = imgs

	def __repr__(self):
		return f"Hom({self.a}, {self.b}, {self.imgs})"

	def __str__(self):
		return f"Z^{self.a} -> Z/{self.b}Z, generators {self.imgs}"

	# Returns the number of invariant circles of the automorphism associated to the homomorphism
	def num_of_inv_circ(self):
		circles = nt.power_set(self.imgs)
		return sum(math.gcd(sum(circle), self.b) == 1 for circle in circles)

	# Returns the number of essential invariant circles of the automorphism associated to the homomorphism
	def num_of_ess_inv_circ(self):
		circles = list(nt.power_set(self.imgs))[self.a + 1, -1]
		return sum(math.gcd(sum(circle), self.b) == 1 for circle in circles if )

def surj_homs(a,b):
	# Returns all the surjective homomorphisms from $\ZZ^a$ into $\ZZ/b\ZZ$
	imgs_of_gens = itertools.product(range(1,b), repeat = a)
	surj_imgs_of_gens = [img for img in imgs_of_gens
	if (nt.gcd_mult(img) == 1 and sum(img) % b != 0)]
	return [Hom(a, b, img) for img in surj_imgs_of_gens]

def genus(hom):
	# Returns the genus of the surface associated to a homomorphism
	l = hom.a + 1
	n = hom.b
	imgs = hom.gens

	g = 1 - n
	sum_ = 0

	for img in imgs:
		sum_ += 1 - (math.gcd(n,img)/n)

	total_img = reduce(lambda x,y: x + y,imgs) % n

	sum_ += 1 - (math.gcd(n,total_img)/n)

	g += (n/2)*sum_

	return round(g)

def nums_of_inv_circ(l, n):
	# Returns all homomorphisms of order $n$ and with $l$ branch points, along with the number of invariant circles associated to each one
	homs = surj_homs(l-1,n)
	return [num_of_inv_circ(hom) for hom in homs]

	# can return ordered pair with hom
	# return [(hom, num_of_inv_circ(hom)) for hom in homs]

def max_ord(g):
	# Returns the maximum order of an automorphism of $S_g$, for $g \geq 2$.
	if g % 2 == 1:
		return(4*g + 2)
	if g % 2 == 0:
		return(4*g + 4)

def foo(g):
	n = 4*g + 2
	l = 3

	homs = surj_homs(l-1,n)
	genus_g_homs = filter(lambda hom: genus(hom) == g, homs)
	genus_g_homs_with_nums = map(lambda hom: (num_of_inv_circ(hom),hom), genus_g_homs)
	return(genus_g_homs_with_nums)

def bar(g):
	n = 2*g-4
	l = 4

	homs = surj_homs(l-1,n)
	genus_g_homs = filter(lambda hom: genus(hom) == g, homs)
	genus_g_homs_with_nums = map(lambda hom: (num_of_ess_inv_circ(hom),hom), genus_g_homs)
	return(genus_g_homs_with_nums)

def barn(g,n):
	l = 4

	homs = surj_homs(l-1,n)
	genus_g_homs = filter(lambda hom: genus(hom) == g, homs)
	genus_g_homs_with_nums = map(lambda hom: (num_of_ess_inv_circ(hom),hom), genus_g_homs)
	return(genus_g_homs_with_nums)


def get_l_n(g):
	# Given a genus, returns the possible values for l and n
	possibles = []
	l = 3
	n = 2

	while 2*g - 2 >= n*(l/2 - 2):
		possibles.append((l,n))
		n += 1

		if not (2*g - 2 >= n*(l/2 - 2) and n <= 4*g + 2):
			l += 1
			n = 2

	return(possibles)		


def num_of_sum_one_circ(hom):
	# Returns the number of circles associated to a given homomorphism that are sent to 1
	a = hom[0]
	b = hom[1]
	imgs = hom[2]

	circ_subsets = tuple(list(itertools.product([0,1], repeat=a))[1:])
	num_of_sum_one_circ = 0

	for subset in circ_subsets:
		count = 0

		for i in range(a):
			if subset[i] == 1:
				count += imgs[i]

		if count % b == 1: 
			num_of_sum_one_circ += 1

	return(num_of_sum_one_circ)

def nums_of_sum_one_circ(l, n):
	# Returns all homomorphisms of order $n$ and with $l$ branch points, along with the number of circles that are sent to 1 for each homomorphism
	homs = surj_homs(l-1,n)
	nums = map(lambda hom: num_of_sum_one_circ(hom), homs)
	return(list(nums))

def num_of_sum_zero_circ(hom):
	# Returns the number of circles associated to a given homomorphism that are sent to 1
	a = hom[0]
	b = hom[1]
	imgs = hom[2]

	circ_subsets = tuple(list(itertools.product([0,1], repeat=a))[1:])
	num_of_sum_one_circ = 0

	for subset in circ_subsets:
		count = 0

		for i in range(a):
			if subset[i] == 1:
				count += imgs[i]

		if count % b == 0: 
			num_of_sum_one_circ += 1

	return(num_of_sum_one_circ)

def nums_of_sum_zero_circ(l, n):
	# Returns all homomorphisms of order $n$ and with $l$ branch points, along with the number of circles that are sent to 1 for each homomorphism
	homs = surj_homs(l-1,n)
	nums = map(lambda hom: num_of_sum_zero_circ(hom), homs)
	return(list(nums))

def num_of_sum_two_circ(hom):
	# Returns the number of circles associated to a given homomorphism that are sent to 1
	a = hom[0]
	b = hom[1]
	imgs = hom[2]

	circ_subsets = tuple(list(itertools.product([0,1], repeat=a))[1:])
	num_of_sum_one_circ = 0

	for subset in circ_subsets:
		count = 0

		for i in range(a):
			if subset[i] == 1:
				count += imgs[i]

		if count % b == 2: 
			num_of_sum_one_circ += 1

	return(num_of_sum_one_circ)

def nums_of_sum_two_circ(l, n):
	# Returns all homomorphisms of order $n$ and with $l$ branch points, along with the number of circles that are sent to 1 for each homomorphism
	homs = surj_homs(l-1,n)
	nums = map(lambda hom: num_of_sum_two_circ(hom), homs)
	return(list(nums))



# for g in range(2,6):
# 	print(list(bar(g)))



# for g in range(2, 90):
# 	possible_nums = map(lambda x: x[0], bar(g))
# 	print(g, set(possible_nums))




for g in filter(lambda n: n%2 == 1, range(21,22)):
	possible_ns = range(3,4*g + 3)
	possible_nums = set()
	for n in possible_ns:
		possible_nums = possible_nums.union(set(barn(g,n)))
		# possible_nums = possible_nums.union(set(map(lambda x: x[0], barn(g,n))))

	for num in possible_nums:
		# if num[0] == 1:
		print(f"g: {g}")
		print(f"hom: {num[1]}")

	# print(g, set(possible_nums))



# for i in filter(is_prime,range(3,14)):
# 	print([i,set(nums_of_sum_two_circ(6, i))])

# for i in filter(is_prime,range(3,14)):
# 	print([i,set(nums_of_sum_one_circ(6, i))])

# for i in filter(is_prime,range(3,14)):
# 	print([i,set(nums_of_sum_zero_circ(6, i))])

# for i in filter(is_prime,range(3,14)):
# 	print([i,set(nums_of_inv_circ(7, i))])

# {(1, (3, 12, (6, 8, 7))), (1, (3, 12, (6, 4, 11))), (1, (3, 12, (8, 1, 6))), (1, (3, 12, (4, 3, 11))), (1, (3, 12, (4, 11, 3))), (1, (3, 12, (7, 3, 6))), (1, (3, 12, (5, 9, 6))), (1, (3, 12, (9, 1, 6))), (1, (3, 12, (1, 6, 9))), (1, (3, 12, (9, 5, 6))), (1, (3, 12, (9, 6, 5))), (1, (3, 12, (3, 11, 6))), (1, (3, 12, (7, 6, 8))), (1, (3, 12, (11, 4, 3))), (1, (3, 12, (5, 9, 4))), (1, (3, 12, (6, 7, 8))), (1, (3, 12, (6, 11, 4))), (1, (3, 12, (6, 5, 4))), (1, (3, 12, (8, 7, 3))), (1, (3, 12, (9, 6, 1))), (1, (3, 12, (7, 3, 8))), (1, (3, 12, (5, 4, 6))), (1, (3, 12, (8, 3, 7))), (1, (3, 12, (9, 4, 5))), (1, (3, 12, (3, 11, 4))), (1, (3, 12, (3, 7, 8))), (1, (3, 12, (5, 4, 9))), (1, (3, 12, (4, 6, 11))), (1, (3, 12, (1, 6, 8))), (1, (3, 12, (6, 8, 1))), (1, (3, 12, (9, 5, 4))), (1, (3, 12, (3, 6, 7))), (1, (3, 12, (11, 3, 6))), (1, (3, 12, (6, 3, 7))), (1, (3, 12, (6, 7, 3))), (1, (3, 12, (6, 4, 5))), (1, (3, 12, (4, 5, 9))), (1, (3, 12, (9, 1, 8))), (1, (3, 12, (4, 9, 5))), (1, (3, 12, (11, 4, 6))), (1, (3, 12, (7, 6, 3))), (1, (3, 12, (4, 6, 5))), (1, (3, 12, (6, 9, 1))), (1, (3, 12, (6, 1, 9))), (1, (3, 12, (11, 3, 4))), (1, (3, 12, (3, 6, 11))), (1, (3, 12, (9, 8, 1))), (1, (3, 12, (7, 8, 3))), (1, (3, 12, (6, 9, 5))), (1, (3, 12, (6, 5, 9))), (1, (3, 12, (8, 6, 7))), (1, (3, 12, (7, 8, 6))), (1, (3, 12, (4, 11, 6))), (1, (3, 12, (6, 1, 8))), (1, (3, 12, (8, 1, 9))), (1, (3, 12, (8, 6, 1))), (1, (3, 12, (5, 6, 4))), (1, (3, 12, (6, 11, 3))), (1, (3, 12, (8, 9, 1))), (1, (3, 12, (3, 7, 6))), (1, (3, 12, (4, 5, 6))), (1, (3, 12, (11, 6, 3))), (1, (3, 12, (1, 9, 8))), (1, (3, 12, (1, 8, 6))), (1, (3, 12, (8, 7, 6))), (1, (3, 12, (3, 4, 11))), (1, (3, 12, (3, 8, 7))), (1, (3, 12, (1, 8, 9))), (1, (3, 12, (5, 6, 9))), (1, (3, 12, (1, 9, 6))), (1, (3, 12, (11, 6, 4))), (1, (3, 12, (6, 3, 11)))}


# homs = surj_homs(5,11)

# max_homs = filter(lambda hom: num_of_sum_two_circ(hom) == 10, homs)

# print(list(max_homs))




# g = 4

# cur_max = (0, ())

# homs = surj_homs(9,2)
# genus_g = filter(lambda hom: genus(hom) == g, homs)
# for hom in genus_g:
# 	possible_max = num_of_inv_circ(hom)
# 	if possible_max > cur_max[0]:
# 		cur_max = (possible_max,hom)

# print(cur_max)


# g = 2

# possibles = filter(lambda ln: ln[1] != 2, get_l_n(g))

# cur_max = 0

# for ln in possibles:	
# 	homs = surj_homs(ln[0] - 1,ln[1])
# 	genus_g_homs = filter(lambda hom: genus(hom) == g, homs)
# 	nums = list(map(lambda hom: num_of_inv_circ(hom), genus_g_homs))
# 	if len(nums) > 0:
# 		cur_max = max(cur_max, max(nums))

# print(cur_max)


# g = 4

# possibles = filter(lambda ln: ln[1] != 2, get_l_n(g))

# max_num_homs = []

# for ln in possibles:	
# 	homs = surj_homs(ln[0] - 1,ln[1])
# 	genus_g_homs = filter(lambda hom: genus(hom) == g, homs)
# 	max_num_homs.append(list(filter(lambda hom: num_of_inv_circ(hom) == 21, genus_g_homs)))

# print(max_num_homs)


# for g in range(2,6):
# 	print(list(foo(g)))

# for g in range(2, 90):
# 	possible_nums = map(lambda x: x[0], foo(g))
# 	print(g, set(possible_nums))


# g = 10

# for i in range(3,45):
# 	homs = surj_homs(4,i)
# 	genus_g_homs = filter(lambda hom: genus(hom) == g, homs)
# 	genus_g_one_inv_circ_homs = filter(lambda hom: num_of_inv_circ(hom) == 1, genus_g_homs)

# 	print(i,list(genus_g_one_inv_circ_homs))



# homs = surj_homs(2,33)
# genus_g_homs = filter(lambda hom: genus(hom) == g, homs)
# genus_g_one_inv_circ_homs = filter(lambda hom: num_of_inv_circ(hom) == 1, genus_g_homs)

# print(33,list(genus_g_one_inv_circ_homs),list(genus_g_one_inv_circ_homs))


# for i in filter(is_prime,range(3,40)):
# 	print([i,set(nums_of_inv_circ(4, i))])


# mint = 16
# for i in range(2,5):
# 	test_mint = min(nums_of_inv_circ(6,i))
# 	if test_mint < mint and test_mint > 0:
# 		mint = test_mint
# 	if test_mint == 1:
# 		print(i,mint)
# 		break
# print(mint)



