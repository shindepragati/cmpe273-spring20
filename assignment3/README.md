
## Question:

What are the best k hashes and m bits values to store one million n keys (E.g. e52f43cd2c23bb2e6296153748382764) suppose we use the same MD5 hash key from pickle_hash.py and explain why?

## Answer:

A Bloom filter is a space-efficient probabilistic data structure, means that the element is not present in the set for sure or may be present in the set.

The more hash functions we use it makes the bloom filter slow and it gets fills up quickly. And if we use few hash functions it might gives use too many false positives.

Best k hashes for one millio n keys:

Given:
      
    n: 1M 

    p: suppose false positive rate is 0..1 means 0.01 for 1%

Find:

    m: bits values

    k: the number of hashes

The formulas:
    
    m = -n*ln(p) / (ln(2)^2) the number of bits

    k = m/n * ln(2) the number of hash functions

Calculation:

    m = -1,000,000*ln(0.01) / (ln(2)^2) = -4605170 / 0.48045 =  9585118 bits (576 kB)

    k = m/n * ln(2) = 9585118/1,000,000 * 0.693147 = 6.643 hash functions ==> almost 7 hash functions are required

------------------------------------------------------------------------------------------------------------------------

when p is 0.02 

Calculation:

    m = -1,000,000*ln(0.02) / (ln(2)^2) = 3912023 / 0.48045 =  8142414 bits (1017 kB)

    k = m/n * ln(2) = 8142414/1,000,000 * 0.693147 = 5.64 hash functions ==> almost 6 hash functions are required



So the m and k value is depends upon the value of p we are going to use.
