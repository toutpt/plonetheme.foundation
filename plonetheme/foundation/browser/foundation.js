//some javascript specific for the theme.
(function($) {
    $().ready(function() {
    	var toremoves = ('<div>', '</div>', '<br>', '<br/>');
    	$('div[contenteditable].textline-field').bind('input', function(event){
    		for (toremove in toremoves){
        		event.originalEvent.srcElement.innerHTML = event.originalEvent.srcElement.innerHTML.replace(toremove, '');
    		}
    	});
    	if ($('[autofocus]').length == 0){
    		if ($('#form-widgets-IDublinCore-title').length != 0){
    			$('#form-widgets-IDublinCore-title').prop('autofocus', true);
    		}else{
        		$('#searchGadget').prop('autofocus', true);
    		}
    	}
    });
})(jQuery);