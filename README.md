# generate-parantheses
 leet code problem solution 
https://leetcode.com/problems/generate-parentheses/


## approach
I use a dictionary to solve the problem. All the i+1 stages are made using the previous i stage's strings.
1. the valid string in the previous i is used and accordingly all the new valid strings are found. 
2. duplicates are avoided using dicitonary.
3. 