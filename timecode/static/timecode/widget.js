$(document).ready(function () {
    var f = $(".timecode-widget");
    f.attr("placeholder", "hh:mm:ss:ff");
    f.keypress(function (event) {
        var key = event.which;
        var valueLength = $(this).val().length;

        if (valueLength >= 11) {
            event.preventDefault();
            return;
        }

        if ($(this).caret() == valueLength) {
            // we are entering at the end of the string
            if (valueLength % 3 == 2) {
                $(this).val($(this).val() + ":");
            }
        }
    });
});