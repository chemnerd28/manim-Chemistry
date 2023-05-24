from manim import (
    VGroup,
    WHITE,
    BLACK,
    BLUE,
    Rectangle,
    color_gradient,
    Text,
    Tex,
    RIGHT,
    ORIGIN,
    DOWN,
)
import pandas as pd
import numpy as np

ElementDict = {
    1: {'Element': 'Hydrogen', 'Symbol': 'H', 'AtomicMass': 1.007, 'Color': '#ffffff'},
    2: {'Element': 'Helium', 'Symbol': 'He', 'AtomicMass': 4.002, 'Color': '#d9ffff'},
    3: {'Element': 'Lithium', 'Symbol': 'Li', 'AtomicMass': 6.941, 'Color': '#cc80ff'},
    4: {'Element': 'Beryllium', 'Symbol': 'Be', 'AtomicMass': 9.012, 'Color': '#c2ff00'},
    5: {'Element': 'Boron', 'Symbol': 'B', 'AtomicMass': 10.811, 'Color': '#ffb5b5'},
    6: {'Element': 'Carbon', 'Symbol': 'C', 'AtomicMass': 12.011, 'Color': '#909090'},
    7: {'Element': 'Nitrogen', 'Symbol': 'N', 'AtomicMass': 14.007, 'Color': '#3050f8'},
    8: {'Element': 'Oxygen', 'Symbol': 'O', 'AtomicMass': 15.999, 'Color': '#ff0d0d'},
    9: {'Element': 'Fluorine', 'Symbol': 'F', 'AtomicMass': 18.998, 'Color': '#90e050'},
    10: {'Element': 'Neon', 'Symbol': 'Ne', 'AtomicMass': 20.18, 'Color': '#b3e3f5'},
    11: {'Element': 'Sodium', 'Symbol': 'Na', 'AtomicMass': 22.99, 'Color': '#ab5cf2'},
    12: {'Element': 'Magnesium', 'Symbol': 'Mg', 'AtomicMass': 24.305, 'Color': '#8aff00'},
    13: {'Element': 'Aluminum', 'Symbol': 'Al', 'AtomicMass': 26.982, 'Color': '#bfa6a6'},
    14: {'Element': 'Silicon', 'Symbol': 'Si', 'AtomicMass': 28.086, 'Color': '#f0c8a0'},
    15: {'Element': 'Phosphorus', 'Symbol': 'P', 'AtomicMass': 30.974, 'Color': '#ff8000'},
    16: {'Element': 'Sulfur', 'Symbol': 'S', 'AtomicMass': 32.065, 'Color': '#ffff30'},
    17: {'Element': 'Chlorine', 'Symbol': 'Cl', 'AtomicMass': 35.453, 'Color': '#1ff01f'},
    18: {'Element': 'Argon', 'Symbol': 'Ar', 'AtomicMass': 39.948, 'Color': '#80d1e3'},
    19: {'Element': 'Potassium', 'Symbol': 'K', 'AtomicMass': 39.098, 'Color': '#8f40d4'},
    20: {'Element': 'Calcium', 'Symbol': 'Ca', 'AtomicMass': 40.078, 'Color': '#3dff00'},
    21: {'Element': 'Scandium', 'Symbol': 'Sc', 'AtomicMass': 44.956, 'Color': '#e6e6e6'},
    22: {'Element': 'Titanium', 'Symbol': 'Ti', 'AtomicMass': 47.867, 'Color': '#bfc2c7'},
    23: {'Element': 'Vanadium', 'Symbol': 'V', 'AtomicMass': 50.942, 'Color': '#a6a6ab'},
    24: {'Element': 'Chromium', 'Symbol': 'Cr', 'AtomicMass': 51.996, 'Color': '#8a99c7'},
    25: {'Element': 'Manganese', 'Symbol': 'Mn', 'AtomicMass': 54.938, 'Color': '#9c7ac7'},
    26: {'Element': 'Iron', 'Symbol': 'Fe', 'AtomicMass': 55.845, 'Color': '#e06633'},
    27: {'Element': 'Cobalt', 'Symbol': 'Co', 'AtomicMass': 58.933, 'Color': '#f090a0'},
    28: {'Element': 'Nickel', 'Symbol': 'Ni', 'AtomicMass': 58.693, 'Color': '#50d050'},
    29: {'Element': 'Copper', 'Symbol': 'Cu', 'AtomicMass': 63.546, 'Color': '#c88033'},
    30: {'Element': 'Zinc', 'Symbol': 'Zn', 'AtomicMass': 65.38, 'Color': '#7d80b0'},
    31: {'Element': 'Gallium', 'Symbol': 'Ga', 'AtomicMass': 69.723, 'Color': '#c28f8f'},
    32: {'Element': 'Germanium', 'Symbol': 'Ge', 'AtomicMass': 72.64, 'Color': '#668f8f'},
    33: {'Element': 'Arsenic', 'Symbol': 'As', 'AtomicMass': 74.922, 'Color': '#bd80e3'},
    34: {'Element': 'Selenium', 'Symbol': 'Se', 'AtomicMass': 78.96, 'Color': '#ffa100'},
    35: {'Element': 'Bromine', 'Symbol': 'Br', 'AtomicMass': 79.904, 'Color': '#a62929'},
    36: {'Element': 'Krypton', 'Symbol': 'Kr', 'AtomicMass': 83.798, 'Color': '#5cb8d1'},
    37: {'Element': 'Rubidium', 'Symbol': 'Rb', 'AtomicMass': 85.468, 'Color': '#702eb0'},
    38: {'Element': 'Strontium', 'Symbol': 'Sr', 'AtomicMass': 87.62, 'Color': '#00ff00'},
    39: {'Element': 'Yttrium', 'Symbol': 'Y', 'AtomicMass': 88.906, 'Color': '#94ffff'},
    40: {'Element': 'Zirconium', 'Symbol': 'Zr', 'AtomicMass': 91.224, 'Color': '#94e0e0'},
    41: {'Element': 'Niobium', 'Symbol': 'Nb', 'AtomicMass': 92.906, 'Color': '#73c2c9'},
    42: {'Element': 'Molybdenum', 'Symbol': 'Mo', 'AtomicMass': 95.96, 'Color': '#54b5b5'},
    43: {'Element': 'Technitium', 'Symbol': 'Tc', 'AtomicMass': 98.0, 'Color': '#3b9e9e'},
    44: {'Element': 'Ruthenium', 'Symbol': 'Ru', 'AtomicMass': 101.07, 'Color': '#248f8f'},
    45: {'Element': 'Rhodium', 'Symbol': 'Rh', 'AtomicMass': 102.906, 'Color': '#0a7d8c'},
    46: {'Element': 'Palladium', 'Symbol': 'Pd', 'AtomicMass': 106.42, 'Color': '#006985'},
    47: {'Element': 'Silver', 'Symbol': 'Ag', 'AtomicMass': 107.868, 'Color': '#c0c0c0'},
    48: {'Element': 'Cadmium', 'Symbol': 'Cd', 'AtomicMass': 112.411, 'Color': '#ffd98f'},
    49: {'Element': 'Indium', 'Symbol': 'In', 'AtomicMass': 114.818, 'Color': '#a67573'},
    50: {'Element': 'Tin', 'Symbol': 'Sn', 'AtomicMass': 118.71, 'Color': '#668080'},
    51: {'Element': 'Antimony', 'Symbol': 'Sb', 'AtomicMass': 121.76, 'Color': '#9e63b5'},
    52: {'Element': 'Tellerium', 'Symbol': 'Te', 'AtomicMass': 127.6, 'Color': '#d47a00'},
    53: {'Element': 'Iodine', 'Symbol': 'I', 'AtomicMass': 126.904, 'Color': '#940094'},
    54: {'Element': 'Xeon', 'Symbol': 'Xe', 'AtomicMass': 131.293, 'Color': '#429eb0'},
    55: {'Element': 'Cesium', 'Symbol': 'Cs', 'AtomicMass': 132.905, 'Color': '#57178f'},
    56: {'Element': 'Barium', 'Symbol': 'Ba', 'AtomicMass': 137.327, 'Color': '#00c900'},
    57: {'Element': 'Lanthanum', 'Symbol': 'La', 'AtomicMass': 138.905, 'Color': '#70d4ff'},
    58: {'Element': 'Cerium', 'Symbol': 'Ce', 'AtomicMass': 140.116, 'Color': '#ffffc7'}, 
    59: {'Element': 'Praseodymium', 'Symbol': 'Pr', 'AtomicMass': 140.908, 'Color': '#d9ffc7'},
    60: {'Element': 'Neodymium', 'Symbol': 'Nd', 'AtomicMass': 144.242, 'Color': '#c7ffc7'},
    61: {'Element': 'Promethium', 'Symbol': 'Pm', 'AtomicMass': 145.0, 'Color': '#a3ffc7'},
    62: {'Element': 'Samarium', 'Symbol': 'Sm', 'AtomicMass': 150.36, 'Color': '#8fffc7'},
    63: {'Element': 'Europium', 'Symbol': 'Eu', 'AtomicMass': 151.964, 'Color': '#61ffc7'},
    64: {'Element': 'Gadolinium', 'Symbol': 'Gd', 'AtomicMass': 157.25, 'Color': '#45ffc7'},
    65: {'Element': 'Terbium', 'Symbol': 'Tb', 'AtomicMass': 158.925, 'Color': '#30ffc7'},
    66: {'Element': 'Dysprosium', 'Symbol': 'Dy', 'AtomicMass': 162.5, 'Color': '#1fffc7'},
    67: {'Element': 'Holmium', 'Symbol': 'Ho', 'AtomicMass': 164.93, 'Color': '#00ff9c'},
    68: {'Element': 'Erbium', 'Symbol': 'Er', 'AtomicMass': 167.259, 'Color': '#00e675'},
    69: {'Element': 'Thulium', 'Symbol': 'Tm', 'AtomicMass': 168.934, 'Color': '#00d452'},
    70: {'Element': 'Ytterbium', 'Symbol': 'Yb', 'AtomicMass': 173.054, 'Color': '#00bf38'},
    71: {'Element': 'Lutetium', 'Symbol': 'Lu', 'AtomicMass': 174.967, 'Color': '#00ab24'},
    72: {'Element': 'Hafnium', 'Symbol': 'Hf', 'AtomicMass': 178.49, 'Color': '#4dc2ff'},
    73: {'Element': 'Tantalum', 'Symbol': 'Ta', 'AtomicMass': 180.948, 'Color': '#4da6ff'},
    74: {'Element': 'Tungsten', 'Symbol': 'W', 'AtomicMass': 183.84, 'Color': '#2194d6'},
    75: {'Element': 'Rhenium', 'Symbol': 'Re', 'AtomicMass': 186.207, 'Color': '#267dab'},
    76: {'Element': 'Osmium', 'Symbol': 'Os', 'AtomicMass': 190.23, 'Color': '#266696'},
    77: {'Element': 'Iridium', 'Symbol': 'Ir', 'AtomicMass': 192.217, 'Color': '#175487'},
    78: {'Element': 'Platinum', 'Symbol': 'Pt', 'AtomicMass': 195.084, 'Color': '#d0d0e0'},
    79: {'Element': 'Gold', 'Symbol': 'Au', 'AtomicMass': 196.967, 'Color': '#ffd123'},
    80: {'Element': 'Mercury', 'Symbol': 'Hg', 'AtomicMass': 200.59, 'Color': '#b8b8d0'},
    81: {'Element': 'Thallium', 'Symbol': 'Tl', 'AtomicMass': 204.383, 'Color': '#a6544d'},
    82: {'Element': 'Lead', 'Symbol': 'Pb', 'AtomicMass': 207.2, 'Color': '#575961'},
    83: {'Element': 'Bismuth', 'Symbol': 'Bi', 'AtomicMass': 208.98, 'Color': '#9e4fb5'},
    84: {'Element': 'Polonium', 'Symbol': 'Po', 'AtomicMass': 210.0, 'Color': '#ab5c00'},
    85: {'Element': 'Astatine', 'Symbol': 'At', 'AtomicMass': 210.0, 'Color': '#754f45'},
    86: {'Element': 'Radon', 'Symbol': 'Rn', 'AtomicMass': 222.0, 'Color': '#428296'},
    87: {'Element': 'Francium', 'Symbol': 'Fr', 'AtomicMass': 223.0, 'Color': '#420066'},
    88: {'Element': 'Radium', 'Symbol': 'Ra', 'AtomicMass': 226.0, 'Color': '#007d00'},
    89: {'Element': 'Actinium', 'Symbol': 'Ac', 'AtomicMass': 227.0, 'Color': '#70abfa'},
    90: {'Element': 'Thorium', 'Symbol': 'Th', 'AtomicMass': 232.038, 'Color': '#00baff'},
    91: {'Element': 'Protactinium', 'Symbol': 'Pa', 'AtomicMass': 231.036, 'Color': '#00a1ff'},
    92: {'Element': 'Uranium', 'Symbol': 'U', 'AtomicMass': 238.029, 'Color': '#008fff'},
    93: {'Element': 'Neptunium', 'Symbol': 'Np', 'AtomicMass': 237.0, 'Color': '#0080ff'},
    94: {'Element': 'Plutonium', 'Symbol': 'Pu', 'AtomicMass': 244.0, 'Color': '#006bff'},
    95: {'Element': 'Americium', 'Symbol': 'Am', 'AtomicMass': 243.0, 'Color': '#545cf2'},
    96: {'Element': 'Curium', 'Symbol': 'Cm', 'AtomicMass': 247.0, 'Color': '#785ce3'},
    97: {'Element': 'Berkelium', 'Symbol': 'Bk', 'AtomicMass': 247.0, 'Color': '#8a4fe3'},
    98: {'Element': 'Californium', 'Symbol': 'Cf', 'AtomicMass': 251.0, 'Color': '#a136d4'},
    99: {'Element': 'Einsteinium', 'Symbol': 'Es', 'AtomicMass': 252.0, 'Color': '#b31fd4'},
    100: {'Element': 'Fermium', 'Symbol': 'Fm', 'AtomicMass': 257.0, 'Color': '#b31fba'},
    101: {'Element': 'Mendelevium', 'Symbol': 'Md', 'AtomicMass': 258.0, 'Color': '#b30da6'},
    102: {'Element': 'Nobelium', 'Symbol': 'No', 'AtomicMass': 259.0, 'Color': '#bd0d87'},
    103: {'Element': 'Lawrencium', 'Symbol': 'Lr', 'AtomicMass': 262.0, 'Color': '#c70066'},
    104: {'Element': 'Rutherfordium', 'Symbol': 'Rf', 'AtomicMass': 261.0, 'Color': '#cc0059'},
    105: {'Element': 'Dubnium', 'Symbol': 'Db', 'AtomicMass': 262.0, 'Color': '#d1004f'},
    106: {'Element': 'Seaborgium', 'Symbol': 'Sg', 'AtomicMass': 266.0, 'Color': '#d90045'},
    107: {'Element': 'Bohrium', 'Symbol': 'Bh', 'AtomicMass': 264.0, 'Color': '#e00038'},
    108: {'Element': 'Hassium', 'Symbol': 'Hs', 'AtomicMass': 267.0, 'Color': '#e6002e'},
    109: {'Element': 'Meitnerium', 'Symbol': 'Mt', 'AtomicMass': 268.0, 'Color': '#eb0026'},
    110: {'Element': 'Darmstadtium', 'Symbol': 'Ds', 'AtomicMass': 271.0, 'Color': '#eb0026'},
    111: {'Element': 'Roentgenium', 'Symbol': 'Rg', 'AtomicMass': 272.0, 'Color': '#eb0026'},
    112: {'Element': 'Copernicium', 'Symbol': 'Cn', 'AtomicMass': 285.0, 'Color': '#eb0026'},
    113: {'Element': 'Nihonium', 'Symbol': 'Nh', 'AtomicMass': 284.0, 'Color': '#eb0026'},
    114: {'Element': 'Flerovium', 'Symbol': 'Fl', 'AtomicMass': 289.0, 'Color': '#eb0026'},
    115: {'Element': 'Moscovium', 'Symbol': 'Mc', 'AtomicMass': 288.0, 'Color': '#eb0026'},
    116: {'Element': 'Livermorium', 'Symbol': 'Lv', 'AtomicMass': 292.0, 'Color': '#eb0026'},
    117: {'Element': 'Tennessine', 'Symbol': 'Ts', 'AtomicMass': 295.0, 'Color': '#eb0026'},
    118: {'Element': 'Oganesson', 'Symbol': 'Og', 'AtomicMass': 294.0, 'Color': '#eb0026'}
    }
