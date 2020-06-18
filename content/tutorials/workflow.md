title: My academic writing toolkit/workflow
tags: word_processing, markdown, office_tech, academic
date: 2020-06-18
author: Paul Gowder

This one is for academics rather than practitioners, though some of the details are applicable to practitioners as well. I have an unusual and complicated academic writing workflow/toolkit, but one that might be of use to some other people, so I thought I'd share it here.  This is a work in progress document; I've promised to share my toolkit with a couple people, so, as those people say to me "hey, this makes no sense," I'll probably edit to clarify. 

Here are the considerations, in rough order of priority, that drive me: 

1.  I like to have lots and lots of backups.  I'm incredibly paranoid about losing work. 

2.  I utterly loathe Microsoft Word.  I won't use it if it can be helped at all.  Yet I recognize that many people that publish things I write need Word format, so I need to do something that converts to Word fairly readily.  Subconsiderations: 
    
  A. I want something that doesn't crash or hang all the time, unlike Word. (It's utterly mind-blowing how badly Word performs.  I have a brand new souped up 16-inch Macbook Pro with an i9 and 32 gigs of ram. Word still takes forever to start. It takes longer to start than XCODE, which, for those of you who program, you're probably screaming in horror at the very idea.)

  B.  If I want to do something weird or automated with my content, I want to be able to do so.  My writing needs to be scriptable---I need to be able to read my writing into an ordinary programming language as a string, run code on it, and spit it back out again as a string.  This requires a plain text format. 

  C.  I also want something that doesn't impose involuntary formatting on me. Word "features" like styled paste, auto-conversion of URLS to links, bizarre dictatorial bullet point numbering, etc. etc. etc. are anathema to me. 

  D.  Most of the major alternatives to word (OpenOffice, Google Docs, Pages) are crap. 

3.  I also hate manually formatting my citations. 

4.  I like being able to relatively seamlessly switch between writing on my MacBook and on my iPad. 

5.  I want to use git for version control so that I can recover prior versions if something gets horribly screwed up. 

So my workflow has the following elements: 

