# Pattern Matching: Analysis

## My Approach

The 10000-character limit is enough for us to concatenate all 50 strings of 100 characters. Therefore, it is not necessary to find the most efficient string.

To construct the inefficient string, the idea is to basically concatenate them. The only problem is that some of the patterns may not allow concatenation on either side, as only patterns with asterisks on both sides (e.g., `*CHOCO*`). For those patterns that have letters on one or more sides, We just take out the heads and tails and concatenate the rest together.

To figure out the combined heads/tails, collect all heads or tails and figure out a head or tail that can entail all of them.
