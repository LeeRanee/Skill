#!/usr/bin/env python3
"""
Draw.io Diagram Generator

A standalone utility for generating draw.io diagrams programmatically.
No external dependencies required - uses only Python standard library.

Usage:
    # As a module
    from generate_diagram import DiagramBuilder

    builder = DiagramBuilder("My Diagram")
    builder.add_node("start", "Start", 200, 40, shape="ellipse", color="green")
    builder.add_node("process", "Process", 200, 140, shape="rectangle", color="blue")
    builder.add_edge("start", "process")
    builder.save("my_diagram.drawio")

    # From command line
    python generate_diagram.py --type flowchart --output my_flowchart.drawio
"""

import xml.etree.ElementTree as ET
from xml.dom import minidom
import argparse
import json
import sys
from typing import Optional, Dict, List, Tuple


# Color schemes
COLORS = {
    "blue": {"fill": "#dae8fc", "stroke": "#6c8ebf"},
    "green": {"fill": "#d5e8d4", "stroke": "#82b366"},
    "yellow": {"fill": "#fff2cc", "stroke": "#d6b656"},
    "orange": {"fill": "#ffe6cc", "stroke": "#d79b00"},
    "red": {"fill": "#f8cecc", "stroke": "#b85450"},
    "purple": {"fill": "#e1d5e7", "stroke": "#9673a6"},
    "gray": {"fill": "#f5f5f5", "stroke": "#666666"},
    "white": {"fill": "#ffffff", "stroke": "#000000"},
}

# Shape styles
SHAPES = {
    "rectangle": "rounded=1;whiteSpace=wrap;html=1;",
    "ellipse": "ellipse;whiteSpace=wrap;html=1;",
    "diamond": "rhombus;whiteSpace=wrap;html=1;",
    "parallelogram": "shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=1;",
    "cylinder": "shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;",
    "cloud": "ellipse;shape=cloud;whiteSpace=wrap;html=1;",
    "actor": "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;",
    "document": "shape=document;whiteSpace=wrap;html=1;boundedLbl=1;",
    "hexagon": "shape=hexagon;perimeter=hexagonPerimeter2;whiteSpace=wrap;html=1;",
}

# Edge styles
EDGE_STYLES = {
    "straight": "endArrow=classic;html=1;",
    "orthogonal": "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;",
    "curved": "edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;curved=1;endArrow=classic;",
    "dashed": "edgeStyle=orthogonalEdgeStyle;html=1;dashed=1;endArrow=classic;",
    "bidirectional": "edgeStyle=orthogonalEdgeStyle;html=1;endArrow=classic;startArrow=classic;",
}


