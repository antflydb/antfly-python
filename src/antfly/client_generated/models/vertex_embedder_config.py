from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VertexEmbedderConfig")


@_attrs_define
class VertexEmbedderConfig:
    """Configuration for Google Cloud Vertex AI embedding models (enterprise-grade).

    Uses Application Default Credentials (ADC) for authentication by default.
    Suitable for production deployments on Google Cloud Platform.

    **Authentication Priority:**
    1. credentials_path (path to service account key file)
    2. GOOGLE_APPLICATION_CREDENTIALS environment variable
    3. Application Default Credentials (ADC) - RECOMMENDED
       - In GCP: automatic (Cloud Run, GKE, Compute Engine)
       - Local dev: `gcloud auth application-default login`

    **Required IAM Permission:** `roles/aiplatform.user`

    **Supported Models:**
    - text-embedding-004 (latest, 768 dimensions)
    - textembedding-gecko@003, @002, @001 (legacy)
    - textembedding-gecko-multilingual@001 (multilingual support)
    - text-multilingual-embedding-002 (multilingual, 768 dimensions)
    - multimodalembedding (images, audio, video - 128/256/512/1408 dimensions)

        Example:
            {'provider': 'vertex', 'model': 'text-embedding-004', 'project_id': 'my-gcp-project', 'location': 'us-central1',
                'dimension': 768}

        Attributes:
            model (str): The name of the Vertex AI embedding model to use. Example: text-embedding-004.
            project_id (Union[Unset, str]): Google Cloud project ID. Can also be set via GOOGLE_CLOUD_PROJECT environment
                variable.
            location (Union[Unset, str]): Google Cloud region for Vertex AI API (e.g., 'us-central1', 'europe-west1'). Can
                also be set via GOOGLE_CLOUD_LOCATION. Defaults to 'us-central1'. Default: 'us-central1'.
            credentials_path (Union[Unset, str]): Path to service account JSON key file. Alternative to ADC for non-GCP
                environments.
            dimension (Union[Unset, int]): The dimension of the embedding vector. Model-specific (e.g., 768 for text-
                embedding-004, 128-1408 for multimodalembedding). Default: 768.
    """

    model: str
    project_id: Union[Unset, str] = UNSET
    location: Union[Unset, str] = "us-central1"
    credentials_path: Union[Unset, str] = UNSET
    dimension: Union[Unset, int] = 768
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model = self.model

        project_id = self.project_id

        location = self.location

        credentials_path = self.credentials_path

        dimension = self.dimension

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model": model,
            }
        )
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if location is not UNSET:
            field_dict["location"] = location
        if credentials_path is not UNSET:
            field_dict["credentials_path"] = credentials_path
        if dimension is not UNSET:
            field_dict["dimension"] = dimension

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model = d.pop("model")

        project_id = d.pop("project_id", UNSET)

        location = d.pop("location", UNSET)

        credentials_path = d.pop("credentials_path", UNSET)

        dimension = d.pop("dimension", UNSET)

        vertex_embedder_config = cls(
            model=model,
            project_id=project_id,
            location=location,
            credentials_path=credentials_path,
            dimension=dimension,
        )

        vertex_embedder_config.additional_properties = d
        return vertex_embedder_config

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
