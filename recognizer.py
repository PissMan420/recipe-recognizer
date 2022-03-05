from typing_extensions import TypedDict

import cv2


class Facture(TypedDict):
    cout: int
    magasin: str
    code_concour: str | None


def reconnaitre_facture(mat):
    """Cette fonction localise une facture dans une image."""
