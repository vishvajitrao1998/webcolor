from django.shortcuts import render
import numpy as np

# Create your views here.

def home(request):
    colors = [
    {"name": "Red", "hex": "#FF0000", "rgb": (255, 0, 0)},
    {"name": "Green", "hex": "#008000", "rgb": (0, 128, 0)},
    {"name": "Blue", "hex": "#0000FF", "rgb": (0, 0, 255)},
    {"name": "Black", "hex": "#000000", "rgb": (0, 0, 0)},
    {"name": "White", "hex": "#FFFFFF", "rgb": (255, 255, 255)},
    {"name": "Yellow", "hex": "#FFFF00", "rgb": (255, 255, 0)},
    {"name": "Orange", "hex": "#FFA500", "rgb": (255, 165, 0)},
    {"name": "Pink", "hex": "#FFC0CB", "rgb": (255, 192, 203)},
    {"name": "Purple", "hex": "#800080", "rgb": (128, 0, 128)},
    {"name": "Gray", "hex": "#808080", "rgb": (128, 128, 128)},
    {"name": "Brown", "hex": "#A52A2A", "rgb": (165, 42, 42)},
    {"name": "Cyan", "hex": "#00FFFF", "rgb": (0, 255, 255)},
    {"name": "Magenta", "hex": "#FF00FF", "rgb": (255, 0, 255)},
    {"name": "Maroon", "hex": "#800000", "rgb": (128, 0, 0)},
    {"name": "Olive", "hex": "#808000", "rgb": (128, 128, 0)},
    {"name": "Teal", "hex": "#008080", "rgb": (0, 128, 128)},
    {"name": "Navy", "hex": "#000080", "rgb": (0, 0, 128)},
    {"name": "Gold", "hex": "#FFD700", "rgb": (255, 215, 0)},
    {"name": "Beige", "hex": "#F5F5DC", "rgb": (245, 245, 220)},
    {"name": "Coral", "hex": "#FF7F50", "rgb": (255, 127, 80)}
    ]

    return render(request, 'home.html', {"colors": colors})


def rgbtohex(request):
    hex_codes = [
    "#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FFA500", "#800080", "#FFC0CB",
    "#808080", "#000000", "#FFFFFF", "#008000", "#800000", "#00FFFF", "#FF00FF",
    "#808000", "#008080", "#000080", "#A52A2A", "#D2691E", "#DC143C", "#B8860B",
    "#556B2F", "#FF1493", "#FFD700",    "#778899", "#B0C4DE", "#32CD32", "#FAFAD2", "#FFB6C1", "#FFA07A", "#20B2AA",
    "#00CED1", "#9400D3", "#FF4500", "#DA70D6", "#EEE8AA", "#98FB98", "#AFEEEE",
    "#DB7093", "#FFDAB9", "#CD853F", "#FFC0CB", "#DDA0DD", "#B0E0E6", "#800000",
    "#4682B4", "#D2B48C", "#008080", "#40E0D0", "#EE82EE", "#F5DEB3", "#F5F5DC",
    "#A0522D", "#B22222", "#5F9EA0", "#7FFF00", "#7FFFD4", "#6495ED", "#DC143C",
    "#00FA9A", "#00FF7F", "#FF6347", "#6B8E23", "#483D8B", "#2F4F4F", "#FAEBD7",
    "#F0E68C", "#E6E6FA", "#FFFACD", "#F8F8FF", "#FF69B4", "#E0FFFF"
    ]
    return render(request, 'rgb-to-hex.html', {"hex_codes": hex_codes})


