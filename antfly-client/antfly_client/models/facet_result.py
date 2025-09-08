from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.date_range_result import DateRangeResult
    from ..models.numeric_range_result import NumericRangeResult
    from ..models.term_facet_result import TermFacetResult


T = TypeVar("T", bound="FacetResult")


@_attrs_define
class FacetResult:
    """
    Attributes:
        field (Union[Unset, str]):
        total (Union[Unset, int]):
        missing (Union[Unset, int]):
        terms (Union[Unset, list['TermFacetResult']]):
        date_ranges (Union[Unset, list['DateRangeResult']]):
        numeric_ranges (Union[Unset, list['NumericRangeResult']]):
    """

    field: Union[Unset, str] = UNSET
    total: Union[Unset, int] = UNSET
    missing: Union[Unset, int] = UNSET
    terms: Union[Unset, list["TermFacetResult"]] = UNSET
    date_ranges: Union[Unset, list["DateRangeResult"]] = UNSET
    numeric_ranges: Union[Unset, list["NumericRangeResult"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field = self.field

        total = self.total

        missing = self.missing

        terms: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.terms, Unset):
            terms = []
            for terms_item_data in self.terms:
                terms_item = terms_item_data.to_dict()
                terms.append(terms_item)

        date_ranges: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.date_ranges, Unset):
            date_ranges = []
            for date_ranges_item_data in self.date_ranges:
                date_ranges_item = date_ranges_item_data.to_dict()
                date_ranges.append(date_ranges_item)

        numeric_ranges: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.numeric_ranges, Unset):
            numeric_ranges = []
            for numeric_ranges_item_data in self.numeric_ranges:
                numeric_ranges_item = numeric_ranges_item_data.to_dict()
                numeric_ranges.append(numeric_ranges_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field is not UNSET:
            field_dict["field"] = field
        if total is not UNSET:
            field_dict["total"] = total
        if missing is not UNSET:
            field_dict["missing"] = missing
        if terms is not UNSET:
            field_dict["terms"] = terms
        if date_ranges is not UNSET:
            field_dict["date_ranges"] = date_ranges
        if numeric_ranges is not UNSET:
            field_dict["numeric_ranges"] = numeric_ranges

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.date_range_result import DateRangeResult
        from ..models.numeric_range_result import NumericRangeResult
        from ..models.term_facet_result import TermFacetResult

        d = dict(src_dict)
        field = d.pop("field", UNSET)

        total = d.pop("total", UNSET)

        missing = d.pop("missing", UNSET)

        terms = []
        _terms = d.pop("terms", UNSET)
        for terms_item_data in _terms or []:
            terms_item = TermFacetResult.from_dict(terms_item_data)

            terms.append(terms_item)

        date_ranges = []
        _date_ranges = d.pop("date_ranges", UNSET)
        for date_ranges_item_data in _date_ranges or []:
            date_ranges_item = DateRangeResult.from_dict(date_ranges_item_data)

            date_ranges.append(date_ranges_item)

        numeric_ranges = []
        _numeric_ranges = d.pop("numeric_ranges", UNSET)
        for numeric_ranges_item_data in _numeric_ranges or []:
            numeric_ranges_item = NumericRangeResult.from_dict(numeric_ranges_item_data)

            numeric_ranges.append(numeric_ranges_item)

        facet_result = cls(
            field=field,
            total=total,
            missing=missing,
            terms=terms,
            date_ranges=date_ranges,
            numeric_ranges=numeric_ranges,
        )

        facet_result.additional_properties = d
        return facet_result

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
