const uploadZone = document.getElementById('upload-zone');
const uploadContainer = document.getElementById('upload-container');
const fileInput = document.getElementById('fileInput');
const imagePreview = document.getElementById('imagePreview');
const previewImg = document.getElementById('previewImg');
// Handle drag and drop events
uploadZone.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadZone.style.backgroundColor = '#d5e6f1';
});

uploadZone.addEventListener('dragleave', () => {
    uploadZone.style.backgroundColor = '#ecf0f1';
});

uploadZone.addEventListener('drop', (e) => {
    alert()
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


// Code for copy to clipboard

function copyToClipboard(value) {
    var textToCopy = document.getElementById(value).innerText; // Get the text to copy
    console.log(textToCopy);

    // Use the Clipboard API to copy the text to the clipboard
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