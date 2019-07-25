title: Don't lose your clients' data to hackers (basic information security for lawyers)
tags: office_tech, security, malpractice_traps
date: 2019-07-21
author: Paul Gowder

This is an adaptation of an ethics CLE that I presented at the University of Iowa on October 19, 2018. The idea is to arm lawyers, particularly small-firm and solo practitioners (with limited resources) on a few basic security improvements and ways to think about security in order to protect client data. At the end of this (long) post, you'll find references to far more comprehensive resources.

I am not a security professional, though I did run the materials for the CLE presentation by one or two people who are in order to make sure that there wasn't anything totally confused in there. So you shouldn't treat this as professional advice, and you really should consult a professional (as usual, all information in here is very much offered without warranty, you assume the risks associated with following advice here). Moreover, this is not meant for people who already have some security practices implemented and are looking to take themselves to the next level--this is more intended for lawyers who have never thought about information security and are looking for a few basics. 

With those caveats in hand, let's begin. 

## Why should I, a lawyer, worry about information security? 

First of all, **you have a duty to do so**. It's widely recognized that the ethical duty of competence includes a duty to be technologically competent. In the words of the [comment to ABA Model Rule 1.1](https://www.americanbar.org/groups/professional_responsibility/publications/model_rules_of_professional_conduct/rule_1_1_competence/comment_on_rule_1_1/): 

> To maintain the requisite knowledge and skill, a lawyer should keep abreast of changes in the law and its practice, including the benefits and risks associated with relevant technology...

