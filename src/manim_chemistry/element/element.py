import pandas as pd
import manim_chemistry.periodic_table.ED as ed 

class Element:
    def __repr__(self) -> str:
        return f"Element {self.atomic_number}: {self.name} ({self.symbol})"

    def __init__(
        self,
        symbol: str = "H",
        name: str = "H",
        atomic_number: int = 1,
        mass: float = 1.008,
        color: str or None = "#FFFFFF",
    ):
        self.symbol = symbol
        self.name = name
        self.atomic_number = atomic_number
        self.mass = mass
        self.color = color or "#ff00ff"

    def from_ED(element):
# Dictionary language does not currently matter in this step, so it defaults to English for ease of use.

        use_valid_reference_string = f"What are you doing? Pass a valid atomic reference. {element} is NOT a valid reference"
        def elementLookUp(element):
            if isinstance(element, str):
                for d in ed.English:
                    if element in ed.English[d].values():
                        poop = d
                        return poop 
            elif isinstance(element, int) and element < 118:
                poop = element
                return poop
            else:
                raise Exception(use_valid_reference_string)

        return Element(
            symbol=ed.English[elementLookUp(element)]["Symbol"],
            name=ed.English[elementLookUp(element)]["Element"],
            atomic_number=elementLookUp(element),
            mass=ed.English[elementLookUp(element)]["AtomicMass"],
            color=ed.English[elementLookUp(element)]["Color"],
        )

#    def from_csv_file(filename, element: str or int):
#        use_valid_reference_string = f"What are you doing? Pass a valid atomic reference. {element} is NOT a valid reference"
#        data = pd.read_csv(filename, index_col=False)
#
#        if isinstance(element, str):
#            search_column = "Symbol"
#
#        elif isinstance(element, int) and element < 118:
#            search_column = "AtomicNumber"
#
#        else:
#            raise Exception(use_valid_reference_string)
#
#        subdata = data.loc[data[search_column] == element]
#
#        if subdata.empty:
#            raise Exception(use_valid_reference_string)
#
#        element_data = subdata.squeeze().to_dict()
#
#        return Element(
#            symbol=element_data["Symbol"],
#            name=element_data["Name"],
#            atomic_number=element_data["AtomicNumber"],
#            mass=element_data["AtomicMass"],
#            color=element_data["Color"],
#        )
