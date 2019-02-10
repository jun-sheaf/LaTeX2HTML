# LaTeX2HTML
A Customizable Python Program for Translating LaTeX to HTML

## Introduction
This program **can**:
* Translates any environment (even enumerate-types) into a fully-customizable HTML container.
* Places footnotes at the end of the document (before `\end{document}`) and hyperlinks them.
* Link references.
* Places a bibliography at the end of the document (before the footnotes) with the citations used as well as hyperlinks them.
* Translates macros into fully-customizable HTML containers/tags.

This program *cannot*:
* Convert `tikzpicture` (and its children such as `tikzcd`) to `SVG` (however, [XyJax](http://sonoisa.github.io/xyjax/xyjax.html) can be used to fully encode diagrams in MathJax).
* Compile (as opposed to [translate](https://en.oxforddictionaries.com/definition/translation)) LaTeX to HTML such as [TeX4HT](https://tug.org/tex4ht/).

### Preparing Python
The following modules are **required**:
* `tkinter`
* `regex` (not `re`)

The following modules are *optional*: 
* `bibtexparser` (for bibliographies)

### Preparing Your Site
The following javascript are **required**:
* [MathJax](https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS_HTML)

The following javascripts are recommended:
* [XyJax](http://sonoisa.github.io/xyjax/xyjax.html) (for diagrams)
  * Although `tikzcd` is not available on MathJax, `xypics` is available through XyJax.
  * [AMScd](http://docs.mathjax.org/en/latest/tex.html#amscd) can also be used (and is faster), but is limited to simple straight arrow diagrams.
* [BigFootJS](http://www.bigfootjs.com/) (for footnotes)
  * Depends on [jquery](https://code.jquery.com/jquery-3.3.1.min.js).
  * BigFootJS removes the need for a footer filled with footnotes and places them in an overlay activated by the footnote's link.

The header in the example is similar to the one I use. The scripts and css are renamed for simplicity.

### Preparing Your LaTeX Code
For footnotes:
* Place footnotes (`\footnote{sometext}`) where you would like the footnote marker to appear.
* Do **not** place your footnote in math delimiters. Use a footnote marker (`\footnotemarker`) and place your footnote text    (`\footnotetext{texthere}`).

For environments:
* All environments (except the ones parsed by MathJax such as `equation`) must be of the form
```latex
\begin{placeholder}[optional]
blah blah blah
\end{placeholder}
```

For references:
* All references should follow a pattern of `prefixnumber` or else they will have to be individually defined in the configuration.
  * It *is* possible to have all references backreference the labels without worry, however they will not be numbered properly since the program does not handle environments and labels jointly (which will not be implemented for obvious reasons). For example, say `\label{banans}` and `\label{pinans}` handle Proposition 4 and Theorem 20. If these are the only labels in the document, then referencing them will just give 1 and 2 rather than 4 and 20.

## Customizing the program
The strength of this program lies in the customizability. The `customize.ini` contains all the information about customizability options.

## Running the program
The ``RunScript.pyw`` file will launch a GUI for the program. **If you have images**, you should upload these online and paste the url in the text box (one per line) in the order they appear in your TeX document. **If you have a bibliography**, assure you have the requirements listed before and select the `.bib` file associated to it. After you choose your file, press `Run` and the freshly-dressed code should appear in the text box (replacing any URLs you may have placed there). You can edit, copy-and-paste, and save (using the ``Save`` button) however you wish. You can process multiple files without closing the window.

## Running the Example
The example is `Example.html` in the Example folder, however it may be of use to learn how to get there.

The `Example.tex` can be compiled in LaTeX to verify it works. Run the program on `Example.tex` and the provided `.bib` file and save the text as `body.html` in the Example folder. You can open the newly-created HTML file to see how raw the output is. From here, you can take the `header.html` and the created HTML file to create a single HTML file with `<header>` on top and `<body>` at the bottom. This will be the same as `Example.html`. Opening this file, you can see how drastically different the stylesheets change the code. In particular, the labeled item is now truly a labeled item (using some `position:relative` trickery). 

## Remarks

All macros and environments (except the ones used by MathJax) used in your document should be defined in the configuration file. Using classes and ids give this program an incredible amount of flexibility (e.g. the proposition environment in the example is defined the same way as the exercise environment, but differs in `css`). Enumerate especially handles well since nesting is built-in to `css` (the program does not process nesting of enumerate environments). See the `environments.css` file from the example for some inspiration.

There are a lot of methods for removing unwanted macros in this program. Not so obvious is the facts we can remove parameters in the HTML using some clever adjustments. For example, using the `enumitems` package allows for adjusting enumerate-type environments in the form `\begin{enumerate}[options]`. The `[options]` can be removed by not referencing it in replacement text. See the `customize.ini` file for some inspiration.

# Contact

You can contact me through my site [The Bracket](https://www.jeongjh.com/about-contact/). I am a starving student, so tips are incredibly welcomed: 

Paypal: [PayPal.me/jeongjh](https://www.paypal.me/jeongjh)

Crypto:
```
BTC: 19AKGxHW19Jx5PtPA55mT4jgByV6ZFmLdL
ETH: 0x5b4e8dde8d7aa983e5fb4f3a58a4cabadb66a6af
LTC: LXcyKsHqLiYbEcgjKCTKUTwh52WfWgfqoX
```
