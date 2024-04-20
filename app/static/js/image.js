function loadImage() {
    const input = document.getElementById('thumbnail');
    const dropzone = document.getElementById('dropzone');

    const file = input.files[0];
    if (file) {
        
        const reader = new FileReader();
        reader.onload = function () {
            img = document.createElement("img");
            img.src = reader.result;
            dropzone.innerHTML = img.outerHTML;
        }
        reader.readAsDataURL(file);
    }
}

document.getElementById('thumbnail').addEventListener('change', loadImage);