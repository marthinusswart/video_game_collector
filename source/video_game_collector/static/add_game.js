$(document).ready(function () {

    $('.btn-secondary').click(function () {
        $.ajax({
            url: '/lookup_game',
            type: 'get',
            contentType: 'application/json',
            data: {
                game_title: $('#title').val()
            },
            success: function (response) {
                $('#title').val(response.sort_title);
                $('#sort_title').val(response.sort_title);
                $('#purchase_price').val(response.purchase_price);
                $('#series').val(response.series);
                $('#game_platform_id').val(response.platform_id);
                $('#release_date').val(response.release_date);
                $('#audience_rating_id').val(response.rating_id);
                $('#developer_id').val(response.developer_id);
                $('#publisher_id').val(response.publisher_id);
                $('#description').text(response.description);
            }
        })

    })

});