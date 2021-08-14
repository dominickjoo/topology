# topology.py #

This is a library for interacting with the data structures that arose in the course of my topology research with Bena Tshishiku (summer 2020). Any errors in the programming are mine. Please let me know if you spot any errors or wish for another relevant function.

### Context ###

Let S<sub>g</sub> denote the orientable genus-g surface, and f: S<sub>g</sub> → S<sub>g</sub> an orientation-preserving automorphism of order n. The orbit space of f is also an orientable, compact surface, which we can denote as S<sub>g'</sub>. Then f induces a branched covering p: S<sub>g</sub> → S<sub>g'</sub> (with branching set B), and we denote the induced representation by ρ: π_1(S<sub>g'</sub> \ B) → **Z**/n**Z**.

In 1979, W. H. Meeks showed that γ ⊂ S<sub>g</sub> \ p<sup>-1</sup>(B) is an invariant circle of f if and only if it is the pre-image of an embedded circle γ' ⊂ S<sub>g'</sub> \ B such that ρ(γ') is a generator of **Z**/n**Z**. Also, since **Z**/n**Z** is abelian, a circle in π<sub>1</sub>(S<sub>g'</sub> \ B) is determined by its homology class.

In other words, finding invariant circles of f boils down to the number-theoretic problem of finding elements of H<sub>1</sub>(S<sub>g'</sub> \ B) (which is isomorphic to a free abelian group **Z**<sup>r</sup>) into **Z**/n**Z** that are sent to an integer relatively prime to n. My research was focused on the possible values for the number of invariant circles given g and n, and I wrote a bunch of Python functions to help determine these, which I've now compiled into this library for posterity.

### Code ###

The code is centered around a class I wrote for these very particular homomorphisms (from **Z**<sup>r</sup> to **Z**/n**Z**), with instance variables r (`a` in the code), n (`b` in the code), and the images of the generators of **Z**<sup>r</sup> (`imgs` in the code, a length-`a` list of integers between 0 and b-1, inclusive). The class has functions for counting the number of invariant circles associated with the homomorphism, as well as small variations (only count essential circles, only count circles with a specific image), and various small utility functions (get the genus of the homomorphism).

The functions outside the code are mostly related to collecting data about all possible homomorphisms satisfying desired properties (e.g. having the values of l and n that you want). I think it's pretty easy to use the code in the Hom class to gather other information in a similar way.