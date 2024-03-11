window.addEventListener('load', function() {
    
    // Find .inline-deletelink  and remove
    document.querySelectorAll('.inline-deletelink')?.forEach( button => button.remove());

    // Unused buttons on edit
    document?.querySelector('.add-row')?.remove();
    document?.getElementsByName('_addanother')?.[0]?.remove();
    document?.getElementsByName('_continue')?.[0]?.remove();
    document?.querySelectorAll('.related-widget-wrapper-link')?.forEach(element => element?.remove())
    
});
