# TeX2Wordpress
A RegEX Python Script for Translating LaTeX to HTML for Wordpress

## Introduction
This is NOT a compiler for LaTeX to HTML such as [TeX4HT](https://tug.org/tex4ht/). This was originally for translating assignments to HTML for my Wordpress-powered site (https://www.jeongjh.com) without having the need to modify my document. It is powerful to some extent, but only goes as far as how clever you use it.

### Preparing Python
The script requires the ```tkinter``` package to use the GUI.

### Preparing Your Site
Wordpress is technically not required, but it allows the use of the `[embed]` tag which I use for figures in this script. 

The following javascripts are recommended:
* [MathJax](https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS_HTML) (for mathing)
* [XyJax](http://sonoisa.github.io/xyjax/xyjax.html) (for diagrams)
* [BigFootJS](http://www.bigfootjs.com/) (for footnotes)

The footnotes script is not required, but removes the need for a footer filled with footnotes. XyJax is not required if you do not draw diagrams; there is also [AMScd](http://docs.mathjax.org/en/latest/tex.html#amscd) which is faster but limited to simple straight arrow diagrams. I recommend placing these scripts in a single folder (e.g. `/js/`) for tidiness.

MathJax gives you the ability to write macros directly into its engine. [link](http://docs.mathjax.org/en/latest/tex.html#defining-tex-macros) A sample is given in the example script below.

BigFootJS also requires a css script for the buttons.

The following example code can be used in your header to install MathJax and the scripts on your site: (replace `PLACEHOLDER` with your scripts location)

```HTML
<script type="text/x-mathjax-config">
   MathJax.Hub.Config({
	extensions: ["tex2jax.js"],
   	tex2jax: {inlineMath: [["\\(","\\)"],["[latex]","[/latex]"]]},
	jax: ["input/TeX","output/HTML-CSS"],
	"HTML-CSS": {
	styles: {".MathJax_Preview": {visibility: "hidden"}}
	},
   	TeX: {
   		Macros: {
   			Z: ["\\mathbb{Z}",0],
   		},
   		equationNumbers: { autoNumber: "AMS" },
   		extensions: ["PLACEHOLDER/XyJax.js"]
   	},
   });
</script>
<script type="text/javascript" async src="PLACEHOLDER/MathJax"></script>
<script type="text/javascript" src="PLACEHOLDER/BigFootJS.js"></script>
<script type="text/javascript">
   $.bigfoot({
    activateCallback: function($popover, $button) {
        if (MathJax && !$button.data('mathjax-processed')) {
            var content_wrapper = $popover.find('.bigfoot-footnote__content')[0];
            MathJax.Hub.Queue(['Typeset', MathJax.Hub, content_wrapper]);
            MathJax.Hub.Queue(function () {
                $button.attr('data-bigfoot-footnote', content_wrapper.innerHTML);
                $button.data('mathjax-processed', true);
            });
        }
    }
   });
</script>
<link rel="stylesheet" href="PLACEHOLDER/BigFootJS.css">
```

### Preparing Your LaTeX Code

For footnotes:
* Place footnotes (`\footnote{sometext}`) where you would like the footnote marker to appear.
* Do **not** place your footnote in math delimiters. Use a footnote marker (`\footnotemarker`) and place your footnote text    (`\footnotetext{texthere}`).

For environments:
* All theorem-type environments (except the ones parsed by MathJax) must be of the form
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

## Usage

Will write soon...
