
document.addEventListener("DOMContentLoaded", function() {
    const nestedContentBlocks = document.querySelectorAll('.nested-content-block');
    
    nestedContentBlocks.forEach(block => {
        const parent = block.parentElement;
        const children = Array.from(block.children);
        
        // Move all children up to the parent's level, then remove the original nested content block div
        children.forEach(child => parent.insertBefore(child, block));
        parent.removeChild(block);
    });

    // Function to place two images side by side
    function placeImagesSideBySide() {
        const images = document.querySelectorAll('.nested-content-block img');
        if (images.length >= 2) {
            const leftImage = images[0];
            const rightImage = images[1];

            // Create a container div for the images
            const imageContainer = document.createElement('div');
            imageContainer.style.display = 'flex';
            imageContainer.style.justifyContent = 'space-between';

            // Set styles for the images
            leftImage.style.width = '48%';
            rightImage.style.width = '48%';

            // Append images to the container
            imageContainer.appendChild(leftImage);
            imageContainer.appendChild(rightImage);

            // Insert the container into the DOM
            const parent = leftImage.parentElement;
            parent.insertBefore(imageContainer, leftImage);
        }
    }

    placeImagesSideBySide();
});
