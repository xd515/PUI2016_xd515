You want to give a **justification of why your idea is interesting**. Why of all citibike possible question do you want to know what the ratio of riders at 8AM is compared to 6PM? Why do you suspect more at 8 than at 6? what interesting thing about NYC citibike riders would that tell us if you were to see suh an effect?

and why exactly 8AM? cant be the exact hour. what do you want to be the buffer around the hour of interest? 7-9 and 5-7? you should specify this in your hypotheses formulations.

Also the formulation People using citibikes at 8am are less than is **not sufficiently quantifiable**: the AVERAGE number of citibike users at 8AM (between ?? and ??) is ... is the appropriate quantifiable question.

**The Null hypothesis is INCORRECT**: the null + alternative need to cover the entire realm of possibilities. The Null that complements your "idea" is FEWER OR EQUAL. (Notice that in English the right word here is *fewer*, not *less* since the quantity you are refering to is countable. Less milk, less water, less rain, fewer cars, fewer mistakes, fewer rides.)

**YOU NEED A MATHEMATICAL FORMULATION OF THE NULL**:
```
H0: N_8am - N_6am...
```

DATA WRANGLING:
why are you pulling the gender out of the notebook if your question has nothing to do with gender?

getting the hour as you do works, but it is not robust to file inconsistencies.

overall good data wrangling style though. SEE MORE SPECIFIC SUGGESTIONS IN THE EDITED NOTEBOOK

You are not done though. You have to decide what it means that there are more rides at 8: do you want to use the absolute number of rides at 8 +- *x* minutes? how many minutes around 8:00 and 6:00? is that the number of rides that *starts* within that time buffer or the number of riders that are ongoing? (but that started at any time before?) Do you want the average number, mean, median? do you instead want to compare the proportion? say the ratio of rides (however you decide to measure that) at 8 over rides at 7AM or 9AM ((rides at 8AM)/(rides at 7AM) or (rides at 8AM)/(rides at 9AM)))compared to the ratio of rides at 6PM/rides at 5PM or 7PM, or maybe the (rides at 8AM)/(([rides at 7AM]+[rides at 9AM])/2) compared to the same at 6PM?? You have not specified your question, so you cannot finish your data prepping and you cannot choose a statistical test yet.
