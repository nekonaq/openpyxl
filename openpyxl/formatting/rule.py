from __future__ import absolute_import
# copyright openpyxl 2010-2015

#Autogenerated schema
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.descriptors import (
    Typed,
    String,
    Sequence,
    Bool,
    Float,
    NoneSet,
    Set,
    Integer,)
from openpyxl.descriptors.excel import HexBinary
from openpyxl.styles import Color

from openpyxl.xml.functions import (
    localname,
    Element,
    SubElement,
)


class ExtensionList(Serialisable):

    pass


class Cfvo(Serialisable):

    type = Set(values=(['num', 'percent', 'max', 'min', 'formula', 'percentile']))
    val = String(allow_none=True)
    gte = Bool(allow_none=True)
    extLst = Typed(expected_type=ExtensionList, allow_none=True)

    def __init__(self,
                 type,
                 val=None,
                 gte=None,
                 extLst=None,
                ):
        self.type = type
        self.val = val
        self.gte = gte
        self.extLst = extLst


class IconSet(Serialisable):

    iconSet = NoneSet(values=(['3Arrows', '3ArrowsGray', '3Flags',
                           '3TrafficLights1', '3TrafficLights2', '3Signs', '3Symbols', '3Symbols2',
                           '4Arrows', '4ArrowsGray', '4RedToBlack', '4Rating', '4TrafficLights',
                           '5Arrows', '5ArrowsGray', '5Rating', '5Quarters']))
    showValue = Bool(allow_none=True)
    percent = Bool()
    reverse = Bool(allow_none=True)
    cfvo = Typed(expected_type=Cfvo, )

    def __init__(self,
                 iconSet=None,
                 showValue=None,
                 percent=None,
                 reverse=None,
                 cfvo=None,
                ):
        self.iconSet = iconSet
        self.showValue = showValue
        self.percent = percent
        self.reverse = reverse
        self.cfvo = cfvo


class DataBar(Serialisable):

    minLength = Integer(allow_none=True)
    maxLength = Integer(allow_none=True)
    showValue = Bool(allow_none=True)
    cfvo = Typed(expected_type=Cfvo, )
    color = Typed(expected_type=Color, )

    def __init__(self,
                 minLength=None,
                 maxLength=None,
                 showValue=None,
                 cfvo=None,
                 color=None,
                ):
        self.minLength = minLength
        self.maxLength = maxLength
        self.showValue = showValue
        self.cfvo = cfvo
        self.color = color


class ColorScale(Serialisable):

    cfvo = Typed(expected_type=Cfvo, )
    color = Typed(expected_type=Color, )

    def __init__(self,
                 cfvo=None,
                 color=None,
                ):
        self.cfvo = cfvo
        self.color = color


class Rule(Serialisable):

    tagname = "cfRule"

    type = Set(values=(['expression', 'cellIs', 'colorScale', 'dataBar',
                        'iconSet', 'top10', 'uniqueValues', 'duplicateValues', 'containsText',
                        'notContainsText', 'beginsWith', 'endsWith', 'containsBlanks',
                        'notContainsBlanks', 'containsErrors', 'notContainsErrors', 'timePeriod',
                        'aboveAverage']))
    dxfId = Integer(allow_none=True)
    priority = Integer()
    stopIfTrue = Bool(allow_none=True)
    aboveAverage = Bool(allow_none=True)
    percent = Bool(allow_none=True)
    bottom = Bool(allow_none=True)
    operator = NoneSet(values=(['lessThan', 'lessThanOrEqual', 'equal',
                            'notEqual', 'greaterThanOrEqual', 'greaterThan', 'between', 'notBetween',
                            'containsText', 'notContains', 'beginsWith', 'endsWith']))
    text = String(allow_none=True)
    timePeriod = NoneSet(values=(['today', 'yesterday', 'tomorrow', 'last7Days',
                              'thisMonth', 'lastMonth', 'nextMonth', 'thisWeek', 'lastWeek',
                              'nextWeek']))
    rank = Integer(allow_none=True)
    stdDev = Integer(allow_none=True)
    equalAverage = Bool(allow_none=True)
    formula = Sequence(expected_type=str)
    colorScale = Typed(expected_type=ColorScale, allow_none=True)
    dataBar = Typed(expected_type=DataBar, allow_none=True)
    iconSet = Typed(expected_type=IconSet, allow_none=True)
    extLst = Typed(expected_type=ExtensionList, allow_none=True)

    __elements__ = ('colorScale', 'dataBar', 'extLst', 'iconSet', 'formula')

    def __init__(self,
                 type,
                 dxfId=None,
                 priority=None,
                 stopIfTrue=None,
                 aboveAverage=None,
                 percent=None,
                 bottom=None,
                 operator=None,
                 text=None,
                 timePeriod=None,
                 rank=None,
                 stdDev=None,
                 equalAverage=None,
                 formula=[],
                 colorScale=None,
                 dataBar=None,
                 iconSet=None,
                 extLst=None,
                ):
        self.type = type
        self.dxfId = dxfId
        self.priority = priority
        self.stopIfTrue = stopIfTrue
        self.aboveAverage = aboveAverage
        self.percent = percent
        self.bottom = bottom
        self.operator = operator
        self.text = text
        self.timePeriod = timePeriod
        self.rank = rank
        self.stdDev = stdDev
        self.equalAverage = equalAverage
        self.formula = formula
        self.colorScale = colorScale
        self.dataBar = dataBar
        self.iconSet = iconSet
        self.extLst = extLst


    @classmethod
    def create(cls, node):
        attrib = dict(node.attrib)
        formula = []
        for el in node:
            tag = localname(el)
            descriptor = getattr(cls, tag, None)
            if descriptor is None:
                continue
            if tag == "formula":
                formula.append(el.text)
            else:
                attrib[tag] = descriptor.expected_type.create(el)
        attrib['formula'] = formula
        return cls(**attrib)


    def serialise(self, tagname=None):
        attrib = dict(self)
        del attrib['formula']
        el = Element(self.tagname, attrib)

        for child in self.__elements__:
            obj = getattr(self, child)
            if obj is None:
                continue
            if child == "formula":
                for value in obj:
                    SubElement(el, "formula").text = value
            else:
                el.append(obj.serialise)
        return el