class MElementObject(VGroup):
    def __init__(
        self,
        atomic_number=1,
        atomic_mass=1,
        element_name="Hydrogen",
        element_symbol="H",
        coloring=BLACK,
        fill_colors=(WHITE, BLUE),
        gradient=10,
        opacity=1,
        text_color=BLACK,
        **kwargs,
    ):
        VGroup.__init__(self, **kwargs)
        self.atomic_number = atomic_number
        self.atomic_mass = atomic_mass
        self.element_name = element_name
        self.element_symbol = element_symbol
        self.coloring = coloring
        self.fill_colors = fill_colors
        self.gradient = gradient
        self.opacity = opacity
        self.text_color = text_color

        element_frame = self.create_frame_with_text()

        self.add(element_frame)

    def frame_name_width_ratio(self, frame, name_text):
        return frame.get_width() / (1.25 * name_text.get_width())

    def max_height_ratio(self, name_text):
        text_height = name_text.get_height()
        if text_height > 0.3:
            ratio = 0.3 / text_height
            name_text.scale(ratio)

        return name_text

    def create_frame_base(self):
        frame_rectangle = (
            Rectangle(
                height=2.8,
                width=2,
                color=self.coloring,
                stroke_width=0.2,
                fill_opacity=self.opacity,
            )
            .scale(0.8)
            .set_fill(color_gradient(self.fill_colors, self.gradient))
        )

        return frame_rectangle

    def create_frame_with_text(self):
        frame_rectangle = self.create_frame_base()
        symbol_text = (
            Text(self.element_symbol, color=self.text_color)
            .scale(1.1)
            .move_to(frame_rectangle.get_center())
        )
        name_text = (
            Text(self.element_name, color=self.text_color)
            .scale(0.2)
            .next_to(frame_rectangle, DOWN, buff=-0.4)
        )
        atomic_number_text = (
            Tex(str(self.atomic_number), color=self.text_color)
            .scale(0.65)
            .next_to(
                frame_rectangle,
                frame_rectangle.get_top() + frame_rectangle.get_left(),
                buff=-0.35,
            )
        )

        ratio = self.frame_name_width_ratio(frame=frame_rectangle, name_text=name_text)
        name_text.scale(ratio)
        name_text = self.max_height_ratio(name_text)

        shifting_ammount = 0
        if 10 <= self.atomic_number:
            shifting_ammount += 0.15

        if self.atomic_number > 100:
            shifting_ammount += 0.15

        atomic_number_text.shift(shifting_ammount * RIGHT)

        return VGroup(frame_rectangle, symbol_text, name_text, atomic_number_text)
    
    def ElementData(atomic_number, **kwargs):
        return MElementObject(
            atomic_number = int(atomic_number),
            atomic_mass=int(ElementDict[atomic_number]['AtomicMass']),
            element_name = str(ElementDict[atomic_number]['Element']),
            element_symbol = str(ElementDict[atomic_number]['Symbol']),
            fill_colors = [ElementDict[atomic_number]['Color'], WHITE]
        )
    #def from_csv_file_data(filename, atomic_number, **kwargs):
        # TODO: Add option to set manually colors.
        # TODO: Create a table that adds this data in a prettier way.
        #df = pd.read_csv(filename)
        #element = df.loc[df["AtomicNumber"] == atomic_number].squeeze().to_dict()

        #return MElementObject(
            #atomic_number=atomic_number,
            #atomic_mass=element.get("AtomicMass"),
            #element_name=element.get("Name"),
            #element_symbol=element.get("Symbol"),
            #fill_colors=[element.get("Color"), WHITE],
       # )


