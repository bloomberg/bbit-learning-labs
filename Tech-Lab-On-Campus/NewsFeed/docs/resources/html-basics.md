# HTML Basics
This page will go through some basics to HTML that should give a quick start for writing in the markdown language. For more in depth explanation and guides, feel free to do a quick search, or [read here](https://developer.mozilla.org/en-US/docs/Web/HTML).

## Common HTML Tags
Below are some common html tags that may be useful in the lab.

### 1. `<div>` Tag
The `<div>` tag is a block-level element used to group other elements together. It does not inherently have any styling but can be styled using CSS.

Example:
```html
<div class="container">
    <p>This is a paragraph inside a div.</p>
</div>
```

### 2. `<span>` Tag
The `<span>` tag is an inline element used to group text or other inline elements. Like `<div>`, it does not have any default styling and relies on CSS for styling.

Example:
```html
<p>This is a <span class="highlight">highlighted</span> text.</p>
```

### 3. `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>`, `<h6>` Tags
These tags represent headings, with `<h1>` being the highest level and `<h6>` the lowest. They have default styles such as font size and weight, but these can be overridden with CSS.

Example:
```html
<h1>Main Heading</h1>
<h2>Subheading</h2>
<h3>Sub-subheading</h3>
```

### 4. `<a>` Tag
The `<a>` tag defines a hyperlink, which is used to link from one page to another. It can be styled using CSS to change its color, underline, etc. It always requires an `href` attribute to where it links to, which can be within the page (a header) or another page (within or outside the website). The `target` attribute can be set to `"_blank"` to tell the browser to open the link in a new tab.

Example:
```html
<!-- Outside website example -->
<a href="https://www.example.com" target="_blank">Visit Example</a>

<!-- Relative page example -->
<a href="/about">About Page</a>

<!-- Header example -->
<a href="#faq">See the FAQ section below</a>
```

### 5. `<p>` Tag
The `<p>` tag defines a paragraph. It is a block-level element with default margin and padding, which can be customized using CSS.

Example:
```html
<p>This is a paragraph of text.</p>
```

### 6. `<img>` Tag
The `<img>` tag is used to embed images in a webpage. It is an inline element and can be styled using CSS to set dimensions, borders, etc. The `src` attribute is always required to tell where the image should be displayed form, which can come from within the webapp or from a link on some hosted site on the internet. The `alt` attribute is good to set in case the image is not able to be rendered, alternative text is shown describing the image.

Example:
```html
<!-- From within the app -->
<img src="image.jpg" alt="Sample Image" width="200" height="150">

<!-- From the internet -->
<img src="https://google.com/some-image.png" alt="Sample Image" width="200" height="150">
```

## Inheriting Styles with CSS

HTML elements inherit styles from their parent elements unless explicitly overridden. CSS (Cascading Style Sheets) is used to apply styles to HTML elements. Here is an example of how class names can be used to style components:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTML Basics</title>
    <!-- This tag below links to the stylesheet, letting the HTML know to read from it. -->
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1 class="title">Welcome to HTML Basics</h1>
        <p class="description">This is a paragraph explaining the basics of HTML.</p>
        <a href="https://developer.mozilla.org/en-US/docs/Web/CSS" class="link">Learn more about CSS</a>
        <img src="image.jpg" alt="Sample Image" class="image">
    </div>
</body>
</html>
```

More on CSS [here](https://developer.mozilla.org/en-US/docs/Web/CSS).
