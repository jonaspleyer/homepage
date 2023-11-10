+++
title = 'Creating Posters with typst'
date = 2023-10-17T23:32:00+02:00
post_image = "typst.png"
tags = ['Programming', 'Science']
math = true
+++

I recently came across a new typesetting system called typst.
It is being developed by [Martin Haug](https://github.com/reknih/) and [Laurenz Mädje](https://github.com/laurmaedje/).
It aims to modernize typesetting systems by introducing a new scripting language to control the layout of documents.
There are many new and great things about typst and we could be talking about all of its aspects and compare it to $\LaTeX$ for quite some time.
However, I would like to focus on how to actually use it and what this means in practice for someone that has used $\LaTeX$ since high-school.

## Scientific Posters with $\LaTeX$

As a researcher, one of my many tasks is to visit conferences and present my work in an understandable manner.
It is custom for Phd students to present posters of their current work and many conferences even award prizes for [best posters](https://jonas.pleyer.org/blog/2023/03/31/physics-of-life-conference/).
But the process of creating posters is not simple at all.
$\LaTeX$ offers some packages which do achieve a good overall job.
But to me, the work required to actually achieve decent results seemed quite high and since I am very peculiar when it comes to presentations and posters I did have the tendency to spend a lot of time on improving and even writing my own set of macros to generate a poster of my liking.

## First steps with typst

Getting started with typst is really simple since it is markup-based which is really convenient for simply writing some text and very effortlessly making it look nice.
For complete beginners, I recommend to work through some of the examples in the [tutorials](https://typst.app/docs/tutorial/).
For my personal goal I needed to learn how to place boxes and fill them with the desired content.
The most obvious candidate are rectangles.
To create one box, I simply stacked two of them on top of each other; the upper one for the title and the lower for the main content of the box.
While it took some time to figure out, how stacking really worked, it was an overall simple process.
As time progressed, I began to add more functionality and eventually wrote a [new function](https://typst.app/docs/reference/foundations/function/) to generate boxes according to the specified arguments.
Doing the same in $\LaTeX$ would have been much more cumbersome.
It is of course doable by defining new macros with default values but the end result is (to my personal taste) not even close in elegance of what typst has to offer.
And I actually can speak from experience as I have tried doing [something similar](https://github.com/Spatial-Systems-Biology-Freiburg/poster-presentation-templates/tree/master/posters/latex) before.

As time went on, the whole project became somewhat bigger and I eventually created a new package [typst-posters](https://github.com/jonaspleyer/typst-posters/tree/main) to share the functionality I created.
There is even a small [documentation](https://jonaspleyer.github.io/typst-posters/) accompanying the package.

## Stretch it to the bottom

While design and content are very important in a poster, but so is layout.
Although I am not a designer by any chance I can still appreciate a well-done poster which effortlessly displays highly bundled information in a concise manner.
To achieve this ultimate goal, we want accurately placed boxes with consistent formatting and no wasted space but also no cluttering.
One important aspect is to have boxes that fill out the whole space of the poster (with a certain margin and spacing of course).
This specifically is a surprisingly hard problem for typesetting tools such as $\LaTeX$ and typst.
Whille you can of course manually assign heights to boxes and thus fill out the space evenly, it is very cumbersome and once a box is changed, all following boxes may have to be adjusted.
Both tools can only calculate the height of the respective boxes after compiling their contents.
Thus the remainer of space towards the bottom of the page is not known before the first full compile-cycle.
WYSIWYG editors can have an advantage for this problem but they make consistent formatting with good support for equations a pain in your royal sitting gadget.

I was able to come up with a solution in $\LaTeX$ to partially solve this problem.
First, I manually calculated the position of the bottom-left corner of the used space.
Then I calculated the vertical distance from the lowest box to this point and simply resized the last box to account for the difference.
While this general method also works in typst it was again the older brother who had some technical difficulties.
The actual implementation required me to store the point and height difference intermediately in a file and read from it in the second compile-pass.

In typst I solved the problem very similarly, but typst makes it very obvious for the user that [some functions](https://typst.app/docs/reference/meta/query/) which are required to calculate these height-differences need to be evaluated at different compile-passes and may thus seem like “jumping in time”.
However, the biggest difference in my approach in typst was using [labels](https://typst.app/docs/reference/meta/label/).
With labels, you can mark any element of your document and later [locate](https://typst.app/docs/reference/meta/locate/) them and calculate distances, sizes, etc.
of these elements.
This is *super convenient* to construct a solution that does not require manual marking of any particular corner of the document or the lowest box.
We simply label every box and then filter all labels whose y-coordinate is higher than the last box which we want to stretch.
Afterwards we can stretch up to the next-highest label (with some spacing).
This is exactly the approach which made it into typst-posters and so far works for most problems.
I can not imagine if I would have been able to come up with such a solution in $\LaTeX$ (at least on my own).
The very good documentation of typst made it easy for me to find what I needed.

## Pure functions can be cumbersome

As I explained in the preceding section, I had to calculate a height and then adjust the size of the desired box in order to fill the vertical space.
Some of you might be tempted to write a function that measures this length and returns the value.
While this is partially possible in typst, we can only return such values as [content](https://typst.app/docs/reference/foundations/content/) which is not suited to be reused as a variable.
In general, locating and querying can only return content-type.
This means, that the function which measures this distance also returns the newly sized box as the content which should finally be displayed.
It also cannot simply resize the box as function do not mutate their arguments.
While this particular problem actually can not be solved otherwise (due to evaluation at different compile-time passes), other simpler problems could benefit from non-pure functions.
But to the largest part, these problems seem to be problems of package developers and maintainers who are by nature more technical people and thus possibly also more willing to spend some time to figure out the solution to these kinds of problems.

## Takeaway

Working with typst continues to be an exciting endeavor.
While many aspects of the real-world functionality of $\LaTeX$ are still missing, the potential to succeed and modernize typesetting programs is huge in my opinion.
Maybe most importantly, I actually really enjoy working with it and thus will continue to use it in the future for more and maybe even bigger projects.
