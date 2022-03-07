from typing_extensions import TypedDict
from typing import Optional

from cv2 import waitKey
import cv2


class Facture(TypedDict):
    cout: int
    magasin: str
    code_concour: Optional[str]


val = 0
def reconnaitre_facture(mat):
    """
    Cette fonction localise une facture dans une image. Cette fonction
    retourne la facture découverte.
    """
    keys = [(ord('z'), (lambda x: x(0.01))), (ord('x'), (lambda x: x(-0.01))),
            (ord('q'), lambda _: exit(1337))]
    for code, func in keys:
        if code == waitKey(10):
            result = func(lambda: val)
            # If it's a slider func
            if str(type(result)) == "<class 'function'>":
                newv = val + result()
                print('old val: %d, new val: %d', val, newv)
                val = newv
                break
    mat = cv2.cvtColor(mat, cv2.COLOR_BGR2RGB)
    cv2.denoise_TVL1(mat, None, 1, niters=3)
    return mat
