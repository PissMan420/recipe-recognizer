from typing_extensions import TypedDict
from typing import Optional

import cv2


class Facture(TypedDict):
    cout: int
    magasin: str
    code_concour: Optional[str]


def reconnaitre_facture(mat):
    """Cette fonction localise une facture dans une image."""
