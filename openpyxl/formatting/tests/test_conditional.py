from __future__ import absolute_import
# Copyright (c) 2010-2015 openpyxl

import pytest

from openpyxl.xml.functions import fromstring, tostring
from openpyxl.xml.constants import SHEET_MAIN_NS

from openpyxl.styles import Font, Color, PatternFill

from openpyxl.tests.helper import compare_xml


@pytest.fixture
def ConditionalFormat():
    from ..conditional import ConditionalFormat
    return ConditionalFormat


def test_parse(ConditionalFormat, datadir):
    datadir.chdir()
    with open("dxf_style.xml") as content:
        src = content.read()
    xml = fromstring(src)
    formats = []
    for node in xml.findall("{%s}dxfs/{%s}dxf" % (SHEET_MAIN_NS, SHEET_MAIN_NS) ):
        formats.append(ConditionalFormat.create(node))
    assert len(formats) == 164
    cond = formats[1]
    assert cond.font == Font(underline="double", color=Color(auto=1), strikethrough=True, italic=True)
    assert cond.fill == PatternFill(end_color='FFFFC7CE')


def test_serialise(ConditionalFormat):
    cond = ConditionalFormat()
    cond.font = Font()
    cond.fill = PatternFill()
    xml = tostring(cond.serialise())
    expected = """
    <dxf>
    <font>
    <name val="Calibri"></name>
    <family val="2"></family>
    <color rgb="00000000"></color>
    <sz val="11"></sz>
    </font>
    <fill>
    <patternFill patternType="none"></patternFill>
    </fill>
    </dxf>
    """
    diff = compare_xml(xml, expected)
    assert diff is None, diff