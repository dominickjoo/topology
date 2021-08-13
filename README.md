# topology.py #

This is a library for interacting with the data structures that arose in the course of my topology research with Bena Tshishiku (summer 2020). Any errors in the programming are mine. Please let me know if you spot any errors or wish for another relevant function.

### Context ###

Let $S_g$ denote the orientable genus-$g$ surface, and $f: S_g \rightarrow S_g$ an orientation-preserving automorphism of order $n$. The orbit space of $f$ is also an orientable, compact surface, which we can denote as $S_{\bar g}$. Then $f$ induces a branched covering $p: S_g \rightarrow S_{\bar g}$ (with branching set $B$), and we denote the induced representation by $\rho: \pi_1(S_{\bar g} \setminus B) \rightarrow \mathbb Z/n \mathbb Z$.

In 1979, W. H. Meeks showed that $\gamma \subset S_g \setminus p^{-1}(B)$ is an invariant circle of $f$ if and only if it is the pre-image of an embedded circle $\gamma' \subset S_{\bar g} \setminus B$ such that $\rho(\gamma')$ is a generator of $\mathbb Z/n \mathbb Z$. Since $\mathbb Z/n \mathbb Z$ is abelian, a circle in $\pi_1(S_{\bar g} \setminus B)$ is determined by its homology.

In other words, finding invariant circles of $f$ boils down to the number-theoretic problem of finding elements of $H_1(S_{\bar g} \setminus B)$ (which is isomorphic to a free abelian group $\mathbb Z^r$) into $\mathbb Z/n \mathbb Z$ that are sent to an integer relatively prime to $n$. My research was focused on the possible values for the number of invariant circles given $g$ and $n$, and I wrote a bunch of Python functions to help determine these, which I've now compiled into this library for posterity.

