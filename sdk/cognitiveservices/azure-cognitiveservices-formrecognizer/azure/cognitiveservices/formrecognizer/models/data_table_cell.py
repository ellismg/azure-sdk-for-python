# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DataTableCell(Model):
    """Information about the extracted cell in a table.

    All required parameters must be populated in order to send to Azure.

    :param row_index: Required. Row index of the cell.
    :type row_index: int
    :param column_index: Required. Column index of the cel.
    :type column_index: int
    :param row_span: Number of rows spanned by this cell. Default value: 1 .
    :type row_span: int
    :param column_span: Number of columns spanned by this cell. Default value:
     1 .
    :type column_span: int
    :param text: Required. The text content of the cell.
    :type text: str
    :param bounding_box: Required. Bounding box of the cell.
    :type bounding_box: list[float]
    :param confidence: Required. Qualitative confidence measure.
    :type confidence: float
    :param elements: List element references.
    :type elements: list[str]
    :param is_header: Is the current cell a header cell?. Default value: False
     .
    :type is_header: bool
    :param is_footer: Is the current cell a footer cell?. Default value: False
     .
    :type is_footer: bool
    """

    _validation = {
        'row_index': {'required': True, 'minimum': 0},
        'column_index': {'required': True, 'minimum': 0},
        'row_span': {'minimum': 1},
        'column_span': {'minimum': 1},
        'text': {'required': True},
        'bounding_box': {'required': True},
        'confidence': {'required': True},
    }

    _attribute_map = {
        'row_index': {'key': 'rowIndex', 'type': 'int'},
        'column_index': {'key': 'columnIndex', 'type': 'int'},
        'row_span': {'key': 'rowSpan', 'type': 'int'},
        'column_span': {'key': 'columnSpan', 'type': 'int'},
        'text': {'key': 'text', 'type': 'str'},
        'bounding_box': {'key': 'boundingBox', 'type': '[float]'},
        'confidence': {'key': 'confidence', 'type': 'float'},
        'elements': {'key': 'elements', 'type': '[str]'},
        'is_header': {'key': 'isHeader', 'type': 'bool'},
        'is_footer': {'key': 'isFooter', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(DataTableCell, self).__init__(**kwargs)
        self.row_index = kwargs.get('row_index', None)
        self.column_index = kwargs.get('column_index', None)
        self.row_span = kwargs.get('row_span', 1)
        self.column_span = kwargs.get('column_span', 1)
        self.text = kwargs.get('text', None)
        self.bounding_box = kwargs.get('bounding_box', None)
        self.confidence = kwargs.get('confidence', None)
        self.elements = kwargs.get('elements', None)
        self.is_header = kwargs.get('is_header', False)
        self.is_footer = kwargs.get('is_footer', False)