1.  I write everything in markdown.  Markdown, for those who aren't familiar, is a plain text format with very lightweight markup for things like bold/italics, links, and the like.  It's readily convertible to MSWord format, as well as PDF (if you've installed LaTeX), HTML, and all kinds of more arcane things---it's very commonly used by programmers and bloggers, and I think it's by far the best way to write initial drafts.   There are different flavors of Markdown (for reasons to be described below, I use the Pandoc version), but [the basics](https://daringfireball.net/projects/markdown/basics) are very simple.  For people who are interested in Markdown, I wrote a tutorial on how to work with Markdown [here](https://techup.lawyer/why-and-how-to-use-markdown-instead-of-or-in-addition-to-word.html). Typically, for longer works (big articles, books) or multi-stage projects, I'll have multiple markdown files with different logically separated portions of text, plus files for notes, paragraphs that need to be discarded or moved to a better home, etc. etc.  

2. On the Mac, I do most of my markdown writing in [Sublime Text](https://www.sublimetext.com), which is a totally bulletproof programmer's text editor.  I use Sublime Text pretty much only for editing markdown or plain text prose---when I write code, I usually use emacs or vim---so I don't have to muck around with complicated file-type-specific settings.  There are fine alternatives for editing plain text, like [Atom](https://atom.io), [BBEdit](http://www.barebones.com/products/bbedit/index.html) (Mac-only), and [Notepad++](https://notepad-plus-plus.org) (Windows-only). But I like Sublime Text over those other alternatives because (a) it's extremely fast, stable, and lightweight (basically the opposite of Word), and (b) it has a plug-in system based in Python, which is one of my preferred programming languages---so it's very easy for me to directly program my editor.  The major downside is that it is expensive, although the developer lets you use it without paying if you can put up with periodic scolding popups. 

3.  Everything is saved to a git repository which gets to be in a private repo on GitHub.  That's a lot of technobabble, let me break that down some.  Git is a version control system---basically, it lets you say "ok, here's a point where I want to declare that this is a version of my document" (called a "commit"), and then it saves all your commits, so any time you want, you can go back to a previously declared version of the document, see the differences between the current version and that version, etc.  This system was designed for programmers, so it really only works reasonably well with plain-text formatted writing. Github is an online service that hosts git repositories---basically, a repository is a project, and you can (manually) synchronize the repository up to the cloud and then access it on another device. For more, [this introductory guide to git and GitHub is a good start](https://guides.github.com/introduction/git-handbook/). 

4.  When I want to work on my iPad (which is my main mobile writing station---an 11-inch ipad pro with the keyboard folio), I use [Working Copy](https://workingcopyapp.com), a git client for iOS that comes with its own built-in text editor that's actually pretty good.  I basically just pull (sync) the repository from Github, write in that app, and then sync it back up, then do the same on my computer when I'm writing there. 

5.  I save all my references in [Zotero](https://www.zotero.org); the only plug-in I really rely on for Zotero is [Better BiBtex](https://retorque.re/zotero-better-bibtex/).  Zotero is a reference manager that allows you to do things like click a browser plug-in button to save a source directly to one's library from something like JSTOR; I've tried them all, and Zotero is the best. Better BibTex is a plugin for Zotero that just smoothes out some of the rough edges in a text-based workflow. With Better Bibtex installed, you can [automatically export all your citations to a reference file](https://retorque.re/zotero-better-bibtex/exporting/auto/) saved in a format that Pandoc can read (see below; I recommend using CSL JSON format). Then, when you write, you add a citation to a document by putting a specially formatted "citation key" in your markdown file.  (For example, a current project of mine contains the text "Manifestly, much of the motivation for Republican legislators to enact this bill was a desire to prevent the Klan from suppressing enough Black voters in the South to forcibly elect Democrats---i.e., to protect their partisan interests [@treleaseWhiteTerrorKu1995, 388-9]."  The bit in the brackets is a citation: BetterBibtex decided that the Trelease book would have the key "treleaseWhiteTerrorKu1995," and I copied that from Zotero to my markdown file.  In the next step, that automatically turns into a real citation.)

6.  Finally, the thing that ties it all together: I use [Pandoc](https://pandoc.org) to convert my writing files to a format that won't make other people angry. Pandoc is a commandline tool that can take a markdown file (or lots of other formats) and convert into PDF (via LaTeX, which is a whole 'nother ball of wax, but with Pandoc you don't have to touch it, though you do have to install it) or Word formats (or, again, lots of others too).  It can also take the citation file produced by Zotero and Better Bibtex and fill in the citations in a format of your choice.  So, you can feed your markdown file and your citation file into Pandoc and get out a PDF with nicely formatted citations, and, incidentally, nicely formatted text, without ever having touched Microsoft Word.  Which is basically Nirvana for me.

I tend to go through a process using these tools over and over.  I'll write some markdown files.  When I think I have a draft of something, I'll convert it to PDF and open it up on my iPad for editing (using [iAnotate](https://www.iannotate.com) and the apple pencil to essentially simulate the experience of printing out a draft and marking it up).  Then I'll go back to my markdown file again and put in my edits.  And so on, and so forth. 

For more complicated, larger, projects (long articles, books), I'll often involve [Scrivener](https://www.literatureandlatte.com/scrivener/overview) into this process.  I don't write in Scrivener (though lots of people do, and seem to do so happily).  Rather, I find that every large project tends to get into a messy, tangled, downright gnarly state where I have like a dozen markdown files with different parts of the text, and I'm no longer clear in my own head on what the best organization is.  When that happens to me, I'll start a new Scrivener project, import all the writing files directly in there, and then use the visual splitting, merging, and reorganization functions that Scrivener is famous for to reorganize the text as a whole.  Then I'll dump the whole thing right back out into one big markdown file, and go right back to Sublime Text to keep working from there. 

This system isn't perfect.  It has the following rough edges: 

- Zotero doesn't really work on iPad.  There's a zotero client for iOS called [Papership](http://www.papershipapp.com), but it's unreliable and has crap features; I haven't figured out any way to actually add sources to my library from within it or even get Better Bibtex citations out.  Don't waste your money. There's also a zotero webapp, but I can barely get it to do anything on mobile Safari; I don't know whether this is because of content blockers or just because it sucks, but it's almost totally unusable.  What this means is that when I want to cite something while writing on iPad, I typically end up putting an inline note to cite it the next time I'm on the computer; when I want to add a source to my Zotero library from iPad I usually just dump it into a designated dropbox folder, again, to handle the next time I'm in front of the computer.  This sucks, but every other alternative is worse; one day I want to write my own damn Zotero client for iOS to do it all (but heaven only knows where the time for that would come from).

- Being git-first means that I don't get manual synchronization, like I would if I stored my work in an iCloud or a Dropbox folder (not OneDrive or Google Drive.  Never OneDrive or Google Grive.  Neither of those works reliably. Gdrive is at least semi reliable.  As for OneDrive, I'd propose that every hard drive containing any of its source code should be set on fire and then launched into space, except judging by Microsoft's record for doing harm to the world it would turn out that aliens would discover it, recover the code, and be so horrified by what they see that they'd exterminate humanity---and really, that would be nothing less than we deserve for buying Microsoft products). I have to remember to manually pull every time I switch devices, and push every time I'm done with a session of working (as well as periodically while working in case something crashes). This is annoying.  In principle, I could automate the macos side of this, though it might be a bit complicated to get the timing of automated push/pulls right. But I can put up with manual; with practice I've gotten pretty good at remembering to do it, and it's not all that hard to fix merge conflicts if I screw something up. Git is reputed to not play nicely with Dropbox, so I can't just store my git repository in a Dropbox folder (although I do have some [jury-rigged tools](https://github.com/paultopia/writingBackup) to back my writing up to them.)

-  My workflow only works until someone else touches a document.  Once I submit to a publisher, or send a draft to a co-author when I use one, it inevitably has to be in MS Word, and then I'm back in the hellpit.  Oh well.  

The technical details of how I set everything up, plus an example github repository that contains a skeleton project, forthcoming. In the meantime, see [Kieran Healy's website](https://plain-text.co): Healy uses many (though not all) of the same tools I do, and has dived into much more detail on them.