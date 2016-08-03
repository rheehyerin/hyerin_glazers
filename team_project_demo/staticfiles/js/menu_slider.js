function(){
    var versionDoc = version.document || version.contentDocument;

    var menuBottom = versionDoc.getElementById( 'cbp-spmenu-s4' ),
    showBottom = versionDoc.getElementById( 'showBottom' ),
    body = versionDoc.body;

    showBottom.onclick = function() {
        classie.toggle( this, 'active' );
        classie.toggle( menuBottom, 'cbp-spmenu-open' );
        disableOther( 'showBottom' );
    };

    function disableOther( button ) {
        if( button !== 'showBottom' ) {
            classie.toggle( showBottom, 'disabled' );
        }
    }
}





