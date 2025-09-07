from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
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
        date_ranges (Union[Unset, list[Any]]):
        numeric_ranges (Union[Unset, list[Any]]):
    """

    field: Union[Unset, str] = UNSET
    total: Union[Unset, int] = UNSET
    missing: Union[Unset, int] = UNSET
    terms: Union[Unset, list["TermFacetResult"]] = UNSET
    date_ranges: Union[Unset, list[Any]] = UNSET
    numeric_ranges: Union[Unset, list[Any]] = UNSET
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

        date_ranges: Union[Unset, list[Any]] = UNSET
        if not isinstance(self.date_ranges, Unset):
            date_ranges = self.date_ranges

        numeric_ranges: Union[Unset, list[Any]] = UNSET
        if not isinstance(self.numeric_ranges, Unset):
            numeric_ranges = self.numeric_ranges

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

        date_ranges = cast(list[Any], d.pop("date_ranges", UNSET))

        numeric_ranges = cast(list[Any], d.pop("numeric_ranges", UNSET))

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
