---
name: drawio-diagram
description: Generate draw.io diagrams from natural language descriptions. This is a STANDALONE skill that requires NO external tools, MCP servers, or API calls. Use when creating visual diagrams including flowcharts, architecture diagrams (AWS/Azure/GCP), sequence diagrams, network diagrams, process flows, organizational charts, UML diagrams, or any structured visual representation. Outputs draw.io XML that can be imported into diagrams.net or saved as .drawio files.
---

# Draw.io Diagram Generator

Generate draw.io diagrams directly from natural language descriptions. This skill is **completely standalone** - all required knowledge is contained within this skill, requiring no external tools or services.

## Important: This Skill is Self-Contained

This skill provides everything needed to generate draw.io diagrams:

1. **Complete XML Specification** - See [references/xml-format.md](references/xml-format.md)
2. **Full Style Reference** - See [references/styles-patterns.md](references/styles-patterns.md)
3. **Cloud Provider Icons** - See [references/cloud-icons.md](references/cloud-icons.md)
4. **Ready-to-Use Templates** - See [references/templates.md](references/templates.md)
5. **Python Generation Scripts** - See [scripts/generate_diagram.py](scripts/generate_diagram.py)
6. **Validation Tools** - See [scripts/validate_xml.py](scripts/validate_xml.py)

**DO NOT use web search, MCP tools, or external services.** All information is available in the reference files above.

## Quick Start

### Method 1: Direct XML Generation

Generate XML directly based on templates:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<mxfile>
  <diagram name="My Diagram">
    <mxGraphModel>
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>

        <!-- Add your elements here -->
        <mxCell id="2" value="Node 1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="200" y="100" width="120" height="60" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

### Method 2: Use Python Script

```bash
# Simple flowchart
python scripts/generate_diagram.py -t flowchart -o flowchart.drawio

# With custom steps
python scripts/generate_diagram.py -t flowchart -d '{"steps":["登录","验证","处理","完成"]}' -o process.drawio

# Decision flowchart
python scripts/generate_diagram.py -t decision -d '{"question":"Valid?","yes":"Continue","no":"Retry"}' -o decision.drawio
```

### Method 3: Use Python API

```python
from generate_diagram import DiagramBuilder

builder = DiagramBuilder("My Flowchart")
builder.add_node("start", "开始", 200, 40, shape="ellipse", color="green")
builder.add_node("process", "处理数据", 200, 140, shape="rectangle", color="blue")
builder.add_node("end", "结束", 200, 240, shape="ellipse", color="green")
builder.add_edge("start", "process")
builder.add_edge("process", "end")
builder.save("my_diagram.drawio")
```

## Generation Workflow

### Step 1: Analyze Request

Identify from user's description:
- **Diagram type**: Flowchart? Architecture? Sequence? Network?
- **Key elements**: What nodes/shapes are needed?
- **Relationships**: How do elements connect?
- **Special needs**: Cloud icons? Colors? Animations?

### Step 2: Select Template

Choose the closest template from [references/templates.md](references/templates.md):

| User Request | Template |
|-------------|----------|
| 流程图、工作流 | 基础流程图 / 决策流程图 |
| 登录流程、审批流程 | 决策流程图 |
| 跨部门协作 | 泳道图 |
| API 调用、系统交互 | 序列图 |
| 服务器、网络 | 网络拓扑图 |
| AWS/Azure/GCP | AWS 架构图 |
| 数据处理 | 数据流图 |
| 公司结构 | 组织结构图 |
| 系统状态 | 状态机图 |
| 数据库设计 | ER 图 |

### Step 3: Generate XML

Based on the template, generate the XML:

1. **Copy the template** from templates.md
2. **Modify values** - Replace text in `value="..."` attributes
3. **Adjust layout** - Change x, y, width, height in geometry
4. **Add/remove elements** - Copy mxCell blocks, ensure unique IDs
5. **Apply styles** - Use styles from [references/styles-patterns.md](references/styles-patterns.md)

### Step 4: Validate and Save

```bash
python scripts/validate_xml.py diagram.drawio
```

Save as `.drawio` file - ready to import into draw.io!

## XML Structure Reference

### Minimal Structure

```xml
<?xml version="1.0" encoding="UTF-8"?>
<mxfile>
  <diagram name="Name">
    <mxGraphModel>
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <!-- Your elements here, starting with id="2" -->
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

### Node (Shape)

```xml
<mxCell id="UNIQUE_ID" value="Label" style="STYLE_STRING" vertex="1" parent="1">
  <mxGeometry x="X" y="Y" width="W" height="H" as="geometry"/>
</mxCell>
```

### Edge (Connector)

```xml
<mxCell id="UNIQUE_ID" value="Label" style="STYLE_STRING" edge="1" parent="1" source="SOURCE_ID" target="TARGET_ID">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

