function isDigit(asciiCode) {
    return asciiCode >= 48 && asciiCode < 58;
}

function isDivider(asciiCode) {
    return asciiCode == 58 || asciiCode == 46;
}

(function($) {
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

        if (!isDigit(key)) {
            event.preventDefault();
        }

        if ($(this).caret() == valueLength) {
            // we are entering at the end of the string
            if (valueLength % 3 == 2) {
                if (isDivider(key)) {
                    event.preventDefault();
                }

                $(this).val($(this).val() + ":");
            }
        }
    });
});
})(django.jQuery)