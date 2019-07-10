title: Don't send your clients to prison with the base rate malpractice trap
tags: math, probability, malpractice_traps
date: 2019-07-10
author: Paul Gowder
javascripts: drunk.js

Here's a hypo for you.  You're a criminal defense attorney, and you have a client who was arrested at a DUI checkpoint. Your client was subjected to a fast breath-test for alcohol, requiring them to blow into a machine. (Let's suppose that for some bizarre reason this counts as minimally intrusive and constitutional under [Michigan Dept. of State Police v. Sitz](https://www.law.cornell.edu/supremecourt/text/496/444); if it eases your mind, you may also assume that your client, and every other person stopped, consented to the test). Unfortunately, the machine reported that your client was intoxicated beyond the statutory limit (though it didn't report a specific blood alcohol content value), and your client was arrested on that basis. 

At the arraignment, the prosecutor comes to you and says the following: 

> I'm prepared to present expert witness testimony showing that the breath test your client took has a 99% accuracy rate, measured against the most reliable way we have to determine whether someone is legally intoxicated. That's enough for a jury to find them guilty beyond a reasonable doubt---when the nice people in the jury box see that the defendant had a 99% chance of having been drunk, they'll be sure to convict on that evidence alone, and it's jail for your client. But I'm feeling merciful today. Tell them that if they plead guilty, I'll ask the court for no time behind bars, just a $5,000 fine and a year's license suspension. 

**How confident should you be that your client was actually drunk?  Should you believe what the prosecutor says?** Think about this question before you scroll down.

...

...

...

...

...

...

...

...

...

...

...

...

...

If you turn around and advise your client to take the deal because conviction is a near-certainty, the next call you make should be to your malpractice insurer. You don't have nearly enough information to know confident you---or a jury---should be that your client is guilty of drunk driving. 

First of all, what does "accuracy" mean?  There are two ways that a test like this could be inaccurate. 

- First, it could emit "false positives"---someone's not drunk, but the test says they are.  

- Second, it could emit "false negatives"---someone's drunk, but the test says they're sober.  

There's no reason to think, *ex ante*, that any kind of test has similar false positive and false negative rates. (For an extreme example, imagine a totally broken test that always reports "drunk."  That test will have a false negative rate of 0, just because it never produces a negative result---but the false positive rate is doubtless rather higher.) If the prosecutor is being really dishonest, they could mean "false negative rate" by "accuracy," and not be telling you anything about the false positive rate at all. 

Let's give our prosecutor the benefit of the doubt on that question and assume that the false positive rate and the false negative rate are both the same, and that "99% accuracy" means that the false positive rate and the false negative rate are each 0.01. **You still don't have enough information to tell your client to take the deal.**

The last piece of information you need to know is the *base rate*---or what proportion of the people who would have been passing the checkpoint were actually drunk. It turns out that if the base rate is sufficiently low, even a very accurate test doesn't give you very much reason to be confident that the thing it's testing for is actually true. 

To see this, let's give you a base rate of 2%.  That is, suppose we know (believe with very high confidence) that 2% of the people who passed the checkpoint were actually intoxicated beyond the legal limit. 

(For simplicity, let's assume this is a constant rate of drunkenness across the whole time the checkpoint is in operation, and let's further assume that we get this information from some reliable external source---not from arrest rates or any other source that itself depends on test accuracy. For example, maybe a team of social scientists did a really good study of intoxication rates by geography and time.) 

Now imagine that 10,000 people get stopped by the checkpoint.  (That's a lot of people, but I'm making the number that high so we don't have to mess around with decimals later on. To make it more realistic, pretend the checkpoint is in New York City, and there are actually a bunch of checkpoints at the same time.)  Because the checkpoints were (let's assume) at random locations, and they test everyone, this is equivalent to a random sample of the population, so we should expect 2% of the people, or 200, to actually be drunk. 

Of those 200 drunk people, the test correctly identifies 198 of them as drunk, and 2 (our 1% false negative rate) are misidentified as sober and get off scot-free.

However, there are also 9,800 sober people who get stopped and tested at the checkpoints. Our 1% false positive rate implies that 98 of those people are misidentified as sober and get arrested. 

So, what does this mean for your client?  Without any other information, the prosecutor (and, more importantly, the jury) can't know whether they were one of the 198 drunk people who got a positive test, or one of the unlucky 98 sober people.  After doing a little bit of easy arithmetic (for those who want the details: we're converting odds to probability), we can conclude that the probability that your client was drunk, if all we know is that they blew a positive result, is only about 67%.  That's better than even, to be sure---it sounds like probable cause... but is it beyond a reasonable doubt? Probably not!

Below, you'll find a series of sliders, and a calculation of the ultimate probability that your client is actually guilty (or that some other claim about the world is true) given a particular false positive rate, false negative rate, and base rate.  Play around with these numbers, try to get a feel for how much of a difference the base rate makes.

 <div id="app">
dynamic content should appear here...
 </div>

Let's work through a few more examples. Imagine that the base rate is only 1%, and the accuracy rate (as described above) is still 99%.  Now, there are only 100 drunk people who take a breath test, and 99 of them get arrested.  There are 9,900 sober people who take a breath test, and 99 of them get arrested too.  There's only a 50-50 chance that your client was one of the drunk ones!  

Let's bump the base rate back to 2% again, but now the test is only 95% accurate (the false negative and false positive rates are both 5%). Of the 200 drunk people, 190 get caught. Of the 9800 sober people, 490 get mistakenly arrested(!!!): it turns out that even though our client blew a positive result on the "95% accurate test," there's only about a 28% chance that they were actually drunk. If that's the only evidence the prosecution has, you shouldn't be taking a plea bargain, you should be filing a motion to dismiss! 

Statisticians and scientists call the mistake that the prosecutor wanted you to make "the base rate fallacy"---the error of neglecting the rules of "conditional probability" and not taking into account the base rate of some tested-for fact in figuring out how much information we learn from a test. But I prefer to call it the "base rate malpractice trap," because, if you fall into it, you'll give lousy advice to your clients and they really oughta sue you.  

There's a simple mathematical formula that you can use to calculate problems like this. Let's use some variables, like in algebra. We'll call the actual chance that your client was drunk (the probability we're trying to calculate): *d*. Let's call the base rate: *b*. Call the false positive rate: *fp*. And call the false negative rate *fn*.  Then you can plug the numbers into the following equation:

$$d = \frac{b \cdot (1 - fn)}{(b \cdot (1- fn)) + ((1-b) \cdot fp)}$$

Let's take our last example and apply this formula:

$$d = \frac{0.02 \cdot (1 - 0.05)}{(0.02 \cdot (1- 0.05)) + ((1-0.02) \cdot 0.05)}$$

With some simplification steps: 

$$d = \frac{0.02 \cdot 0.95}{(0.02 \cdot 0.95) + (0.98 \cdot 0.05)}$$

$$d = \frac{0.019}{0.019 + 0.049}$$

$$d = \frac{0.019}{0.068}$$

$$d \simeq 0.279$$

which is what we got before, and what our calculator tells us. 

### Further reading
- For a detailed and mathier explanation of conditional probability and lots more in basic probability, you can see [a lesson I gave to my students in a data science for lawyers course](https://sociologicalgobbledygook.com/the-basics-of-probability.html).  

- For an academic paper reporting on a variety of evidence that judges fall into the base rate fallacy, see Christian Dahlman, Frank Zenker & Farhan Sarwar, [Miss rate neglect in legal evidence](https://academic.oup.com/lpr/article/15/4/239/2580528), 15 Law, Probability and Risk, 239 (2016).


