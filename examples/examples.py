from manim import Scene, ThreeDScene
from manim_chemistry import (
    MMoleculeObject,
    ThreeDMolecule,
    MElementObject,
    PeriodicTable,
)

from pathlib import Path

script_path = Path(__file__).absolute().parent
files_path = script_path / "element_files"

# 2D Molecule example
class Draw2DMorphine(Scene):
    def construct(self):    
        self.add(MMoleculeObject.from_mol_file(filename=files_path / "morphine.mol"))


# 3D Molecule example
class Draw3DMorphine(ThreeDScene):
    def construct(self):
        self.add(ThreeDMolecule.from_mol_file(filename=files_path / "morphine3d.mol", source_csv=files_path / "Elementos.csv"))
        self.wait()


# Element example
class DrawCarbonElement(Scene):
    def construct(self):
        self.add(
            MElementObject.from_csv_file_data(
                filename=files_path / "Elementos.csv", atomic_number=6
            )
        )


# Periodic Table example
class DrawPeriodicTable(Scene):
    def construct(self):
        self.add(PeriodicTable(data_file=files_path / "Elementos.csv"))


# Orbitals example #TODO
