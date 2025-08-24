# Blocks

<div id='blocks-container'></div>

<script>
const blocksByCategory = {
    "Uncategorized": [
        
    ],
    "Building_Blocks": [
        "Block.png",
        "Cone.png",
        "Corner_Quadrant.png",
        "Corner_Wedge.png",
        "Corner_Wedge_2.png",
        "Cube.png",
        "Cylinder.png",
        "Cylinder_V2.png",
        "Cylinder_panel.png",
        "Hexagon.png",
        "Hexagon_panel.png",
        "Hollow Sphere.png",
        "Hollow_Cone.png",
        "Hollow_cylinder.png",
        "Image.png",
        "Inverted_Cylinder.png",
        "Inverted_Quarter_Cylinder.png",
        "Inverted_cylinder_panel.png",
        "Octagon.png",
        "Octagon_panel.png",
        "Panel.png",
        "Pyramid.png",
        "Quadrant.png",
        "Seat Block.png",
        "Slab.png",
        "Sphere.png",
        "Truss.png",
        "Wedge.png",
        "Wedge_2.png"
    ],
    "Christmas": [
        "Menorah.png",
        "Present.png",
        "Wreath.png"
    ],
    "Decorations": [
        "Holographic_Text.png",
        "Label.png",
        "Light_Block.png",
        "Sign.png",
        "Surface_Light_Block.png"
    ],
    "Functional_Block": [
        "Sound_Block.png",
        "SpawnLocation.png"
    ],
    "Logics": [
        "And_Gate.png",
        "Bool_Storage.png",
        "Bool_Switch_Gate.png",
        "Button.png",
        "Constant_If.png",
        "Decrement_Gate.png",
        "Delay_Gate.png",
        "Door_Block.png",
        "Increment_Gate.png",
        "Inverter_Gate.png",
        "Number_Storage.png",
        "Or_Gate.png",
        "Setter_Boolean.png",
        "Setter_Number.png",
        "Setter_String.png",
        "String_Storage.png",
        "Switch.png",
        "XOR_Gate.png"
    ],
    "Nature": [
        "Pole.png",
        "Pole_End.png",
        "Post.png",
        "Snow.png",
        "Thin_post.png"
    ],
    "SciFi": [
        "Captains_Chair.png",
        "Catwalk.png",
        "Chair_Short.png",
        "Chair_Tall.png",
        "Exterior_Column.png",
        "Interior_Hall_Panel.png",
        "Space_Bed.png",
        "Space_Window.png",
        "Space_Window_Corner.png"
    ],
    "Terrain": [
        "Asphalt.png",
        "Basalt.png",
        "Brick.png",
        "Cobblestone.png",
        "Concrete.png",
        "Cracked_Lava.png",
        "Glacier.png",
        "Grass.png",
        "Ground.png",
        "Ice.png",
        "Leafy_Grass.png",
        "Limestone.png",
        "Mud.png",
        "Pavement.png",
        "Rock.png",
        "Salt.png",
        "Sand.png",
        "Sandstone.png",
        "Slate.png",
        "Snow.png",
        "Water.png",
        "Wood_Planks.png"
    ],
    "Urban": [
        "No_Cycling_Sign.png",
        "No_Parking_Sign.png",
        "Speed_Limit_Sign.png"
    ],
};


const container = document.getElementById("blocks-container");

for (const category in blocksByCategory) {
    const catDiv = document.createElement("div");
    catDiv.style.marginBottom = "40px";

    const catTitle = document.createElement("h2");
    catTitle.innerText = category.replace(/_/g," ");
    catDiv.appendChild(catTitle);

    blocksByCategory[category].forEach(file => {
        const name = file.replace(".png","").replace(/_/g," ");
        const blockDiv = document.createElement("div");
        blockDiv.style.marginBottom = "20px";

        const title = document.createElement("h3");
        title.innerText = name;

        const img = document.createElement("img");
        img.src = "Blocks/" + file;
        img.width = 100;

        blockDiv.appendChild(title);
        blockDiv.appendChild(img);
        catDiv.appendChild(blockDiv);
    });

    container.appendChild(catDiv);
}
</script>