def hextorgb(request):
    hex_codes = [
    "#1E90FF", "#BA55D3", "#9370DB", "#3CB371", "#191970", "#FFE4E1", "#FFE4B5",
    "#FFEBCD", "#FFDEAD", "#FFF5EE", "#FFF8DC", "#FFFACD", "#FDF5E6", "#F5F5F5",
    "#F0FFF0", "#F0F8FF", "#E6E6FA", "#E0FFFF", "#D8BFD8", "#D3D3D3", "#C71585",
    "#BDB76B", "#BC8F8F", "#B0E0E6", "#8B0000", "#8B008B", "#8B4513", "#7B68EE",
    "#6A5ACD", "#5F9EA0", "#4B0082", "#4682B4", "#4169E1", "#2E8B57", "#228B22",
    "#191970", "#0000CD", "#00008B", "#000080", "#708090", "#778899", "#7CFC00",
    "#6B8E23", "#66CDAA", "#48D1CC", "#00CED1", "#1E90FF", "#20B2AA", "#4682B4",
    "#5F9EA0", "#6A5ACD", "#7B68EE", "#8B0000", "#8B008B", "#8B4513", "#90EE90",
    "#98FB98", "#9ACD32", "#A9A9A9", "#B0C4DE", "#B22222", "#BC8F8F", "#BDB76B",
    "#C0C0C0", "#D2691E", "#DAA520", "#DC143C", "#E9967A", "#F4A460", "#FA8072",
    "#F5DEB3", "#FFE4C4", "#FFEFD5", "#FFFAF0", "#8B4513", "#A0522D", "#D2691E", "#CD853F", "#DEB887", "#F4A460"
    ]
    return render(request, 'hex-to-rgb.html', {"hex_codes": hex_codes})


def color_palettes(request):
    return render(request, 'color-palettes.html')


