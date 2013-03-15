//some javascript specific for the theme.
(function($) {
    $().ready(function() {
    	var toremoves = ('<div>', '</div>', '<br>', '<br/>');
    	$('div[contenteditable].textline-field').bind('input', function(event){
    		for (toremove in toremoves){
        		event.originalEvent.srcElement.innerHTML = event.originalEvent.srcElement.innerHTML.replace(toremove, '');
    		}
    	});
    });
})(jQuery);