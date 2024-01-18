export function onImageUpload(images, select, submit) {
    const profileImages = document.querySelectorAll(images)
    const selectImage = document.querySelector(select)
    const submitBtn = document.querySelector(submit)

    submitBtn.addEventListener('click', (event) => {
        event.preventDefault()
        const image = selectImage.files[0]
        const newUrl = URL.createObjectURL(image)
        profileImages.forEach(image => {
            image.src = newUrl
        });
        selectImage.value = ""
    }) 
}