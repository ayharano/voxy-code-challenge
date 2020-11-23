"use strict";


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');


$(document).ready(
  function() {
    $( 'textarea#textbox' ).bind(
      'input',
      function() {
        $( 'textarea#textbox.is-invalid' ).removeClass('is-invalid');
      }
    );

    $( 'form' ).submit(
      function(e) {
        var form = $(this);

        $.ajax({
          headers: {
            'X-CSRFToken': csrftoken,
          },
          method: 'POST',
          data: $(form).serialize(),
        })
        .done(
          function(data) {
            $( 'div.modal-body' ).html(data);
            $( 'div#staticBackdrop' ).modal('show');
          }
        )
        .fail(
          function(data) {
            $( 'textarea#textbox' ).addClass('is-invalid');
          }
        );

        e.preventDefault();
        return false;
      }
    );
  }
);
