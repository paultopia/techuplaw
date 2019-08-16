title: Don't lose your clients' data to hackers (basic information security for lawyers)
tags: office_tech, security, malpractice_traps
date: 2019-07-21
author: Paul Gowder

This is an adaptation of an ethics CLE that I presented at the University of Iowa on October 19, 2018. The idea is to arm lawyers, particularly small-firm and solo practitioners (with limited resources) on a few basic security improvements and ways to think about security in order to protect client data. At the end of this (long) post, you'll find references to far more comprehensive resources.

I am not a security professional, though I did run the materials for the CLE presentation by one or two people who are in order to make sure that there wasn't anything totally confused in there. So you shouldn't treat this as professional advice, and you really should consult a professional (as usual, all information in here is very much offered without warranty, you assume the risks associated with following advice here). Moreover, this is not meant for people who already have some security practices implemented and are looking to take themselves to the next level--this is more intended for lawyers who have never thought about information security and are looking for a few basics. 

With those caveats in hand, let's begin. 

## I only have a minute, just tell me some things I can do? 

If you want a menu of quick security improvements to make it less likely that someone will make off with your client information or trust account, start with the following three basic and minimal techniques: 

1.  Use a password manager, and let it generate unique, random passwords for everything.  

2.  Keep your operating system and other software updated. 

3.  Train everyone who works for you to use a designated contact to independently verify any request for client information or funds transfer that they receive over phone, email, or text---and not to trust that identities on phone, email, and text are what they say they are.

All of those steps, as well as much more, are described below. 

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
    - This is a good spot to talk about backups. They also prevent catastrophe from things like hard drive failures or natural disasters.  You should have at least one local backup hard drive and one offsite, like a cloud backup. 
        - Cloud backup providers: Backblaze, SpiderOak, Carbonite. Dropbox can also be a backup solution (and similar enterprise services by other companies)


- Second, let your operating system help you prevent malware. When possible, rely on software downloaded, for example, from the Mac App Store (or the equivalent in your operating system) rather than from less trusted sources. That sort of thing isn't a panacea, but at least big company run app stores have some screening as well as identity registration for programmers. (The Mac App Store is particularly good, because there are also specific technical restrictions imposed on getting access to it, such as "sandboxing" which limits the access to your data that an application can get.  Also, Macs have other security features, like only allowing code signed by a registered developer---leave those turned on.)

    - Also, listen to warnings---if an application generates a popup asking for permission to do something that sounds weird, like "control your computer"---don't just mindlessly click yes!  The same goes for browser security warnings, by the way. 

