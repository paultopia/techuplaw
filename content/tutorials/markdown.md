title: Why and how to use markdown instead of (or in addition to) Word
tags: word_processing, markdown, office_tech
date: 2019-07-09
author: Paul Gowder


## Why you should consider writing documents in Markdown

Markdown is a plain text formatting language.  It allows you, as the cool kids say, to separate content and the *semantic properties of content* (i.e., which bits of text are what---which bits are footnotes, which bits are quotes, which bits are headings) from the *style* of that content (which bits are italic, how much paragraphs are indented by, what font you're using, etc.).  

In other words: you know how whenever you write a document in Word, you get into a nightmarish rabbit hole of things like trying to convince Word when to start and stop numbering a list?  Or how you can copy and paste some text in from somewhere else, and sometimes it includes the formatting, and sometimes it doesn't?  (And "paste and match formatting" seems to do something entirely random.)  Well, if you just write the text in one place, and then apply styling after the fact, you don't need to worry about that at all!  

Here's an example of a simple Markdown document. 

```markdown

# My Amazing Heading 

Here I am.  Writing a document.  For the following reasons: 

1.  Because I want to.

2.  Because I said so. 

3.  Shut up.

Now I'm going to write a paragraph.  Look at me, paragraph. 

This paragraph [has a link](https://google.com) in it.  Neat-o. 

```

You can write this with any ordinary plain text editor (like Textedit on a Mac or Notepad on a Windows machine), and then you can use a program like Pandoc (we'll cover this below) to convert it into a Microsoft Word document.  The numbered lists will be correctly formatted, without you having to fight with them.  The link will work right. Every paragraph will be consistently formatted.  And, best of all, you won't have had to click sub-sub-sub menus or figure out what "ribbon" some obscure command is on.  And, do you see how quickly your text editor started?  And how your text editor, unlike Word, didn't crash when you gave it a big document? 

Not only that, but you might not need to touch Microsoft Word at all.  You can also convert a Markdown file directly to PDF, or to a HTML page for display on the web (and to lots of other formats too). 

Moreover, when you're working in plain text, you open up lots of other superpowers. For example: Microsoft Word track changes is terrible; it makes things super-slow and, when you're doing a lot of changes, makes them almost totally unreadable. (Law professors who have gotten thousands of tiny changes back from Law Review editors: can I get a 'hell yeah'?)  But if you're working in plain text, you can use a *version control* tool called Git to track changes instead; it's vastly more powerful, and, once you learn it, vastly easier to use on a day-to-day basis. (Git is a subject for a future article on this site.)  If you're working with really large documents, you can use programming languages and advanced, powerful, text editors to do [sophisticated search and replace](https://sociologicalgobbledygook.com/regular-expressions.html) functions that Microsoft can't handle.  The same goes for other kinds of added functionality: lots of things that you can do in a slow and crash-prone way in Word, like insert citations with a citation manager, can be done in a more fast and reliable way using text-based tools. 

There's a little bit of a learning curve, but once you get through it, I think you'll see that it's worthwhile!


## How to use Markdown

There are a few things you need to have on your computer in order to use Markdown.

### A good text editor

You shouldn't try to use Microsoft Word to edit Markdown. First of all, that would totally defeat the purpose (we're trying to *avoid* that terrible program, remember?)  Second, Word isn't designed to produce plain text files.  You should use a plain text editor.

As I said, you already have one on your computer: Windows users have Notepad, Mac users have Textedit. (If you use Linux, you don't need this tutorial.) But in all honesty, those are kind of weaksauce text editors.  Here are my recommendations.

If you, like me, are deeply embedded in the Apple ecosystem, just get [Byword](https://bywordapp.com/).  It's designed for Markdown, so it can do things like preview formatting. It syncs over iCloud between Mac and iOS devices.  It's very cheap. It's very simple. I use it for all my basic writing, like letters and such. Some people swear by [Ulysses](https://ulysses.app/), but it's vastly more expensive with an obnoxious subscription pricing model, so I won't recommend it or use it.

For more demanding uses/if you want an editor that can be extended with code, I recommend one of the following two applications, which are both available for Windows and Mac: 

- [Atom](https://atom.io/).  Pros: free, scriptable in Javascript.  Cons: can be a bit of a battery drain and resource hog (though probably not as bad as Microsoft Word).

- [Sublime Text](https://www.sublimetext.com/). Pros: fast, lightweight, scriptable in Python (way better than JavaScript), just a beautifully designed piece of software---there are cults of people who love it.  Cons: A bit expensive ($80), although if you're willing to tolerate nag messages you can use for free. 

On Mac there is also [BBEdit](https://www.barebones.com/products/bbedit/), which is fine. There are also dedicated Markdown editors for both platforms; like I said, I like Byword for Mac; for Windows I'm not sure what's best. 

Worth an honorable mention is [Scrivener](https://www.literatureandlatte.com/scrivener/overview) which is a multi-platform application that is beloved by many writers. It's a kind of complicated program that allows you to break up a document into chunks and reorganize them, among many other features. It can handle Markdown input and output with a little bit of persuasion, though it's not really a plain-text editor at heart.  It's mostly useful as an intermediate writing stage to reorganize long documents; I will often just import a bunch of sections of a long article as individual Markdown files, organize them in Scrivener, and then dump them back out as one big Markdown file for further revision.

Regardless of what platform you're on, you'll want to save markdown files with the extension `md` like `myfile.md`.  This will help your preferred text editor know that you're working with a Markdown file, and hence show you things like formatting previews and markup highlighting to make it easier to see what you're doing. 

### Pandoc and LaTeX

[Pandoc](https://pandoc.org/) is a program that allows you to convert Markdown files to numerous other formats. (It has many other superpowers as well, but this is the key use.)

To use it, you need to get comfortable with your command line.  (For Mac, this is the Terminal application under Utilities, although once you get happy with using the commandline you'll probably want to upgrade to [iTerm2](https://www.iterm2.com/). I'm not sure how to get at it in Windows, but Google will help.)  Learning how to use the command line is the subject of a different tutorial, yet to be written, but here I'll assume you know how, or can google your way through it. 

To install Pandoc, you can [download and run the relevant installer for your OS](https://pandoc.org/installing.html).  If you're using a package manager you'll see instructions on how to do that from this page too (if you don't use a package manager, don't worry about it). 

In order to make nicely formatted PDFs, you should also install a program called LaTeX, which is the gold standard of typesetting software. It's a gigantic download (multiple gigs). For Mac, you can use [MacTeX](https://tug.org/mactex/); for Windows use [MiKTeX](https://miktex.org/).  I recommend just using the full, gigantic, version of the install so that you don't ever have to worry about not having something that you turn out to need. 

Pandoc and LaTeX are both free.

### Using your shiny new software tools

Suppose you've written a Markdown file called `myfile.md`. Navigate, in the command line, to the folder it's in and type: 

`pandoc myfile.md -s -o myfile.docx`

Pandoc will convert your Markdown file to a properly formatted Word file. 

You can also do `pandoc myfile.md -s -o myfile.pdf` to get a PDF file, and the same with `myfile.html` at the end to get a web page. 

That's really it!  There are lots of other options, and I really encourage you to read Pandoc's documentation, but this is the basic process. 

For further assistance, see [Pandoc's Getting Started](https://pandoc.org/getting-started.html) page, which also includes a basic command line tutorial.

### Writing Markdown

Markdown is a very simple format.  [This web page](https://daringfireball.net/projects/markdown/basics) describes the basic version of the format and how it gets converted to HTML tags (the original purpose for which it was designed).

One thing you'll notice is that Markdown as originally specified doesn't give you a lot of features. There's no way to add tables, for example, or footnotes, or even nested lists. Fortunately, there are a variety of extended versions of Markdown floating around.  I use [Pandoc's own version of Markdown](https://pandoc.org/MANUAL.html#pandocs-markdown), which is much more complex than the original but also much more powerful; you can just use that in a Markdown file in place of original Markdown and Pandoc will seamlessly handle it. Pandoc's Markdown gives you nested lists, footnotes, tables, smallcaps (always nice for law review articles) and numerous other fancy things.  But you should start with reading the original description of Markdown; it might be enough for you.

## Markdown with Word

Another piece of the secret sauce for efficient document generation is to use Markdown *in conjunction with* Word.  Pandoc's built-in Word template uses styles to carry out all its formatting---just like [everyone keeps telling you](https://law-hawaii.libguides.com/TLC_Research_Writing/WordStyles) you're supposed to be doing. The only difference is that adding styles in a Markdown document is lots faster easier than adding them in a Word document---if you want something to be an outline, you just have to put the little dash in, if you want something to be a block quote you just have to put a `>` at the start of the paragraph, etc. 

Then, when you make your Word document, you already have styles defined for all the different semantic elements of your content---Microsoft Word already knows what chunks of text are outline items, what chunks of text are blockquotes, what chunks of text are footnotes, and so forth.  So all you need to do is edit the styles to have them look the way you want them to look, for example, making the blockquote text indented rather than italicized.  Then Word will be kind enough (assuming you know the correct clickey-clack menu incantations) to automatically change how everything else with that style looks.

This is by far the easiest way to get all the advantages of Markdown, while still having granular control over the look of your document, and without having to create or install custom templates.

## Toward the future!

One very useful thing to have for lawyers would be LaTeX and Word templates for a variety of common legal documents. For example, we could build templates for the formats required for filings in various courts, so that a final document PDF could be created without ever having to touch a Microsoft product. I will happy accept contributions for any such templates on this site; I may also try to write some myself. 

In the absence of this, it's probably still necessary for the time being to use the Markdown -> Word workflow I described above for documents with interesting formatting. However, for simple documents, such as internal memos, or to generate draft documents to be worked up by support staff, Markdown with Pandoc on its own should be sufficient. 

## Addendum: a thread reproduced from Twitter. 

In case you need some more convincing, here are my [ten theses](https://twitter.com/PaulGowder/status/1148612480920358912) for why a Markdown/Pandoc-based workflow is better than anything involving Word (largely repetitive of the above, but in a nice list for easy propaganda distribution): 

1. Performance. Even on my fast machines, word takes forever to start up and occasionally lags.  A lightweight text editor doesn't. 

2.  I can keep track of changes by putting documents in a git repository, as opposed to the slow unreadable mess of Word track changes. 

3.  I can easily edit on other devices, even an iPhone. 

4.  Pandoc's word template is fine formatting for most of my uses; LaTeX, of course, is actually good formatting unlike anything Word can produce (which is why people who produce serious documents with actual desktop publishing appearance demands do not ever use Word---they use LaTeX if they're math/science people, and Adobe InDesign if they're artsy/marketing people). 

5. As you add special features to Word documents, like citations linked in with Zotero, it gets even more slow and crash-prone.  With Markdown and Pandoc, this is plain text and you can just compile with a Zotero-generated BibTex file. 

6. Same goes for math when I use it.  In Markdown you can use LaTeX math.  I once lost an entire chapter's worth of equations in copy editing because of MS Word bugs/version incompatability. 

7. For putting together or tweaking large documents, doing them in plain text makes it much easier to automate things, like regular expression replacements. 

8. Markdown produces many other formats. For example, if I decide I want an HTML page for my document, it's easy. (And markdown processors, unlike word, do not produce shit HTML.)

9. I don't have to use lightweight text editors like Byword.  If I need really fancy stuff, I can use text editors with insane amounts of power, like Vim or Emacs.


10. Numbering and bullet points are actually predictable with Markdown syntax. It's not random shit where Word guesses as to whether you want a bullet and you have to sacrifice a goat to get it to change its mind.  More generally, you know how lawyers cling to WordPerfect because of the magical "Reveal Codes" functionality?  Well, working in a lightweight, text-based, markup language like Markdown is like having reveal codes turned on all the time, but it doesn't obstruct your ability to see the text!