and in the words of [Model Rule 1.6](https://www.americanbar.org/groups/professional_responsibility/publications/model_rules_of_professional_conduct/rule_1_6_confidentiality_of_information/):

> A lawyer shall make reasonable efforts to prevent the inadvertent or unauthorized disclosure of, or unauthorized access to, information relating to the representation of a client.

Moreover, negligence in information security could potentially compromise the attorney-client privilege. See [FRE 502(b)(2)](https://www.law.cornell.edu/rules/fre/rule_502) (inadvertently disclosed information still protected by privilege *if "the holder of the privilege or protection took reasonable steps to prevent disclosure"*). 

In addition, information security may be required by state consumer protection laws, in jurisdictions where lawyers are covered, and, obviously, there's also a serious risk of malpractice liability. 

Second, **lawyers are increasingly targets of data breach efforts**. In an ABA survey, [23% of respondents](https://www.americanbar.org/groups/law_practice/publications/techreport/ABATECHREPORT2018/2018Cybersecurity/) said they'd had a data breach. 

Some of those breaches have been successful and huge. Here are some prominent examples (and see [this ABA Journal article](http://www.abajournal.com/magazine/article/law_firm_hacking_history) for more): 

- [In 2016](https://www.reuters.com/article/us-cyber-insidertrading-idUSKBN14G1D5), hackers got into the files of (apparently) Cravath and Weil Gotshal to get information about impending mergers, which they used to make millions of dollars in insider trading. 

- [In 2017](https://casetext.com/case/oneill-bragg-staffin-pc-v-bank-of-am-corp), hackers got into the e-mail account of a partner in a Pennsylvania law firm and used that access to convince another partner to transfer them half a million dollars from the client trust account. 

- [In 2016](https://canadianlawyermag.com/author/marg-bruineman/phishing-for-victims-17392/) Dentons Canada was phished into sending away 2.5 million dollars from the client trust account. 

- [In 2013](http://www.abajournal.com/news/article/hacker_steals_large_6-figure_sum_from_law_firm_trust_account_using_trojan_b) the bookkeeper for a Canadian law firm was fooled by a spoofed online banking page and the firm had “a large six-figure” looted.

- [In 2017](https://fortune.com/2017/06/29/dla-piper-cyber-attack/), DLA Piper suffered a malware attack that led to their entire IT operation being shut down---producing stuff like this: 

![DLA Chaos]({static}../images/dla.jpeg)

([source](https://twitter.com/ericgeller/status/879738598244835328?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E879738598244835328&ref_url=https%3A%2F%2Ffortune.com%2F2017%2F06%2F29%2Fdla-piper-cyber-attack%2F))

Probably the most prominent and destructive law firm security breach, however, was the Panama Papers. Remember that? [A Panamanian law firm lost 11.5 million documents](https://www.theguardian.com/news/2016/apr/03/what-you-need-to-know-about-the-panama-papers) which included offshore account information for numerous crooked political leaders, which led to numerous [ongoing criminal investigations](https://www.icij.org/investigations/panama-papers/what-happened-after-the-panama-papers/), as well as firings, resignations, etc., and [caused the law firm to shut down](https://www.theguardian.com/world/2018/mar/14/mossack-fonseca-shut-down-panama-papers). 


## Threat Modeling and Preparation

The first step in any security checkup should be **threat modeling**.  The basic idea of threat modeling is *figure out what the risks are in judging what kind of measures you have to take*.  This is also the advice the ABA gives in [the comments to Model Rule 1.6](https://www.americanbar.org/groups/professional_responsibility/publications/model_rules_of_professional_conduct/rule_1_6_confidentiality_of_information/comment_on_rule_1_6/): 

> Factors to be considered in determining the reasonableness of the lawyer’s efforts include, but are not limited to, the sensitivity of the information, the likelihood of disclosure if additional safeguards are not employed, the cost of employing additional safeguards, the difficulty of implementing the safeguards, and the extent to which the safeguards adversely affect the lawyer’s ability to represent clients (e.g., by making a device or important piece of software excessively difficult to use).

One helpful way to think about threat modeling is as a function of two characteristics of your practice: 

1.  *What could attackers have to gain if they breached your data?*  (And, tracking that, what do you have to lose?)  For example, do you have a lot of sensitive information, like corporate financials right before a merger?  Do you typically hold a lot of money in your client trust account, so someone could get a big windfall by phishing your accountant? Do you represent clients who are involved in big social or political controversies who might be targets? How high are the stakes you're playing with? 

2.  *How well-resourced are potential attackers?*  (Do they have a lot of money, technical capacity, or, as with governments, legal privileges?)  Are you or your clients involved in international politics, where you might have the unwanted attention of nasty governments?  Are your clients involved in an industry where there's a lot of corporate espionage? 

Thus, we can imagine a two-dimensional spectrum of threats. On the upper-right, maybe you represent Russian dissidents, or Chelsea Manning, or Joe Biden, or a gigantic publicly traded company about to do a stock split. In which case, get off this website right now and hire an army of the best security professionals in the business and do exactly what they say, money is no object, because, come the fuck on, you're facing a state-level adversary here and you really shouldn't be listening to me. 

On the lower-left, say, you have a criminal defense practice where the criminals aren't rich or famous or political---you're defending people against drug charges, and murder charges, and the like. Blessedly, it's probably reasonable to assume that the DA's office won't be trying to read your e-mail. (I hope... maybe this is too optimistic? Anyway, you know the threats you face better than I do.) It might be reasonable to spend a little bit less time and money stressing about security, and to focus your effort and expense on protections that are more closely directed toward threats you're most likely to face.  Still, you should probably do most of what's in this guide, because it's all pretty easy and cheap---at least grab the low-hanging security fruit. 

Another great thing about threat modeling is that it helps you understand the specific stuff you have to lose, and then you can plan for what happens if you lose it.  What will do you if there's an e-mail breach?  Is there a plan you can pull off the shelf and implement immediately to mitigate your losses, and the losses to your clients?  You don't want to be trying to figure this stuff off when the crisis is happening. 

Ok, with that preliminary out of the way, let's cover the two broad categories of vulnerability: human and technical. 

## Human Vulnerability

Human psychology---your own, and that of your staff---is a big threat to your and your clients' information and money. The urge to respond hastily to manufactured urgency, to be polite and not treat people as suspicious, to follow the orders of apparent authority---these are all qualities that attackers can exploit.

A lot of real-world data breaches happen not because someone found a hole in your e-mail server, but because someone convinced your associate, or your paralegal, or you, that they were the client's vice president and you need to send them the financial documents at this e-mail right now, hurry, crisis! That is, [they happen because of human vulnerabilities rather than because of computer vulnerabilities](http://smbc-comics.com/comic/2012-02-20), or, in infosec person lingo, "[social engineering](https://www.amazon.com/Art-Deception-Controlling-Element-Security/dp/076454280X)".

The ABA is on the case of this one too. See comment 18 to rule 1.6: 

> “safeguard information... against inadvertent or unauthorized disclosure by the lawyer or other persons who are participating in the representation of the client or who are under the lawyer’s supervision.”

If you follow the security world at all, you'll never cease to be shocked by how many seemingly obvious mistakes people make. For example, would you send a two-factor authentication text message that you received (more on this below) to a random stranger? [Some people will](https://twitter.com/RachelTobac/status/996556819886583808).  Would you plug a random USB drive that you find on the street into your computer? [Some people will](https://www.theregister.co.uk/2016/04/11/half_plug_in_found_drives/). 

Familiar examples of security problems that rely on human vulnerability include: 

- The fake log-in page. Someone sends a phishing e-mail purporting to be from, say, Google, or Facebook, or your bank, asking you to log into the site to carry out some task. You click the link, and your credentials are stolen. This is [how the Russians got a bunch of e-mails](https://www.apnews.com/dea73efc01594839957c3c9a6c962b8a) in the 2016 election.

    - The standard advice people give for mitigating this threat is to make sure that you go directly to websites, i.e., by typing the address into the browser. 
    - On the telephone, if people from some company call asking for any information, call them back at some number you know/find independently.
    - Also: hover the mouse over links, don’t go to them if they look suspicious (including URL shortener links like bit.ly), and be careful with common typo tricks, like .co domains instead of .com, similar- appearing typoes.

Here is a chart of common deceptive URL forms, which I have swiped from [So Long, And No Thanks for the Externalities: The Rational Rejection of Security Advice by Users](https://www.microsoft.com/en-us/research/publication/so-long-and-no-thanks-for-the-externalities-the-rational-rejection-of-security-advice-by-users/), by Cormac Herley of Microsoft Research (so, obviously, copyright on that image is Herley's/Microsoft's, and I'm using it under a fair use claim).

![Deceptive URLs]({static}../images/urls.png)

- The malicious attachment (or, in some cases, the malicious web page) that, when clicked on, runs dangerous code. Most people know about threats like Microsoft Office macros, but did you know that even [PDFs can carry malware?](https://www.sophos.com/en-us/security-news-trends/security-trends/the-rise-of-document-based-malware.aspx).  Also, suspicious file types can have file names/extensions suggesting that they're innocent.

    - In general, the best practice is probably to avoid e-mail attachments anyway. 
        - When possible, prefer sharing information in ordinary e-mail text rather than attachments. 
        - For internal file sharing, you can use a good enterprise quality file-sharing service from a company like Dropbox, Microsoft, or Google. 
        - For files from clients, you should probably pay someone to provide a secure upload portal. (Suggestions for legal tech vendors would be welcome here...) 
    - If you MUST use attachments: 
        - Turn on your operating system’s ability to see extensions, and watch out for double extensions (like .pdf.exe). 
        - Never allow an e-mail attachment to run macros or any other code that MS Word etc. might prompt you to run. 
        - Take advantage of attachment screening and preview functionality in webmail applications. For example, Outlook in Office 365 online will let you preview attachment contents without downloading to your computer.


- The "urgent" e-mail from a trusted person, like a boss, asking for sensitive information or to carry out sensitive actions. *Do your office staff know what to do if they get an e-mail from "you" asking them to send confidential client information?*

    - A common recommendation to mitigate this threat is to directly reach out to the supposed sender by a known and trusted contact method (i.e., call the boss before sending the contents of the trust account). Ideally, employees should have a designated point of contact to independently reach out to in order to verify all sensitive requests. 

Sophisticated social engineering attacks can go through multiple steps, tricking people out of small bits of information at each step, and then using that information to get the next, bigger, bit of information later. 

- The first call might be to the firm's receptionist: "*This is Joe Schmoe from SensitiveCo! I need to talk to the partner in charge of our file ASAP!*" "*Ok, I’ll pass you to Laura Lawyer.*" 

- Now the attacker has verified the identity of the client (which might have been confidential) and gotten the name of the partner in charge. That information might be used in a second social engineering attempt. Call to paralegal in a different office: "*This is Laura Lawyer, I need the last letter from SensitiveCo faxed to this number ASAP!*"

Also, for god's sake, don't plug random devices (USB drives or anything else) into your computer or your network.. 

## Technical Vulnerability

I'll describe a few categories of standard technical vulnerability.

### Malware/Viruses/Trojans/Spyware

Hopefully following some of the advice above will reduce the surface area exposed to attack in your firm. But it can't eliminate it. Here are a couple more things that might help.

- First, ransomware attacks have been in the news a lot.  The best strategy for ransomware mitigation is to have a strong backup strategy. You should have multiple backups, in different locations (i.e., on local hard drives, remote), and they should be keeping old backups (e.g., if you run daily backups, it should have plenty of previous days stored).  Then you will hopefully be capable of restoring your whole hard drive to a time before the malware hit the machine and minimizing data loss. 

- Second, let your operating system help you prevent malware. When possible, rely on software downloaded, for example, from the Mac App Store (or the equivalent in your operating system) rather than from less trusted sources. That sort of thing isn't a panacea, but at least big company run app stores have some screening as well as identity registration for programmers. (The Mac App Store is particularly good, because there are also specific technical restrictions imposed on getting access to it, such as "sandboxing" which limits the access to your data that an application can get.  Also, Macs have other security features, like only allowing code signed by a registered developer---leave those turned on.)

    - Also, listen to warnings---if an application generates a popup asking for permission to do something that sounds weird, like "control your computer"---don't just mindlessly click yes!  The same goes for browser security warnings, by the way. 

- Antivirus programs are controversial: many are garbage, some are malware themselves (one common attack is to generate a popup saying that you have an infection and prompt you to install some "antivirus" program that isn't).  
    - For Windows, Microsoft provides one of its own, called "Windows Defender."  That's probably your best bet.
    - For Macs, big corporate IT departments seem to recommend Sophos a lot. 

### Routers and Other Network Setups

Networking tends to be a major security hole in general. If someone has access to your network, they can sit around and listen to any unencrypted data you send or receive. (That's very bad.)

- Learn how to change the administrator password and update the firmware for the router you use for your office/home networking, and do it!

- Have separate networks for staff and for visitors, and don't let any client data touch the visitor network.

- Don't use public WiFi for anything sensitive. (Some people recommend using VPN services, but there's a debate about whether they really make it any safer.)

### Obsolete Software

On some reports, the Panama Papers hack was potentially facilitated [because of obsolete versions of the popular website authoring software, WordPress and Drupal](https://www.theregister.co.uk/2016/04/07/panama_papers_unpatched_wordpress_drupal/), which didn't important security patches.


### The Special Problem of Android

Frankly, I wouldn't let most Android phones touch any sensitive data.  Maybe the Google-made one (the Pixel), maybe. Several reasons: 

- Manufacturers are responsible for OS updates, and in many cases they don’t bother. (That's why the Pixel is probably the least horrible, as we can probably expect Google's own Android phone to get updates.)

- Android is less strict about user data control than iOS; a number of applications have been caught leaking data all over the place.

-  Some of the manufacturers are shady (the U.S. intelligence community has actually recommended against using some Chinese-manufactured phones, for e.g., because of worries about spying).


## Further Reading

- [ABA Techreport 2018 on Cybersecurity](https://www.americanbar.org/groups/law_practice/publications/techreport/ABATECHREPORT2018/2018Cybersecurity/)