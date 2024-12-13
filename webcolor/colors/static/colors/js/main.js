// ============= Code to Extract Dominate Colors from Image =================

const uploadZone = document.getElementById('upload-zone');
const uploadContainer = document.getElementById('upload-container');
const fileInput = document.getElementById('fileInput');
const imagePreview = document.getElementById('imagePreview');
const canvas = document.getElementById('previewImg');


if (uploadZone && uploadContainer && fileInput && fileInput && imagePreview && previewImg) {
    // Handle drag and drop events
    uploadZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        uploadZone.style.backgroundColor = '#d5e6f1';
    });

    uploadZone.addEventListener('dragleave', () => {
        uploadZone.style.backgroundColor = '#ecf0f1';
    });

    uploadZone.addEventListener('drop', (e) => {
        e.preventDefault();
        uploadZone.style.backgroundColor = '#ecf0f1';

        const file = e.dataTransfer.files[0];
        if (file && file.type.startsWith('image')) {
            displayImage(file);
        }
    });

    // Handle file input selection
    fileInput.addEventListener('change', (e) => {
        const file = e.target.files[0];
        if (file && file.type.startsWith('image')) {
            displayImage(file);
        }
    });

    // Display image preview
    function displayImage(file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            // Load the image into a canvas for processing
            const img = new Image();
            // Using color thief
            const colorThief = new ColorThief();
            // Hide the upload container and show the preview
            uploadContainer.style.display = 'none';
            img.src = e.target.result;
            imagePreview.style.display = 'block';
            img.onload = function () {
                const ctx = canvas.getContext('2d');
                // Set canvas dimensions to match the image
                canvas.width = img.width;
                canvas.height = img.height;

                // Draw the image onto the canvas
                ctx.drawImage(img, 0, 0);
                // extractColors(ctx, canvas.width, canvas.height);

                // Getting color palette
                const palette = colorThief.getPalette(canvas, 8);  // Get 8 dominant colors
                displayColorPalette(palette);
            };
            // img.src = e.target.result;
        };
        reader.readAsDataURL(file);
    }


    // Extract dominant colors
    // function extractColors(ctx, width, height) {

        // ============ THis code to get colors from canvas =======
        // const imageData = ctx.getImageData(0, 0, width, height);
        // const data = imageData.data;
        // const colorCount = {};

        // // Count pixel colors
        // for (let i = 0; i < data.length; i += 4) {
        //     const r = data[i];
        //     const g = data[i + 1];
        //     const b = data[i + 2];
        //     const rgb = `rgb(${r},${g},${b})`;
        //     colorCount[rgb] = (colorCount[rgb] || 0) + 1;
        // }

        // // Sort colors by frequency
        // const sortedColors = Object.keys(colorCount).sort((a, b) => colorCount[b] - colorCount[a]);
        // const colors = sortedColors.splice(0, 8);


        // =============== Closing ================

        // displayColorPalette(colors);
    // }

    function displayColorPalette(colors) {
        const paletteContainer = document.getElementById('color-palette');
        paletteContainer.innerHTML = ''; // Clear previous palette
        colors.forEach(color => {
            color = `rgb(${color[0]}, ${color[1]}, ${color[2]})`;
            const colorBox = document.createElement('div');
            colorBox.classList.add('color-block');
            colorBox.style.backgroundColor = color;
            colorBox.style.width = '80px';
            colorBox.style.height = '80px';
            colorBox.style.margin = '5px';
            colorBox.style.cursor = 'pointer';

            // Add click-to-copy functionality
            colorBox.onclick = () => {
                navigator.clipboard.writeText(color);
                alert(`Copied ${color} to clipboard!`);
            };

            paletteContainer.appendChild(colorBox);
        });
    }

}




// ===================== Closing Here ============================

// Code for copy to clipboard

function copyToClipboard(value) {
    var textToCopy = document.getElementById(value).innerText; // Get the text to copy
    console.log(textToCopy);

    // Use the Clipboard API to copy the text to the clipboard
    const modalMessage = document.getElementById('modal-body');
    modalMessage.textContent = "The color code has been successfully copied to your clipboard!";
    navigator.clipboard.writeText(textToCopy).then(function () {

        // Show the modal if the copy was successful
        var myModal = new bootstrap.Modal(document.getElementById('copyModal'), {
            keyboard: false
        });
        myModal.show();
    }).catch(function (error) {
        alert('Failed to copy text: ' + error);
    });
};


