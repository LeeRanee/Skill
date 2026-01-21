#!/usr/bin/env python3
"""
Draw.io XML Validator

Validates draw.io XML diagrams for:
- Well-formed XML structure
- Required elements (mxfile, diagram, mxGraphModel, root, cells 0 and 1)
- Valid cell IDs (unique, non-duplicate)
- Valid geometry (positive dimensions, reasonable coordinates)
- Valid edge connections (source/target exist)
- Common style issues

Usage:
    python validate_xml.py <diagram.xml>
    python validate_xml.py <diagram.drawio>
"""

import sys
import xml.etree.ElementTree as ET
from typing import List, Tuple, Set


class ValidationResult:
    def __init__(self):
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.info: List[str] = []

    def is_valid(self) -> bool:
        return len(self.errors) == 0

    def add_error(self, msg: str):
        self.errors.append(f"❌ ERROR: {msg}")

    def add_warning(self, msg: str):
        self.warnings.append(f"⚠️  WARNING: {msg}")

    def add_info(self, msg: str):
        self.info.append(f"ℹ️  INFO: {msg}")

    def print_results(self):
        if self.errors:
            print("\n=== ERRORS ===")
            for error in self.errors:
                print(error)

        if self.warnings:
            print("\n=== WARNINGS ===")
            for warning in self.warnings:
                print(warning)

        if self.info:
            print("\n=== INFO ===")
            for info in self.info:
                print(info)

        if self.is_valid():
            print("\n✅ Validation passed! Diagram is valid.")
        else:
            print(f"\n❌ Validation failed with {len(self.errors)} error(s).")


def validate_xml_structure(tree: ET.ElementTree, result: ValidationResult):
    """Validate basic XML structure"""
    root = tree.getroot()

    # Check root element
    if root.tag != 'mxfile':
        result.add_error(f"Root element should be 'mxfile', got '{root.tag}'")
        return

    # Check for diagram element
    diagrams = root.findall('.//diagram')
    if not diagrams:
        result.add_error("No 'diagram' element found")
        return

    result.add_info(f"Found {len(diagrams)} diagram(s)")

    # Check for mxGraphModel
    model = root.find('.//mxGraphModel')
    if model is None:
        result.add_error("No 'mxGraphModel' element found")
        return

    # Check for root element
    root_elem = model.find('./root')
    if root_elem is None:
        result.add_error("No 'root' element found in mxGraphModel")
        return

    # Check for cells 0 and 1
    cells = root_elem.findall('./mxCell')
    cell_ids = {cell.get('id') for cell in cells}

    if '0' not in cell_ids:
        result.add_error("Missing required cell with id='0'")
    if '1' not in cell_ids:
        result.add_error("Missing required cell with id='1'")


def validate_cell_ids(tree: ET.ElementTree, result: ValidationResult) -> Set[str]:
    """Validate cell IDs are unique and non-empty"""
    cells = tree.findall('.//mxCell')
    cell_ids: Set[str] = set()
    duplicates: List[str] = []

    for cell in cells:
        cell_id = cell.get('id')

        if not cell_id:
            result.add_error("Found cell without 'id' attribute")
            continue

        if cell_id in cell_ids:
            duplicates.append(cell_id)
        else:
            cell_ids.add(cell_id)

    if duplicates:
        result.add_error(f"Duplicate cell IDs found: {', '.join(duplicates)}")

    result.add_info(f"Total cells: {len(cells)}, Unique IDs: {len(cell_ids)}")
    return cell_ids