def color_chart(request):
    modern_colors = [
    {"name": "Ultra Violet", "hex": "#5F4B8B"},
    {"name": "Vibrant Yellow", "hex": "#F9A825"},
    {"name": "Turquoise", "hex": "#1ABC9C"},
    {"name": "Sunset Orange", "hex": "#FF6F61"},
    {"name": "Emerald", "hex": "#2ECC71"},
    {"name": "Electric Blue", "hex": "#00B0FF"},
    {"name": "Fuchsia", "hex": "#D500F9"},
    {"name": "Teal", "hex": "#008080"},
    {"name": "Blush Pink", "hex": "#F2B5D4"},
    {"name": "Mint", "hex": "#98FF98"},
    {"name": "Coral", "hex": "#FF6A6A"},
    {"name": "Lime Green", "hex": "#32CD32"},
    {"name": "Sky Blue", "hex": "#87CEEB"},
    {"name": "Lilac", "hex": "#B39EB5"},
    {"name": "Ruby Red", "hex": "#E0115F"},
    {"name": "Sunshine Yellow", "hex": "#FFEB3B"},
    {"name": "Steel Blue", "hex": "#4682B4"},
    {"name": "Charcoal", "hex": "#36454F"},
    {"name": "Slate Gray", "hex": "#708090"},
    {"name": "Lavender", "hex": "#E6E6FA"},
    {"name": "Crimson", "hex": "#DC143C"},
    {"name": "Candy Apple Red", "hex": "#FF0800"},
    {"name": "Azure", "hex": "#007FFF"},
    {"name": "Tangerine", "hex": "#FF6347"},
    {"name": "Deep Sea Blue", "hex": "#2A3D66"},
    {"name": "Lemon Chiffon", "hex": "#FFFACD"},
    {"name": "Olive Green", "hex": "#808000"},
    {"name": "Moss Green", "hex": "#8A9A5B"},
    {"name": "Goldenrod", "hex": "#DAA520"},
    {"name": "Periwinkle", "hex": "#CCCCFF"},
    {"name": "Cobalt Blue", "hex": "#0047AB"},
    {"name": "Pink Salmon", "hex": "#FF91A4"},
    {"name": "Cinnamon", "hex": "#D2691E"},
    {"name": "Pastel Yellow", "hex": "#F8F8A3"},
    {"name": "Indigo", "hex": "#4B0082"},
    {"name": "Chocolate Brown", "hex": "#D2691E"},
    {"name": "Royal Purple", "hex": "#6A0DAD"},
    {"name": "Powder Blue", "hex": "#B0E0E6"},
    {"name": "Burgundy", "hex": "#800020"},
    {"name": "Neon Green", "hex": "#39FF14"},
    {"name": "Electric Violet", "hex": "#8A2BE2"},
    {"name": "Burnt Sienna", "hex": "#E97451"},
    {"name": "Saffron", "hex": "#F4C430"},
    {"name": "Peach Puff", "hex": "#FFDAB9"},
    {"name": "Seafoam Green", "hex": "#9FE2BF"},
    {"name": "Ash Gray", "hex": "#B2BEB5"},
    {"name": "Midnight Blue", "hex": "#191970"},
    {"name": "Cherry Blossom", "hex": "#FFB7C5"},
    {"name": "Violet", "hex": "#8F00FF"},
    {"name": "Magenta", "hex": "#FF00FF"},
    {"name": "Cadmium Red", "hex": "#E30022"},
    {"name": "Ivory", "hex": "#FFFFF0"},
    {"name": "Honeydew", "hex": "#F0FFF0"},
    {"name": "Seaweed Green", "hex": "#4B7F52"},
    {"name": "Grape", "hex": "#6F2DA8"},
     {"name": "Aqua Marine", "hex": "#7FFFD4"},
    {"name": "Periwinkle Blue", "hex": "#8C9EFF"},
    {"name": "Amber", "hex": "#FFBF00"},
    {"name": "Ochre", "hex": "#CC7722"},
    {"name": "Peach", "hex": "#FFDAB9"},
    {"name": "Turquoise Blue", "hex": "#00CFFF"},
    {"name": "Coral Reef", "hex": "#FF7F50"},
    {"name": "Copper", "hex": "#B87333"},
    {"name": "Spring Green", "hex": "#00FF7F"},
    {"name": "Autumn Orange", "hex": "#F57C00"},
    {"name": "Papaya Whip", "hex": "#FFEFD5"},
    {"name": "Lime", "hex": "#00FF00"},
    {"name": "Baby Blue", "hex": "#89CFF0"},
    {"name": "Mauve", "hex": "#E0B0FF"},
    {"name": "Cantaloupe", "hex": "#FFA07A"},
    {"name": "Jade", "hex": "#00A86B"},
    {"name": "Sapphire", "hex": "#0F52BA"},
    {"name": "Cobalt", "hex": "#0047AB"},
    {"name": "Almond", "hex": "#EFDECD"},
    {"name": "Plum", "hex": "#8E4585"},
     {"name": "Sunset Pink", "hex": "#FDB0C0"},
    {"name": "Frostbite", "hex": "#E5A6B8"},
    {"name": "Electric Lime", "hex": "#00FF00"},
    {"name": "Blush", "hex": "#F8C8DC"},
    {"name": "Scarlet", "hex": "#FF2400"},
    {"name": "Limeade", "hex": "#A1C935"},
    {"name": "Cobalt Green", "hex": "#006F3C"},
    {"name": "Lava", "hex": "#CF1020"},
    {"name": "Persian Blue", "hex": "#1C39BB"},
    {"name": "Tiffany Blue", "hex": "#0ABAB5"},
    {"name": "Mandarin", "hex": "#FF6A13"},
    {"name": "Honey", "hex": "#E5A700"},
    {"name": "Iceberg", "hex": "#71A6D2"},
    {"name": "Zaffre", "hex": "#0018A8"},
    {"name": "Viridian", "hex": "#40826D"}
    ]
    color_variants = []
    for i in ['#8B4513', '#7CFC00', '#8B0000', '#FF4500', '#800080', '#FF4500', '#14de39', '#0B192C', '#FF1493']:
        color_versions = generate_multiple_hex_variants(i)
        color_variants.extend(color_versions)

    material_colors = [
    # Red shades
    "#F44336",  # Red
    "#E57373",  # Red 100
    "#EF5350",  # Red 300
    "#D32F2F",  # Red 600
    "#C62828",  # Red 700
    "#B71C1C",  # Red 900

    # Pink shades
    "#E91E63",  # Pink
    "#F06292",  # Pink 100
    "#EC407A",  # Pink 300
    "#D81B60",  # Pink 600
    "#C2185B",  # Pink 700
    "#880E4F",  # Pink 900

    # Purple shades
    "#9C27B0",  # Purple
    "#BA68C8",  # Purple 100
    "#AB47BC",  # Purple 300
    "#8E24AA",  # Purple 600
    "#7B1FA2",  # Purple 700
    "#4A148C",  # Purple 900

    # Deep Purple shades
    "#673AB7",  # Deep Purple
    "#9575CD",  # Deep Purple 100
    "#7E57C2",  # Deep Purple 300
    "#5E35B1",  # Deep Purple 600
    "#512DA8",  # Deep Purple 700
    "#311B92",  # Deep Purple 900

    # Indigo shades
    "#3F51B5",  # Indigo
    "#7986CB",  # Indigo 100
    "#5C6BC0",  # Indigo 300
    "#3949AB",  # Indigo 600
    "#303F9F",  # Indigo 700
    "#1A237E",  # Indigo 900

    # Blue shades
    "#2196F3",  # Blue
    "#64B5F6",  # Blue 100
    "#42A5F5",  # Blue 300
    "#1976D2",  # Blue 600
    "#1565C0",  # Blue 700
    "#0D47A1",  # Blue 900

    # Light Blue shades
    "#03A9F4",  # Light Blue
    "#4FC3F7",  # Light Blue 100
    "#29B6F6",  # Light Blue 300
    "#0288D1",  # Light Blue 600
    "#0277BD",  # Light Blue 700
    "#01579B",  # Light Blue 900

    # Cyan shades
    "#00BCD4",  # Cyan
    "#80DEEA",  # Cyan 100
    "#4DD0E1",  # Cyan 300
    "#0097A7",  # Cyan 600
    "#00838F",  # Cyan 700
    "#006064",  # Cyan 900

    # Teal shades
    "#009688",  # Teal
    "#80CBC4",  # Teal 100
    "#4DB6AC",  # Teal 300
    "#00796B",  # Teal 600
    "#00695C",  # Teal 700
    "#004D40",  # Teal 900

    # Green shades
    "#4CAF50",  # Green
    "#81C784",  # Green 100
    "#66BB6A",  # Green 300
    "#388E3C",  # Green 600
    "#2C6A2F",  # Green 700
    "#1B5E20",  # Green 900

    # Light Green shades
    "#8BC34A",  # Light Green
    "#A5D6A7",  # Light Green 100
    "#7CB342",  # Light Green 300
    "#689F38",  # Light Green 600
    "#558B2F",  # Light Green 700
    "#33691E",  # Light Green 900

    # Lime shades
    "#CDDC39",  # Lime
    "#DCE775",  # Lime 100
    "#FDD835",  # Lime 300
    "#AFB42B",  # Lime 600
    "#9E9D24",  # Lime 700
    "#827717",  # Lime 900

    # Yellow shades
    "#FFEB3B",  # Yellow
    "#FFF176",  # Yellow 100
    "#FFEE58",  # Yellow 300
    "#FBC02D",  # Yellow 600
    "#F9A825",  # Yellow 700
    "#F57F17",  # Yellow 900

    # Amber shades
    "#FFC107",  # Amber
    "#FFEB3B",  # Amber 100
    "#FFCA28",  # Amber 300
    "#FFA000",  # Amber 600
    "#FF8F00",  # Amber 700
    "#FF6F00",  # Amber 900

    # Orange shades
    "#FF9800",  # Orange
    "#FFB74D",  # Orange 100
    "#FF7043",  # Orange 300
    "#F57C00",  # Orange 600
    "#E65100",  # Orange 700
    "#BF360C",  # Orange 900

    # Deep Orange shades
    "#FF5722",  # Deep Orange
    "#FF7043",  # Deep Orange 100
    "#F4511E",  # Deep Orange 300
    "#E64A19",  # Deep Orange 600
    "#D84315",  # Deep Orange 700
    "#BF360C",  # Deep Orange 900

    # Brown shades
    "#795548",  # Brown
    "#A1887F",  # Brown 100
    "#8D6E63",  # Brown 300
    "#6D4C41",  # Brown 600


    ]
    

    dark_colors = [
    "#000000",  # Black
    "#1A1A1A",  # Dark Gray
    "#2C2C2C",  # Charcoal Gray
    "#333333",  # Dark Gray (Alternative)
    "#3E3E3E",  # Dim Gray
    "#4B4B4B",  # Ash Gray
    "#5A5A5A",  # Gunmetal Gray
    "#616161",  # Slate Gray
    "#666666",  # Onyx
    "#707070",  # Slate
    "#808080",  # Gray
    "#8B0000",  # Dark Red
    "#800000",  # Maroon
    "#B22222",  # Firebrick
    "#A52A2A",  # Brown
    "#3E2723",  # Dark Brown
    "#2F4F4F",  # Dark Slate Gray
    "#008B8B",  # Dark Cyan
    "#006400",  # Dark Green
    "#004d00",  # Dark Forest Green
    "#0A0A0A",  # Very Dark Gray
    "#191970",  # Midnight Blue
    "#00008B",  # Dark Blue
    "#000080",  # Navy Blue
    "#191970",  # Midnight Blue
    "#003366",  # Dark Blue (Alternative)
    "#4B0082",  # Indigo
    "#2E3A87",  # Dark Purple
    "#6A0DAD",  # Purple (Dark)
    "#8B008B",  # Dark Magenta
    "#800080",  # Purple
    "#003300",  # Dark Green (Alternate)
    "#556B2F",  # Dark Olive Green
    "#5D4037",  # Dark Brown (Alternative)
    "#8B4513",  # Saddle Brown
    "#483D8B",  # Dark Slate Blue
    "#2F4F4F",  # Dark Slate Gray
    "#4B0082",  # Indigo
    "#556B2F",  # Dark Olive Green
    "#2E2E2E",  # Dark Gray (Alternative)
    "#1C1C1C",  # Onyx Black
    "#2B2B2B",  # Charcoal
    "#4C4C4C",  # Gunmetal
    "#8A8A8A",  # Platinum
        ]
    dark_colors = [
    "#000000",  # Black
    "#1A1A1A",  # Dark Gray
    "#2C2C2C",  # Charcoal Gray
    "#333333",  # Dark Gray (Alternative)
    "#3E3E3E",  # Dim Gray
    "#4B4B4B",  # Ash Gray
    "#5A5A5A",  # Gunmetal Gray
    "#616161",  # Slate Gray
    "#666666",  # Onyx
    "#707070",  # Slate
    "#808080",  # Gray
    "#8B0000",  # Dark Red
    "#800000",  # Maroon
    "#B22222",  # Firebrick
    "#A52A2A",  # Brown
    "#3E2723",  # Dark Brown
    "#2F4F4F",  # Dark Slate Gray
    "#008B8B",  # Dark Cyan
    "#006400",  # Dark Green
    "#004d00",  # Dark Forest Green
    "#0A0A0A",  # Very Dark Gray
    "#191970",  # Midnight Blue
    "#00008B",  # Dark Blue
    "#000080",  # Navy Blue
    "#191970",  # Midnight Blue
    "#003366",  # Dark Blue (Alternative)
    "#4B0082",  # Indigo
    "#2E3A87",  # Dark Purple
    "#6A0DAD",  # Purple (Dark)
    "#8B008B",  # Dark Magenta
    "#800080",  # Purple
    "#003300",  # Dark Green (Alternate)
    "#556B2F",  # Dark Olive Green
    "#5D4037",  # Dark Brown (Alternative)
    "#8B4513",  # Saddle Brown
    "#483D8B",  # Dark Slate Blue
    "#2F4F4F",  # Dark Slate Gray
    "#4B0082",  # Indigo
    "#556B2F",  # Dark Olive Green
    "#2E2E2E",  # Dark Gray (Alternative)
    "#1C1C1C",  # Onyx Black
    "#2B2B2B",  # Charcoal
    "#4C4C4C",  # Gunmetal
    "#8A8A8A",  # Platinum
    "#212121",  # Very Dark Gray
    "#1F1F1F",  # Dark Ash
    "#3B3B3B",  # Onyx Gray
    "#3A3A3A",  # Charcoal Gray (Alt)
    "#4B4B4B",  # Warm Charcoal
    "#2C3539",  # Charcoal Blue
    "#3E4A5B",  # Charcoal Blue
    "#383838",  # Charcoal (Deep)
    "#2F3B3F",  # Gunmetal Blue
    "#36454F",  # Charcoal Blue (Alternate)
    "#0D1B2A",  # Space Black
    "#102027",  # Charcoal Dark Blue
    "#607D8B",  # Blue Gray
    "#2C3E50",  # Midnight
    "#4A4A4A",  # Smoky Gray
    "#263238",  # Blue Black
    "#2B3A42",  # Dark Ocean Blue
    "#0C1C2A",  # Deep Black
    "#232323",  # Carbon Black
    "#283593",  # Indigo Dark
    "#0A2A39",  # Blue Blackish
    "#4C6A92",  # Dark Steel Blue
    "#5A6E8F",  # Steel Blue Dark
    "#37474F",  # Blue Gray (Dark)
    "#2C3E50",  # Midnight Blue (Alt)
    "#1C2833",  # Deep Blue Black
    "#0A1929",  # Almost Black Blue
    "#1B2A41",  # Dark Navy Blue
    "#283593",  # Dark Indigo
    "#3F5D8C",  # Steel Blue Dark
    "#4F4F4F",  # Cool Gray
    "#4A5A6B",  # Storm Gray
    "#5F6368",  # Concrete Gray
    "#263238",  # Blue Black (Deep)
    "#3D3D3D",  # Soft Charcoal
    "#1D2021",  # Dark Slate
    "#2C3E50",  # Deep Midnight Blue
    "#1C2833",  # Shadow Blue
    "#2C2C2C",  # Mid Charcoal
    "#303030",  # Gunmetal
    "#232B2B",  # Ash Black
    "#282828",  # Shadow Charcoal
    "#121212",  # Ultra Dark Gray
]
    dark_colors = [
    "#000000",  # Black
    "#1A1A1A",  # Dark Gray
    "#2C2C2C",  # Charcoal Gray
    "#333333",  # Dark Gray (Alternative)
    "#3E3E3E",  # Dim Gray
    "#4B4B4B",  # Ash Gray
    "#5A5A5A",  # Gunmetal Gray
    "#616161",  # Slate Gray
    "#666666",  # Onyx
    "#707070",  # Slate
    "#808080",  # Gray
    "#8B0000",  # Dark Red
    "#800000",  # Maroon
    "#B22222",  # Firebrick
    "#A52A2A",  # Brown
    "#3E2723",  # Dark Brown
    "#2F4F4F",  # Dark Slate Gray
    "#008B8B",  # Dark Cyan
    "#006400",  # Dark Green
    "#004d00",  # Dark Forest Green
    "#0A0A0A",  # Very Dark Gray
    "#191970",  # Midnight Blue
    "#00008B",  # Dark Blue
    "#000080",  # Navy Blue
    "#191970",  # Midnight Blue
    "#003366",  # Dark Blue (Alternative)
    "#4B0082",  # Indigo
    "#2E3A87",  # Dark Purple
    "#6A0DAD",  # Purple (Dark)
    "#8B008B",  # Dark Magenta
    "#800080",  # Purple
    "#003300",  # Dark Green (Alternate)
    "#556B2F",  # Dark Olive Green
    "#5D4037",  # Dark Brown (Alternative)
    "#8B4513",  # Saddle Brown
    "#483D8B",  # Dark Slate Blue
    "#2F4F4F",  # Dark Slate Gray
    "#4B0082",  # Indigo
    "#556B2F",  # Dark Olive Green
    "#2E2E2E",  # Dark Gray (Alternative)
    "#1C1C1C",  # Onyx Black
    "#2B2B2B",  # Charcoal
    "#4C4C4C",  # Gunmetal
    "#8A8A8A",  # Platinum
    "#212121",  # Very Dark Gray
    "#1F1F1F",  # Dark Ash
    "#3B3B3B",  # Onyx Gray
    "#3A3A3A",  # Charcoal Gray (Alt)
    "#4B4B4B",  # Warm Charcoal
    "#2C3539",  # Charcoal Blue
    "#3E4A5B",  # Charcoal Blue
    "#383838",  # Charcoal (Deep)
    "#2F3B3F",  # Gunmetal Blue
    "#36454F",  # Charcoal Blue (Alternate)
    "#0D1B2A",  # Space Black
    "#102027",  # Charcoal Dark Blue
    "#607D8B",  # Blue Gray
    "#2C3E50",  # Midnight
    "#4A4A4A",  # Smoky Gray
    "#263238",  # Blue Black
    "#2B3A42",  # Dark Ocean Blue
    "#0C1C2A",  # Deep Black
    "#232323",  # Carbon Black
    "#283593",  # Indigo Dark
    "#0A2A39",  # Blue Blackish
    "#4C6A92",  # Dark Steel Blue
    "#5A6E8F",  # Steel Blue Dark
    "#37474F",  # Blue Gray (Dark)
    "#2C3E50",  # Midnight Blue (Alt)
    "#1C2833",  # Deep Blue Black
    "#0A1929",  # Almost Black Blue
    "#1B2A41",  # Dark Navy Blue
    "#283593",  # Dark Indigo
    "#3F5D8C",  # Steel Blue Dark
    "#4F4F4F",  # Cool Gray
    "#4A5A6B",  # Storm Gray
    "#5F6368",  # Concrete Gray
    "#263238",  # Blue Black (Deep)
    "#3D3D3D",  # Soft Charcoal
    "#1D2021",  # Dark Slate
    "#2C3E50",  # Deep Midnight Blue
    "#1C2833",  # Shadow Blue
    "#2C2C2C",  # Mid Charcoal
    "#303030",  # Gunmetal
    "#232B2B",  # Ash Black
    "#282828",  # Shadow Charcoal
    "#121212",  # Ultra Dark Gray
    "#3B2F2F",  # Dark Brown Red
    "#2A2926",  # Dark Taupe
    "#5D3F3B",  # Dark Chestnut
    "#1B2631",  # Charcoal Blue (Deep)
    "#2F4F4F",  # Dark Sea Green
    "#4F4F4F",  # Dark Olive Gray
    "#334E68",  # Gunmetal Blue
    "#36454F",  # Charcoal Blue (Steel)
    "#7A4B3B",  # Rust Brown
    "#2A3D3D",  # Deep Sea Green
    "#4C5C68",  # Stormy Blue
    "#434343",  # Deep Charcoal
    "#5A5A5A"   # Smoke Gray (Deep)
]

    return render(request, 'color-chart.html', {'colors': modern_colors, 'color_versions': color_variants, 'material_colors': material_colors, 'dark_colors': dark_colors})