class DiagramBuilder:
    """Build draw.io diagrams programmatically."""

    def __init__(self, name: str = "Diagram"):
        self.name = name
        self.nodes: Dict[str, dict] = {}
        self.edges: List[dict] = []
        self._id_counter = 2  # 0 and 1 are reserved

    def _get_next_id(self) -> str:
        """Get next available ID."""
        id_str = str(self._id_counter)
        self._id_counter += 1
        return id_str

    def _build_style(self, shape: str, color: str, **kwargs) -> str:
        """Build style string from parameters."""
        base_style = SHAPES.get(shape, SHAPES["rectangle"])
        colors = COLORS.get(color, COLORS["blue"])

        style = f"{base_style}fillColor={colors['fill']};strokeColor={colors['stroke']};"

        # Add extra style properties
        for key, value in kwargs.items():
            style += f"{key}={value};"

        return style

    def add_node(
        self,
        node_id: str,
        label: str,
        x: float,
        y: float,
        width: float = 120,
        height: float = 60,
        shape: str = "rectangle",
        color: str = "blue",
        **style_kwargs
    ) -> str:
        """
        Add a node to the diagram.

        Args:
            node_id: Unique identifier for the node
            label: Text to display
            x, y: Position coordinates
            width, height: Dimensions
            shape: One of: rectangle, ellipse, diamond, parallelogram, cylinder, cloud, actor
            color: One of: blue, green, yellow, orange, red, purple, gray, white
            **style_kwargs: Additional style properties

        Returns:
            The internal ID assigned to this node
        """
        internal_id = self._get_next_id()
        style = self._build_style(shape, color, **style_kwargs)

        self.nodes[node_id] = {
            "internal_id": internal_id,
            "label": label,
            "x": x,
            "y": y,
            "width": width,
            "height": height,
            "style": style,
        }
        return internal_id

    def add_edge(
        self,
        source_id: str,
        target_id: str,
        label: str = "",
        style: str = "orthogonal",
        **style_kwargs
    ) -> str:
        """
        Add an edge connecting two nodes.

        Args:
            source_id: ID of source node
            target_id: ID of target node
            label: Optional label text
            style: One of: straight, orthogonal, curved, dashed, bidirectional
            **style_kwargs: Additional style properties

        Returns:
            The internal ID assigned to this edge
        """
        internal_id = self._get_next_id()
        base_style = EDGE_STYLES.get(style, EDGE_STYLES["orthogonal"])

        # Add extra style properties
        for key, value in style_kwargs.items():
            base_style += f"{key}={value};"

        self.edges.append({
            "internal_id": internal_id,
            "source": source_id,
            "target": target_id,
            "label": label,
            "style": base_style,
        })
        return internal_id

    def add_container(
        self,
        node_id: str,
        label: str,
        x: float,
        y: float,
        width: float = 300,
        height: float = 200,
        color: str = "gray"
    ) -> str:
        """Add a container/group element."""
        return self.add_node(
            node_id, label, x, y, width, height,
            shape="rectangle", color=color,
            verticalAlign="top", dashed="1"
        )

    def to_xml(self) -> str:
        """Generate draw.io XML string."""
        # Create root structure
        mxfile = ET.Element("mxfile")
        diagram = ET.SubElement(mxfile, "diagram", name=self.name)
        model = ET.SubElement(diagram, "mxGraphModel")
        root = ET.SubElement(model, "root")

        # Add required cells 0 and 1
        ET.SubElement(root, "mxCell", id="0")
        ET.SubElement(root, "mxCell", id="1", parent="0")

        # Add nodes
        for node_id, node in self.nodes.items():
            cell = ET.SubElement(
                root, "mxCell",
                id=node["internal_id"],
                value=node["label"],
                style=node["style"],
                vertex="1",
                parent="1"
            )
            ET.SubElement(
                cell, "mxGeometry",
                x=str(node["x"]),
                y=str(node["y"]),
                width=str(node["width"]),
                height=str(node["height"]),
                **{"as": "geometry"}
            )

        # Add edges
        for edge in self.edges:
            source_internal = self.nodes.get(edge["source"], {}).get("internal_id")
            target_internal = self.nodes.get(edge["target"], {}).get("internal_id")

            if not source_internal or not target_internal:
                print(f"Warning: Edge references unknown node(s): {edge['source']} -> {edge['target']}")
                continue

            cell_attrs = {
                "id": edge["internal_id"],
                "style": edge["style"],
                "edge": "1",
                "parent": "1",
                "source": source_internal,
                "target": target_internal,
            }
            if edge["label"]:
                cell_attrs["value"] = edge["label"]

            cell = ET.SubElement(root, "mxCell", **cell_attrs)
            ET.SubElement(cell, "mxGeometry", relative="1", **{"as": "geometry"})

        # Convert to string with proper formatting
        rough_string = ET.tostring(mxfile, encoding="unicode")
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")

    def save(self, filepath: str):
        """Save diagram to file."""
        xml_content = self.to_xml()

        # Add XML declaration
        if not xml_content.startswith("<?xml"):
            xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n' + xml_content

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(xml_content)

        print(f"Diagram saved to: {filepath}")


def create_flowchart(steps: List[str], title: str = "Flowchart") -> DiagramBuilder:
    """Create a simple linear flowchart."""
    builder = DiagramBuilder(title)

    # Add start
    builder.add_node("start", "Start", 200, 40, 100, 50, shape="ellipse", color="green")

    # Add steps
    prev_id = "start"
    y = 130
    for i, step in enumerate(steps):
        node_id = f"step{i}"
        builder.add_node(node_id, step, 190, y, 120, 60, shape="rectangle", color="blue")
        builder.add_edge(prev_id, node_id)
        prev_id = node_id
        y += 100

    # Add end
    builder.add_node("end", "End", 200, y, 100, 50, shape="ellipse", color="green")
    builder.add_edge(prev_id, "end")

    return builder


