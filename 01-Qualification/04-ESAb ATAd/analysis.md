# ESAb ATAd: Analysis

## My Approach

### General Discussion

My solution focuses on symmetry, and the data are accessed in groups of two. More specifically, the first bit and the last bit are grouped together, the second bit and the second last bit are grouped together, etc.

For each group, they can either have the same value, or different values. Denote the groups with same value **S** groups and the groups with different values **D** groups.

* For an **S** group, *reversing* the data does not affect this group.
  * If, after a quantum fluctuation, an **S** group's value changes, then the data is *complemented*. Otherwise, data is not *complemented*; however, this gives no information about whether *reversing* took place.
* For a **D** group, *reversing* the data and *complementing* it produce the same result.
  * If, after a quantum fluctuation, a **D** group's value switches, then one and only one of *reversing* and a *complementing* has occurred. Otherwise, either both or neither of *reversing* and *complementing* occurred.

Utilizing both information,

| **S** group     | **D** group     | What happened                 |
| :-------------: | :-------------: | :---------------------------: |
| Does not change | Does not change | Nothing                       |
| Does not change | Switches places | Reversing                     |
| Changes         | Does not change | Reversing *and* Complementing |
| Changes         | Switches places | Complementing                 |

### Implementation

The first fluctuation doesn't matter because we didn't get any data before that anyway. We can obtain five pairs of data points. *Test set 1* is swiftly solved.

The tricky part comes after that. The next result comes after some quantum fluctuation. After the 10th, 20th, 30th, etc. query, the next two queries are used to check what fluctuations have occurred.

* If, among the data pairs collected so far, there are no **S** groups (i.e., all pairs are **D** groups), then *reversing* and *complementing* have the same effect. Check the first value of any pair.
  * If the new value is the same as the value before the fluctuation, either both or neither of *reversing* and *complementing* happened. Either way, the data does not change. Otherwise, either *reversing* or *complementing* has occurred.
* If, among the data pairs collected so far, at least one pair is an **S** group, check the first value of any **S** group.
  * If the new value is the same as the value before the fluctuation, then *complementing* did not occur. Otherwise, *complementing* occurred.
  * If, among the data pairs collected so far, there are no **D** groups (i.e., all pairs are **S** groups), then *reversing* has no effect. Otherwise, check the first value of any **D** group.
    * If the new value is same as the value after the potential *complementing*, then *reversing* did not occur. Otherwise, *reversing* occurred.

In short, it follows this flowchart:

```text
                                                                           |-------|
                                                                           | Start |
                                                                           |-------|
                                                                               |
                                                                               |
                                                                               |
                                                                               v
                                                            Yes  |---------------------------|  No
                                     ----------------------------| There are no **S** groups |----------------------------
                                     |                           |---------------------------|                           |
                                     |                                                                                   |
                                     |                                                                                   |
                                     v                                                                                   v
          Changed  |-----------------------------------|  No change                        Changed  |------------------------------------------|  No change
        -----------| Query the first value of any pair |-------------                    -----------| Query the first value of any **S** group |-------------
        |          |-----------------------------------|            |                    |          |------------------------------------------|            |
        |                                                           |                    |                                                                  |
        |                                                           |                    |                                                                  |
        v                                                           v                    v                                                                  v
|--------------|                                              |------------|    |-----------------|                                                   |------------|
| Reverse data |                                              | Do nothing |    | Complement data |                                                   | Do nothing |
|--------------|                                              |------------|    |-----------------|                                                   |------------|
        |                                                           |                    |                                                                  |
        -------------------------------------------------------------        --------------------------------------------------------------------------------
                      |                                                      |
                      v                                                      v
              |---------------|                           Yes  |---------------------------|  No
              | Waste 1 Query |                   -------------| There are no **D** groups |------------
              |---------------|                   |            |---------------------------|           |
                                                  |                                                    |
                                                  |                                                    |
                                                  v                                                    v
                                          |---------------|          As expected  |------------------------------------------|  Different from expected
                                          | Waste 1 Query |        ---------------| Query the first value of any **D** group |---------------------------
                                          |---------------|        |              |------------------------------------------|                          |
                                                                   |                                                                                    |
                                                                   |                                                                                    |
                                                                   v                                                                                    v
                                                            |------------|                                                                      |--------------|
                                                            | Do nothing |                                                                      | Reverse data |
                                                            |------------|                                                                      |--------------|
```

The above process takes at most two queries; in fact, when it takes only one query, we'll waste one query such that the above process always takes two queries. All hail consistency.

The first 10 queries get data for 10 data points, after which 8 data points are got for each 10 queries. Therefore, *Test set 2* takes 24 queries each, and *Test set 3* takes 124 queries each, which is less than the 150 required.

### Why the Procedure does not Exactly Match the Table

If you're somehow still with me, you may notice that in the scenario where

* both **S** and **D** groups exist, and
* **S** group value changes,

the table says that an unchanging value for **D** group translates to *reversing* and *complementing*, but in the flowchart and procedures the data is reversed when the value of the **D** group is "different from expected".

This is a result of the step before this query, where data is *complemented* after the first query as **S** group values have changed. This step flipped data of all **D** groups. Therefore, if originally a change in bits was not expected, after the *complementing* step it should be expected, and vice versa.
