Title: License and How to Contribute
Date: 2019-07-09

## License Information

All textual content, images, document templates, and other content that isn't primarily intended to be executable software on this site is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/). All code and other content primarily intended to be executable software is licensed under a [MIT License](https://opensource.org/licenses/MIT). 

If there's any ambiguity as to whether some content is covered by the Creative Commons or the MIT license noted above, you are hereby granted permission to reproduce it under either license, as you may choose. Paul Gowder and all other authors who have contributed content to this site hereby disclaim all warranties with respect to the accuracy of content or the correctness or functionality of code or software distributed here; you use all material provided by this site at your own risk.

All contributing authors retain the copyright to material they contribute, and authors as well as dates of creation are listed on each contributed post. Where no author is listed, you may assume [Paul Gowder](https://gowder.io) is the author unless specified otherwise. 

This site uses the [Pelican](https://blog.getpelican.com/) static site generator (and is served with continuous integration on [Netlify](https://www.netlify.com/)). It also uses third-party plugins and themes, which appear in the Github repository. License information, where provided, is in those folders or in the Pelican static site generator website and/or Github repository; I (Paul Gowder) disclaim all copyright in modifications made to the third-party theme on this site. The Blue Penguin theme which this site uses belongs to [Jody Frankowski](https://github.com/jody-frankowski/blue-penguin). 

## Contributing

To contribute to this site, write a tutorial in [Markdown](https://daringfireball.net/projects/markdown/) format (with a name of the form `something.md`), as a post, and submit it as a pull request to the [site Github repository](https://github.com/paultopia/techuplaw). All posts should be contributed to the `content/tutorials` folder in this repository. This site uses tags, not categories, to organize content.

By contributing, you agree that any content you contribute will be available under the licenses described in the first paragraph of this page, though you will retain ownership of the copyright to that content.

In order for your post to work on this site, you'll need to add several lines to the top of your markdown file.  At a minimum, you will need to specify a post title, date, tags, and author. (If you don't include an author, it'll automatically attribute the post to me, which you probably don't want!)  When you select tags, please consult [the tags page](/tags) and endeavor where possible to use tags that correspond to existing content.

The following is an example of a minimal post which includes the header block 

```
title: How to Not Ever Use a Microsoft Product!!
tags: microsoft, things_that_suck, reveal_codes
date: 2019-12-10
author: Your Name

Buy a very old computer and get a copy of WordPerfect somehow!  Cool idea, huh, bro? 

```

If you don't know how to submit a pull request, consult [Github's documentation](https://help.github.com/en/articles/creating-a-pull-request). The basic workflow is to fork the repository, create a branch containing your pull request, and then use Github's web interface to start a pull request.  Then we can talk about it, and, if it's ready, I can merge it into the site... which should immediately publish it if I have things set up right. 

You can also add posts with dynamic (JavaScript) content!  Just add a `javascripts` tag to the metadata block of your post with the filename of your script.  HTML tags work in markdown, so you can add classes and whatnot as needed to render the content. And put your script in the `content/js` directory. For an example, see [the source of the base rate tutorial](https://raw.githubusercontent.com/paultopia/techuplaw/master/content/tutorials/base_rate.md), which points to a file called `drunk.js` in the js directory, which in turn is a chunk of React created (because I personally hate writing JavaScript) by Clojurescript and Reagent ([source](https://github.com/paultopia/bayesruleslider)).  So your tutorials can now include demos!

Over time, I plan to build in the capacity to contribute more interesting content, such as binary files, templates (LaTeX pleading templates anyone?!), etc. This page will be updated when that happens. 
