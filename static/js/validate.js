document.addEventListener("DOMContentLoaded", () => {
    const $ = (selector) => document.querySelector(selector); //Wanted to practice making and using a dynamic querySelector function
    const form = $("form");
    const imageBtn = document.getElementById("image");

    form.addEventListener("submit", (event) => {
        const file = imageBtn.files[0];

        if (file) {
            const allowedFileTypes = ["image/jpeg", "image/png", "image/gif"];
            if (!allowedFileTypes.includes(file.type)) {
                alert('Please upload an image file (jpg, gif, png).');
                event.preventDefault();
            }
        }
    });
});