// close



// ======== Code to convert RGB To HEX ================


// Function to display a modal with a specific message
function showModal(message) {
    let modalMessage = document.getElementById('modal-body');
    modalMessage.textContent = message;
    var myModal = new bootstrap.Modal(document.getElementById('copyModal'), {
        keyboard: false
    });
    myModal.show();
}

// Select elements from the DOM
const redInput = document.getElementById("red");
const greenInput = document.getElementById("green");
const blueInput = document.getElementById("blue");
const convertBtn = document.getElementById("convertBtn");
const resetBtn = document.getElementById("resetBtn");
const hexValue = document.getElementById("hex-code");
const rgbCode = document.getElementById("rgb-code");
const colorPreview = document.getElementById("color-preview");
// Function to convert RGB to Hex
function rgbToHex(r, g, b) {
    const redHex = r.toString(16).padStart(2, '0').toUpperCase();
    const greenHex = g.toString(16).padStart(2, '0').toUpperCase();
    const blueHex = b.toString(16).padStart(2, '0').toUpperCase();
    return `#${redHex}${greenHex}${blueHex}`;
}

// Function to validate input values and convert them to Hex
function convertRGBToHex() {
    const red = parseInt(redInput.value, 10);
    const green = parseInt(greenInput.value, 10);
    const blue = parseInt(blueInput.value, 10);


    // Check if any of the RGB values are out of range
    if (red < 0 || red > 255 || green < 0 || green > 255 || blue < 0 || blue > 255) {
        showModal('Value of RGB must be between 0 and 255.');
    }

    // Check if any of the RGB values are out of range or empty
    else if (redInput.value === '' || greenInput.value === '' || blueInput.value === '') {
        showModal('All RGB fields must be filled in.');
    }

    else {
        // No error, proceed to convert to Hex
        const hexColor = rgbToHex(parseInt(red), parseInt(green), parseInt(blue));
        colorPreview.style.backgroundColor = `rgb(${parseInt(red)}, ${parseInt(green)}, ${parseInt(blue)})`;
        colorPreview.style.border = '1px solid grey';
        hexValue.textContent = `${hexColor}`;
        rgbCode.textContent = `rgb(${parseInt(red)}, ${parseInt(green)}, ${parseInt(blue)})`
    }

}

// Function to reset all values
function resetValues() {
    redInput.value = '';
    greenInput.value = '';
    blueInput.value = '';
    colorPreview.style.border = '1px solid grey';
    colorPreview.style.backgroundColor = `#FFFFFF`;
    hexValue.textContent = `#FFFFFF`;
    rgbCode.textContent = 'rgb(rgb(255, 255, 255)'
}




// ================= Code to Hex to RGB ==================

// Select elements from the DOM
const hexColorPreview = document.getElementById("hex-color-preview");
const modalMessage = document.getElementById('modal-body');
const modalElement = document.getElementById('copyModal');
const hexCode = document.getElementById('hexCode');

// Function to convert Hex to RGB
function hexToRGB(hex) {
    // Remove the "#" if it exists
    if (hex.startsWith("#")) {
        hex = hex.slice(1);
    }
    // Convert the hex values to integers
    const r = parseInt(hex.slice(0, 2), 16);
    const g = parseInt(hex.slice(2, 4), 16);
    const b = parseInt(hex.slice(4, 6), 16);
    return { r, g, b };
}

// Function to validate input values and convert them to RGB
function convertHexToRGB() {
    const hex = hexValue.value.trim();

    // Validate hex color format
    const hexRegex = /^#?([a-fA-F0-9]{6})$/;
    if (!hexRegex.test(hex)) {
        showModal('Please enter a valid 6-digit hex color code (e.g., #FFFFFF).');
    } else {
        // No error, proceed to convert to RGB
        const { r, g, b } = hexToRGB(hex);
        colorPreview.style.backgroundColor = `rgb(${r}, ${g}, ${b})`;
        rgbCode.textContent = `rgb(${r}, ${g}, ${b})`;
        hexCode.innerText = hex;
    }
}

// Function to reset all values
function resetHexValues() {
    hexValue.value = '';
    hexCode.innerText = '#FFFFFF';
    rgbCode.innerText = '#FFFFFF';
    colorPreview.style.backgroundColor = '#FFFFFF';
    colorPreview.style.border = '1px solid grey';
}

// ============ Close ===============
