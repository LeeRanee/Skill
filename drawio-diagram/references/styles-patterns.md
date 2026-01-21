# Styles and Diagram Patterns

## Table of Contents
- [Common Styles](#common-styles)
- [Diagram Patterns](#diagram-patterns)
- [Edge Routing](#edge-routing)
- [Animations](#animations)

## Common Styles

Styles are semicolon-separated key=value pairs.

### Basic Shape Styles

```
rounded=1;whiteSpace=wrap;html=1;
```

**Properties:**
- `rounded=0|1`: Rounded corners
- `whiteSpace=wrap`: Text wrapping
- `html=1`: Enable HTML labels
- `fillColor=#hex`: Background color
- `strokeColor=#hex`: Border color
- `strokeWidth=number`: Border thickness
- `fontColor=#hex`: Text color
- `fontSize=number`: Font size
- `fontStyle=0|1|2|4`: 0=normal, 1=bold, 2=italic, 4=underline

### Common Shapes

**Rectangle:**
```
rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;
```

**Rounded Rectangle:**
```
rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;
```

**Ellipse/Circle:**
```
ellipse;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;
```

**Diamond (Decision):**
```
rhombus;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;
```

**Parallelogram (Input/Output):**
```
shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=1;
```

**Cylinder (Database):**
```
shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;
```

**Cloud:**
```
ellipse;shape=cloud;whiteSpace=wrap;html=1;
```

### Edge Styles

**Straight Line:**
```
endArrow=classic;html=1;
```

**Orthogonal (Right Angles):**
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;
```

**Curved:**
```
edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;curved=1;endArrow=classic;
```

**Dashed:**
```
edgeStyle=orthogonalEdgeStyle;html=1;dashed=1;endArrow=classic;
```

**Arrow Types:**
- `endArrow=classic`: Standard arrow
- `endArrow=block`: Solid block arrow
- `endArrow=open`: Open arrow
- `endArrow=diamond`: Diamond (composition)
- `endArrow=oval`: Oval (aggregation)
- `endArrow=none`: No arrow
- `startArrow=classic`: Arrow at start

### Color Schemes

**Blue (Process):**
```
fillColor=#dae8fc;strokeColor=#6c8ebf;
```

**Green (Success/Data):**
```
fillColor=#d5e8d4;strokeColor=#82b366;
```

**Yellow (Warning/Input):**
```
fillColor=#fff2cc;strokeColor=#d6b656;
```

**Orange (Decision):**
```
fillColor=#ffe6cc;strokeColor=#d79b00;
```

**Red (Error/Critical):**
```
fillColor=#f8cecc;strokeColor=#b85450;
```

**Purple (External):**
```
fillColor=#e1d5e7;strokeColor=#9673a6;
```

## Diagram Patterns

### Flowchart Pattern

```xml
<!-- Start/End (Ellipse) -->
<mxCell id="2" value="Start" style="ellipse;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
  <mxGeometry x="200" y="40" width="120" height="60" as="geometry"/>
</mxCell>

<!-- Process (Rectangle) -->
<mxCell id="3" value="Process Data" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
  <mxGeometry x="200" y="140" width="120" height="60" as="geometry"/>
</mxCell>

<!-- Decision (Diamond) -->
<mxCell id="4" value="Valid?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;" vertex="1" parent="1">
  <mxGeometry x="210" y="240" width="100" height="80" as="geometry"/>
</mxCell>

<!-- Connectors -->
<mxCell id="5" style="edgeStyle=orthogonalEdgeStyle;html=1;endArrow=classic;" edge="1" parent="1" source="2" target="3">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

### Sequence Diagram Pattern

Horizontal flow with actors and interactions:

```xml
<!-- Actor 1 -->
<mxCell id="2" value="User" style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="30" height="60" as="geometry"/>
</mxCell>

<!-- Actor 2 -->
<mxCell id="3" value="System" style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;" vertex="1" parent="1">
  <mxGeometry x="400" y="100" width="30" height="60" as="geometry"/>
</mxCell>

<!-- Message -->
<mxCell id="4" value="Request" style="endArrow=classic;html=1;exitX=1;exitY=0.5;entryX=0;entryY=0.5;" edge="1" parent="1" source="2" target="3">
  <mxGeometry width="50" height="50" relative="1" as="geometry"/>
</mxCell>
```

### Network Diagram Pattern

```xml
<!-- Server/Node -->
<mxCell id="2" value="Server" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
  <mxGeometry x="200" y="100" width="120" height="60" as="geometry"/>
</mxCell>

<!-- Database -->
<mxCell id="3" value="Database" style="shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
  <mxGeometry x="400" y="100" width="80" height="80" as="geometry"/>
</mxCell>

<!-- Bidirectional Connection -->
<mxCell id="4" value="" style="endArrow=classic;startArrow=classic;html=1;rounded=0;" edge="1" parent="1" source="2" target="3">
  <mxGeometry width="50" height="50" relative="1" as="geometry"/>
</mxCell>
```

## Edge Routing

### Preventing Overlaps

When multiple edges connect the same nodes, use different exit/entry points:

```xml
<!-- Edge 1: Bottom to Top -->
<mxCell id="4" style="edgeStyle=orthogonalEdgeStyle;html=1;exitX=0.5;exitY=1;entryX=0.5;entryY=0;" edge="1" parent="1" source="2" target="3">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>

<!-- Edge 2: Right to Left (different path) -->
<mxCell id="5" style="edgeStyle=orthogonalEdgeStyle;html=1;exitX=1;exitY=0.5;entryX=0;entryY=0.5;" edge="1" parent="1" source="2" target="3">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

**Exit/Entry Values (0-1 relative):**
- `0.5, 0`: Top center
- `1, 0.5`: Right center
- `0.5, 1`: Bottom center
- `0, 0.5`: Left center

### Waypoints for Complex Routing

```xml
<mxCell id="4" style="edgeStyle=orthogonalEdgeStyle;html=1;" edge="1" parent="1" source="2" target="3">
  <mxGeometry relative="1" as="geometry">
    <Array as="points">
      <mxPoint x="300" y="150"/>
      <mxPoint x="300" y="250"/>
    </Array>
  </mxGeometry>
</mxCell>
```

## Animations

### Animated Connectors

Add `flow=1` to style for flowing animation:

```
edgeStyle=orthogonalEdgeStyle;html=1;endArrow=classic;flow=1;
```

### Direction Control

Add labels to show data flow direction:

```xml
<mxCell id="4" value="Data Flow →" style="edgeStyle=orthogonalEdgeStyle;html=1;endArrow=classic;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="2" target="3">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

## Layout Best Practices

1. **Spacing**: Keep 150-200px between major elements
2. **Alignment**: Align elements to grid (use multiples of 10 or 20)
3. **Flow Direction**:
   - Flowcharts: Top to bottom
   - Processes: Left to right
   - Hierarchies: Top to bottom
4. **Grouping**: Use containers for related elements
5. **Margins**: Start from (40, 40) minimum
6. **Page Bounds**: Stay within 0-2000 for x/y coordinates

## Quick Reference: Common Combinations

**Start/End Node:**
```
ellipse;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;
```

**Process Step:**
```
rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;
```

**Decision Point:**
```
rhombus;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;
```

**Data Store:**
```
shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;fillColor=#d5e8d4;strokeColor=#82b366;
```

**Standard Connector:**
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;
```
