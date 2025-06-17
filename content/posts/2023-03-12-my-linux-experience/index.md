+++
title = 'My Linux Experience'
date = 2023-03-12T01:07:00+02:00
post_image = "33718-1-cropped.jpg"
tags = ['Programming', 'Science']
aliases = ['/blog/2023/03/12/my-linux-experience/']
+++

If you are part of the scientific community, you must have heard of Linux. This small post is not meant to capture everything good and bad or even everything important there is to know about GNU, Linux and many of the other open source projects out there. It is simply my story and view and why it is my preferred operating system. Feel free to jump to the end to skip my personal story.

# Story-Time
## First Steps

As for most people, my first experiences with computers were all Windows based. The CD-ROM and DVD were the first storage devices I actively used, although I still got to know what a floppy disk is. Windows XP was my first operating system. My experience back then was constrained to playing games and only occasionally browsing the web. This would not change much, even when I got my first own machine with Windows Vista. Only that the amount, I was using the device was increasing.

When I was around the age of 16, a friend of mine talked to me about Linux and it was then when I first discovered, how to install and use [Ubuntu](https://ubuntu.com/). My initial steps consisted of creating a bootable USB drive and installing it via the graphical installer but still on a much older PC and not my main machine. I started playing around with it and at the time found it much simpler to use than the current iteration of Windows Vista. Although none of my games were running on this operating system, I stuck with it for a while. We had went to the US for a very large trip in the preceding year and my dad had bought a light and cheap laptop to write a diary during our visit. It was horribly slow and could not handle Windows at all. Although I had read that Linux should be much more resource friendly, I was still surprised that the device became usable again after installing Ubuntu on it.

The next chapter of my Linux experiences were more on a serious front. I actually wrote my preparation for my mathematics high school finals in [$\LaTeX$](https://www.latex-project.org/). [Debian](https://www.debian.org/) with the older [KDE 4](https://kde.org/) interface was my preferred distribution. I stopped using any of the Microsoft Office products and resorted to only using open-source applications, only resorting to Windows when necessary or for the occasional games, which I was still playing. Windows and Linux came along just fine as a dual-boot system. During this time, I slowly began shifting my productive work from Windows to Linux altogether. However, apart from the occasional dabbling in bash commands, I was never really introduced to programming in any language. The closest, I would come was using the computer algebra system wxmaxima for calculations. I would even use this system in the beginning of my studies.

## Taking it more serious

Around 2015, I became more interested in different distributions. Up to this point, I had mainly used Ubuntu and Debian, and played around with [Linux Mint](https://linuxmint.com/). All of them were fine but as many more seasoned Linux users might relate to, you can go down the rabbit hole a lot more. I watched and read many comparisons between distributions, but Archlinux with its simple “KISS” principle really intrigued me. So I installed Archlinux as my main production system. I have to emphasize that during this time, there was no automated installer but a very solid guide on the Wiki was already present. Up to this point, I had no idea what a file-system or bootloader were and while I was used to learning new concepts, I could not comprehend all of them at once. So my installation crashed multiple times and I needed to start over but after many iterations I ended up with a working system.

My initial experiences with Arch were very unstable. The KDE plasma desktop environment was just released and still in an early version but I was eager to adopt it along with the still present bugs and in addition, I had no idea how to properly maintain my operating system. When googling my problems I would often try to use proposed solutions meant for other distributions. [NVIDIA](https://www.nvidia.com/)s support for Linux has also not been the brightest and problems with their particular products still haunt me to this day. Needless to say, I had to reinstall Arch from scratch multiple times but was stubborn enough to stick with it. My Laptop (Thinkpad T440) also got the Arch-Linux treatment.

## Actively using Linux

I was now at a point where I could actively use Linux as my daily driver and was not afraid to instantaneously mess up the system. Studying physics was no problem at all. At this point most of my work was writing [$\LaTeX$](https://www.latex-project.org/) documents, researching stuff and producing plots occasionally. I slowly started to automate some of my processes. For example, I started using [unison](https://www.cis.upenn.edu/~bcpierce/unison/) to synchronize files across my machines and had some experience in writing small bash scripts. My attempts to fix my system became more precise and were necessary less often. Instead, I wanted to test the boundaries of my current setup more and more often. And along this way of continuously screwing up my system, fixing it and tinkering with it again, I started to learn many important details and concepts of operating and file systems, kernels, modules, etc. I can still remember the switch from the traditional init system to systemd in [Archlinux](https://bbs.archlinux.org/) as this was highly debated and advertised as possible breaking your system but was highly relieved when this major update left my machine unharmed.

At some point, I was actively searching in threads on the archlinux forums and thus decided to create an account. I became much more active and tried to help while also looking for advice. However, the amount of interactions, I had remained limited since I was still learning lots of things. I think at some point, I had made so many mistakes that I could not be surprised by anything new. If some of my tinkering brought the system to a non-bootable state (which thankfully did not happen very often) I knew how to handle the problem. The command line had gotten my friend as a precise and unforgiving instrument. Please do not mistake these words with anything else but a feeling my poor younger self was experiencing at this time.

# General Thoughts on Linux
## How am I using Linux today?

My typical workflow is dominated by 3 applications: A text-editor for coding (currently using [Visual-Studio Code](https://github.com/microsoft/vscode) or [vim](https://www.vim.org/)/[neovim](https://neovim.io/) from the command-line) some terminal windows (zsh with powerlevel10k), many browser tabs and windows ([firefox](https://www.mozilla.org/firefox/)). I like to use vscode strictly for writing code and will execute and test it in one of the terminal windows. My setup has a vertical monitor so this space is already designated.
Since I am running Archlinux with KDE, I am using [dolphin](https://apps.kde.org/en-gb/dolphin/) to browse my files. Mail and Calendars are handled by [thunderbird](https://www.thunderbird.net/). I am using [Zotero](https://www.zotero.org/) to store papers for my research. These are my most-used graphical applications. There are loads of command-line tools which would be another post for itself.

Since I develop numerical simulations, I will execute simulations or calculations very frequently to manually test them. To be honest, I would not even know how to do this on a Windows device (Mac would work though). I am particularly interested in scenarios where performance is usually pretty important. Faster execution times in my world means that I can analyze larger parameter-spaces which leads to more reliable results. Linux allows me to retain fine-grained control over every aspect of my simulations.

## The community

The openness of projects allows (although this is no guarantee) for truly democratic principles. There are advantages and disadvantages to having bigger or smaller teams. The important aspect is that projects which are freely accessible permit both. There are projects which are mainly influenced by a single person or very small group, but as long as the user-base is happy with the efforts, there is no need to take action. However as time has already told us multiple times ([GCC & EGCS](https://gcc.gnu.org/wiki/History#EGCS), Audacity), forks can happen and subsequently improve the overall state of the project. That is not to say that this systems is perfect, but maybe lets spare this discussion for another time.

The people doing open source can sometimes be technically versatile while being socially challenging. Especially older generations of developers are known for their temperament. I believe that every person can find a place to fit in. We need both types of people. The ones who are passionate about [print-statements](https://lore.kernel.org/lkml/20210126211551.26536-1-john.ogness@linutronix.de/) and communicators to bring in helping hands and of course every nuance in between. Most larger community projects contain a wide variety of tasks to pick from and get started.
Traditionally, the Linux space has always been very developer focused, since most of the users come from this background themselves. This is probably the reason, why it appeals to me so much.

For the future, I would like to see more public money invested into open-source projects on which our whole modern infrastructure is built upon. Germany has made a small effort to spend more money, but more drastic measures need to be put in place in my opinion.

## What is open source to me?

The work, I am doing right now could not be possible without the immense supply of open-source software and knowledge. Although I have access to proprietary applications and licenses via my university, I rarely use it and try to rely and free solutions. I cannot pinpoint to one particular strength of open source which I like. From a security standpoint, it makes no sense to do anything else as security through obscurity is just a poor excuse. The same applies for publicly funded research projects. The ability to play with the code itself at all depths is vital for the sometimes creative development process in the scientific community.

To say that my life would have not been the same weren’t it for the vast amounts of open-source software is probably equally true for every human being on earth. But I am now at a point where I can directly see very transparently how this affects me personally. For this I am forever grateful.

Image Credit: [kde store, techsolo](https://store.kde.org/p/1075629)
