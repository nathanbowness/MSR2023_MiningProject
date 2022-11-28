# The Algorithms - Go
[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod&style=flat-square)](https://gitpod.io/#https://github.com/TheAlgorithms/Go)&nbsp;
![golangci-lint](https://github.com/TheAlgorithms/Go/workflows/golangci-lint/badge.svg)
![godocmd](https://github.com/tjgurwara99/Go/workflows/godocmd/badge.svg)
![](https://img.shields.io/github/repo-size/TheAlgorithms/Go.svg?label=Repo%20size&style=flat-square)&nbsp;
![update_directory_md](https://github.com/TheAlgorithms/Go/workflows/update_directory_md/badge.svg)
[![Discord chat](https://img.shields.io/discord/808045925556682782.svg?logo=discord&colorB=7289DA&style=flat-square)](https://the-algorithms.com/discord/)&nbsp;

### Algorithms implemented in Go (for education)

The repository is a collection of open-source implementation of a variety of algorithms implemented in Go and licensed under [MIT License](LICENSE).

Read our [Contribution Guidelines](CONTRIBUTING.md) before you contribute.

## List of Algorithms
<!--- GODOCMD BEGIN --->
# Packages:

<details>
	<summary> <strong> ahocorasick </strong> </summary>	

---

##### Functions:

1. [`Advanced`](./strings/ahocorasick/advancedahocorasick.go#L10):  Advanced Function performing the Advanced Aho-Corasick algorithm. Finds and prints occurrences of each pattern.
2. [`AhoCorasick`](./strings/ahocorasick/ahocorasick.go#L15):  AhoCorasick Function performing the Basic Aho-Corasick algorithm. Finds and prints occurrences of each pattern.
3. [`ArrayUnion`](./strings/ahocorasick/shared.go#L86):  ArrayUnion Concats two arrays of int's into one.
4. [`BoolArrayCapUp`](./strings/ahocorasick/shared.go#L78):  BoolArrayCapUp Dynamically increases an array size of bool's by 1.
5. [`BuildAc`](./strings/ahocorasick/ahocorasick.go#L54):  Functions that builds Aho Corasick automaton.
6. [`BuildExtendedAc`](./strings/ahocorasick/advancedahocorasick.go#L46):  BuildExtendedAc Functions that builds extended Aho Corasick automaton.
7. [`ComputeAlphabet`](./strings/ahocorasick/shared.go#L61):  ComputeAlphabet Function that returns string of all the possible characters in given patterns.
8. [`ConstructTrie`](./strings/ahocorasick/shared.go#L4):  ConstructTrie Function that constructs Trie as an automaton for a set of reversed & trimmed strings.
9. [`Contains`](./strings/ahocorasick/shared.go#L39):  Contains Returns 'true' if array of int's 's' contains int 'e', 'false' otherwise.
10. [`CreateNewState`](./strings/ahocorasick/shared.go#L111):  CreateNewState Automaton function for creating a new state 'state'.
11. [`CreateTransition`](./strings/ahocorasick/shared.go#L116):  CreateTransition Creates a transition for function σ(state,letter) = end.
12. [`GetParent`](./strings/ahocorasick/shared.go#L99):  GetParent Function that finds the first previous state of a state and returns it. Used for trie where there is only one parent.
13. [`GetTransition`](./strings/ahocorasick/shared.go#L121):  GetTransition Returns ending state for transition σ(fromState,overChar), '-1' if there is none.
14. [`GetWord`](./strings/ahocorasick/shared.go#L49):  GetWord Function that returns word found in text 't' at position range 'begin' to 'end'.
15. [`IntArrayCapUp`](./strings/ahocorasick/shared.go#L70):  IntArrayCapUp Dynamically increases an array size of int's by 1.
16. [`StateExists`](./strings/ahocorasick/shared.go#L133):  StateExists Checks if state 'state' exists. Returns 'true' if it does, 'false' otherwise.

---
##### Types

1. [`Result`](./strings/ahocorasick/ahocorasick.go#L9): No description provided.


---
</details><details>
	<summary> <strong> armstrong </strong> </summary>	

---

##### Functions:

1. [`IsArmstrong`](./math/armstrong/isarmstrong.go#L14): No description provided.

---
</details><details>
	<summary> <strong> binary </strong> </summary>	

---

#####  Package binary describes algorithms that use binary operations for different calculations.

---
##### Functions:

1. [`Abs`](./math/binary/abs.go#L10):  Abs returns absolute value using binary operation Principle of operation: 1) Get the mask by right shift by the base 2) Base is the size of an integer variable in bits, for example, for int32 it will be 32, for int64 it will be 64 3) For negative numbers, above step sets mask as 1 1 1 1 1 1 1 1 and 0 0 0 0 0 0 0 0 for positive numbers. 4) Add the mask to the given number. 5) XOR of mask + n and mask gives the absolute value.
2. [`BitCounter`](./math/binary/bitcounter.go#L11):  BitCounter - The function returns the number of set bits for an unsigned integer number
3. [`IsPowerOfTwo`](./math/binary/checkisnumberpoweroftwo.go#L21):  IsPowerOfTwo This function uses the fact that powers of 2 are represented like 10...0 in binary, and numbers one less than the power of 2 are represented like 11...1. Therefore, using the and function:	  10...0	& 01...1	  00...0 -> 0 This is also true for 0, which is not a power of 2, for which we have to add and extra condition.
4. [`IsPowerOfTwoLeftShift`](./math/binary/checkisnumberpoweroftwo.go#L28):  IsPowerOfTwoLeftShift This function takes advantage of the fact that left shifting a number by 1 is equivalent to multiplying by 2. For example, binary 00000001 when shifted by 3 becomes 00001000, which in decimal system is 8 or = 2 * 2 * 2
5. [`LogBase2`](./math/binary/logarithm.go#L7):  LogBase2 Finding the exponent of n = 2**x using bitwise operations (logarithm in base 2 of n) [See more](https://en.wikipedia.org/wiki/Logarithm)
6. [`MeanUsingAndXor`](./math/binary/arithmeticmean.go#L12):  MeanUsingAndXor This function finds arithmetic mean using "AND" and "XOR" operations
7. [`MeanUsingRightShift`](./math/binary/arithmeticmean.go#L17):  MeanUsingRightShift This function finds arithmetic mean using right shift
8. [`ReverseBits`](./math/binary/reversebits.go#L14):  ReverseBits This function initialized the result by 0 (all bits 0) and process the given number starting from its least significant bit. If the current bit is 1, set the corresponding most significant bit in the result and finally move on to the next bit in the input number. Repeat this till all its bits are processed.
9. [`SequenceGrayCode`](./math/binary/rbc.go#L11):  SequenceGrayCode The function generates an "Gray code" sequence of length n
10. [`Sqrt`](./math/binary/sqrt.go#L16): No description provided.
11. [`XorSearchMissingNumber`](./math/binary/xorsearch.go#L11):  XorSearchMissingNumber This function finds a missing number in a sequence

---
</details><details>
	<summary> <strong> cache </strong> </summary>	

---

##### Functions:

1. [`NewLRU`](./cache/lru.go#L20):  NewLRU represent initiate lru cache with capacity

---
##### Types

1. [`LRU`](./cache/lru.go#L12): No description provided.


---
</details><details>
	<summary> <strong> caesar </strong> </summary>	

---

#####  Package caesar is the shift cipher ref: https://en.wikipedia.org/wiki/Caesar_cipher

---
##### Functions:

1. [`Decrypt`](./cipher/caesar/caesar.go#L27):  Decrypt decrypts by left shift of "key" each character of "input"
2. [`Encrypt`](./cipher/caesar/caesar.go#L6):  Encrypt encrypts by right shift of "key" each character of "input"
3. [`FuzzCaesar`](./cipher/caesar/caesar_test.go#L158): No description provided.

---
</details><details>
	<summary> <strong> catalan </strong> </summary>	

---

##### Functions:

1. [`CatalanNumber`](./math/catalan/catalannumber.go#L16):  CatalanNumber This function returns the `nth` Catalan number

---
</details><details>
	<summary> <strong> checksum </strong> </summary>	

---

#####  Package checksum describes algorithms for finding various checksums

---
##### Functions:

1. [`CRC8`](./checksum/crc8.go#L25):  CRC8 calculates CRC8 checksum of the given data.
2. [`Luhn`](./checksum/luhn.go#L11):  Luhn validates the provided data using the Luhn algorithm.

---
##### Types

1. [`CRCModel`](./checksum/crc8.go#L15): No description provided.


---
</details><details>
	<summary> <strong> coloring </strong> </summary>	

---

#####  Package coloring provides implementation of different graph coloring algorithms, e.g. coloring using BFS, using Backtracking, using greedy approach. Author(s): [Shivam](https://github.com/Shivam010)

---
##### Functions:

1. [`BipartiteCheck`](./graph/coloring/bipartite.go#L40):  basically tries to color the graph in two colors if each edge connects 2 differently colored nodes the graph can be considered bipartite

---
##### Types

1. [`Graph`](./graph/coloring/graph.go#L14): No description provided.


---
</details><details>
	<summary> <strong> combination </strong> </summary>	

---

#####  Package combination ...

---
##### Functions:

1. [`Start`](./strings/combination/combination.go#L13):  Start ...

---
##### Types

1. [`Combinations`](./strings/combination/combination.go#L7): No description provided.


---
</details><details>
	<summary> <strong> conversion </strong> </summary>	

---

#####  Package conversion is a package of implementations which converts one data structure to another.

---
##### Functions:

1. [`Base64Decode`](./conversion/base64.go#L57):  Base64Decode decodes the received input base64 string into a byte slice. The implementation follows the RFC4648 standard, which is documented at https://datatracker.ietf.org/doc/html/rfc4648#section-4
2. [`Base64Encode`](./conversion/base64.go#L19):  Base64Encode encodes the received input bytes slice into a base64 string. The implementation follows the RFC4648 standard, which is documented at https://datatracker.ietf.org/doc/html/rfc4648#section-4
3. [`BinaryToDecimal`](./conversion/binarytodecimal.go#L25):  BinaryToDecimal() function that will take Binary number as string, and return it's Decimal equivalent as integer.
4. [`DecimalToBinary`](./conversion/decimaltobinary.go#L32):  DecimalToBinary() function that will take Decimal number as int, and return it's Binary equivalent as string.
5. [`FuzzBase64Encode`](./conversion/base64_test.go#L113): No description provided.
6. [`HEXToRGB`](./conversion/rgbhex.go#L10):  HEXToRGB splits an RGB input (e.g. a color in hex format; 0x<color-code>) into the individual components: red, green and blue
7. [`IntToRoman`](./conversion/integertoroman.go#L17):  IntToRoman converts an integer value to a roman numeral string. An error is returned if the integer is not between 1 and 3999.
8. [`RGBToHEX`](./conversion/rgbhex.go#L41):  RGBToHEX does exactly the opposite of HEXToRGB: it combines the three components red, green and blue to an RGB value, which can be converted to e.g. Hex
9. [`Reverse`](./conversion/decimaltobinary.go#L22):  Reverse() function that will take string, and returns the reverse of that string.
10. [`RomanToInteger`](./conversion/romantointeger.go#L40):  RomanToInteger converts a roman numeral string to an integer. Roman numerals for numbers outside the range 1 to 3,999 will return an error. Nil or empty string return 0 with no error thrown.

---
</details><details>
	<summary> <strong> diffiehellman </strong> </summary>	

---

#####  Package diffiehellman implements Diffie-Hellman Key Exchange Algorithm for more information watch : https://www.youtube.com/watch?v=NmM9HA2MQGI

---
##### Functions:

1. [`GenerateMutualKey`](./cipher/diffiehellman/diffiehellmankeyexchange.go#L19):  GenerateMutualKey : generates a mutual key that can be used by only alice and bob mutualKey = (shareKey^prvKey)%primeNumber
2. [`GenerateShareKey`](./cipher/diffiehellman/diffiehellmankeyexchange.go#L13):  GenerateShareKey : generates a key using client private key , generator and primeNumber this key can be made public shareKey = (g^key)%primeNumber

---
</details><details>
	<summary> <strong> dynamic </strong> </summary>	

---

#####  Package dynamic is a package of certain implementations of dynamically run algorithms.

---
##### Functions:

1. [`Abbreviation`](./dynamic/abbreviation.go#L24):  Returns true if it is possible to make a equals b (if b is an abbreviation of a), returns false otherwise
2. [`Bin2`](./dynamic/binomialcoefficient.go#L21):  Bin2 function
3. [`CoinChange`](./dynamic/coinchange.go#L5):  CoinChange finds the number of possible combinations of coins of different values which can get to the target amount.
4. [`CutRodDp`](./dynamic/rodcutting.go#L21):  CutRodDp solve the same problem using dynamic programming
5. [`CutRodRec`](./dynamic/rodcutting.go#L8):  CutRodRec solve the problem recursively: initial approach
6. [`EditDistanceDP`](./dynamic/editdistance.go#L35):  EditDistanceDP is an optimised implementation which builds on the ideas of the recursive implementation. We use dynamic programming to compute the DP table where dp[i][j] denotes the edit distance value of first[0..i-1] and second[0..j-1]. Time complexity is O(m * n) where m and n are lengths of the strings, first and second respectively.
7. [`EditDistanceRecursive`](./dynamic/editdistance.go#L10):  EditDistanceRecursive is a naive implementation with exponential time complexity.
8. [`IsSubsetSum`](./dynamic/subsetsum.go#L14): No description provided.
9. [`Knapsack`](./dynamic/knapsack.go#L17):  Knapsack solves knapsack problem return maxProfit
10. [`LongestCommonSubsequence`](./dynamic/longestcommonsubsequence.go#L13):  LongestCommonSubsequence function
11. [`LongestIncreasingSubsequence`](./dynamic/longestincreasingsubsequence.go#L9):  LongestIncreasingSubsequence returns the longest increasing subsequence where all elements of the subsequence are sorted in increasing order
12. [`LongestIncreasingSubsequenceGreedy`](./dynamic/longestincreasingsubsequencegreedy.go#L9):  LongestIncreasingSubsequenceGreedy is a function to find the longest increasing subsequence in a given array using a greedy approach. The dynamic programming approach is implemented alongside this one. Worst Case Time Complexity: O(nlogn) Auxiliary Space: O(n), where n is the length of the array(slice). Reference: https://www.geeksforgeeks.org/construction-of-longest-monotonically-increasing-subsequence-n-log-n/
13. [`LpsDp`](./dynamic/longestpalindromicsubsequence.go#L25):  LpsDp function
14. [`LpsRec`](./dynamic/longestpalindromicsubsequence.go#L20):  LpsRec function
15. [`MatrixChainDp`](./dynamic/matrixmultiplication.go#L24):  MatrixChainDp function
16. [`MatrixChainRec`](./dynamic/matrixmultiplication.go#L10):  MatrixChainRec function
17. [`Max`](./dynamic/knapsack.go#L11):  Max function - possible duplicate
18. [`NthCatalanNumber`](./dynamic/catalan.go#L13):  NthCatalan returns the n-th Catalan Number Complexity: O(n²)
19. [`NthFibonacci`](./dynamic/fibonacci.go#L6):  NthFibonacci returns the nth Fibonacci Number

---
</details><details>
	<summary> <strong> dynamicarray </strong> </summary>	

---

#####  Package dynamicarray A dynamic array is quite similar to a regular array, but its Size is modifiable during program runtime, very similar to how a slice in Go works. The implementation is for educational purposes and explains how one might go about implementing their own version of slices.  For more details check out those links below here: GeeksForGeeks article : https://www.geeksforgeeks.org/how-do-dynamic-arrays-work/ Go blog: https://blog.golang.org/slices-intro Go blog: https://blog.golang.org/slices authors [Wesllhey Holanda](https://github.com/wesllhey), [Milad](https://github.com/miraddo) see dynamicarray.go, dynamicarray_test.go

---
##### Types

1. [`DynamicArray`](./structure/dynamicarray/dynamicarray.go#L21): No description provided.


---
</details><details>
	<summary> <strong> factorial </strong> </summary>	

---

#####  Package factorial describes algorithms Factorials calculations.

---
##### Functions:

1. [`Iterative`](./math/factorial/factorial.go#L12):  Iterative returns the iteratively brute forced factorial of n
2. [`Recursive`](./math/factorial/factorial.go#L21):  Recursive This function recursively computes the factorial of a number
3. [`UsingTree`](./math/factorial/factorial.go#L30):  UsingTree This function finds the factorial of a number using a binary tree

---
</details><details>
	<summary> <strong> fibonacci </strong> </summary>	

---

##### Functions:

1. [`Formula`](./math/fibonacci/fibonacci.go#L42):  Formula This function calculates the n-th fibonacci number using the [formula](https://en.wikipedia.org/wiki/Fibonacci_number#Relation_to_the_golden_ratio) Attention! Tests for large values fall due to rounding error of floating point numbers, works well, only on small numbers
2. [`Matrix`](./math/fibonacci/fibonacci.go#L15):  Matrix This function calculates the n-th fibonacci number using the matrix method. [See](https://en.wikipedia.org/wiki/Fibonacci_number#Matrix_form)

---
</details><details>
	<summary> <strong> gcd </strong> </summary>	

---

##### Functions:

1. [`Extended`](./math/gcd/extended.go#L12):  Extended simple extended gcd
2. [`ExtendedIterative`](./math/gcd/extendedgcditerative.go#L4):  ExtendedIterative finds and returns gcd(a, b), x, y satisfying a*x + b*y = gcd(a, b).
3. [`ExtendedRecursive`](./math/gcd/extendedgcd.go#L4):  ExtendedRecursive finds and returns gcd(a, b), x, y satisfying a*x + b*y = gcd(a, b).
4. [`Iterative`](./math/gcd/gcditerative.go#L4):  Iterative Faster iterative version of GcdRecursive without holding up too much of the stack
5. [`Recursive`](./math/gcd/gcd.go#L4):  Recursive finds and returns the greatest common divisor of a given integer.
6. [`TemplateBenchmarkExtendedGCD`](./math/gcd/extendedgcd_test.go#L44): No description provided.
7. [`TemplateBenchmarkGCD`](./math/gcd/gcd_test.go#L37): No description provided.
8. [`TemplateTestExtendedGCD`](./math/gcd/extendedgcd_test.go#L7): No description provided.
9. [`TemplateTestGCD`](./math/gcd/gcd_test.go#L18): No description provided.

---
</details><details>
	<summary> <strong> generateparentheses </strong> </summary>	

---

##### Functions:

1. [`GenerateParenthesis`](./strings/generateparentheses/generateparentheses.go#L12): No description provided.

---
</details><details>
	<summary> <strong> genetic </strong> </summary>	

---

#####  Package genetic provides functions to work with strings using genetic algorithm. https://en.wikipedia.org/wiki/Genetic_algorithm  Author: D4rkia

---
##### Functions:

1. [`GeneticString`](./strings/genetic/genetic.go#L71):  GeneticString generates PopultaionItem based on the imputed target string, and a set of possible runes to build a string with. In order to optimise string generation additional configurations can be provided with Conf instance. Empty instance of Conf (&Conf{}) can be provided, then default values would be set. Link to the same algorithm implemented in python: https://github.com/TheAlgorithms/Python/blob/master/genetic_algorithm/basic_string.py

---
##### Types

1. [`Conf`](./strings/genetic/genetic.go#L32): No description provided.

2. [`PopulationItem`](./strings/genetic/genetic.go#L26): No description provided.

3. [`Result`](./strings/genetic/genetic.go#L52): No description provided.


---
</details><details>
	<summary> <strong> geometry </strong> </summary>	

---

#####  Package geometry contains geometric algorithms

---
##### Functions:

1. [`Distance`](./math/geometry/straightlines.go#L18):  Distance calculates the shortest distance between two points.
2. [`IsParallel`](./math/geometry/straightlines.go#L42):  IsParallel checks if two lines are parallel or not.
3. [`IsPerpendicular`](./math/geometry/straightlines.go#L47):  IsPerpendicular checks if two lines are perpendicular or not.
4. [`PointDistance`](./math/geometry/straightlines.go#L53):  PointDistance calculates the distance of a given Point from a given line. The slice should contain the coefficiet of x, the coefficient of y and the constant in the respective order.
5. [`Section`](./math/geometry/straightlines.go#L24):  Section calculates the Point that divides a line in specific ratio. DO NOT specify the ratio in the form m:n, specify it as r, where r = m / n.
6. [`Slope`](./math/geometry/straightlines.go#L32):  Slope calculates the slope (gradient) of a line.
7. [`YIntercept`](./math/geometry/straightlines.go#L37):  YIntercept calculates the Y-Intercept of a line from a specific Point.

---
##### Types

1. [`Line`](./math/geometry/straightlines.go#L13): No description provided.

2. [`Point`](./math/geometry/straightlines.go#L9): No description provided.


---
</details><details>
	<summary> <strong> graph </strong> </summary>	

---

#####  Package graph demonstrates Graph search algorithms reference: https://en.wikipedia.org/wiki/Tree_traversal

---
##### Functions:

1. [`ArticulationPoint`](./graph/articulationpoints.go#L19):  ArticulationPoint is a function to identify articulation points in a graph. The function takes the graph as an argument and returns a boolean slice which indicates whether a vertex is an articulation point or not. Worst Case Time Complexity: O(|V| + |E|) Auxiliary Space: O(|V|) reference: https://en.wikipedia.org/wiki/Biconnected_component and https://cptalks.quora.com/Cut-Vertex-Articulation-point
2. [`BreadthFirstSearch`](./graph/breadthfirstsearch.go#L9):  BreadthFirstSearch is an algorithm for traversing and searching graph data structures. It starts at an arbitrary node of a graph, and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level. Worst-case performance	 		O(|V|+|E|)=O(b^{d})}O(|V|+|E|)=O(b^{d}) Worst-case space complexity	 	O(|V|)=O(b^{d})}O(|V|)=O(b^{d}) reference: https://en.wikipedia.org/wiki/Breadth-first_search
3. [`DepthFirstSearch`](./graph/depthfirstsearch.go#L53): No description provided.
4. [`DepthFirstSearchHelper`](./graph/depthfirstsearch.go#L21): No description provided.
5. [`FloydWarshall`](./graph/floydwarshall.go#L15):  FloydWarshall Returns all pair's shortest path using Floyd Warshall algorithm
6. [`GetIdx`](./graph/depthfirstsearch.go#L3): No description provided.
7. [`KruskalMST`](./graph/kruskal.go#L87):  KruskalMST will return a minimum spanning tree along with its total cost to using Kruskal's algorithm. Time complexity is O(m * log (n)) where m is the number of edges in the graph and n is number of nodes in it.
8. [`LowestCommonAncestor`](./graph/lowestcommonancestor.go#L111):  For each node, we will precompute its ancestor above him, its ancestor two nodes above, its ancestor four nodes above, etc. Let's call `jump[j][u]` is the `2^j`-th ancestor above the node `u` with `u` in range `[0, numbersVertex)`, `j` in range `[0,MAXLOG)`. These information allow us to jump from any node to any ancestor above it in `O(MAXLOG)` time.
9. [`New`](./graph/graph.go#L16):  Constructor functions for graphs (undirected by default)
10. [`NewDSU`](./graph/kruskal.go#L34):  NewDSU will return an initialised DSU using the value of n which will be treated as the number of elements out of which the DSU is being made
11. [`NewTree`](./graph/lowestcommonancestor.go#L84): No description provided.
12. [`NotExist`](./graph/depthfirstsearch.go#L12): No description provided.
13. [`Topological`](./graph/topological.go#L7):  Assumes that graph given is valid and possible to get a topo ordering. constraints are array of []int{a, b}, representing an edge going from a to b

---
##### Types

1. [`DisjointSetUnion`](./graph/kruskal.go#L29): No description provided.

2. [`DisjointSetUnionElement`](./graph/kruskal.go#L21): No description provided.

3. [`Edge`](./graph/kruskal.go#L14): No description provided.

4. [`Graph`](./graph/graph.go#L9): No description provided.

5. [`Item`](./graph/dijkstra.go#L5): No description provided.

6. [`Query`](./graph/lowestcommonancestor_test.go#L9): No description provided.

7. [`Tree`](./graph/lowestcommonancestor.go#L25): No description provided.

8. [`TreeEdge`](./graph/lowestcommonancestor.go#L12): No description provided.

9. [`WeightedGraph`](./graph/floydwarshall.go#L9): No description provided.


---
</details><details>
	<summary> <strong> hashmap </strong> </summary>	

---

##### Functions:

1. [`Make`](./structure/hashmap/hashmap.go#L32):  Make creates a new HashMap instance with input size and capacity
2. [`New`](./structure/hashmap/hashmap.go#L24):  New return new HashMap instance

---
##### Types

1. [`HashMap`](./structure/hashmap/hashmap.go#L17): No description provided.


---
</details><details>
	<summary> <strong> kmp </strong> </summary>	

---

##### Functions:

1. [`Kmp`](./strings/kmp/kmp.go#L70):  Kmp Function kmp performing the Knuth-Morris-Pratt algorithm. Prints whether the word/pattern was found and on what position in the text or not. m - current match in text, i - current character in w, c - amount of comparisons.

---
##### Types

1. [`Result`](./strings/kmp/kmp.go#L15): No description provided.


---
</details><details>
	<summary> <strong> lcm </strong> </summary>	

---

##### Functions:

1. [`Lcm`](./math/lcm/lcm.go#L10):  Lcm returns the lcm of two numbers using the fact that lcm(a,b) * gcd(a,b) = | a * b |

---
</details><details>
	<summary> <strong> levenshtein </strong> </summary>	

---

##### Functions:

1. [`Distance`](./strings/levenshtein/levenshteindistance.go#L10):  Distance Function that gives Levenshtein Distance

---
</details><details>
	<summary> <strong> linkedlist </strong> </summary>	

---

#####  Package linkedlist demonstrates different implementations on linkedlists.

---
##### Functions:

1. [`JosephusProblem`](./structure/linkedlist/cyclic.go#L120):  https://en.wikipedia.org/wiki/Josephus_problem This is a struct-based solution for Josephus problem.
2. [`NewCyclic`](./structure/linkedlist/cyclic.go#L12):  Create new list.
3. [`NewDoubly`](./structure/linkedlist/doubly.go#L31): No description provided.
4. [`NewNode`](./structure/linkedlist/shared.go#L12):  Create new node.
5. [`NewSingly`](./structure/linkedlist/singlylinkedlist.go#L19):  NewSingly returns a new instance of a linked list

---
##### Types

1. [`Cyclic`](./structure/linkedlist/cyclic.go#L6): No description provided.

2. [`Doubly`](./structure/linkedlist/doubly.go#L18): No description provided.

3. [`Node`](./structure/linkedlist/shared.go#L5): No description provided.

4. [`Singly`](./structure/linkedlist/singlylinkedlist.go#L10): No description provided.

5. [`testCase`](./structure/linkedlist/cyclic_test.go#L105): No description provided.


---
</details><details>
	<summary> <strong> manacher </strong> </summary>	

---

##### Functions:

1. [`LongestPalindrome`](./strings/manacher/longestpalindrome.go#L37): No description provided.

---
</details><details>
	<summary> <strong> math </strong> </summary>	

---

#####  Package math is a package that contains mathematical algorithms and its different implementations.

---
##### Functions:

1. [`Abs`](./math/abs.go#L11):  Abs returns absolute value
2. [`Combinations`](./math/binomialcoefficient.go#L20):  C is Binomial Coefficient function This function returns C(n, k) for given n and k
3. [`Cos`](./math/cos.go#L10):  Cos  returns the cosine of the radian argument x. [See more](https://en.wikipedia.org/wiki/Sine_and_cosine) [Based on the idea of Bhaskara approximation of cos(x)](https://math.stackexchange.com/questions/3886552/bhaskara-approximation-of-cosx)
4. [`DefaultPolynomial`](./math/pollard.go#L16):  DefaultPolynomial is the commonly used polynomial g(x) = (x^2 + 1) mod n
5. [`FindKthMax`](./math/kthnumber.go#L11):  FindKthMax returns the kth large element given an integer slice with nil `error` if found and returns -1 with `error` `search.ErrNotFound` if not found. NOTE: The `nums` slice gets mutated in the process.
6. [`FindKthMin`](./math/kthnumber.go#L19):  FindKthMin returns kth small element given an integer slice with nil `error` if found and returns -1 with `error` `search.ErrNotFound` if not found. NOTE: The `nums` slice gets mutated in the process.
7. [`IsPerfectNumber`](./math/perfectnumber.go#L34):  Checks if inNumber is a perfect number
8. [`IsPowOfTwoUseLog`](./math/checkisnumberpoweroftwo.go#L10):  IsPowOfTwoUseLog This function checks if a number is a power of two using the logarithm. The limiting degree can be from 0 to 63. See alternatives in the binary package.
9. [`Lerp`](./math/lerp.go#L5):  Lerp or Linear interpolation This function will return new value in 't' percentage  between 'v0' and 'v1'
10. [`LiouvilleLambda`](./math/liouville.go#L24):  Lambda is the liouville function This function returns λ(n) for given number
11. [`Mean`](./math/mean.go#L7): No description provided.
12. [`Median`](./math/median.go#L12): No description provided.
13. [`Mode`](./math/mode.go#L19): No description provided.
14. [`Mu`](./math/mobius.go#L21):  Mu is the Mobius function This function returns μ(n) for given number
15. [`Phi`](./math/eulertotient.go#L5):  Phi is the Euler totient function. This function computes the number of numbers less then n that are coprime with n.
16. [`PollardsRhoFactorization`](./math/pollard.go#L29):  PollardsRhoFactorization is an implementation of Pollard's rho factorization algorithm using the default parameters x = y = 2
17. [`Sin`](./math/sin.go#L9):  Sin returns the sine of the radian argument x. [See more](https://en.wikipedia.org/wiki/Sine_and_cosine)
18. [`SumOfProperDivisors`](./math/perfectnumber.go#L17):  Returns the sum of proper divisors of inNumber.

---
</details><details>
	<summary> <strong> max </strong> </summary>	

---

##### Functions:

1. [`Bitwise`](./math/max/bitwisemax.go#L11):  Bitwise computes using bitwise operator the maximum of all the integer input and returns it
2. [`Int`](./math/max/max.go#L6):  Int is a function which returns the maximum of all the integers provided as arguments.

---
</details><details>
	<summary> <strong> maxsubarraysum </strong> </summary>	

---

#####  Package maxsubarraysum is a package containing a solution to a common problem of finding max contiguous sum within a array of ints.

---
##### Functions:

1. [`MaxSubarraySum`](./other/maxsubarraysum/maxsubarraysum.go#L13):  MaxSubarraySum returns the maximum subarray sum

---
</details><details>
	<summary> <strong> min </strong> </summary>	

---

##### Functions:

1. [`Bitwise`](./math/min/bitwisemin.go#L11):  Bitwise This function returns the minimum integer using bit operations
2. [`Int`](./math/min/min.go#L6):  Int is a function which returns the minimum of all the integers provided as arguments.

---
</details><details>
	<summary> <strong> modular </strong> </summary>	

---

##### Functions:

1. [`Exponentiation`](./math/modular/exponentiation.go#L22):  Exponentiation returns base^exponent % mod
2. [`Inverse`](./math/modular/inverse.go#L19):  Inverse Modular function
3. [`Multiply64BitInt`](./math/modular/exponentiation.go#L51):  Multiply64BitInt Checking if the integer multiplication overflows

---
</details><details>
	<summary> <strong> moserdebruijnsequence </strong> </summary>	

---

##### Functions:

1. [`MoserDeBruijnSequence`](./math/moserdebruijnsequence/sequence.go#L7): No description provided.

---
</details><details>
	<summary> <strong> nested </strong> </summary>	

---

#####  Package nested provides functions for testing strings proper brackets nesting.

---
##### Functions:

1. [`IsBalanced`](./other/nested/nestedbrackets.go#L20):  IsBalanced returns true if provided input string is properly nested. Input is a sequence of brackets: '(', ')', '[', ']', '{', '}'. A sequence of brackets `s` is considered properly nested if any of the following conditions are true:   - `s` is empty;   - `s` has the form (U) or [U] or {U} where U is a properly nested string;   - `s` has the form VW where V and W are properly nested strings. For example, the string "()()[()]" is properly nested but "[(()]" is not. **Note** Providing characters other then brackets would return false, despite brackets sequence in the string. Make sure to filter input before usage.

---
</details><details>
	<summary> <strong> palindrome </strong> </summary>	

---

##### Functions:

1. [`IsPalindrome`](./strings/palindrome/ispalindrome.go#L26): No description provided.
2. [`IsPalindromeRecursive`](./strings/palindrome/ispalindrome.go#L39): No description provided.

---
</details><details>
	<summary> <strong> pangram </strong> </summary>	

---

##### Functions:

1. [`IsPangram`](./strings/pangram/ispangram.go#L21): No description provided.

---
</details><details>
	<summary> <strong> parenthesis </strong> </summary>	

---

##### Functions:

1. [`Parenthesis`](./strings/parenthesis/parenthesis.go#L12):  parcounter will be 0 if all open parenthesis are closed correctly

---
</details><details>
	<summary> <strong> pascal </strong> </summary>	

---

##### Functions:

1. [`GenerateTriangle`](./math/pascal/pascaltriangle.go#L24):  GenerateTriangle This function generates a Pascal's triangle of n lines

---
</details><details>
	<summary> <strong> password </strong> </summary>	

---

#####  Package password contains functions to help generate random passwords

---
##### Functions:

1. [`Generate`](./other/password/generator.go#L15):  Generate returns a newly generated password

---
</details><details>
	<summary> <strong> permutation </strong> </summary>	

---

##### Functions:

1. [`GenerateElementSet`](./math/permutation/heaps.go#L37): No description provided.
2. [`Heaps`](./math/permutation/heaps.go#L8):  Heap's Algorithm for generating all permutations of n objects

---
</details><details>
	<summary> <strong> pi </strong> </summary>	

---

#####  spigotpi_test.go description: Test for Spigot Algorithm for the Digits of Pi author(s) [red_byte](https://github.com/i-redbyte) see spigotpi.go

---
##### Functions:

1. [`MonteCarloPi`](./math/pi/montecarlopi.go#L17): No description provided.
2. [`MonteCarloPiConcurrent`](./math/pi/montecarlopi.go#L36):  MonteCarloPiConcurrent approximates the value of pi using the Monte Carlo method. Unlike the MonteCarloPi function (first version), this implementation uses goroutines and channels to parallelize the computation. More details on the Monte Carlo method available at https://en.wikipedia.org/wiki/Monte_Carlo_method. More details on goroutines parallelization available at https://go.dev/doc/effective_go#parallel.
3. [`Spigot`](./math/pi/spigotpi.go#L12): No description provided.

---
</details><details>
	<summary> <strong> polybius </strong> </summary>	

---

#####  Package polybius is encrypting method with polybius square ref: https://en.wikipedia.org/wiki/Polybius_square#Hybrid_Polybius_Playfair_Cipher

---
##### Functions:

1. [`NewPolybius`](./cipher/polybius/polybius.go#L21):  NewPolybius returns a pointer to object of Polybius. If the size of "chars" is longer than "size", "chars" are truncated to "size".

---
##### Types

1. [`Polybius`](./cipher/polybius/polybius.go#L12): No description provided.


---
</details><details>
	<summary> <strong> power </strong> </summary>	

---

##### Functions:

1. [`IterativePower`](./math/power/fastexponent.go#L4):  IterativePower is iterative O(logn) function for pow(x, y)
2. [`RecursivePower`](./math/power/fastexponent.go#L18):  RecursivePower is recursive O(logn) function for pow(x, y)
3. [`RecursivePower1`](./math/power/fastexponent.go#L30):  RecursivePower1 is recursive O(n) function for pow(x, y)
4. [`UsingLog`](./math/power/powvialogarithm.go#L14): No description provided.

---
</details><details>
	<summary> <strong> prime </strong> </summary>	

---

##### Functions:

1. [`Factorize`](./math/prime/primefactorization.go#L5):  Factorize is a function that computes the exponents of each prime in the prime factorization of n
2. [`Generate`](./math/prime/sieve.go#L26):  Generate returns a int slice of prime numbers up to the limit
3. [`GenerateChannel`](./math/prime/sieve.go#L9):  Generate generates the sequence of integers starting at 2 and sends it to the channel `ch`
4. [`MillerRabinDeterministic`](./math/prime/millerrabintest.go#L121):  MillerRabinDeterministic is a Deterministic version of the Miller-Rabin test, which returns correct results for all valid int64 numbers.
5. [`MillerRabinProbabilistic`](./math/prime/millerrabintest.go#L101):  MillerRabinProbabilistic is a probabilistic test for primality of an integer based of the algorithm devised by Miller and Rabin.
6. [`MillerRandomTest`](./math/prime/millerrabintest.go#L77):  MillerRandomTest This is the intermediate step that repeats within the miller rabin primality test for better probabilitic chances of receiving the correct result with random witnesses.
7. [`MillerTest`](./math/prime/millerrabintest.go#L49):  MillerTest tests whether num is a strong probable prime to a witness. Formally: a^d ≡ 1 (mod n) or a^(2^r * d) ≡ -1 (mod n), 0 <= r <= s
8. [`MillerTestMultiple`](./math/prime/millerrabintest.go#L84):  MillerTestMultiple is like MillerTest but runs the test for multiple witnesses.
9. [`OptimizedTrialDivision`](./math/prime/primecheck.go#L26):  OptimizedTrialDivision checks primality of an integer using an optimized trial division method. The optimizations include not checking divisibility by the even numbers and only checking up to the square root of the given number.
10. [`Sieve`](./math/prime/sieve.go#L16):  Sieve Sieving the numbers that are not prime from the channel - basically removing them from the channels
11. [`TrialDivision`](./math/prime/primecheck.go#L9):  TrialDivision tests whether a number is prime by trying to divide it by the numbers less than it.
12. [`Twin`](./math/prime/twin.go#L15):  This function returns twin prime for given number returns (n + 2) if both n and (n + 2) are prime -1 otherwise

---
</details><details>
	<summary> <strong> pythagoras </strong> </summary>	

---

##### Functions:

1. [`Distance`](./math/pythagoras/pythagoras.go#L15):  Distance calculates the distance between to vectors with the   Pythagoras theorem

---
##### Types

1. [`Vector`](./math/pythagoras/pythagoras.go#L8): No description provided.


---
</details><details>
	<summary> <strong> queue </strong> </summary>	

---

##### Functions:

1. [`BackQueue`](./structure/queue/queuearray.go#L32):  BackQueue return the Back value
2. [`DeQueue`](./structure/queue/queuearray.go#L20):  DeQueue it will be removed the first value that added into the list
3. [`EnQueue`](./structure/queue/queuearray.go#L15):  EnQueue it will be added new value into our list
4. [`FrontQueue`](./structure/queue/queuearray.go#L27):  FrontQueue return the Front value
5. [`IsEmptyQueue`](./structure/queue/queuearray.go#L42):  IsEmptyQueue check our list is empty or not
6. [`LenQueue`](./structure/queue/queuearray.go#L37):  LenQueue will return the length of the queue list

---
##### Types

1. [`LQueue`](./structure/queue/queuelinklistwithlist.go#L20): No description provided.

2. [`Node`](./structure/queue/queuelinkedlist.go#L13): No description provided.

3. [`Queue`](./structure/queue/queuelinkedlist.go#L19): No description provided.


---
</details><details>
	<summary> <strong> rot13 </strong> </summary>	

---

#####  Package rot13 is a simple letter substitution cipher that replaces a letter with the 13th letter after it in the alphabet. ref: https://en.wikipedia.org/wiki/ROT13

---
##### Functions:

1. [`FuzzRot13`](./cipher/rot13/rot13_test.go#L72): No description provided.

---
</details><details>
	<summary> <strong> rsa </strong> </summary>	

---

#####  Package rsa shows a simple implementation of RSA algorithm

---
##### Functions:

1. [`Decrypt`](./cipher/rsa/rsa.go#L43):  Decrypt decrypts encrypted rune slice based on the RSA algorithm
2. [`Encrypt`](./cipher/rsa/rsa.go#L28):  Encrypt encrypts based on the RSA algorithm - uses modular exponentitation in math directory

---
</details><details>
	<summary> <strong> search </strong> </summary>	

---

##### Functions:

1. [`BoyerMoore`](./strings/search/boyermoore.go#L5):  Implementation of boyer moore string search O(l) where l=len(text)
2. [`Naive`](./strings/search/naive.go#L5):  Implementation of naive string search O(n*m) where n=len(txt) and m=len(pattern)

---
</details><details>
	<summary> <strong> segmenttree </strong> </summary>	

---

##### Functions:

1. [`NewSegmentTree`](./structure/segmenttree/segmenttree.go#L116): No description provided.

---
##### Types

1. [`SegmentTree`](./structure/segmenttree/segmenttree.go#L17): No description provided.


---
</details><details>
	<summary> <strong> set </strong> </summary>	

---

#####  package set implements a Set using a golang map. This implies that only the types that are accepted as valid map keys can be used as set elements. For instance, do not try to Add a slice, or the program will panic.

---
##### Functions:

1. [`New`](./structure/set/set.go#L7):  New gives new set.

---
</details><details>
	<summary> <strong> sha256 </strong> </summary>	

---

##### Functions:

1. [`Hash`](./hashing/sha256/sha256.go#L50):  Hash hashes the input message using the sha256 hashing function, and return a 32 byte array. The implementation follows the RGC6234 standard, which is documented at https://datatracker.ietf.org/doc/html/rfc6234

---
</details><details>
	<summary> <strong> sort </strong> </summary>	

---

#####  Package sort a package for demonstrating sorting algorithms in Go

---
##### Functions:

1. [`Bubble`](./sort/bubblesort.go#L9):  Bubble is a simple generic definition of Bubble sort algorithm.
2. [`Bucket Sort`](./sort/bucketsort.go#L5): Bucket Sort works with the idea of distributing the elements of an array into a number of buckets. Each bucket is then sorted individually, either using a different sorting algorithm, or by recursively applying the bucket sorting algorithm.
3. [`Comb`](./sort/combSort.go#L17):  Comb is a simple sorting algorithm which is an improvement of the bubble sorting algorithm.
4. [`Count`](./sort/countingsort.go#L11): No description provided.
5. [`Exchange`](./sort/exchangesort.go#L8): No description provided.
6. [`HeapSort`](./sort/heapsort.go#L116): No description provided.
7. [`ImprovedSimple`](./sort/simplesort.go#L27):  ImprovedSimple is a improve SimpleSort by skipping an unnecessary comparison of the first and last. This improved version is more similar to implementation of insertion sort
8. [`Insertion`](./sort/insertionsort.go#L5): No description provided.
9. [`Merge`](./sort/mergesort.go#L41):  Merge Perform merge sort on a slice
10. [`MergeIter`](./sort/mergesort.go#L55): No description provided.
11. [`Pancake Sort`](./sort/pancakesort.go#L7): Pancake Sort is a sorting algorithm that is similar to selection sort that reverses elements of an array. The Pancake Sort uses the flip operation to sort the array.
12. [`ParallelMerge`](./sort/mergesort.go#L66):  ParallelMerge Perform merge sort on a slice using goroutines
13. [`Partition`](./sort/quicksort.go#L12): No description provided.
14. [`Patience`](./sort/patiencesort.go#L13): No description provided.
15. [`Pigeonhole`](./sort/pigeonholesort.go#L15):  Pigeonhole sorts a slice using pigeonhole sorting algorithm. NOTE: To maintain time complexity O(n + N), this is the reason for having only Integer constraint instead of Ordered.
16. [`Quicksort`](./sort/quicksort.go#L39):  Quicksort Sorts the entire array
17. [`QuicksortRange`](./sort/quicksort.go#L26):  QuicksortRange Sorts the specified range within the array
18. [`RadixSort`](./sort/radixsort.go#L43): No description provided.
19. [`Selection`](./sort/selectionsort.go#L5): No description provided.
20. [`Shell`](./sort/shellsort.go#L5): No description provided.
21. [`Simple`](./sort/simplesort.go#L13): No description provided.

---
##### Types

1. [`MaxHeap`](./sort/heapsort.go#L5): No description provided.


---
</details><details>
	<summary> <strong> stack </strong> </summary>	

---

##### Types

1. [`Node`](./structure/stack/stacklinkedlist.go#L13): No description provided.

2. [`SList`](./structure/stack/stacklinkedlistwithlist.go#L18): No description provided.

3. [`Stack`](./structure/stack/stacklinkedlist.go#L19): No description provided.


---
</details><details>
	<summary> <strong> strings </strong> </summary>	

---

#####  Package strings is a package that contains all algorithms that are used to analyse and manipulate strings.

---
##### Functions:

1. [`CountChars`](./strings/charoccurrence.go#L12):  CountChars counts the number of a times a character has occurred in the provided string argument and returns a map with `rune` as keys and the count as value.

---
</details><details>
	<summary> <strong> transposition </strong> </summary>	

---

##### Functions:

1. [`Decrypt`](./cipher/transposition/transposition.go#L82): No description provided.
2. [`Encrypt`](./cipher/transposition/transposition.go#L54): No description provided.

---
##### Types

1. [`KeyMissingError`](./cipher/transposition/transposition.go#L16): No description provided.

2. [`NoTextToEncryptError`](./cipher/transposition/transposition.go#L15): No description provided.


---
</details><details>
	<summary> <strong> tree </strong> </summary>	

---

#####  For more details check out those links below here: Wikipedia article: https://en.wikipedia.org/wiki/Binary_search_tree authors [guuzaa](https://github.com/guuzaa)

---
##### Functions:

1. [`NewAVL`](./structure/tree/avl.go#L13):  NewAVL create a novel AVL tree
2. [`NewBinarySearch`](./structure/tree/bstree.go#L18):  NewBinarySearch create a novel Binary-Search tree
3. [`NewRB`](./structure/tree/rbtree.go#L23):  Create a new Red-Black Tree

---
##### Types

1. [`AVL`](./structure/tree/avl.go#L8): No description provided.

2. [`BinarySearch`](./structure/tree/bstree.go#L13): No description provided.

3. [`Node`](./structure/tree/tree.go#L25): No description provided.

4. [`RB`](./structure/tree/rbtree.go#L18): No description provided.


---
</details><details>
	<summary> <strong> tree_test </strong> </summary>	

---

##### Functions:

1. [`FuzzRBTree`](./structure/tree/rbtree_test.go#L90): No description provided.

---
</details><details>
	<summary> <strong> trie </strong> </summary>	

---

#####  Package trie provides Trie data structures in golang.  Wikipedia: https://en.wikipedia.org/wiki/Trie

---
##### Functions:

1. [`NewNode`](./structure/trie/trie.go#L14):  NewNode creates a new Trie node with initialized children map.

---
##### Types

1. [`Node`](./structure/trie/trie.go#L7): No description provided.


---
</details><details>
	<summary> <strong> xor </strong> </summary>	

---

#####  Package xor is an encryption algorithm that operates the exclusive disjunction(XOR) ref: https://en.wikipedia.org/wiki/XOR_cipher

---
##### Functions:

1. [`Decrypt`](./cipher/xor/xor.go#L19):  Decrypt decrypts with Xor encryption
2. [`Encrypt`](./cipher/xor/xor.go#L10):  Encrypt encrypts with Xor encryption after converting each character to byte The returned value might not be readable because there is no guarantee which is within the ASCII range If using other type such as string, []int, or some other types, add the statements for converting the type to []byte.
3. [`FuzzXOR`](./cipher/xor/xor_test.go#L108): No description provided.

---
</details>
<!--- GODOCMD END --->
