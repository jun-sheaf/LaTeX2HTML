# LaTeX2HTML
A Customizable Python Program for Translating LaTeX to HTML

## Introduction
This program **can**:
* Translates any environment (even enumerate-types) into a fully-customizable HTML container
* Places footnotes at the end of the document (before `\end{document}`) and hyperlinks them.
* Places a bibliography at the end of the document (before the footnotes) with the citations used as well as hyperlinks them.
* Translates macros into fully-customizable HTML containers/tags

This program *cannot*:
* Convert `tikzpicture` (and its children such as `tikzcd`) to `SVG` (however, [XyJax](http://sonoisa.github.io/xyjax/xyjax.html) can be used to fully encode diagrams in MathJax)
* Compile (as opposed to [translate](https://en.oxforddictionaries.com/definition/translation)) LaTeX to HTML such as [TeX4HT](https://tug.org/tex4ht/) 

### Preparing Python
The following modules are **required**:
* `tkinter`

The following modules are *optional*: 
* `bibtexparser` (for bibliographies)

### Preparing Your Site
The following javascripts are **required**:
* [MathJax](https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS_HTML)

The following javascripts are recommended:
* [XyJax](http://sonoisa.github.io/xyjax/xyjax.html) (for diagrams)
  * Although `tikzcd` is not available on MathJax, `xypics` is available through XyJax.
  * [AMScd](http://docs.mathjax.org/en/latest/tex.html#amscd) can also be used (and is faster), but is limited to simple straight arrow diagrams.
* [BigFootJS](http://www.bigfootjs.com/) (for footnotes)
  * Depends on [jquery](https://code.jquery.com/jquery-3.3.1.min.js)
  * BigFootJS removes the need for a footer filled with footnotes and places them in an overlay activated by the footnote's link.

The header in the example is similar to the one I use. The scripts and css are renamed for simplicity.

### Preparing Your LaTeX Code
For footnotes:
* Place footnotes (`\footnote{sometext}`) where you would like the footnote marker to appear.
* Do **not** place your footnote in math delimiters. Use a footnote marker (`\footnotemarker`) and place your footnote text    (`\footnotetext{texthere}`).

For environments:
* All non-enumerate-type environments (except the ones parsed by MathJax such as `equation`) must be of the form
```latex
\begin{placeholder}[optional]
blah blah blah
\end{placeholder}
```

## Customizing the program
The strength of this program lies in the customizability. The `config.ini` contains all the information about customizability options.

## Running the script
The ``RunScript.pyw`` file will launch a GUI for the script. **If you have images**, you should upload these online and paste the url in the text box (one per line) in the order they appear in your TeX document. **If you have a bibliography**, assure you have the requirements listed before and select the `.bib` file associated to it. After you choose your file, press `Run` and the freshly-pressed code should appear in the text box (replacing any URLs you may have placed there). You can edit, copy-and-paste, and save (using the ``Save`` button) however you wish. You can process multiple files without closing the window.

## Remarks

All macros and environments (except the ones used by MathJax) used in your document should be defined in the configuration file. Using classes and ids give this script an incredible amount of flexibility (e.g. the proposition environment in the example is defined the same way as the exercise environment, but differs in `css`). Enumerate especially handles well since nesting is built-in to `css` (the script does not process nesting of enumerate environments). There are numerous ways to simply delete macros in your TeX file during translation, so I won't implement this any time soon.

# Contact

You can contact me through my site [The Bracket](https://www.jeongjh.com/about-contact/). I am a starving student, so tips are incredibly welcomed: 

Paypal: [PayPal.me/jeongjh](https://www.paypal.me/jeongjh)

Crypto:
```
BTC: 19AKGxHW19Jx5PtPA55mT4jgByV6ZFmLdL
ETH: 0x5b4e8dde8d7aa983e5fb4f3a58a4cabadb66a6af
LTC: LXcyKsHqLiYbEcgjKCTKUTwh52WfWgfqoX
```
