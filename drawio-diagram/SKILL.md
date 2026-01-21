---
name: drawio-diagram
description: Generate draw.io diagrams from natural language descriptions. Use when creating visual diagrams including flowcharts, architecture diagrams (AWS/Azure/GCP), sequence diagrams, network diagrams, process flows, organizational charts, UML diagrams, or any structured visual representation. Outputs draw.io XML that can be imported into diagrams.net or saved as .drawio files.
---

# Draw.io Diagram Generator

Generate draw.io diagrams directly from natural language descriptions by producing valid draw.io XML.

## Quick Start

Generate diagrams in three steps:

1. **Understand the requirement** - Clarify diagram type, key components, and relationships
2. **Generate XML** - Create mxGraphModel XML following draw.io specifications
3. **Validate and save** - Check XML validity and save as `.drawio` or `.xml` file

### Example Usage

**User:** "Create a simple login flowchart"

**Response:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<mxfile>
  <diagram name="Login Flow">
    <mxGraphModel>
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>

        <mxCell id="2" value="Start" style="ellipse;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
          <mxGeometry x="200" y="40" width="120" height="60" as="geometry"/>
        </mxCell>

        <mxCell id="3" value="Enter Credentials" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="200" y="140" width="120" height="60" as="geometry"/>
        </mxCell>

        <mxCell id="4" value="Valid?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;" vertex="1" parent="1">
          <mxGeometry x="210" y="240" width="100" height="80" as="geometry"/>
        </mxCell>

        <mxCell id="5" value="Dashboard" style="ellipse;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
          <mxGeometry x="360" y="250" width="120" height="60" as="geometry"/>
        </mxCell>

        <mxCell id="6" value="Error Message" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;" vertex="1" parent="1">
          <mxGeometry x="40" y="250" width="120" height="60" as="geometry"/>
        </mxCell>

        <mxCell id="7" style="edgeStyle=orthogonalEdgeStyle;html=1;" edge="1" parent="1" source="2" target="3">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <mxCell id="8" style="edgeStyle=orthogonalEdgeStyle;html=1;" edge="1" parent="1" source="3" target="4">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <mxCell id="9" value="Yes" style="edgeStyle=orthogonalEdgeStyle;html=1;" edge="1" parent="1" source="4" target="5">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <mxCell id="10" value="No" style="edgeStyle=orthogonalEdgeStyle;html=1;" edge="1" parent="1" source="4" target="6">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

Save as `login_flow.drawio` - ready to import into draw.io!

## Core Workflow

### 1. Analyze the Request

Before generating XML, identify:

- **Diagram type**: Flowchart, architecture, sequence, network, etc.
- **Key elements**: What nodes/shapes are needed?
- **Relationships**: How do elements connect?
- **Special requirements**: Cloud icons, specific colors, animations?

### 2. Select Appropriate Patterns

Based on diagram type, reference the appropriate guide:

**Flowcharts and Process Diagrams**
- Use ellipses for start/end
- Rectangles for processes
- Diamonds for decisions
- See [references/styles-patterns.md](references/styles-patterns.md#flowchart-pattern)

**Architecture Diagrams (AWS/Azure/GCP)**
- Use cloud provider icons
- Group related components in containers
- See [references/cloud-icons.md](references/cloud-icons.md)

**Sequence Diagrams**
- Horizontal flow with actors
- Messages as arrows
- See [references/styles-patterns.md](references/styles-patterns.md#sequence-diagram-pattern)

**Network Diagrams**
- Servers, databases, load balancers
- Bidirectional connections
- See [references/styles-patterns.md](references/styles-patterns.md#network-diagram-pattern)

### 3. Generate XML Structure

Follow this template structure:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<mxfile>
  <diagram name="Diagram Name">
    <mxGraphModel>
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>

        <!-- Vertices (shapes) -->
        <mxCell id="2" value="..." style="..." vertex="1" parent="1">
          <mxGeometry x="..." y="..." width="..." height="..." as="geometry"/>
        </mxCell>

        <!-- Edges (connectors) -->
        <mxCell id="N" style="..." edge="1" parent="1" source="2" target="3">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

**Critical Rules:**
1. IDs must be unique, sequential (0, 1, 2, 3...)
2. All user elements must have `parent="1"`
3. Vertices need `vertex="1"`, edges need `edge="1"`
4. Edges must reference valid source/target IDs
5. All elements need geometry (x, y, width, height)

See [references/xml-format.md](references/xml-format.md) for complete specification.

### 4. Apply Styles

Use semantic, consistent styles:

**Common Element Styles:**
- **Start/End**: `ellipse;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;`
- **Process**: `rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;`
- **Decision**: `rhombus;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;`
- **Database**: `shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;fillColor=#d5e8d4;strokeColor=#82b366;`

**Common Connector Styles:**
- **Standard**: `edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;`
- **Curved**: Add `curved=1;`
- **Dashed**: Add `dashed=1;`
- **Animated**: Add `flow=1;`

See [references/styles-patterns.md](references/styles-patterns.md) for complete style reference.

### 5. Layout Elements

**Spacing guidelines:**
- Start from (40, 40) minimum
- Space major elements 150-200px apart
- Align to grid (multiples of 10 or 20)
- Keep within 0-2000 for x/y coordinates

**Flow direction:**
- Flowcharts: Top to bottom
- Processes: Left to right
- Sequences: Left to right

### 6. Validate

Use the validation script to check for errors:

```bash
python scripts/validate_xml.py diagram.drawio
```

Or manually verify:
- [ ] All IDs are unique
- [ ] Cells 0 and 1 exist
- [ ] All elements have parent="1"
- [ ] All edges reference valid source/target
- [ ] All coordinates are positive
- [ ] All tags are properly closed

## Advanced Features

### Cloud Architecture Diagrams

For AWS/Azure/GCP diagrams, use provider-specific icons:

**AWS Example:**
```xml
<mxCell id="2" value="EC2" style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;fillColor=#ED7100;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.ec2;" vertex="1" parent="1">
  <mxGeometry x="200" y="100" width="78" height="78" as="geometry"/>
</mxCell>
```

See [references/cloud-icons.md](references/cloud-icons.md) for complete cloud icon reference.

### Edge Routing

Prevent overlapping edges by using different exit/entry points:

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

### Waypoints for Complex Paths

Route edges around obstacles using waypoints:

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

### Containers and Grouping

Group related elements using containers:

```xml
<mxCell id="2" value="VPC" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5;strokeColor=#666666;dashed=1;verticalAlign=top;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="400" height="300" as="geometry"/>
</mxCell>

<!-- Elements inside container have parent="2" instead of parent="1" -->
<mxCell id="3" value="Subnet" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="2">
  <mxGeometry x="20" y="40" width="120" height="60" as="geometry"/>
</mxCell>
```

## Common Diagram Types

### Flowchart
- Use ellipses (start/end), rectangles (process), diamonds (decision)
- Top-to-bottom flow
- Orthogonal connectors

### AWS Architecture
- Use AWS icons from `mxgraph.aws4.*`
- Group in VPC containers
- Show data flow with arrows

### Sequence Diagram
- Actors on left
- Horizontal message flow
- Time flows downward

### Network Diagram
- Use server/database shapes
- Bidirectional connections
- Group by network segments

### UML Class Diagram
- Rectangles with compartments
- Different arrow types for relationships
- Vertical layout

## Tips for High-Quality Diagrams

1. **Be consistent**: Use same size for similar elements (120x60 for most shapes)
2. **Use semantic colors**: Green for success, red for errors, blue for processes
3. **Label everything**: Clear, concise labels on all elements
4. **Avoid overlap**: Space elements adequately, use waypoints for complex routing
5. **Follow conventions**: Match industry-standard diagram styles
6. **Test in draw.io**: Always validate the XML can be imported

## Troubleshooting

**Diagram doesn't appear:**
- Check cells 0 and 1 exist
- Verify all elements have `parent="1"`
- Ensure geometry is defined

**Edges don't connect:**
- Verify source/target IDs exist
- Check IDs are unique
- Ensure edge has `edge="1"` attribute

**Elements overlap:**
- Increase spacing between elements
- Use waypoints for edge routing
- Check x/y coordinates

**XML parsing error:**
- Run validation script
- Check all tags are closed
- Verify special characters are escaped

## Resources

### References

- **[XML Format Specification](references/xml-format.md)** - Complete mxGraphModel structure, cell types, geometry
- **[Styles and Patterns](references/styles-patterns.md)** - Common styles, color schemes, diagram patterns, edge routing
- **[Cloud Icons](references/cloud-icons.md)** - AWS, Azure, GCP service icons and examples

### Scripts

- **validate_xml.py** - Validate draw.io XML for errors and warnings

```bash
python scripts/validate_xml.py diagram.drawio
```

## Example Gallery

### Simple Flowchart
Start → Process → Decision → End

### AWS 3-Tier Architecture
User → CloudFront → ALB → EC2 → RDS

### Sequence Diagram
User → Frontend → API → Database → Response

### Network Topology
Router → Switch → Servers → Firewall → Internet

For complete examples, see the respective reference files.