def validate_geometry(tree: ET.ElementTree, result: ValidationResult):
    """Validate geometry attributes"""
    cells = tree.findall('.//mxCell')

    for cell in cells:
        cell_id = cell.get('id')
        geometry = cell.find('./mxGeometry')

        if geometry is None:
            # Only vertices need geometry
            if cell.get('vertex') == '1':
                result.add_warning(f"Cell '{cell_id}' is a vertex but missing geometry")
            continue

        # Check dimensions
        width = geometry.get('width')
        height = geometry.get('height')

        if width is not None:
            try:
                w = float(width)
                if w <= 0:
                    result.add_warning(f"Cell '{cell_id}' has non-positive width: {width}")
                elif w > 5000:
                    result.add_warning(f"Cell '{cell_id}' has unusually large width: {width}")
            except ValueError:
                result.add_error(f"Cell '{cell_id}' has invalid width: {width}")

        if height is not None:
            try:
                h = float(height)
                if h <= 0:
                    result.add_warning(f"Cell '{cell_id}' has non-positive height: {height}")
                elif h > 5000:
                    result.add_warning(f"Cell '{cell_id}' has unusually large height: {height}")
            except ValueError:
                result.add_error(f"Cell '{cell_id}' has invalid height: {height}")

        # Check coordinates
        x = geometry.get('x')
        y = geometry.get('y')

        if x is not None:
            try:
                x_val = float(x)
                if x_val < 0:
                    result.add_warning(f"Cell '{cell_id}' has negative x coordinate: {x}")
                elif x_val > 10000:
                    result.add_warning(f"Cell '{cell_id}' is far outside typical canvas: x={x}")
            except ValueError:
                result.add_error(f"Cell '{cell_id}' has invalid x coordinate: {x}")

        if y is not None:
            try:
                y_val = float(y)
                if y_val < 0:
                    result.add_warning(f"Cell '{cell_id}' has negative y coordinate: {y}")
                elif y_val > 10000:
                    result.add_warning(f"Cell '{cell_id}' is far outside typical canvas: y={y}")
            except ValueError:
                result.add_error(f"Cell '{cell_id}' has invalid y coordinate: {y}")


def validate_edges(tree: ET.ElementTree, cell_ids: Set[str], result: ValidationResult):
    """Validate edge connections"""
    cells = tree.findall('.//mxCell')

    for cell in cells:
        if cell.get('edge') != '1':
            continue

        cell_id = cell.get('id')
        source = cell.get('source')
        target = cell.get('target')

        if source and source not in cell_ids:
            result.add_error(f"Edge '{cell_id}' references non-existent source: {source}")

        if target and target not in cell_ids:
            result.add_error(f"Edge '{cell_id}' references non-existent target: {target}")

        if not source and not target:
            result.add_warning(f"Edge '{cell_id}' has no source or target")


def validate_parents(tree: ET.ElementTree, cell_ids: Set[str], result: ValidationResult):
    """Validate parent references"""
    cells = tree.findall('.//mxCell')

    for cell in cells:
        cell_id = cell.get('id')
        parent = cell.get('parent')

        # Skip root cells (0 and 1)
        if cell_id in ('0', '1'):
            continue

        if not parent:
            result.add_warning(f"Cell '{cell_id}' has no parent attribute")
        elif parent not in cell_ids:
            result.add_error(f"Cell '{cell_id}' references non-existent parent: {parent}")


def validate_file(filepath: str) -> ValidationResult:
    """Main validation function"""
    result = ValidationResult()

    try:
        tree = ET.parse(filepath)
    except ET.ParseError as e:
        result.add_error(f"XML parsing failed: {e}")
        return result
    except FileNotFoundError:
        result.add_error(f"File not found: {filepath}")
        return result
    except Exception as e:
        result.add_error(f"Unexpected error: {e}")
        return result

    result.add_info(f"File: {filepath}")

    # Run validations
    validate_xml_structure(tree, result)

    if result.is_valid():  # Only continue if structure is valid
        cell_ids = validate_cell_ids(tree, result)
        validate_geometry(tree, result)
        validate_edges(tree, cell_ids, result)
        validate_parents(tree, cell_ids, result)

    return result


def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_xml.py <diagram.xml>")
        sys.exit(1)

    filepath = sys.argv[1]
    result = validate_file(filepath)
    result.print_results()

    sys.exit(0 if result.is_valid() else 1)


if __name__ == '__main__':
    main()
