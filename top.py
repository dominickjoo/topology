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
		return sum(math.gcd(sum(circle), self.b) == 1 for circle in circles)

	# Returns the genus of the surface associated to the homomorphism
	def genus(self):
		l = self.a + 1
		n = self.b
		count = 0

		for img in imgs:
			count += 1 - math.gcd(n,img)/n
		
		total = sum(imgs) % n
		count += 1 - math.gcd(n,total)/n

		return int(1 - n + (n/2)*total)

	# Returns the number of circles whose image is exactly n
	def num_of_sum_n_circ(self, n):
		circ_subsets = tuple(list(itertools.product([0,1], repeat=self.a))[1:])
		num_of_sum_n_circ = 0

		for subset in circ_subsets:
			count = 0
			for i in range(self.a):
				if subset[i]:
					count += self.imgs[i]
			if count % self.b == n: 
				num_of_sum_n_circ += 1

		return(num_of_sum_n_circ)

# Returns the maximum order of an automorphism of S_g, for g >= 2
def max_ord(g):
	if g % 2 == 1:
		return(4*g + 2)
	if g % 2 == 0:
		return(4*g + 4)

# Returns a list of all the surjective homomorphisms from Z^a into Z/bZ
def surj_homs(a,b):
	imgs_of_gens = itertools.product(range(1,b), repeat = a)
	surj_imgs_of_gens = [img for img in imgs_of_gens
	if (nt.gcd_mult(img) == 1 and sum(img) % b != 0)]
	return [Hom(a, b, img) for img in surj_imgs_of_gens]

# Returns a list of all homomorphisms of order n and with l branch points, along with the number of invariant circles associated to each one
def nums_of_inv_circ(l, n):
	homs = surj_homs(l-1,n)
	return [(hom, hom.num_of_inv_circ()) for hom in homs]

# Given a genus g, returns a list of the possible values for (l, n) as tuples
def get_l_n(g):
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

# Returns a list of all homomorphisms of order n and with l branch points, along with the number of circles whose image is01 for each homomorphism
def nums_of_sum_zero_circ(l, n):
	homs = surj_homs(l-1,n)
	homs_with_nums = map(lambda hom: hom.num_of_sum_n_circ(0), homs)
	return(list(homs_with_nums))

# Returns a list of all homomorphisms of order n and with l branch points, along with the number of circles that are sent to 1 for each homomorphism
def nums_of_sum_one_circ(l, n):
	homs = surj_homs(l-1,n)
	homs_with_nums = map(lambda hom: hom.num_of_sum_n_circ(1), homs)
	return(list(homs_with_nums))

# Returns a list of all homomorphisms of order n and with l branch points, along with the number of circles that are sent to 2 for each homomorphism
def nums_of_sum_two_circ(l, n):
	homs = surj_homs(l-1,n)
	homs_with_nums = map(lambda hom: hom.num_of_sum_n_circ(2), homs)
	return(list(homs_with_nums))