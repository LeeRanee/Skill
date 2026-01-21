# Draw.io XML Format Specification

## Basic Structure

All draw.io diagrams follow this XML structure:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="app.diagrams.net" modified="..." agent="..." version="...">
  <diagram name="Page-1" id="...">
    <mxGraphModel dx="..." dy="..." grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="0">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <!-- Your diagram elements here -->
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

## Core Elements

### mxCell - The Building Block

Every shape, connector, and text element is represented by an `mxCell`:

```xml
<mxCell id="unique-id" value="Label Text" style="..." vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="120" height="60" as="geometry"/>
</mxCell>
```

**Key attributes:**
- `id`: Unique identifier (required, typically sequential: "2", "3", "4"...)
- `value`: Display text/label
- `style`: Semicolon-separated style properties
- `vertex="1"`: Marks as a shape/node (omit for edges)
- `edge="1"`: Marks as a connector/edge (omit for vertices)
- `parent="1"`: Parent container (usually "1" for top-level elements)

### Vertices (Shapes)

```xml
<mxCell id="2" value="Process" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
  <mxGeometry x="200" y="150" width="120" height="60" as="geometry"/>
</mxCell>
```

### Edges (Connectors)

```xml
<mxCell id="3" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;" edge="1" parent="1" source="2" target="4">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

**Key edge attributes:**
- `source="id"`: Starting cell ID
- `target="id"`: Ending cell ID
- `exitX/exitY`: Exit point (0-1, relative to source cell)
- `entryX/entryY`: Entry point (0-1, relative to target cell)

### Geometry

```xml
<mxGeometry x="100" y="100" width="120" height="60" as="geometry"/>
```

**For edges:**
```xml
<mxGeometry relative="1" as="geometry">
  <mxPoint x="100" y="100" as="sourcePoint"/>
  <mxPoint x="300" y="200" as="targetPoint"/>
  <Array as="points">
    <mxPoint x="200" y="100"/>
    <mxPoint x="200" y="200"/>
  </Array>
</mxGeometry>
```

## ID Management

- IDs "0" and "1" are reserved (root and default parent)
- User elements start from "2" onwards
- IDs must be unique within a diagram
- Use simple sequential numbering: "2", "3", "4", etc.

## Positioning Guidelines

**Canvas constraints:**
- Keep all elements within reasonable bounds (e.g., 0-2000 for x/y)
- Default page size: 850x1100 (Letter size)
- Start elements from (40, 40) for margins
- Space elements 150-200px apart for clarity

## Common Pitfalls

1. **Missing parent="1"**: Elements won't appear
2. **Duplicate IDs**: Only one element will render
3. **Invalid source/target**: Edges won't connect
4. **Unclosed tags**: XML parsing errors
5. **Missing geometry**: Elements won't be visible
6. **Negative coordinates**: Elements outside viewport

## Minimal Working Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<mxfile>
  <diagram name="Example">
    <mxGraphModel>
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <mxCell id="2" value="Start" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="200" y="100" width="120" height="80" as="geometry"/>
        </mxCell>
        <mxCell id="3" value="End" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="200" y="250" width="120" height="80" as="geometry"/>
        </mxCell>
        <mxCell id="4" value="" style="edgeStyle=orthogonalEdgeStyle;html=1;" edge="1" parent="1" source="2" target="3">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```
