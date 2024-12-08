const uploadZone = document.getElementById('upload-zone');
const uploadContainer = document.getElementById('upload-container');
const fileInput = document.getElementById('fileInput');
const imagePreview = document.getElementById('imagePreview');
const previewImg = document.getElementById('previewImg');


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
            // Code to hide drag and drop section from code and display loaded image
            uploadContainer.style.display = 'none';
            // Close
            previewImg.src = e.target.result;
            imagePreview.style.display = 'block';
        };
        reader.readAsDataURL(file);
    }
}



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



// Code to convert RGB To HEX

// Select elements from the DOM
const redInput = document.getElementById("red");
const greenInput = document.getElementById("green");
const blueInput = document.getElementById("blue");
const convertBtn = document.getElementById("convertBtn");
const resetBtn = document.getElementById("resetBtn");
const hexValueDisplay = document.getElementById("hexValue");
const errorMessage = document.getElementById("errorMessage");
// Function to convert RGB to Hex
function rgbToHex(r, g, b) {
    // Convert each value to Hex and pad with zero if necessary
    const redHex = r.toString(16).padStart(2, '0').toUpperCase();
    const greenHex = g.toString(16).padStart(2, '0').toUpperCase();
    const blueHex = b.toString(16).padStart(2, '0').toUpperCase();
    return `#${redHex}${greenHex}${blueHex}`;
}

// Function to validate input values and convert them to Hex
function convertRGBToHex() {
    const modalMessage = document.getElementById('modal-body');
    const red = parseInt(redInput.value);
    const green = parseInt(greenInput.value);
    const blue = parseInt(blueInput.value);


    // Check if any of the RGB values are out of range or empty
    if (redInput.value === '' || greenInput.value === '' || blueInput.value === '') {
        // Show the modal if any field is empty
        const modalMessage = document.getElementsByClassName('modal-body')[0];
        modalMessage.textContent = 'All RGB fields must be filled in.';

        var myModal = new bootstrap.Modal(document.getElementById('copyModal'), {
            keyboard: false
        });
        myModal.show();
    }

    // Check if any of the RGB values are out of range
    else if (red < 0 || red > 255 || green < 0 || green > 255 || blue < 0 || blue > 255) {

        // Show the modal if the copy was successful
        modalMessage.textContent = 'Value of RGB must be between 0 and 255.';
        var myModal = new bootstrap.Modal(document.getElementById('copyModal'), {
            keyboard: false
        });
        myModal.show();
    }

    // No error, proceed to convert to Hex
    const hexColor = rgbToHex(red, green, blue);
    hexValueDisplay.textContent = `Hex: ${hexColor}`;
    errorMessage.textContent = '';  // Clear any previous error messages
}

// Function to reset all values
function resetValues() {
    redInput.value = '';
    greenInput.value = '';
    blueInput.value = '';
    hexValueDisplay.textContent = '';
    errorMessage.textContent = '';
}

// Event listeners for the buttons
convertBtn.addEventListener("click", convertRGBToHex);
resetBtn.addEventListener("click", resetValues);


//   Close