# Blocks

<div id="blocks-container"></div>

<script>
const blockFiles = [
    
];

const container = document.getElementById("blocks-container");

blockFiles.forEach(file => {
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
    container.appendChild(blockDiv);
});
</script>
