# Probable Grade?

On a day during the examination week of my first year, I vividly remebmer not wanting to study for the exam the next day... I just wanted a grade that would be passable and not affect my score card much. So, I just wanted to know how much I needed to score, just a vague value so that I would get the grade I wanted. \
We usually get the Min, Max, Average marks of the mid sem exams in the class comittee meeting and all I had was this little info and now I want to know how to compute the possible grades, given this info.
And that's the story behind this repo. \

## How does it work?
Well, it's just some simple random algorithm I just made up, which might not cover up great details or the corner cases, but presents you with a vague idea of the marks needed. Also, I utilised `numpy`'s random triangular distribution to generate the grades as well.

So, the idea is that given the `Number of Students`, `Mean/Average`, `Maximum Score` and `Minimum Score` we need to compute the possible marks required for a grade.

The grading scheme is the below (Usually used for a class of more than 50 students).

| **Range for X**                       | **Grade** |
|---------------------------------------|-----------|
| $X \geq \mu + 1.65\sigma $         | S         |
| $\mu + 0.85\sigma \leq X 4< \mu + 1.65\sigma $ | A         |
| $\mu + 0.12\sigma \leq X < \mu + 0.85\sigma $ | B         |
| $\mu - 0.65\sigma \leq X < \mu + 0.12\sigma $ | C         |
| $\mu - 1.3\sigma \leq X < \mu - 0.65\sigma $  | D         |

Where $\mu$ is the `Mean`, $\sigma$ is the `Standard Deviation` and $X$ is the score in that subject.

## How to use?

Clone the repo or download the zip or just copy the code then follow the below procedure.

Lines `6-9` need to be changed in order to get your required output \
The below is an example
```python
min_val = 20 # give the minimum value here
max_val = 99 # the max here
mean_val = 65 # the mean here
no_ppl = 89 # the number of students attending the course
```
Run after changing these lines and you'll see the output in a file titled `std_devs.txt`, which has about 25 cases in two different algorithms.
Go through it to get a general idea.



> [!CAUTION]
> This is just a reference marks that is completely generated using pseudorandomness and might not align with the grading system of the instructor. \
> Use this as a reference and nothing more than that. 
