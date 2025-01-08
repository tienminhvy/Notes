## TOC

Table of content

- [Getting shape currently selected](#getting-shape-currently-selected-toc)
- [Getting current position of the mouse pointer](#getting-current-position-of-the-mouse-pointer-toc)
- [Getting shape by defintion](#getting-shape-by-defintion-toc)
- [Adding new shape base on its defition](#adding-new-shape-base-on-its-defition-toc)

## Getting shape currently selected ([TOC](#toc))

```js
var selectedTargets = this.canvas.getSelectedTargets();
var parent = selectedTargets[0];
```

## Getting current position of the mouse pointer ([TOC](#toc))

```js
// code works on Action performed
var loc = this.canvas.getEventLocation(event, "withoutZoom");
```

## Getting shape by defintion ([TOC](#toc))

```js
var def = CollectionManager.shapeDefinition.locateDefinition("Evolus.Common:arrow");
```

## Adding new shape base on its defition ([TOC](#toc))

```js
this.canvas.insertShapeImpl_(def, new Bound(loc.x, loc.y, null, null));
```