### Critical Rules

1. **IDs must be unique** - Use sequential: 2, 3, 4, 5...
2. **parent="1"** - All elements must have this
3. **vertex="1"** for shapes, **edge="1"** for connectors
4. **source/target** must reference existing IDs
5. **All tags must be closed**

## Common Styles Quick Reference

### Shapes

| Shape | Style |
|-------|-------|
| 矩形 | `rounded=1;whiteSpace=wrap;html=1;` |
| 椭圆 | `ellipse;whiteSpace=wrap;html=1;` |
| 菱形 | `rhombus;whiteSpace=wrap;html=1;` |
| 圆柱 | `shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;` |
| 云 | `ellipse;shape=cloud;whiteSpace=wrap;html=1;` |
| 人物 | `shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;` |

### Colors

| Color | Fill | Stroke |
|-------|------|--------|
| 蓝色 | `#dae8fc` | `#6c8ebf` |
| 绿色 | `#d5e8d4` | `#82b366` |
| 黄色 | `#fff2cc` | `#d6b656` |
| 橙色 | `#ffe6cc` | `#d79b00` |
| 红色 | `#f8cecc` | `#b85450` |
| 紫色 | `#e1d5e7` | `#9673a6` |

Usage: `fillColor=#dae8fc;strokeColor=#6c8ebf;`

### Edge Styles

| Type | Style |
|------|-------|
| 直线箭头 | `endArrow=classic;html=1;` |
| 正交箭头 | `edgeStyle=orthogonalEdgeStyle;html=1;endArrow=classic;` |
| 曲线 | `edgeStyle=orthogonalEdgeStyle;html=1;curved=1;endArrow=classic;` |
| 虚线 | `dashed=1;` |
| 双向 | `endArrow=classic;startArrow=classic;` |

## Layout Guidelines

**Positioning:**
- Start from (40, 40)
- Space elements 100-150px apart vertically
- Space elements 150-200px apart horizontally
- Keep within 0-2000 range

**Flow Direction:**
- Flowcharts: Top → Bottom
- Processes: Left → Right
- Sequences: Left → Right

**Sizing:**
- Standard node: 120x60
- Decision diamond: 100x80
- Ellipse (start/end): 100x50
- Cloud icons: 78x78

## Examples by Diagram Type

### Simple Flowchart

User: "创建一个用户登录流程图"

Generate:
1. Start (ellipse, green)
2. Enter credentials (rectangle, blue)
3. Validate (diamond, orange)
4. Success → Dashboard (rectangle, green)
5. Failure → Error message (rectangle, red)
6. End (ellipse, green)

### AWS Architecture

User: "创建 AWS 三层架构图"

Generate:
1. Users (actor)
2. CloudFront (AWS icon)
3. ALB (AWS icon)
4. EC2 instances x2 (AWS icon)
5. RDS (AWS icon)
6. Connect with arrows

For AWS icons, see [references/cloud-icons.md](references/cloud-icons.md).

### Sequence Diagram

User: "创建登录 API 序列图"

Generate:
1. User lifeline
2. Frontend lifeline
3. Backend lifeline
4. Database lifeline
5. Horizontal arrows between lifelines

## Resources

### Reference Documents

All required knowledge is in these files:

- **[references/xml-format.md](references/xml-format.md)** - Complete XML specification
- **[references/styles-patterns.md](references/styles-patterns.md)** - All styles and patterns
- **[references/cloud-icons.md](references/cloud-icons.md)** - AWS/Azure/GCP icons
- **[references/templates.md](references/templates.md)** - Ready-to-use complete templates

### Scripts

- **[scripts/generate_diagram.py](scripts/generate_diagram.py)** - Python diagram generator
- **[scripts/validate_xml.py](scripts/validate_xml.py)** - XML validator

## Troubleshooting

**Diagram blank:**
- Verify cells 0 and 1 exist
- Check all elements have `parent="1"`
- Ensure geometry is defined with x, y, width, height

**Edges not connecting:**
- Verify source/target IDs exist
- Check IDs are unique
- Ensure edge has `edge="1"`

**XML parse error:**
- Run validator: `python scripts/validate_xml.py file.drawio`
- Check all tags are closed
- Escape special characters: `&` → `&amp;`, `<` → `&lt;`, `>` → `&gt;`

**Elements overlap:**
- Increase x/y spacing
- Check coordinates are not negative

## Summary

This skill enables generating professional draw.io diagrams without any external dependencies. The workflow is:

1. **Read user requirement**
2. **Select template** from templates.md
3. **Modify XML** based on requirement
4. **Apply styles** from styles-patterns.md
5. **Validate** with validate_xml.py
6. **Save** as .drawio file

All knowledge needed is contained in the reference files. DO NOT search externally.
