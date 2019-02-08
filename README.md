# TeX2Wordpress
A RegEX Python Script for Translating LaTeX to HTML for Wordpress

## Introduction
This is NOT a compiler for LaTeX to HTML such as [TeX4HT](https://tug.org/tex4ht/). This was originally used for translating assignments to HTML for my Wordpress-powered site (https://www.jeongjh.com) without having the need to modify the original TeX. It is powerful to some extent, but as far as how clever you use it.

### Preparing Python
The script requires the ```tkinter``` package to use the GUI.

### Preparing Your Site
Wordpress is technically not required (as shown in the example), but it allows the use of the `[embed]` tag which I use for figures in this script. 

The following javascripts are recommended:
* [MathJax](https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS_HTML) (for mathing)
* [XyJax](http://sonoisa.github.io/xyjax/xyjax.html) (for diagrams)
* [BigFootJS](http://www.bigfootjs.com/) (for footnotes)

The footnotes script is not required, but removes the need for a footer filled with footnotes. XyJax is not required if you do not draw diagrams; there is also [AMScd](http://docs.mathjax.org/en/latest/tex.html#amscd) which is faster but limited to simple straight arrow diagrams. I recommend placing these scripts in a single folder (e.g. `/js/`) for tidiness.

MathJax gives you the ability to [write macros](http://docs.mathjax.org/en/latest/tex.html#defining-tex-macros) directly into its engine.

BigFootJS also requires a css script for the buttons.

The header in the example is similar to the one I use. The scripts and css are renamed for simplicity.

### Preparing Your LaTeX Code
In general, keep `\begin` on a separate line.

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
* All enumerate environments (nesting allowed) must be of the form
```latex
\begin{placeholder}
\item blah blah blah
\end{placeholder}
```
* If you use ```enumitems```, set these values before the enumerate environment and place the code into the 'Delete Macros' section of the configuration file.

## Configuring the script

The `config.ini` file will need some configuration before running the script. The descriptions for all the values are listed in the file.

## Running the script

The ``Run Script.pyw`` file will launch a GUI for the script. **If you have images**, you should upload these online and paste the url in the text box (one per line) in the order they appear in your TeX document. After you choose your file, press ``Run`` and the freshly-pressed code should appear in the text box (replacing any URLs you may have placed there). You can save this using the ``Save`` button or copy-and-paste as you wish. You can process multiple files without closing the window.

## Remarks

All macros and environments (except the ones used by MathJax) used in your document should be defined in the configuration file. Using classes and ids give this script an incredible amount of flexibility (e.g. the proposition environment in the example is defined the same way as the exercise environment, but differs in `css`). Enumerate especially handles well since nesting is built-in to `css` (the script does not process nesting of enumerate environments). There are numerous ways to simply delete macros in your TeX file during translation, so I won't implement this any time soon.

# Contact

You can contact me through my site [The Bracket](https://www.jeongjh.com/about-contact/). I am a starving student, so tips are incredibly welcomed: 

Paypal: [PayPal.me/jeongjh](paypal.me/jeongjh)

Crypto:
```
BTC: 19AKGxHW19Jx5PtPA55mT4jgByV6ZFmLdL
ETH: 0x5b4e8dde8d7aa983e5fb4f3a58a4cabadb66a6af
LTC: LXcyKsHqLiYbEcgjKCTKUTwh52WfWgfqoX
```
