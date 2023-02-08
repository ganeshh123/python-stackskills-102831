$(document).ready(() => {
    console.log('loaded')
    $.material.init()

    $(document).on('submit', '#register-form', (e) => {
        e.preventDefault()
        console.log('form submitted')
    })
})