def create_decision_flowchart(
    question: str,
    yes_action: str,
    no_action: str,
    title: str = "Decision Flowchart"
) -> DiagramBuilder:
    """Create a flowchart with a decision point."""
    builder = DiagramBuilder(title)

    builder.add_node("start", "Start", 250, 40, 100, 50, shape="ellipse", color="green")
    builder.add_node("decision", question, 240, 130, 120, 80, shape="diamond", color="orange")
    builder.add_node("yes", yes_action, 400, 140, 120, 60, shape="rectangle", color="blue")
    builder.add_node("no", no_action, 80, 140, 120, 60, shape="rectangle", color="red")
    builder.add_node("end", "End", 250, 280, 100, 50, shape="ellipse", color="green")

    builder.add_edge("start", "decision")
    builder.add_edge("decision", "yes", "Yes")
    builder.add_edge("decision", "no", "No")
    builder.add_edge("yes", "end")
    builder.add_edge("no", "end")

    return builder


def create_architecture(
    layers: List[Tuple[str, List[str]]],
    title: str = "Architecture"
) -> DiagramBuilder:
    """
    Create a layered architecture diagram.

    Args:
        layers: List of (layer_name, [components...]) tuples
        title: Diagram title
    """
    builder = DiagramBuilder(title)

    y = 40
    colors = ["purple", "blue", "green", "yellow", "orange"]

    for i, (layer_name, components) in enumerate(layers):
        color = colors[i % len(colors)]
        x = 40

        for j, comp in enumerate(components):
            node_id = f"layer{i}_comp{j}"
            builder.add_node(node_id, comp, x, y, 120, 60, shape="rectangle", color=color)
            x += 160

        y += 120

    # Add vertical connections between layers
    for i in range(len(layers) - 1):
        for j in range(min(len(layers[i][1]), len(layers[i+1][1]))):
            builder.add_edge(
                f"layer{i}_comp{j}",
                f"layer{i+1}_comp{j}",
                style="dashed"
            )

    return builder


def main():
    """Command line interface."""
    parser = argparse.ArgumentParser(
        description="Generate draw.io diagrams from command line"
    )
    parser.add_argument(
        "--type", "-t",
        choices=["flowchart", "decision", "architecture"],
        default="flowchart",
        help="Type of diagram to generate"
    )
    parser.add_argument(
        "--output", "-o",
        default="diagram.drawio",
        help="Output file path"
    )
    parser.add_argument(
        "--title",
        default="Diagram",
        help="Diagram title"
    )
    parser.add_argument(
        "--data", "-d",
        help="JSON data for diagram (format depends on type)"
    )

    args = parser.parse_args()

    # Parse data if provided
    data = json.loads(args.data) if args.data else None

    if args.type == "flowchart":
        steps = data.get("steps", ["Step 1", "Step 2", "Step 3"]) if data else ["Step 1", "Step 2", "Step 3"]
        builder = create_flowchart(steps, args.title)

    elif args.type == "decision":
        if data:
            question = data.get("question", "Condition?")
            yes_action = data.get("yes", "Yes Action")
            no_action = data.get("no", "No Action")
        else:
            question = "Condition?"
            yes_action = "Yes Action"
            no_action = "No Action"
        builder = create_decision_flowchart(question, yes_action, no_action, args.title)

    elif args.type == "architecture":
        if data:
            layers = [(l["name"], l["components"]) for l in data.get("layers", [])]
        else:
            layers = [
                ("Presentation", ["Web App", "Mobile App"]),
                ("Application", ["API Gateway", "Services"]),
                ("Data", ["Database", "Cache"]),
            ]
        builder = create_architecture(layers, args.title)

    builder.save(args.output)


if __name__ == "__main__":
    main()