- Antivirus programs are controversial: many are garbage, some are malware themselves (one common attack is to generate a popup saying that you have an infection and prompt you to install some "antivirus" program that isn't).  
    - For Windows, Microsoft provides one of its own, called "Windows Defender."  That's probably your best bet.
    - For Macs, big corporate IT departments seem to recommend Sophos a lot. 

### Routers and Other Network Setups

Networking tends to be a major security hole in general. If someone has access to your network, they can sit around and listen to any unencrypted data you send or receive. (That's very bad.)

- Learn how to change the administrator password and update the firmware for the router you use for your office/home networking, and do it!

- Have separate networks for staff and for visitors, and don't let any client data touch the visitor network. 

    - For that matter, don't let employees' personal devices touch the staff network. They can use the visitor network; anything that touches client data or that touches any network that touches client data should be a centrally managed device (i.e., you know and can control what software is installed) that you own.

- Don't use public WiFi for anything sensitive. Anyone else connected to the access point can just listen to all unencrypted data you send. Turn off the WiFi when you go to the airport.
    - Some people recommend using VPN services, but there's a debate about whether they really make it any safer. The idea is that encrypt all the data, which gets sent to the VPN, and then passed along to destination, so local network never sees unencrypted data. Unfortunately, that means you have to trust the VPN provider. Still, any of the major companies are likely much better than some random airport wifi. Big organizations often offer a corporate VPN for these purposes.)
    - Tor is a more complicated system for concealing internet traffic from snoopers; it’s 
probably not necessary for ordinary threats, and if you’re thinking about using it, you probably should talk to a pro.

- Browser security hygiene: *https* means encrypted connections to websites so that passwords and such can’t be intercepted. *http* is not encrypted.
    - Modern browsers are nice enough to warn you when you’re not on an encrypted connection; pay attention to these warnings. And look for the nice padlock and such.  
    - The EFF [kindly provides a browser extension](https://www.eff.org/https-everywhere) to force encrypted connections where possible

- Don't let anything connect to your internal network unless you need it.  Do you need that WiFi connected coffeemaker?  Do you really want to take on the burden of any holes it may introduce?

### Obsolete Software

**UPDATE ALL YOUR SOFTWARE!** Yes, Windows updates are super annoying.  Run them anyway!  New security vulnerabilities are discovered all the time, and when they are discovered, they tend to propagate fairly quickly: if you don't update, suddenly you're running software with a known hole in it. 

*Real-world dire example*: On some reports, the Panama Papers hack was potentially facilitated [because of obsolete versions of the popular website authoring software, WordPress and Drupal](https://www.theregister.co.uk/2016/04/07/panama_papers_unpatched_wordpress_drupal/), which didn't have important security patches.  

Operating system security updates are probably the most important, but any software you use is important. Vulnerabilities in other software can give attackers the power to run their own commands on your system, which is very bad. Other particularly high-priority updates include Microsoft Office, web browsers, anything providing a client-facing service (like WordPress). But really, update everything.

A quick conceptual note.  There are roughly three different kinds of update in the world: 

- *Security updates* or *security patches* are updates to a given version of an operating system (like to Microsoft Word 314.15), where the update doesn't change the version number of the product. These should be free (if they're not, you really shouldn't do business with that vendor), and sometimes are installed automatically if you have your software's auto-update feature turned on.

- *Minor version updates* or patches are updates to the general functionality of an existing product, that usually don't change the branding or major usage of a product, and are often accompanied by a change in version numbers after a period --- for example, from iOS version 12.3 to 12.4.  Sometimes minor version updates also include security updates, and sometimes you can't get security updates separate from minor version updates (like in iOS). These are usually free, and sometimes are installed automatically if you have your software's auto-update feature turned on.  Usually, the further to the right a digit is in the update, the "smaller" the update will be, i.e., 12.3.1 is a much smaller update than 12.4.

- *Major version updates* are big revisions to a product. For example, the change from Office 2016 to Office 365, or Windows 8 to Windows 10.  These often are accompanied by a branding change, sometimes (Microsoft) involve paying more money and sometimes (Apple) don't. Usually this involved a number change to the left of the period (with the exception of MacOS, which has moved major versions with 10.1, 10.2, 10.3 etc. for years and years). Effectively, a major version update is a whole new product, and might involve a radical change in functionality or user interface.

You should *always* apply security updates right away.  You should *usually* apply minor version updates right away, depending on whether they include security updates or whether those come separately---sometimes it might be reasonable to let it wait a little bit to make sure they don't break your machine. You have a bit more discretion in terms of major updates.

Old major versions of operating systems usually get security updates, so you don't have to buy a whole new version of Windows every year; the same applies to old versions of Word etc.  But this is limited: at a certain point, the companies will announce "end of life" or "end of support," and the software will be officially obsolete; at that point it won't get security updates and will officially be dangerous to use. For example, [Windows 7 reaches end of support on January 14, 2020](https://www.microsoft.com/en-us/microsoft-365/windows/end-of-windows-7-support).  If you're using Windows 7 after that, you're asking for trouble. 

- Here's [Microsoft's end-of-support hub](https://support.microsoft.com/en-gb/hub/4095338/microsoft-lifecycle-policy) which points you to information about updates for specific processes. Apple tends to be a bit more aggressive about demanding you update operating system versions to get the latest security updates and such, but apple operating systems are free, so fair enough.

*Commentary interlude:* [Iowa Ethics Opinion 14-01](https://www.iowabar.org/group/Ethics) has decided that Iowa lawyers are under an obligation to "engage in a due diligence process" to determine what to do about end-of-life for operating systems, but aren't specifically required to update. This seems too weak to me, and the bar is going to regret it when some idiot who is still using Windows 95 gets hacked.

Also, hardware sometimes reaches end of life and then won't be compatible with new operating systems. At a certain point, I'm afraid you have to shell out for new laptops. Sorry. 

### The Special Problem of Android

Frankly, I wouldn't let most Android phones touch any sensitive data.  Maybe the Google-made one (the Pixel), maybe. Several reasons: 

- Manufacturers are responsible for OS updates, and in many cases they don’t bother. (That's why the Pixel is probably the least horrible, as we can probably expect Google's own Android phone to get updates.)

- Android is less strict about user data control than iOS; a number of applications have been caught leaking data all over the place.

-  Some of the manufacturers are shady (the U.S. intelligence community has actually recommended against using some Chinese-manufactured phones, for e.g., because of worries about spying).

## Passwords and Login Codes

The reality is that passwords get leaked. Lots of companies do dumb things with encryption, and so it's inevitable that, for example, that company that asked you to make an account to buy discount pet food or something is going to lose its password database, and then there'll be a spreadsheet floating around with your e-mail and password for that site. This will happen, you can't avoid it.  (If you want to see what's been leaked, [haveibeenpwned](https://haveibeenpwned.com) is pretty good at tracking many of these breaches. 

- Incidentally, this is why [people have started trying to con suckers](https://www.theguardian.com/technology/askjack/2019/jan/17/phishing-email-blackmail-sextortion-webcam) with "blackmail spam," e-mails where they send you one of your passwords to prove they know it, and then claim they've hacked your computer and have videos of you watching really nasty porn, so send money.  Crooks just grab leaked passwords from these datasets and use them to try to social engineer people into believing they've been hacked. 

    - That being said, it's probably a good idea to cover webcam cameras when you're not actively using them. Can't hurt, better safe than sorry.

So if your passwords are going to get leaked, what do you do?  Easy.

**1.  NEVER NEVER EVER NEVER EVER REUSE PASSWORDS.** (And obviously, if you learn that a service you use has been breached, change your password there.)

**2.  USE LONG, RANDOM PASSWORDS.** AKA "strong" passwords.

"Ok Gowder, how do I remember all the passwords I use?  And how do I type them in reliably? And how do I know if the password I've made is good?"  The answer is: 

**3.  USE A PASSWORD MANAGER.**

A good password manager should: 

1.  Securely save all your passwords, relieving you of the obligation to remember them (except for the one password that protects your password manager).

2.  Auto-fill those passwords at least sometimes, so you don't have to type them in.

3.  Generate strong passwords for you.

If you have to pick one thing to do to make your security much stronger, and incidentally make life easier as well (the one security improvement that actually makes life *more* convenient), get a password manager, and also require your employees to use one. 

Popular password managers include [LastPass](https://www.lastpass.com/), [1Password](https://1password.com), and  [Dashlane](https://www.dashlane.com).  If you're embedded in the Apple ecosystem, you can also just use [Apple's built-in solution](https://support.apple.com/en-gb/HT204085). Wired Magazine has a [writeup of good password manager options](https://www.wired.com/story/best-password-managers/).

Using a password manager is the bare minimum of computer security. In my opinion, it’s flat-out negligent to store client data anywhere with a reused password. 

- Your password manager will need a master password; that one you need to memorize. [Here’s a good guide for picking one](https://support.1password.com/strong-master-password/).

- Your password manager, when it generates random passwords for you, will ask you how long and how many types of characters. Make it long and use lots of types of characters. You usually won’t have to type it.
    - Most password managers have browser extensions that just insert it into the web form you, also mobile apps with similar functionality.
    - 20 characters is a good number.
- When you get your password manager, change all your passwords. Once your existing passwords are in there, some password managers have a function to automatically change many of them for you.

- Some companies still ask you to answer password recovery questions like "what was the make of your first car" when you sign up for an account. That sort of thing is a big security hole (how hard would it be for a social engineer to find out? Not very.), so many people give them fake information and treat that like another password, to be randomly generated and stored in the password manager.

After a password manager, there's one other easy step that's really important: 

**4.  TURN ON TWO-FACTOR AUTHENTICATION WHEREVER POSSIBLE**

The idea of two-factor authentication is that you can tell a service to not just demand a password ("*something you know*) but also for you to prove your identity by giving them information associated with *something you have*. That way, if your password is compromised, there's still another layer of defense. 

There are roughly three different kinds of 2-factor authentication. 

- Text messages. This is where you give a service your phone number, and they text you a code that you use to login after you enter your password.  This is better than nothing, but it's generally considered *not as secure as the other options*, because it depends on the security of your phone number.  And it turns out that phone companies are notoriously susceptible to social engineering, and many people have been victimized by [SIM-Jacking](https://www.vice.com/en_us/article/5984zn/listen-to-sim-jacking-account-ransom-instagram-email-tmobile), where they get the phone company to transfer your number to a SIM card they control. Then they can receive your texts (and also generate password resets and such)---it's really bad. 
    - Incidentally, one thing to do to help with this risk is to [get a pin on your cellular account](https://www.wired.com/story/sim-swap-attack-defend-phone/). 
    
- Authentication apps.  Most companies that support 2-factor authentication will let you use an application to generate your code. Popular examples include Google Authenticator and [Authy](https://authy.com).  These applications work by using fancy cryptography math to generate time-limited codes which the server can also generate, so that only the person who has your physical phone with the app can get in.  Some applications also have the ability to receive push notifications; one common enterprise solution is [Duo](https://duo.com/). Some companies also generate their own authentication codes for their own apps, for example, by letting you use one device to authenticate another (Facebook, Apple) or have special authenticators to download (Microsoft).

- Physical devices that you attach to your keychain and plug into a machine to generate a code (or just leave in a USB port on your computer). The most popular is the [Yubikey](https://www.yubico.com), though Google [just rolled one out too](https://cloud.google.com/titan-security-key/). 

The EFF has a [great explainer on two-factor authentication](https://www.eff.org/deeplinks/2016/12/12-days-2fa-how-enable-two-factor-authentication-your-online-accounts). 

[explain]

## Security as a practice management problem

You're ethically obliged to manage your staff to protect client data and property; this means training your staff in security and supervising them to ensure sound practices.  Here are some strategies: 

- No personal accounts (email etc.) touch client information, only the enterprise-level firm e-mail account that you're paying a nice big and competent company to run. 

- Require employees to use 2-factor authentication to access anything that has client information).

- Make sure any device that touches client information is managed by you (i.e., a firm device) and updated (both operating system and 3rd party applications). Don’t allow employees to touch client information with personal devices

- If you have high security needs (if your threat model involves corporate spies or governments, for example), pay for professional staff training and testing.     - There are "red team" or "pentesting" companies that will try to exploit staff weaknesses (+ network, physical weaknesses), and then report to you on what they managed to do.

- Physical security matters. Require staff to lock computers when they leave the desk, ask unknown people lurking around workspaces if they need help, refrain from discussing client business in public, etc.

- Don’t give staff access to client information they don’t need.

- Do not share user accounts on firm computers, networks. Every employee has their own account, with central IT capacity to limit access to sensitive resources and revoke access on termination.

### But don't overburden your employees

If you impose unnecessary demands on your employees, they are more likely to just ignore it, to suffer from security fatigue and just click "yes" on everything, etc.  Be sure that you prioritize security rules on the basis of your threat model. 

In particular, avoid *security theater*. [According to security expert Bruce Schneier](https://www.schneier.com/blog/archives/2009/11/beyond_security.html): 

> Security theater refers to security measures that make people feel more secure without doing anything to actually improve their security. An example: the photo ID checks that have sprung up in office buildings. No-one has ever explained why verifying that someone has a photo ID provides any actual security, but it looks like security to have a uniformed guard-for-hire looking at ID cards.

A common IT example are rules requiring that passwords be changed on a fixed schedule. There [isn't any evidence that this actually improves security](https://www.sans.org/security-awareness-training/blog/time-password-expiration-die), and certainly not compared to things like using unique passwords in a password manager and maintaining the central control to revoke access if there's a breach. It's probably harmful, because it encourages people to be lazy and stick their ever-changing password on a post-it note by the computer. (The same is true of arbitrary password complexity rules like "has to have one capital letter, one lower case letter, one symbol," blah blah.  Just require use of a password manager that actually has the capacity to generate good random long passwords.)

### Have someone in charge.

- Who is responsible for making sure all software is updated?
- Who will employees call if their firm laptop is stolen? 
- Make sure you have the capacity to revoke any privileges it has and remotely wipe it if it connects to the internet. IT vendors can help with this.
- If employees have access to firm data on their personal devices, you need to know about it, and make sure they let you know if that’s lost/stolen too.
- Who will employees call to verify sensitive requests (like money 
transfers?) 
    - There needs to be a clear point of contact and clear responsibility for security

## A few more pieces 

- What happens if you lose your laptop, or your phone?  Both Windows and Mac have a full-disk encryption product built in; it's called BitLocker in Windows and FileVault in Mac. It will encrypt your hard drive when the computer is off, and is pretty much costless (if you have a slow hard drive it might make startup take a few extra seconds). On your phone, use a passcode and have it automatically lock very quickly. (If you're worried about the government, there's conflicting opinion on whether the compelled use of FaceID or TouchID as opposed to a passcode is problematic under the 5th Amendment.)

- What about borders?  Governments (including ours) claim the right to search electronic devices carried across international borders. Ours is bad, but other countries are even worse.  Some countries have been known to demand passwords to cloud accounts at the border, for example. 
    -  If you have extremely sensitive information on your device (you’re a human rights lawyer suing that country, for example), it’s probably a good idea to do things like bring a burner device, use 2factor authentication tied to a second factor left at home to disable yourself from accessing sensitive accounts, etc. There's a [Wired Magazine article with some strategies](https://www.wired.com/2017/02/guide-getting-past-customs-digital-privacy-intact/).
    
- In terms of ordinary messaging, probably the most secure application is [Signal](https://signal.org). It's written by dedicated security people to encrypt as much as possible. WhatsApp, Telegram and the built in iOS iMessage are all more secure than ordinary SMS or e-mail as well, because they too use "end-to-end encryption."  E-mail is very hard to secure; there are companies that offer encrypted e-mail (like ProtonMail), but it's still not terribly clear how secure it is---it's probably safest to assume that e-mail is not for very sensitive information. 
    - Remember that Signal and similar apps can’t protect you against people who voluntarily share messages they can see (social engineering, etc.)---they’re just decent anti-hacking protections.

- It's generally a very good idea to outsource as much as possible of your sensitive IT to pros.  This is what "enterprise" software is *for*.  Gigantic companies like Microsoft and Google will happily take your money to run all your firm's e-mail, file-sharing, calendaring, etc. etc. in the cloud, and they can do it much better than you can (probably cheaper too). 
    - Remember the Panama Papers case again. Apparently that firm [was running its own website where clients could upload sensitive documents](https://www.wired.co.uk/article/panama-papers-mossack-fonseca-website-security-problems). That is incredibly stupid. Don't do that. Pay someone who knows what they're doing. 


Be careful with browser autofill, there have been exploits published recently where people 
have gotten browser autofill to leak all kinds of sensitive data to hidden form fields.
• Firewalls control network access to/from machines. Beyond my expertise, but it’s worth 
consulting with an IT person.
• Paper is still a thing to protect. Criminals still go through trash cans, so shredding is still a 
thing to do.
• Secure deletion of data: before you let any physical storage device go out of the building 
(e.g., junking old devices), make sure that deleted files are really deleted. This is much 
harder (possibly impossible) on SSDs than on HDDs.
• Don’t let people hover by your shoulder when you type your password in.
• Never access sensitive sites/type passwords/etc. on public kiosks, like hotel computers. 
They can be full of keyloggers and other horribleness.

P2P file sharing (torrents etc.) can be full of malware; don’t let anything that has touched it 
also touch your network/client data.
• Have a separate "guest" wifi network at your office, don’t let nonemployees onto the same 
network that your staff uses.
• Don’t abandon domain names; even if your firm changes name or winds up keep paying 
the registration on the old one. Otherwise malicious actors can take them over. What 
happens if a former client sends confidential information to an e-mail there?
• Don’t install unnecessary software, even things like browser extensions can introduce 
security holes. Keep it lean.
• Minimize use of Internet of Things devices (smart thermostats, lightbulbs, etc.), they tend 
to have terrible security vulnerabilities. Don’t let them on a network that also sees client 
data. 



## Further Reading

- [ABA Techreport 2018 on Cybersecurity](https://www.americanbar.org/groups/law_practice/publications/techreport/ABATECHREPORT2018/2018Cybersecurity/)
- [Citizen Lab's Security Planner](https://securityplanner.org/#/)
- [EFF on Surveillance Self-Defense](https://ssd.eff.org)

UC Berkeley has several good guides, including: 
• International travel: https://security.berkeley.edu/resources/best-practices-
how-articles/international-travel/security-tips-international-travel
• Phishing: https://security.berkeley.edu/resources/phishing
• A company called PagerDuty put (most of) the security trainings it 
gives its employees online: https://sudo.pagerduty.com

Frontline Defenders (a human rights group), Workbook on Security: 
https://www.frontlinedefenders.org/en/resource-
publication/workbook-security-practical-steps-human-rights-
defenders-risk (Mostly focused on physical security, but has a ton of 
material about threat assessment.)
• Belfer Center (Harvard) cybersecurity playbook for political 
campaigns: https://www.belfercenter.org/CyberPlaybook
• TechSolidarity security guide: 
https://techsolidarity.org/resources/basic_security.htm

The ABA law practice division sells a book called "Locked Down: 
Practical Information Security for Lawyers." I highly recommend it.
• Two recent ABA formal ethics opinions (this is an ethics CLE, after all): 
• Formal opinion 477, May 11 2017: the ABA’s take on the lawyer’s ethical 
obligation to use sound security principles to protect confidential information.
• Formal opinion 483, October 17, 2018: lawyer’s ethical obligations after a 
data breach to inform clients and mitigate consequences.

Get these slides: http://paul-gowder.com/infosec.pdf