def hex_to_rgb(hex_color):
    """
    Convert a hex color string (e.g., "#3366CC") to an RGB tuple (R, G, B).
    
    :param hex_color: A string representing the hex color (e.g., "#3366CC").
    :return: A tuple representing the RGB value (R, G, B) in the range [0, 255].
    """
    hex_color = hex_color.lstrip('#')  # Remove '#' if present
    r, g, b = [int(hex_color[i:i+2], 16) for i in (0, 2, 4)]
    return r, g, b

def rgb_to_hex(rgb_color):
    """
    Convert an RGB tuple (R, G, B) to a hex color string.
    
    :param rgb_color: A tuple representing the RGB value (R, G, B) in the range [0, 255].
    :return: A string representing the hex color (e.g., "#3366CC").
    """
    return '#{:02x}{:02x}{:02x}'.format(rgb_color[0], rgb_color[1], rgb_color[2])

def generate_multiple_hex_variants(base_hex_color, num_variants=10, variation_factor=0.1):
    """
    Generate multiple lighter and darker versions of a base hex color by modifying RGB values.
    
    :param base_hex_color: A string representing the base color in hex format (e.g., "#3366CC").
    :param num_variants: The number of color variants to generate (including the base color).
    :param variation_factor: The percentage by which to lighten/darken each RGB component in each step.
    
    :return: A list of hex color variants.
    """
    # Convert base hex color to RGB
    base_color = hex_to_rgb(base_hex_color)
    
    # Create an array to hold the variants
    variants = []
    
    # Generate variants progressively lighter/darker
    for i in range(num_variants):
        # Calculate variation for each step (darker or lighter)
        factor = (i - (num_variants - 1) / 2) * variation_factor  # Center the adjustment
        
        # Adjust each RGB component
        new_r = np.clip(base_color[0] * (1 + factor), 0, 255)
        new_g = np.clip(base_color[1] * (1 + factor), 0, 255)
        new_b = np.clip(base_color[2] * (1 + factor), 0, 255)
        
        # Append the new color as a hex value
        variants.append(rgb_to_hex((int(new_r), int(new_g), int(new_b))))
    
    return variants

