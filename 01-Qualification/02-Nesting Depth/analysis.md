# Nesting Depth: Analysis

## My Approach

Construct a valid string, and then reduce it to minimal form.

To construct a valid string, attach pairs of parentheses around each number, with the number of pairs the same as the number. E.g., `1243` → `(1)((2))((((4))))(((3)))`.

To reduce it to minimal form, get rid of `)(` until there is none. This is because a `)` reduces the number of encasement, while the following `(` immediately increases it. Effectively, these two cancels each other out. For our example, `(1)((2))((((4))))(((3)))` → `(1(2)(((4)))((3)))` → `(1(2((4))(3)))` → `(1(2((4)3)))`