class PeriodicTable(VGroup):
    # TODO Change to english database
    def __init__(self, data_file, *vmobjects, **kwargs):
        VGroup.__init__(self, *vmobjects, **kwargs)
        self.data_file = data_file
        self.table = self.add_elements()

        self.add(self.table)

    def add_elements(self):
        positions = self.elements_position_dict()
        base_element = MElementObject()
        mult_array = np.array([base_element.get_width(), -base_element.get_height(), 0])

        table = VGroup()
        for element, position in positions.items():
            new_position = np.multiply(mult_array, np.array(position))
            new_element = MElementObject.from_csv_file_data(
                self.data_file, element
            ).move_to(new_position)

            table.add(new_element)

        table.move_to(ORIGIN).scale(0.25)
        return table

    def elements_position_dict(self):
        # TODO: Think of a better way of doing this. However, it works and looks good
        positions = {
            1: [0, 0, 0],
            2: [17, 0, 0],
            3: [0, 1, 0],
            4: [1, 1, 0],
            5: [12, 1, 0],
            6: [13, 1, 0],
            7: [14, 1, 0],
            8: [15, 1, 0],
            9: [16, 1, 0],
            10: [17, 1, 0],
            11: [0, 2, 0],
            12: [1, 2, 0],
            13: [12, 2, 0],
            14: [13, 2, 0],
            15: [14, 2, 0],
            16: [15, 2, 0],
            17: [16, 2, 0],
            18: [17, 2, 0],
            19: [0, 3, 0],
            20: [1, 3, 0],
            21: [2, 3, 0],
            22: [3, 3, 0],
            23: [4, 3, 0],
            24: [5, 3, 0],
            25: [6, 3, 0],
            26: [7, 3, 0],
            27: [8, 3, 0],
            28: [9, 3, 0],
            29: [10, 3, 0],
            30: [11, 3, 0],
            31: [12, 3, 0],
            32: [13, 3, 0],
            33: [14, 3, 0],
            34: [15, 3, 0],
            35: [16, 3, 0],
            36: [17, 3, 0],
            37: [0, 4, 0],
            38: [1, 4, 0],
            39: [2, 4, 0],
            40: [3, 4, 0],
            41: [4, 4, 0],
            42: [5, 4, 0],
            43: [6, 4, 0],
            44: [7, 4, 0],
            45: [8, 4, 0],
            46: [9, 4, 0],
            47: [10, 4, 0],
            48: [11, 4, 0],
            49: [12, 4, 0],
            50: [13, 4, 0],
            51: [14, 4, 0],
            52: [15, 4, 0],
            53: [16, 4, 0],
            54: [17, 4, 0],
            55: [0, 5, 0],
            56: [1, 5, 0],
            57: [2, 7.5, 0],
            58: [3, 7.5, 0],
            59: [4, 7.5, 0],
            60: [5, 7.5, 0],
            61: [6, 7.5, 0],
            62: [7, 7.5, 0],
            63: [8, 7.5, 0],
            64: [9, 7.5, 0],
            65: [10, 7.5, 0],
            66: [11, 7.5, 0],
            67: [12, 7.5, 0],
            68: [13, 7.5, 0],
            69: [14, 7.5, 0],
            70: [15, 7.5, 0],
            71: [2, 5, 0],
            72: [3, 5, 0],
            73: [4, 5, 0],
            74: [5, 5, 0],
            75: [6, 5, 0],
            76: [7, 5, 0],
            77: [8, 5, 0],
            78: [9, 5, 0],
            79: [10, 5, 0],
            80: [11, 5, 0],
            81: [12, 5, 0],
            82: [13, 5, 0],
            83: [14, 5, 0],
            84: [15, 5, 0],
            85: [16, 5, 0],
            86: [17, 5, 0],
            87: [0, 6, 0],
            88: [1, 6, 0],
            89: [2, 8.5, 0],
            90: [3, 8.5, 0],
            91: [4, 8.5, 0],
            92: [5, 8.5, 0],
            93: [6, 8.5, 0],
            94: [7, 8.5, 0],
            95: [8, 8.5, 0],
            96: [9, 8.5, 0],
            97: [10, 8.5, 0],
            98: [11, 8.5, 0],
            99: [12, 8.5, 0],
            100: [13, 8.5, 0],
            101: [14, 8.5, 0],
            102: [15, 8.5, 0],
            103: [2, 6, 0],
            104: [3, 6, 0],
            105: [4, 6, 0],
            106: [5, 6, 0],
            107: [6, 6, 0],
            108: [7, 6, 0],
            109: [8, 6, 0],
            110: [9, 6, 0],
            111: [10, 6, 0],
            112: [11, 6, 0],
            113: [12, 6, 0],
            114: [13, 6, 0],
            115: [14, 6, 0],
            116: [15, 6, 0],
            117: [16, 6, 0],
            118: [17, 6, 0],
        }
        return positions
