$('.dialog').hide()

let openDialog = function(interlocutor_id,profile_dialog_url,public_profile_url,media_url){
    $('.dialogs').remove()
    $('.dialog').show()
    $.ajax({
        data: $(this).serialize(),
        url: (`${profile_dialog_url}`+"?interlocutor_id=" + `${interlocutor_id}`),
        success: function (response) {
            let interlocutor = JSON.parse(response.interlocutor).at(0)
            $('.dialog .header .name').append(`${interlocutor.fields.username}`)
            $('.dialog .header .img').attr("href",`${public_profile_url}`+`${interlocutor.pk}`)
            $('.dialog .header .img img').attr("src",`${media_url}`+`${interlocutor.fields.user_favicon}`)
            $('.dialog .input .new').attr("data-url",`${profile_dialog_url}`)
            $('.dialog .input .new').attr("data-id",`${interlocutor_id}`)
        },
        error: function (response) {
            console.log(response.responseJSON.errors)
        }
    });
    return false;
}
$('.dialog .input .new').submit(function(event){
    event.preventDefault();
    let profile_dialog_url = $('.dialog .input .new').attr("data-url")
    let interlocutor_id = $('.dialog .input .new').attr("data-id")
    $.ajax({
        data:  $(this).serialize(),
        type: "POST", // GET или POST
        url: (`${profile_dialog_url}`+"?interlocutor_id=" + `${interlocutor_id}`),
        success: function (response) {},
        error: function (response) {
            console.log('fucked up')
            alert(response.responseJSON.errors);
            console.log(response.responseJSON.errors)
        }
    });
    return false;
})








let $infinite_container = $('.infinite_container').infiniteScroll({
    path: '.infinite-more-link',
    append: '.infinite-item',
    });
let infScroll = $infinite_container.data('infiniteScroll');