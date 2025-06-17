+++
title = 'Ownership in Rust – Yet another explanation'
date = 2023-12-09T17:00:00+02:00
post_image = "AP_20210410_153701_IMG_7681.jpg"
tags = ['Programming', 'Rust']
description = "A naive and hopefully intuitive explanation of ownership rules in Rust."
aliases = ['/blog/2023/12/09/ownership-in-rust-yet-another-explanation/']
+++

Rust is a very popular programming language for many good reasons.
It seems to fix many annoyances which people have with longstanding alternatives such as C++.
On top of that it has concepts for ownership of variables.
These concepts are often hard to grasp when looking at datastructures and algorithms.
This is my attempt to explain them in a very naive and intuitive way.

## Grandma’s Cake Recipe

Your grandma has this very unique recipe to make your most favorite birthday cake. She wrote down every small step how to bake it.

{{< highlight Rust "linenos=table,linenostart=0" >}}
struct Cake;
struct Recipe {
    flour: u16,// in grams
    sugar: u16,// in grams
    // ...
}
{{< /highlight >}}

## Borrowing

You are not the only person to get this birthday cake every year.
Your father is the other lucky one.
But this year, grandma is on vacation and will not have enough time to prepare the cake before
coming to your fathers birthday party.
So you decide to take things into your own hands and bake the cake by yourself.
For this you borrow your grandmothers recipe.

You promise your grandma not to change anything in the recipe and since you are a very responsible
grandson, you only use it to read what is inside the recipe.

{{< highlight Rust "linenos=table,linenostart=7" >}}
fn bake_cake(recipe: &Recipe) -> Cake {
    // Bake the cake and return it
    return Cake;
}
{{< /highlight >}}

After you are done, you hand back the recipe.
It is like you never even held the recipe in your own hand and in exactly the same condition as
before.

Some time has passed since the last time you made the cake but you are still thinking about it.
Maybe it would be better with a little bit more sugar and a bit less flour.
You decide to visit your grandma and ask for the recipe again.
But this time you tell her about your idea.
She trusts you with the changes you are going to do to her precious recipe.
And so you modify the recipe just so slightly to really make the perfect cake.

{{< highlight Rust "linenos=table,linenostart=12" >}}
fn optimize_recipe(recipe: &mut Recipe) {
    // Add 10 grams of sugar
    recipe.sugar += 10;
    // Remove 10 grams of flour
    recipe.flour -= 10;
}
{{< /highlight >}}

After you are done, you hand back the recipe to its original owner which is your grandma.
She tries the new one and is really happy about it.

## Copy or Clone

You have a good friend from school who is always at your birthday.
One day he asks you for the amount of sugar in the cake.
You get the recipe and tell him the number.

{{< highlight Rust "linenos=table,linenostart=16" >}}
fn get_sugar_from_recipe(recipe: &Recipe) -> u16 {
    // These two are exactly identical
    // return recipe.sugar.copy();
    return recipe.sugar;
}
{{< /highlight >}}

The recipe is not being modified in any way.
You simply took a number and copied it for your friend.

Some time later, the same friend comes along again.
He’s not sure how to correctly bake the cake
without the complete Recipe.
So you promise him to make an identical Clone of the recipe itself.
Once more, you borrow the recipe and simply copy every entry of it.
Afterwards you hand back the recipe.
After all, the recipe still belongs to its rightful owner which is your grandma.

{{< highlight Rust "linenos=table,linenostart=22" >}}
// We can clone a complete struct by copy/cloning
// every single entry to create a new one.
#[derive(Clone)]
struct Recipe {
    flour: u16,
    sugar: u16,
    // ...
}

fn make_copy_for_friend(recipe: &Recipe) -> Recipe {
    return recipe.clone();
}
{{< /highlight >}}

## Taking Ownership

Some years have passed and your grandmother has moved to another city to live with her new lover.
Before she leaves, she hands you the recipe.
You are so happy that your grandmother would even consider this.
The recipe now belongs to you, meaning you are now the new owner of the original recipe.

{{< highlight Rust "linenos=table,linenostart=22" >}}
fn take_the_recipe(recipe: Recipe) {
    // I am now the owner of this recipe
}
{{< /highlight >}}
